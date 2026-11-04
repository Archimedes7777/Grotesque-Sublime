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

# Stress drawdown v2 (Phase 6, changelog C4): peak-to-trough loss in a correlated stress episode,
# anchored on 2008-09 for incumbents and on data/drawdowns.csv for crypto. Incumbent 2008-09 figures
# are from red team A and lead memory, tagged [Unverified] in assumptions.md P6-3.
STRESS = {"R-27": 0, "R-26": 2, "M-09": 2, "L-03": 2, "R-31": 2,
          "R-09": 50, "R-10": 60, "A-01": 50, "A-02": 60, "R-11": 80, "A-05": 80,
          "R-12": 65, "R-13": 80, "R-14": 70, "R-18": 60, "R-19": 65,
          "R-15": 65, "R-16": 80, "R-17": 70,
          "R-01": 83, "R-36": 83, "R-34": 83,
          "R-02": 92, "R-03": 92, "R-35": 92, "A-04": 92, "L-09": 92, "R-38": 92,
          "R-20": 77, "M-08": 30, "M-11": 40, "A-03": 70}
def stress(row):
    c, pid = row["vehicle_class"], row["play_id"]
    if pid in STRESS: return float(STRESS[pid])
    if c in ("spot_crypto_etp_grantor_trust", "spot_crypto_etp_staking", "network_token_direct"): return 85.0
    if pid.startswith("G-"): return 60.0
    if c == "blockchain_equity_etf_1940": return 75.0
    if c in ("private_secondary", "venture_fund_lp"): return 75.0
    return 80.0

def band_mid(s):
    m = re.findall(r"-?\d+(?:\.\d+)?", str(s))
    return (float(m[0]) + float(m[1])) / 2 if len(m) >= 2 else float("nan")

def band_lo_hi(s):
    m = re.findall(r"-?\d+(?:\.\d+)?", str(s))
    return (float(m[0]), float(m[1])) if len(m) >= 2 else (float("nan"), float("nan"))

# Central estimate v2 (changelog C1): treat each band as roughly the 10th to 90th percentile of
# annual returns; sigma = (high - low) / 2.563; geometric (compounding) central = midpoint - sigma^2 / 2.
# Scenario weighting of bands (v1) is retired: it mapped adoption states onto non-adoption assets.
def geo_central(s):
    lo, hi = band_lo_hi(s)
    if lo != lo: return float("nan")
    mid = (lo + hi) / 2
    sig = (hi - lo) / 2.563 / 100
    return round(mid - 100 * sig * sig / 2, 2)

TBILL = 4.21
plays["return_mid_pct"] = plays["return_band_annual_pct"].map(band_mid)
plays["geo_central_pct"] = plays["return_band_annual_pct"].map(geo_central)
plays["stress_drawdown_pct"] = plays.apply(stress, axis=1)
plays["excess_vs_tbill_pct"] = (plays["geo_central_pct"] - TBILL).round(2)
plays.loc[plays["play_id"] == "R-27", "excess_vs_tbill_pct"] = 0.0
# Rank on excess return, with stress drawdown shown alongside (no ratio; changelog C2).
plays["rank_in_tier"] = (plays[plays["play_id"] != "R-27"].groupby("tier")["excess_vs_tbill_pct"]
                         .rank(ascending=False, method="min"))
plays.to_csv("plays.csv", index=False)

with pd.ExcelWriter("plays.xlsx", engine="openpyxl") as xw:
    summ = plays[["play_id", "vehicle", "ticker_or_route", "layer", "tier", "horizon", "return_band_annual_pct",
                  "return_mid_pct", "geo_central_pct", "excess_vs_tbill_pct", "stress_drawdown_pct", "rank_in_tier", "kill_criterion",
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
print(plays[["play_id", "tier", "ticker_or_route", "return_band_annual_pct", "geo_central_pct", "excess_vs_tbill_pct", "stress_drawdown_pct", "rank_in_tier"]]
      .sort_values(["tier", "rank_in_tier"]).to_string(index=False))
