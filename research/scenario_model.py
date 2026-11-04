"""Scenario model for the programmable-ledger research mandate (Phase 2).

Inspectable by design. Every weight and constant is declared at the top and
documented in assumptions.md (entries P2-*). Standard library plus pandas and numpy.

Method
------
1. Driver composite. WS3 driver tree gives each driver a current score in
   [-2, +2] (+2 strongly favors Bull) and a weight (weights sum to 1).
   Composite C = sum(w_i * s_i), so C is in [-2, +2].
2. Momentum term. Measured stablecoin supply and tokenized RWA growth (WS0)
   are projected to 2030 and 2035 with a decaying growth rate. The projection
   is scored against the schema.md scenario bands and converted to a momentum
   score M in [-2, +2]. Final latent score L = (1 - MOMENTUM_WEIGHT) * C + MOMENTUM_WEIGHT * M.
3. Prior. Analog adoption curves (WS3) give a base rate: the share of
   infrastructure analogs that reached 10% penetration within the horizon.
   That base rate anchors P(Bull or Base) when L = 0.
4. Ordered logit. P(Bear) = sigmoid(c1 - k*L); P(Bear or Base) = sigmoid(c2 - k*L).
   Cut points c1 and c2 are solved so that at L = 0 the probabilities equal
   the prior. k (slope) is smaller for 2035 to reflect wider uncertainty.
5. Sensitivity. Each driver is shocked by +1 and -1 (clipped to [-2, 2]);
   the change in P(Bull) and P(Bear) is recorded. Tornado ranking orders
   drivers by the total swing.

Run:  python3 scenario_model.py    (from the research/ directory)
Outputs: scenario_results.csv, data/scenario_sensitivity.csv, printed tables.
"""

from __future__ import annotations

import math
import os
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")

# ---------------------------------------------------------------------------
# Constants (documented in assumptions.md, P2-1 to P2-9)
# ---------------------------------------------------------------------------
SLOPE_K = {"2030": 1.6, "2035": 1.1}          # P2-1: sensitivity of latent score to probabilities
MOMENTUM_WEIGHT = 0.30                         # P2-2: weight of measured momentum vs driver composite
PRIOR_BASE_SHARE_OF_NONBEAR = 0.75             # P2-3: of the non-Bear mass at L=0, share that is Base
GROWTH_DECAY = 0.80                            # P2-4: annual multiplicative decay of growth rate
HORIZON_YEARS = {"2030": 4.16, "2035": 9.16}   # P2-5: from 2026-11-04
SHOCK = 1.0                                    # P2-6: driver shock size for sensitivity
ANALOG_THRESHOLD_PCT = 10.0                    # P2-7: penetration that counts as "reached scale"
PRIOR_FLOOR, PRIOR_CEIL = 0.20, 0.85           # P2-8: clamp on analog base rate

# Scenario bands, USD billions: (bear_upper, bull_lower).
# 2030 uses the WS3 recalibration (ws/ws3.md section 2; assumptions.md P2-10);
# 2035 uses schema.md Section 3 unchanged.
BANDS = {
    "2030": {"S": (500.0, 1500.0), "T": (100.0, 500.0)},
    "2035": {"S": (1000.0, 4000.0), "T": (500.0, 5000.0)},
}


def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))


def logit(p: float) -> float:
    p = min(max(p, 1e-6), 1 - 1e-6)
    return math.log(p / (1 - p))


# ---------------------------------------------------------------------------
# Loaders
# ---------------------------------------------------------------------------
def load_drivers(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df = df[["driver", "current_score", "weight"]].copy()
    df["current_score"] = pd.to_numeric(df["current_score"], errors="coerce").clip(-2, 2)
    df["weight"] = pd.to_numeric(df["weight"], errors="coerce").fillna(0)
    df = df.dropna(subset=["current_score"])
    total = df["weight"].sum()
    if total <= 0:
        df["weight"] = 1.0 / len(df)
    else:
        df["weight"] = df["weight"] / total  # renormalize so weights sum to 1
    return df.reset_index(drop=True)


def analog_prior(path: str, horizon_years: float) -> tuple[float, pd.DataFrame]:
    """Share of analogs reaching ANALOG_THRESHOLD_PCT within horizon_years."""
    df = pd.read_csv(path)
    df["years_since_launch"] = pd.to_numeric(df["years_since_launch"], errors="coerce")
    df["penetration_pct"] = pd.to_numeric(df["penetration_pct"], errors="coerce")
    df = df.dropna(subset=["years_since_launch", "penetration_pct"])
    rows = []
    for analog, g in df.groupby("analog"):
        hit = g[g["penetration_pct"] >= ANALOG_THRESHOLD_PCT]
        yrs = hit["years_since_launch"].min() if len(hit) else np.nan
        rows.append({"analog": analog, "years_to_threshold": yrs,
                     "reached_within_horizon": bool(len(hit)) and yrs <= horizon_years})
    summary = pd.DataFrame(rows)
    rate = summary["reached_within_horizon"].mean() if len(summary) else 0.5
    return float(np.clip(rate, PRIOR_FLOOR, PRIOR_CEIL)), summary


def momentum_score(current: dict, cagr: dict, horizon: str) -> tuple[float, dict]:
    """Project S and T with decaying growth; score each against bands; average.

    Score per measure: -2 at or below half the Bear upper bound, +2 at or above
    twice the Bull lower bound, linear in log space between, 0 at the geometric
    midpoint of the Base band.
    """
    years = HORIZON_YEARS[horizon]
    proj, scores = {}, []
    for m in ("S", "T"):
        g, v, t = cagr[m], current[m], 0.0
        while t < years:
            step = min(1.0, years - t)
            v *= (1 + g) ** step
            g *= GROWTH_DECAY ** step
            t += step
        proj[m] = v
        lo, hi = BANDS[horizon][m]
        lo_anchor, hi_anchor = lo / 2.0, hi * 2.0
        mid = math.sqrt(lo * hi)
        lv = math.log(v)
        if lv <= math.log(mid):
            s = -2 * (math.log(mid) - lv) / (math.log(mid) - math.log(lo_anchor))
        else:
            s = 2 * (lv - math.log(mid)) / (math.log(hi_anchor) - math.log(mid))
        scores.append(float(np.clip(s, -2, 2)))
    return float(np.mean(scores)), proj


def probabilities(latent: float, prior_nonbear: float, horizon: str) -> dict:
    p_bear0 = 1 - prior_nonbear
    p_bull0 = prior_nonbear * (1 - PRIOR_BASE_SHARE_OF_NONBEAR)
    c1 = logit(p_bear0)
    c2 = logit(1 - p_bull0)
    k = SLOPE_K[horizon]
    p_bear = sigmoid(c1 - k * latent)
    p_le_base = sigmoid(c2 - k * latent)
    return {"Bear": p_bear, "Base": p_le_base - p_bear, "Bull": 1 - p_le_base}


def run(drivers: pd.DataFrame, prior: dict, current: dict, cagr: dict) -> tuple[pd.DataFrame, pd.DataFrame]:
    rows, sens = [], []
    for h in ("2030", "2035"):
        comp = float((drivers["weight"] * drivers["current_score"]).sum())
        mom, proj = momentum_score(current, cagr, h)
        latent = (1 - MOMENTUM_WEIGHT) * comp + MOMENTUM_WEIGHT * mom
        base_p = probabilities(latent, prior[h], h)
        for sc, p in base_p.items():
            rows.append({"run": "base", "horizon": h, "scenario": sc, "probability": round(p, 4),
                         "composite": round(comp, 3), "momentum": round(mom, 3),
                         "latent": round(latent, 3), "prior_nonbear": round(prior[h], 3),
                         "proj_S_busd": round(proj["S"], 1), "proj_T_busd": round(proj["T"], 1)})
        for i, d in drivers.iterrows():
            out = {}
            for sign in (+1, -1):
                shocked = drivers.copy()
                shocked.loc[i, "current_score"] = float(np.clip(d["current_score"] + sign * SHOCK, -2, 2))
                c2 = float((shocked["weight"] * shocked["current_score"]).sum())
                l2 = (1 - MOMENTUM_WEIGHT) * c2 + MOMENTUM_WEIGHT * mom
                out[sign] = probabilities(l2, prior[h], h)
            swing = (abs(out[1]["Bull"] - out[-1]["Bull"]) + abs(out[1]["Bear"] - out[-1]["Bear"]))
            sens.append({"horizon": h, "driver": d["driver"], "weight": round(d["weight"], 3),
                         "score": d["current_score"],
                         "bull_up": round(out[1]["Bull"] - base_p["Bull"], 4),
                         "bull_down": round(out[-1]["Bull"] - base_p["Bull"], 4),
                         "bear_up": round(out[1]["Bear"] - base_p["Bear"], 4),
                         "bear_down": round(out[-1]["Bear"] - base_p["Bear"], 4),
                         "total_swing": round(swing, 4)})
    return pd.DataFrame(rows), pd.DataFrame(sens)


def main() -> int:
    drivers_path = os.path.join(DATA, "driver_tree.csv")
    analog_path = os.path.join(DATA, "analog_curves.csv")
    inputs_path = os.path.join(DATA, "model_inputs.csv")
    for p in (drivers_path, analog_path, inputs_path):
        if not os.path.exists(p):
            print(f"missing input: {p}", file=sys.stderr)
            return 1
    drivers = load_drivers(drivers_path)
    overrides_path = os.path.join(DATA, "driver_overrides.csv")  # lead overrides, assumptions.md P2-12
    if os.path.exists(overrides_path):
        ov = pd.read_csv(overrides_path)
        for _, o in ov.iterrows():
            mask = drivers["driver"] == o["driver"]
            if mask.any():
                print(f"override: {o['driver']} {drivers.loc[mask, 'current_score'].iloc[0]} -> {o['current_score']}")
                drivers.loc[mask, "current_score"] = float(o["current_score"])
    inputs = pd.read_csv(inputs_path).set_index("key")["value"].astype(float).to_dict()
    current = {"S": inputs["S_current_busd"], "T": inputs["T_current_busd"]}
    cagr = {"S": inputs["S_cagr"], "T": inputs["T_cagr"]}
    prior, analog_tables = {}, {}
    for h in ("2030", "2035"):
        prior[h], analog_tables[h] = analog_prior(analog_path, HORIZON_YEARS[h])
    results, sens = run(drivers, prior, current, cagr)

    # scenario_results.csv in schema format (run, scenario, probability_2030,
    # probability_2035, driver, driver_delta, prob_shift, note)
    out_rows = []
    piv = results.pivot(index="scenario", columns="horizon", values="probability")
    meta = results.groupby("horizon").first()
    for sc in ("Bear", "Base", "Bull"):
        out_rows.append({"run": "base", "scenario": sc,
                         "probability_2030": piv.loc[sc, "2030"], "probability_2035": piv.loc[sc, "2035"],
                         "driver": "ALL", "driver_delta": 0, "prob_shift": 0,
                         "note": (f"composite={meta.loc['2030','composite']}; momentum2030={meta.loc['2030','momentum']}; "
                                  f"momentum2035={meta.loc['2035','momentum']}; prior_nonbear2030={meta.loc['2030','prior_nonbear']}; "
                                  f"prior_nonbear2035={meta.loc['2035','prior_nonbear']}; projS2030={meta.loc['2030','proj_S_busd']}B; "
                                  f"projT2030={meta.loc['2030','proj_T_busd']}B; projS2035={meta.loc['2035','proj_S_busd']}B; "
                                  f"projT2035={meta.loc['2035','proj_T_busd']}B")})
    for _, r in sens[sens["horizon"] == "2030"].sort_values("total_swing", ascending=False).iterrows():
        for sign, col_bull, col_bear in ((+1, "bull_up", "bear_up"), (-1, "bull_down", "bear_down")):
            out_rows.append({"run": "sensitivity_2030", "scenario": "Bull", "probability_2030": np.nan,
                             "probability_2035": np.nan, "driver": r["driver"], "driver_delta": sign * SHOCK,
                             "prob_shift": r[col_bull], "note": f"Bear shift {r[col_bear]}"})
    # Momentum-assumption variants (assumptions.md P2-11): growth window and decay.
    global GROWTH_DECAY
    variants = [
        ("12m_growth_decay0.8", inputs["S_cagr_12m"], inputs["T_cagr_12m"], 0.80),
        ("36m_growth_decay0.8", inputs["S_cagr_36m"], inputs["T_cagr_36m"], 0.80),
        ("blend_growth_decay0.9", cagr["S"], cagr["T"], 0.90),
        ("36m_growth_decay0.9", inputs["S_cagr_36m"], inputs["T_cagr_36m"], 0.90),
        ("drivers_only_no_momentum", None, None, None),
    ]
    saved_decay, saved_mw = GROWTH_DECAY, globals()["MOMENTUM_WEIGHT"]
    variant_rows = []
    for name, gs, gt, dec in variants:
        if gs is None:
            globals()["MOMENTUM_WEIGHT"] = 0.0
            r, _ = run(drivers, prior, current, cagr)
        else:
            GROWTH_DECAY = dec
            r, _ = run(drivers, prior, current, {"S": gs, "T": gt})
        GROWTH_DECAY, globals()["MOMENTUM_WEIGHT"] = saved_decay, saved_mw
        pv = r.pivot(index="scenario", columns="horizon", values="probability")
        mt = r.groupby("horizon").first()
        for sc in ("Bear", "Base", "Bull"):
            out_rows.append({"run": f"variant:{name}", "scenario": sc,
                             "probability_2030": pv.loc[sc, "2030"], "probability_2035": pv.loc[sc, "2035"],
                             "driver": "momentum", "driver_delta": 0, "prob_shift": 0,
                             "note": f"projS2030={mt.loc['2030','proj_S_busd']}B; projS2035={mt.loc['2035','proj_S_busd']}B; projT2035={mt.loc['2035','proj_T_busd']}B"})
            variant_rows.append({"variant": name, "scenario": sc, "p2030": pv.loc[sc, "2030"], "p2035": pv.loc[sc, "2035"]})
    pd.DataFrame(out_rows).to_csv(os.path.join(HERE, "scenario_results.csv"), index=False)
    sens.to_csv(os.path.join(DATA, "scenario_sensitivity.csv"), index=False)
    for h in ("2030", "2035"):
        analog_tables[h].to_csv(os.path.join(DATA, f"analog_prior_{h}.csv"), index=False)

    pd.set_option("display.width", 200)
    print("Drivers (renormalized weights):")
    print(drivers.to_string(index=False))
    print("\nScenario probabilities:")
    print(piv.round(3).to_string())
    print("\nModel internals:")
    print(meta[["composite", "momentum", "latent", "prior_nonbear", "proj_S_busd", "proj_T_busd"]].to_string())
    print("\nMomentum variants:")
    print(pd.DataFrame(variant_rows).pivot(index="variant", columns="scenario", values=["p2030", "p2035"]).round(3).to_string())
    print("\nTornado ranking (2030):")
    print(sens[sens["horizon"] == "2030"].sort_values("total_swing", ascending=False)
          [["driver", "weight", "score", "bull_up", "bull_down", "bear_up", "bear_down", "total_swing"]].to_string(index=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
