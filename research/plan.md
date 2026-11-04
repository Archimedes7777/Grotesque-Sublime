# Phase 0: Mandate critique and execution plan

Date: 2026-11-04. Author: research lead. Status: complete before any workstream launch.

## 1. Execution plan

| Phase | Owner | Output | Model tier |
|---|---|---|---|
| 0 | Lead | `plan.md`, `schema.md`, `queries.md`, `null_hypothesis.md`, `assumptions.md` | Strongest |
| 1 | 10 concurrent subagents (WS0 to WS9) | `ws/ws0.md` to `ws/ws9.md`, CSVs | Mid-tier (collection) |
| 2 | Lead | `scenario_model.py`, `scenario_results.csv`, `return_methods.md` | Strongest |
| 3 | Lead | `REPORT.md`, merged `plays.csv`, `plays.xlsx`, `personalized_plays.md`, `sources.md` | Strongest |
| 4 | Fresh verification agent | `verification.md` | Strongest |
| 5 | Red team A and B, independent | `ws/redteam_a.md`, `ws/redteam_b.md`, `external_review_packet.md` | Strongest |
| 6 | Lead plus one red-team re-run on diff | `changelog.md`, `ws/redteam_diff.md`, final `REPORT.md` | Strongest |

Write-conflict rule: each subagent writes only its own files. Shared logs are per-workstream (`ws/search_log_wsN.md`) and merged by the lead into `search_log.md`.

## 2. Critique: ambiguities

| # | Ambiguity | Resolution (recorded in `assumptions.md`) |
|---|---|---|
| A1 | "Materially changes where value accrues" has no threshold. | Define materiality: a layer gains or loses at least 10% of a dated fee pool, or a new revenue pool of at least $5B per year appears, by 2030. |
| A2 | "Largest risk-adjusted after-tax return" with no risk metric. | Rank plays by expected after-tax return per unit of max drawdown (return band midpoint / estimated stressed drawdown), plus qualitative tail notes. No Sharpe ratios are computed from short, regime-specific crypto histories. |
| A3 | Bear, Base, Bull are "defined in schema.md" but the mandate gives no thresholds. | `schema.md` sets numeric thresholds for 2030 and 2035. WS3 may recalibrate with a stated reason. |
| A4 | Tier definitions overlap with accreditation. Mid tier says "accredited" but the personal case is non-accredited with $50k. | Retail = non-accredited, public markets only. Mid = accredited or qualified purchaser access. Personal case maps to Retail only. |
| A5 | Horizons (0 to 12 months, 1 to 3 years, 3 to 10 years) are measured from 2026-11-04. | Short ends 2027-11; Medium 2027-11 to 2029-11; Long 2029-11 to 2036-11. |
| A6 | "Tokenized deposits" and "stablecoins" blur when banks issue stablecoins under GENIUS-type law. | `schema.md` separates by legal claim: deposit liability (tokenized deposit) vs. reserve-backed payment stablecoin vs. MMF share. |
| A7 | Return bands without a price anchor date are meaningless. | Every valuation and price is stamped with its as-of date. Return bands are annualized, nominal USD, pre-tax and after-tax for the personal case. |

## 3. Critique: missing questions a skeptical PM would ask (added to briefs)

| # | Gap | Added to |
|---|---|---|
| G1 | What is already priced in? Implied growth in current multiples of CRCL, COIN, HOOD, etc. (reverse DCF). | WS5 |
| G2 | Correlation: do "tokenization" equities just trade as levered BTC beta? Need beta to BTC and to Nasdaq, dated. | WS5, WS6 |
| G3 | Interest-rate sensitivity: stablecoin issuer revenue is float income. What happens to issuer earnings per 100 bp of Fed cuts? | WS4, WS5 |
| G4 | Base-rate of financial-infrastructure hype cycles failing (Blockchain consortium wave 2016 to 2019: we.trade, Marco Polo, ASX CHESS replacement, TradeLens). | WS0, WS3 |
| G5 | Revenue concentration: Circle's distribution payments to Coinbase; Tether's profit vs. regulated issuers. Who keeps the float? | WS4 |
| G6 | Counterfactual: would the same value accrue to incumbents via non-DLT modernization (FedNow, ISO 20022, T+1)? | WS0, WS4 |
| G7 | Fee compression trajectory for tokenized MMFs vs. conventional MMFs (expense ratios, dated). | WS1, WS4 |
| G8 | What can a $50k non-accredited California investor actually buy, by account type, today? | WS5, WS7 |
| G9 | Benchmark: what return does the plain alternative earn (T-bills, S&P 500, Nasdaq-100) so plays are judged on excess return? | WS5, Phase 2 |
| G10 | Dilution and supply: token unlocks, equity SBC and lockup expirations for 2025 to 2026 IPOs. | WS5, WS6 |
| G11 | Legal enforceability of tokenized title and insolvency remoteness of reserves in issuer bankruptcy. | WS4, WS6 |
| G12 | Who has already failed or exited (e.g., shut-down tokenization platforms, abandoned CBDCs), as evidence of survival bias. | WS0, WS1 |
| G13 | Data integrity: which adoption dashboards (RWA.xyz, DefiLlama, Artemis, Visa Onchain Analytics) disagree, and by how much. | WS0 |
| G14 | Political durability of US policy beyond the 2028 election cycle. | WS2, WS3 |
| G15 | Concentration of the personal case in one theme: what share of a $50k total cash position should go to a 40% drawdown sleeve? | Phase 3 personalized |

## 4. Critique: overlapping scopes and how they are split

| Overlap | Owner | Others |
|---|---|---|
| Institution facts (JPM, Circle, etc.) appear in WS1, WS2, WS4, WS5 | WS2 owns facts and `institutions.csv` | WS1 lists products only; WS4 and WS5 reference by canonical name |
| Volume and AUM numbers appear in WS0 and WS1 | WS0 owns time series | WS1 cites a single latest figure with source and date |
| Timeline items appear in WS2 and WS3 | WS3 owns `timeline.csv` | WS2 states current status only |
| Agentic payments appear in WS1 and WS4 | WS8 owns | Others link |
| Jurisdictions | WS2 core (US, EU, UK, CN, SG, HK, JP, CH-SNB only) | WS9 everything else, plus Swiss and Liechtenstein market frameworks |
| Stablecoin yield legality | WS2 owns the law | WS5 owns the retail access answer; WS7 owns the tax character |
| Risks | WS6 owns `risks.csv` | WS5 states the single key risk per play only |

## 5. Critique: structural weaknesses in the mandate

1. Budget realism: 10 workstreams at 40 searches each is 400 searches. Subagents will hit the "marginal search stops changing the summary" rule early on narrow streams (WS8). That is acceptable.
2. The mandate asks for a "Mermaid diagram" and xlsx; both are produced, but Mermaid renders only in compatible viewers.
3. Phase 4 verification of 30 claims cannot cover 300+ claims. Highest-risk categories (legal status, dates, numbers driving probabilities) are prioritized.
4. The external review packet depends on the user. If `external_dissent.md` is absent in Phase 6, the report says so.
5. Risk of narrative capture: most primary-source material on tokenization is written by interested parties (issuers, consultancies). The null hypothesis workstream and bias notes are the counterweight.
6. Python model weights are judgment. They are documented as such; the model is a structured opinion, not an estimate from data.
