"""Phase 3 merge: WS5 + WS8 + WS9 plays, WS7 tax character, stress drawdown, xlsx.

Inputs: data/plays_ws5_raw.csv, data/plays_ws8.csv, data/plays_ws9.csv, data/tax_lookup.csv
Outputs: plays.csv, plays.xlsx
Stress drawdowns are judgment anchored on data/drawdowns.csv (assumptions.md P3-2).
"""
import re
import pandas as pd

ws5 = pd.read_csv("data/plays_ws5_raw.csv")
ws8 = pd.read_csv("data/plays_ws8.csv")
ws9 = pd.read_csv("data/plays_ws9.csv")
ws9.columns = [re.sub(r" \(.*\)$", "", c) for c in ws9.columns]
plays = pd.concat([ws5, ws8, ws9[ws5.columns]], ignore_index=True)
tax = pd.read_csv("data/tax_lookup.csv").set_index("vehicle_class")

CLASS = {}
for i in list(range(1, 20)) + list(range(34, 39)):
    CLASS[f"R-{i:02d}"] = "us_common_stock"
CLASS.update({"R-20": "spot_crypto_etp_grantor_trust", "R-21": "spot_crypto_etp_grantor_trust",
              "R-24": "spot_crypto_etp_grantor_trust", "R-22": "spot_crypto_etp_staking",
              "R-23": "spot_crypto_etp_staking", "R-25": "blockchain_equity_etf_1940",
              "R-26": "tokenized_mmf_registered", "R-27": "treasury_bill_direct",
              "R-28": "network_token_direct", "R-29": "network_token_direct", "R-30": "network_token_direct",
              "R-31": "stablecoin_held_no_yield", "R-32": "stablecoin_yield_exchange",
              "R-33": "stablecoin_yield_defi"})
for i in range(1, 7):
    CLASS[f"M-{i:02d}"] = "private_secondary"
CLASS.update({"M-07": "venture_fund_lp", "M-08": "tokenized_private_credit",
              "M-09": "tokenized_mmf_private_offshore", "M-10": "validator_operations",
              "M-11": "structured_notes", "M-12": "offshore_tokenized_fund_pfic"})
for i in range(1, 11):
    CLASS[f"L-{i:02d}"] = "entity_level"
CLASS.update({"L-03": "tokenized_mmf_private_offshore", "L-09": "us_common_stock"})
for i in range(1, 6):
    CLASS[f"A-{i:02d}"] = "us_common_stock"
CLASS.update({"A-06": "private_secondary", "A-07": "venture_fund_lp", "A-08": "network_token_direct"})
for i in range(1, 4):
    CLASS[f"G-{i:02d}"] = "foreign_adr_or_foreign_common"
for i in range(4, 8):
    CLASS[f"G-{i:02d}"] = "blockchain_equity_etf_1940"

EXTRA = {  # classes WS7 did not cover; lead-written, flagged for CPA review
    "treasury_bill_direct": ("Ordinary interest federal; exempt from CA tax (31 USC 3124)",
                             "Taxable: good (CA exempt); IRA/Roth: yes", "N"),
    "stablecoin_yield_defi": ("Unclear: likely ordinary income when received; no direct authority found",
                              "Taxable only in practice; avoid in IRA (custody)", "Y"),
    "private_secondary": ("LTCG over 1 year; QSBS generally unavailable for secondary purchases (Sec 1202 requires original issuance); CA taxes full gain",
                          "Taxable; accredited only", "Y"),
    "entity_level": ("Corporate or fund-level: depends on structure (C corp ordinary income; partnership K-1)",
                     "Entity, not personal account", "Y"),
    "foreign_adr_or_foreign_common": ("Dividends qualified only if treaty or US-listed test met; foreign withholding possible; LTCG over 1 year; confirm non-PFIC status in annual report",
                                      "Taxable: yes (foreign tax credit usable); IRA: yes but withholding credit lost", "Y"),
    "tokenized_mmf_private_offshore": ("Ordinary dividends; PFIC if non-US fund (check domicile, e.g., BUIDL BVI)",
                                       "Accredited or qualified purchaser only; IRA if custodian permits", "Y"),
}

def tax_cols(pid):
    c = CLASS.get(pid, "us_common_stock")
    if c in tax.index:
        r = tax.loc[c]
        return c, r["tax_character"], r["account_placement"], r["verify_with_cpa"]
    t = EXTRA[c]
    return c, t[0], t[1], t[2]

rows = [tax_cols(p) for p in plays["play_id"]]
plays.insert(plays.columns.get_loc("tax_character"), "vehicle_class", [r[0] for r in rows])
plays["tax_character"] = [r[1] for r in rows]
plays["account_placement"] = [r[2] for r in rows]
plays["verify_with_cpa"] = [r[3] for r in rows]

# Stress drawdown (percent loss in a crypto-bear or credit-stress year), judgment anchored on data/drawdowns.csv
def stress(row):
    c, lay, pid = row["vehicle_class"], row["layer"], row["play_id"]
    if pid in ("R-27",): return 0.0
    if pid in ("R-26", "M-09", "L-03", "R-31"): return 2.0
    if pid in ("R-09", "R-10", "A-01", "A-02"): return 30.0
    if pid in ("R-12", "R-13", "R-14", "R-15", "R-16", "R-17", "R-18", "R-19", "R-11"): return 40.0
    if pid in ("R-01", "R-36"): return 83.0
    if pid in ("R-02", "R-03", "R-35", "A-04", "L-09"): return 90.0
    if c in ("spot_crypto_etp_grantor_trust",) and "IBIT" in str(row["ticker_or_route"]): return 77.0
    if c in ("spot_crypto_etp_grantor_trust", "spot_crypto_etp_staking", "network_token_direct"): return 85.0
    if pid.startswith("G-"): return 45.0
    if c == "blockchain_equity_etf_1940": return 70.0
    if c in ("private_secondary", "venture_fund_lp"): return 70.0
    if c == "tokenized_private_credit": return 15.0
    return 75.0

def band_mid(s):
    m = re.findall(r"-?\d+(?:\.\d+)?", str(s))
    return (float(m[0]) + float(m[1])) / 2 if len(m) >= 2 else float("nan")

def band_lo_hi(s):
    m = re.findall(r"-?\d+(?:\.\d+)?", str(s))
    return (float(m[0]), float(m[1])) if len(m) >= 2 else (float("nan"), float("nan"))

# Lead scenario probabilities (assumptions.md P3-1): average of model base run and WS3 judgment.
P = {"2030": (0.57, 0.36, 0.07), "2035": (0.53, 0.38, 0.09)}

def scen_expected(row):
    lo, hi = band_lo_hi(row["return_band_annual_pct"])
    mid = (lo + hi) / 2
    pb, pm, pu = P["2035"] if row["horizon"] == "Long" else P["2030"]
    return round(pb * lo + pm * mid + pu * hi, 2)

plays["return_mid_pct"] = plays["return_band_annual_pct"].map(band_mid)
plays["scenario_expected_pct"] = plays.apply(scen_expected, axis=1)
plays["stress_drawdown_pct"] = plays.apply(stress, axis=1)
plays["excess_vs_tbill_pct"] = (plays["scenario_expected_pct"] - 4.21).round(2)
plays["ra_score"] = (plays["excess_vs_tbill_pct"] / plays["stress_drawdown_pct"].where(plays["stress_drawdown_pct"] > 0)).round(3)
plays.to_csv("plays.csv", index=False)

with pd.ExcelWriter("plays.xlsx", engine="openpyxl") as xw:
    summ = plays[["play_id", "vehicle", "ticker_or_route", "layer", "tier", "horizon", "return_band_annual_pct",
                  "return_mid_pct", "scenario_expected_pct", "stress_drawdown_pct", "excess_vs_tbill_pct", "ra_score", "kill_criterion",
                  "tax_character", "confidence", "source_ws"]]
    summ.to_excel(xw, sheet_name="Summary", index=False)
    for tier in ("Retail", "Mid", "Large"):
        plays[plays["tier"] == tier].to_excel(xw, sheet_name=tier, index=False)
    for ws in xw.book.worksheets:
        ws.auto_filter.ref = ws.dimensions
        ws.freeze_panes = "B2"
        for col in ws.columns:
            ws.column_dimensions[col[0].column_letter].width = min(45, max(10, max(len(str(c.value or "")) for c in col[:40]) * 0.9))
print(plays.groupby(["tier"]).size().to_string())
pd.set_option("display.width", 220)
print(plays[["play_id", "tier", "ticker_or_route", "return_band_annual_pct", "scenario_expected_pct", "stress_drawdown_pct", "ra_score"]]
      .sort_values("ra_score", ascending=False).to_string(index=False))
