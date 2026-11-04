# Changelog

All changes to `REPORT.md`, `personalized_plays.md`, `plays.csv` and the packet after the Phase 3 draft (commit 3e30367).

## Phase 4: verification fixes (2026-11-04)

| # | File | Change | Trigger |
|---|---|---|---|
| V1 | REPORT.md Section 8 | Form 1099-DA: gross proceeds start for sales on or after 2025-01-01 (was "after 2025"); basis for covered units acquired on or after 2026-01-01 | verification.md row 16 FAIL |
| V2 | REPORT.md Section 6 | CRCL drawdown: about 74% below the intraday peak (was 83%; 83% applies at the 52-week low); crypto-equity drawdown range 68% to 74% | verification.md row 27 FAIL |
| V3 | REPORT.md exec summary; packet | Circle $409.2M relabeled as "distribution and transaction costs" (was "paid to distribution partners") | verification.md row 26 qualifier |
| V4 | REPORT.md exec summary | T-bill 4.21% labeled constant-maturity yield; discount basis 4.03% added | verification.md row 20 qualifier |
| V5 | personalized_plays.md | $15.1B clarified as distributed tokenized assets on Ethereum, not total tokenized Treasuries | verification.md row 24 cross-file mismatch |

## Phase 6: revision after red teams A and B (2026-11-04)

### Method and content changes

| # | Change | Files | Trigger |
|---|---|---|---|
| C1 | Retired the v1 scenario weighting of play bands. New central estimate = midpoint - sigma^2/2 (bands read as 10th to 90th percentile). | merge_plays.py, plays.csv, plays.xlsx, return_methods.md, REPORT.md Section 6 | A2, B1 |
| C2 | Removed the ratio score (ra_score). Ranking is within tier on central excess over 4.21%, with stress shown; the T-bill benchmark is excluded from its own ranking. Top-five overrides are marked (J). | same | A3, B6 |
| C3 | Scenario probabilities now come from a five-estimator panel mean with ranges. 2030 moved from 57/36/7 to 51/42/7; 2035 from 53/38/9 to 46/43/11. | REPORT.md exec summary, Section 4C | A5, B4 |
| C4 | Stress drawdowns raised to 2008 to 2009 anchors for incumbents. Tokenized private credit 15% to 30%; EM equities 45% to 60%. | merge_plays.py, plays.csv | A4, B5, B10 |
| C5 | Sizing rule restated as a portfolio sum of weight x stress with correlation near 1 | REPORT.md Section 7 | A4, B5 |
| C6 | Personal allocation rebuilt. Option A (incumbent core, 60% cash-like): stress 25.0%, central 5.70%. Option B adds 10% CRCL, COIN, IBIT, ETHA: stress 33.4%, central 5.41%. The v1 allocation (stress 26.3% on v1 stress values) is withdrawn. | personalized_plays.md | A4, B5, B7 |
| C7 | Added a macro regime section: September hike, December hike priced, CPI 3.7%, Iran war, real hurdle. Rate sensitivity made symmetric (±100 bp). | REPORT.md Section 4A | A1, B3 |
| C8 | Scenario definitions shown in full; split outcomes count as Base; Bear relabeled for public-chain T; represented variant run (2030 Bear 50%). | REPORT.md Section 4B, scenario_model.py, data/model_inputs.csv | A5, B2 |
| C9 | Added a disorderly sub-path (about 10% over five years) and the run row in the risks table | REPORT.md Sections 4B, 7 | A7 |
| C10 | Added Tron and Hyperliquid value-capture counterexamples, the Base token risk to COIN, and Canton single-application concentration | REPORT.md Section 5, Section 6 | B7, B8, B9 |
| C11 | Added Fed payment account terms and the access lever | REPORT.md Section 3 | A8 |
| C12 | Added credit card interchange legislation as a V and MA risk and kill criterion | REPORT.md Section 7; personalized_plays.md | A12 |
| C13 | BIS WP 1270 magnitudes marked contested, with the outflow asymmetry | REPORT.md Section 5 | A7 |
| C14 | "Thesis not priced in" reworded to "not cheap on own reverse-DCF hurdles" | REPORT.md Section 6 | A14 |
| C15 | Stablecoin peak series clarified (USD-only $315.5B vs all-stablecoin $322.4B) | REPORT.md Section 1 | B4 |
| C16 | Both dissents appended verbatim as Appendices A and B. Heading levels were demoted to nest under the appendix; text is unchanged. | REPORT.md | Mandate rule 13 |

### Disposition of remaining red-team items

| Item | Disposition | Reason |
|---|---|---|
| A6 (model is crypto-cycle extrapolation; regress S on crypto cap and rates) | Partly adopted | The model is now one of five panel estimators. A regression model is deferred: no clean series of crypto market cap or policy rate was gathered this session. |
| A9 (deposit franchise economics) | Noted, not modeled | Needs bank-level deposit beta data; flagged for the next revision |
| A10 (capital rules, custody enabler) | Partly adopted | The Basel row remains; specific capital misstatements are not verified this session |
| A11 (Treasury clearing mandate; survivorship in analogs) | Noted | The clearing mandate creates collateral demand that favors tokenized Treasuries. Added to the watch list, not modeled. |
| A13 (midterm override overweights politics) | Partly adopted | The override stays (AP-called). Its weight is diluted by the panel. |
| A15 (M-08 gating wave) | Adopted | Stress 30%; gates noted; (J) label |
| A16, B12 (issuer build and buy economics) | Adopted as caveat | Breakeven noted as assuming Circle-like terms |
| A17 (licence moat commoditizing) | Adopted | Custody row now says licences are commoditizing |
| A18, A19 (duplicate rows; number conflicts) | Partly adopted | Duplicate plays (R-09 vs A-01, etc.) are kept because they come from different workstreams with different theses; the conflict is noted here |
| A20 (tokenized MMFs dominated by T-bills) | Adopted | BENJI scores -0.36 pts. It is kept at 5% as a learning position, not as a return play. |
| A21 (sanctions underweighted) | Noted | Covered by the disorderly sub-path |
| A22, B24 (geography off-theme) | Adopted | Section 10 states the thin link; no G-play in the allocation |
| A23 (theft probability too low) | Not adopted | WS6 already puts it at 80%; the red team's own evidence is the same two incidents |
| A24, B11 (private marks anchored favorably) | Adopted as caveat | Kraken mark disputed; Ripple tagged as an XRP proxy |
| A25, B20 (denominators; supply is not usage) | Adopted | Section 1 bullet on supply versus usage |
| A26 (forecasts labeled as facts) | Adopted | Forecasts in Section 4 now say "marks" from interested parties |
| A27 (event trades, unpriced rows) | Partly adopted | Unpriced rows keep NA and are excluded from ranks |
| B13 (stablecoin-chain wave; Arc presale refund contingency) | Noted | Arc presale ($182M of Q3 revenue) is non-recurring; added to the CRCL caveats in the next revision |
| B14 (staking ETP liquidity mismatch) | Noted | Staking variants already excluded from the taxable personal case |
| B15 (custody and self-custody operations; freeze risk) | Noted | The personal case uses ETPs only |
| B16 (DeFi convergence routes to yield) | Noted | Out of scope for the Retail personal case; R-33 remains unscored |
| B17 (token unlocks absent) | Noted | Gap: no unlock calendar gathered (search cap) |
| B18 (missing plays: TRX, HYPE ETPs, avoid list) | Partly adopted | Named in Section 5 as watch items; not added as scored rows because no band was researched |
| B19 (wrong hurdle; pre-tax ranking) | Partly adopted | After-tax and real figures added in personalized_plays.md; ranking stays pre-tax for comparability across investors |
| B21, B22 (ETH test stops at fees; Base economics stale) | Noted | Staking yield and MEV not re-researched; Base token risk added |
| B23 (13 unpriced rows dilute the matrix) | Adopted | Unpriced rows excluded from ranks (rank NA) |
| B25 (tax confidence overstated) | Partly adopted | Rev. Proc. 2026-20 marked as secondary only |
