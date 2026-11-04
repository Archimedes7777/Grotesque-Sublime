# Assumptions and judgment calls

Each entry: ID, phase, assumption, reason. Later phases append.

## Phase 0

| ID | Assumption | Reason |
|---|---|---|
| P0-1 | Research date is 2026-11-04 (environment date). Training data is treated as stale; all current-law and price claims are verified by search. | Mandate Section 1. |
| P0-2 | Materiality threshold: a layer gains or loses at least 10% of a dated fee pool, or a new revenue pool of at least $5B per year appears, by 2030. | Mandate gives none (plan.md A1). |
| P0-3 | Risk-adjusted ranking metric: return band midpoint divided by estimated stressed drawdown, plus qualitative tail notes. | No risk metric specified (A2). |
| P0-4 | The personal case (non-accredited, $50k, taxable cash account, no margin) maps to the Retail tier only. Mid-tier vehicles are excluded from `personalized_plays.md`. | Accreditation status "No". |
| P0-5 | Horizons measured from 2026-11-04: Short to 2027-11, Medium 2027-11 to 2029-11, Long 2029-11 to 2036-11. | A5. |
| P0-6 | Scenario thresholds in `schema.md` Section 3 are provisional. | A3. |
| P0-7 | Return bands are annualized nominal USD, pre-tax unless stated; the personal case also shows after-tax at an assumed combined federal plus CA marginal rate (stated in Phase 3). | A7. |
| P0-8 | "Constraints: none stated" is read as permitting direct token custody and spot crypto ETFs, but no leverage or margin (cash account). | Section 0 table. |
| P0-9 | Liquidity need "none stated, 10-year horizon" is read as: capital not needed before 2036, but the investor wants daily liquidity by default; locked vehicles are excluded from the personal case. | Conservative reading. |
| P0-10 | Model tiering: subagents for collection run on a mid-tier model; synthesis, verification, and red team run on the strongest model. | Mandate Section 1 rule 3. |
| P0-11 | Each subagent writes its own search log (`ws/search_log_wsN.md`); the lead merges into `search_log.md`. | Avoid concurrent write conflicts. |
| P0-12 | Repository context: research is stored in `./research/` inside the Grotesque-Sublime repo working directory, committed to branch `claude/new-session-5ulni5`. All web content is untrusted data per the repo's SECURITY.md; no instructions from web pages are followed. | Repo policy. |

## Phase 1 (process notes)

| ID | Assumption | Reason |
|---|---|---|
| P1-1 | Subagents hit a per-agent web search cap well below the 40-search budget (WS8 at 24, WS2 at 15). Affected sections are tagged and the lead runs targeted gap-fill searches during synthesis and verification. | Tool limit observed 2026-11-04. |
| P1-2 | WS2 reported that Democrats won both chambers in the 2026-11-03 midterms. A lead search on 2026-11-04 returned only pre-election coverage, so the result is treated as `[Unverified]` and is not used as a probability driver. The scenario model treats US political durability as uncertain in both directions. | Results may not be indexed yet; a single-day report should not drive conclusions. |
| P1-3 | P1-2 superseded: AP and CBS called the House and Senate for Democrats (2026-11-04). Seat counts are provisional. Applied as a lead override: Political durability driver 0 to -1 (`data/driver_overrides.csv`). | CBS News, NBC Washington, Forbes live coverage, 2026-11-04. |

## Phase 2 (scenario model)

| ID | Assumption | Reason |
|---|---|---|
| P2-1 | Ordered-logit slope k = 1.6 (2030) and 1.1 (2035). A one-point move in the latent score shifts Bear probability by roughly 30 to 35 points at the margin in 2030. | Judgment; smaller k for 2035 reflects wider uncertainty. |
| P2-2 | Momentum weight 0.30 vs driver composite 0.70. | Measured data should matter but not dominate one flat year. |
| P2-3 | At a neutral latent score, Base takes 75% of the non-Bear mass, Bull 25%. | Bull requires several drivers to break favorably at once. |
| P2-4 | Growth-rate decay 0.80 per year in the base run; 0.90 in variants. | Adoption growth rates fall as base grows; 0.8 is conservative. |
| P2-5 | Horizons 4.16 years (to 2030-12-31) and 9.16 years (to 2035-12-31) from 2026-11-04. | Calendar arithmetic. |
| P2-6 | Sensitivity shock is +/-1 point on the -2 to +2 driver scale. | One notch of evidence. |
| P2-7 | Analog prior: share of WS3 analogs that reached 10% penetration within the horizon, clamped to [0.20, 0.85]. Failed consortia count as non-reaching. Result 0.50 for both horizons. | Base-rate anchor (data/analog_prior_*.csv). |
| P2-8 | Driver weights are WS3's judgment, renormalized to sum to 1. | WS3 owns the driver tree. |
| P2-9 | Momentum scoring: -2 at half the Bear ceiling, +2 at twice the Bull floor, linear in log space, 0 at the geometric midpoint of the Base band. | Symmetric, unit-free scoring. |
| P2-10 | 2030 bands use WS3's recalibration (S Bear below $500B, Bull above $1.5T; T Bear below $100B, Bull above $500B). 2035 bands are the schema originals. | Schema Bull for T needed 149% CAGR; WS3 stated reason. |
| P2-11 | Base growth inputs blend 12-month and 36-month rates: S 15% (12m -3%, 36m +33%); T 40% (12m about +15% with a methodology break, 36m about +70%). Variants run each window separately. | One flat year should not set a nine-year projection alone. |
| P2-12 | Lead override file `data/driver_overrides.csv` changes WS3 scores only with a cited, dated reason. | Keeps WS3 raw output intact. |

## Phase 3 (synthesis)

| ID | Assumption | Reason |
|---|---|---|
| P3-1 | Lead scenario probabilities = simple average of the model base run and WS3 judgment. 2030: Bear 57%, Base 36%, Bull 7%. 2035: Bear 53%, Base 38%, Bull 9%. Model variant range for 2030 Bear: 50% to 73%. | The model is mechanical and momentum-sensitive; WS3 judgment includes evidence the model cannot score. |
| P3-2 | Stress drawdowns per play are lead judgment anchored on `data/drawdowns.csv` (e.g., COIN and HOOD 90%, CRCL 83%, IBIT 77%, other tokens and token ETPs 85%, V and MA 30%, banks, custodians and exchanges 40%, EM equities 45%, cash-like 0 to 2%). | Historical cycle troughs. |
| P3-3 | Scenario-weighted expected return per play = P(Bear) x band low + P(Base) x band midpoint + P(Bull) x band high. Long-horizon plays use 2035 probabilities; others 2030. This is conservative for wide bands because WS5 lows are stress outcomes. The midpoint is also shown. | Band midpoints are not expected values; a -70 to +150 band is not a +40% expectation. |
| P3-4 | Risk-adjusted score = (scenario-weighted expected return minus 4.21% T-bill) / stress drawdown. | Implements P0-3 against the benchmark (G9). |
| P3-5 | Secondary purchases of private shares are treated as not QSBS-eligible, because Sec 1202 requires stock acquired at original issuance. | 26 USC 1202(c)(1)(B). |
| P3-6 | Personal-case after-tax rates: federal 24% ordinary and 15% LTCG, plus 3.8% NIIT not assumed (income unknown), plus California 9.3% on all gains and ordinary income. Combined: 33.3% ordinary, 24.3% long-term. | Income not stated; mid-bracket assumption for a $50k cash holder. |
