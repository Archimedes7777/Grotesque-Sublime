# WS3: When and how likely: timeline and scenario analysis

## Summary

Fact: As of 2026-11-04 the US stablecoin law clock is running (GENIUS Act effective 2027-01-18; OCC final rule 2026-10-21) but market structure legislation stalled (CLARITY cloture failed 2026-09-15). Stablecoin supply has been flat at about $300-320B for 12 months (about $295B on 2026-11-04). Distributed tokenized RWA ex-stablecoins is $39.4B.

Inference: Observed trajectory sits at the Bear/Base boundary, not the Bull path implied by sell-side marks. Sell-side forecasts (Standard Chartered $2T by 2030, Citi $5.5T tokenized by 2030) are interested, definition-dependent, and already being delayed. [Moderate]

Inference: Recalibrated 2030 probabilities: Bear 50%, Base 43%, Bull 7%. 2035 (schema bands unchanged): Bear 38%, Base 51%, Bull 11%. Basis: growth-rate arithmetic from today's levels, forecast-cut history, analog speeds, and the driver tree (weighted score -0.02 on a -2 to +2 scale). [Low]

Inference: Top drivers by weight and sensitivity: US/EU regulatory clarity (0.14), end-user demand (0.14), bank capital treatment (0.10), political durability (0.09), interoperability (0.09). Weakest verified link is demand, not law. [Moderate]

Recommendation: Treat the Bull path as an option, not a base case. Watch the three Bear-vs-Base indicators in section 3 through 2027-12. [Low]

## Key numbers

| Metric | Value | Date | Source | Confidence |
|---|---|---|---|---|
| USD stablecoin supply | about $295B to $309B | 2026-10-20 to 2026-11-04 | DefiLlama via The Block, StanChart | [Moderate] |
| Stablecoin all-time high | about $315.5B to $322B | 2026-05 | third-party DefiLlama readings | [Low] |
| USDT / USDC | $177.8B / $71.3B | 2026-11-04 | stablecoins.llama.fi | [Moderate] |
| Distributed RWA ex-stablecoins | $39.40B | 2026-11-04 | app.rwa.xyz | [Moderate] [Interested source] |
| Represented RWA (not counted in T) | $395.97B | 2026-11-04 | app.rwa.xyz | [Moderate] |
| Tokenized Treasuries | about $14.7B | 2026-09 | RWA.xyz via secondary | [Low] |
| US MMF assets | $7.979T | 2026-09-02 | ICI via Crane Data | [Moderate] |
| Tokenized Treasuries / US MMF | 0.18% | 2026-09 | derived | [Low] |
| Fed funds target | 3.75%-4.00% | 2026-10-28 | FOMC statement | [Moderate] |
| GENIUS Act effective | 2027-01-18 | 2026-10-21 | OCC Bulletin 2026-50 | [High] |

## Body

### 1. Timeline (see `timeline.csv`, 71 rows)

Fact: 71 dated rows from 2019 to 2035. Status counts are in the CSV. Rows resting on training knowledge only carry confidence `unverified` and are not used as drivers.

| Date | Milestone | Status | Signal | Source date |
|---|---|---|---|---|
| 2026-09-15 | CLARITY Act cloture fails; needs reintroduction in 120th Congress | occurred | bear | 2026-09-15 |
| 2026-09-17 | SEC Innovation Exemption for tokenized NMS stock, expires 2031-09-17 | occurred | bull | 2026-09-17 |
| 2026-10-21 | OCC GENIUS final rule (BSA/AML/OFAC reserved) | occurred | base | 2026-10-21 |
| 2026-12-31 | Digital euro regulation targeted; BoE Code of Practice; Basel update | expected | neutral | various |
| 2027-01-18 | GENIUS Act takes effect | scheduled | base | 2026-11-04 |
| 2027-10-11 | EU, UK, CH T+1 | scheduled | neutral | 2026-11-04 |
| 2027-10-25 | UK FCA stablecoin regime effective | scheduled | base | 2026-07-16 |
| 2028-07-18 | GENIUS DASP deadline for non-permitted stablecoins | scheduled | base | 2026-11-04 |
| 2029 | Eurosystem ready for potential digital euro issuance | expected | neutral | 2026-09-23 |

Fact: Conflicts flagged in the CSV: HKMA first licences (03-24 vs 04-10), SWIFT ledger go-live (one aggregator, contradicted), DTCC October launch (secondary only), Kraken IPO status (cancelled March, filed April). [Moderate]

### 2. Scenario calibration

Fact: Schema thresholds (2030) require stablecoin supply S above $600B for Base and above $2T for Bull, and tokenized RWA T above $150B and $1.5T. From S about $300B and T $39.4B, Base needs CAGR 19% (S) and 40% (T); Bull needs 61% (S) and 148% (T) over four years. (Derived from RWA.xyz and DefiLlama, 2026-11-04.)

Inference: Bull T above $1.5T by 2030 is not reachable on any observed growth rate; Base lower bounds are above current trend. I recalibrate 2030 only. 2035 bands are kept because nine years allows regime change. [Moderate]

| Measure (2030) | Schema Bear / Base / Bull | Recalibrated Bear / Base / Bull | Reason |
|---|---|---|---|
| S | <$600B / $600B-2T / >$2T | <$500B / $500B-1.5T / >$1.5T | Supply flat 12 months; $500B is 14% CAGR |
| T | <$150B / $150B-1.5T / >$1.5T | <$100B / $100B-500B / >$500B | $500B needs 89% CAGR; $1.5T needs 149% |
| W | <0.5% / 0.5-3% / >3% | unchanged | No verified W series; DTCC and Broadridge data absent |

Fact: Assignment rule unchanged: a scenario occurs if two of three measures fall in its band. Under the unrecalibrated schema bands my 2030 probabilities would be Bear 62%, Base 36%, Bull 2%. [Low]

### 3. Scenarios

| | Bear | Base | Bull |
|---|---|---|---|
| P(2030) recalibrated | 50% | 43% | 7% |
| P(2035) schema bands | 38% | 51% | 11% |
| Narrative | Stablecoins stay crypto plumbing and offshore dollars; flat supply persists; DTC tokenization stays small; CLARITY dies; Basel keeps punitive treatment | GENIUS issuers bring bank-backed supply; tokenized Treasuries become collateral; Innovation Exemption venues trade small volumes; wholesale DLT handles a minority of collateral | Law plus Basel relief plus 24/7 tokenized equity venues create a primary settlement layer; agentic payments material |
| Probability basis | S, T both below Base floors under current trend; W below 0.5% about 75% likely; two sell-side marks already delayed | Law is in place; hybrid adoption fits analog speeds (EMV, Pix) once rails are mandated or subsidized | Requires T growth of 89% per year for four years; no analog reached this from 0.2% penetration in under 5 years except mandated EMV |
| Indicator 1 | DefiLlama stablecoin total (stablecoins.llama.fi) below $350B on 2027-12-31 | Federal Register dockets: FDIC and Fed GENIUS final rules plus Treasury BSA/AML rule by 2027-07-18; count of OCC-approved issuers | RWA.xyz tokenized stocks (distributed) above $20B; first Tokenized Securities Venue notices filed with SEC under the 2026-09-17 order |
| Indicator 2 | RWA.xyz Distributed Asset Value ex-stablecoins below $60B on 2027-12-31 | RWA.xyz tokenized Treasuries above $30B on 2027-12-31 | BCBS publication revising SCO60 (docket: bis.org/bcbs) removing permissionless penalty in 2027 |
| Indicator 3 | CLARITY or successor not reported out of Senate Banking in 120th Congress by 2027-09-30 (congress.gov) | DTC tokenization service participant count and first-year volume disclosed by DTCC by 2027-12 | Stablecoin total above $600B by 2028-06-30 with Visa Onchain Analytics adjusted payments volume growing above 100% per year |
| Falsifier | Two measures above Base floors by 2028-12-31 | S below $400B and T below $60B on 2028-12-31 (falls to Bear) or S above $1.2T (rises to Bull) | S below $600B on 2028-12-31 |

Inference: Probabilities are structured judgment, not estimates fit to data. They move 5 to 10 points on a single new datum such as a Basel revision. [Low]

### 4. Driver tree (also `data/driver_tree.csv`)

Score +2 strongly favors Bull. Weights sum to 1.00. Sensitivity is judgment: change in 2030 P(Bear) and P(Bull) per +1 step in the driver, using a uniform rule (Bear -40 points x weight; Bull +12 points x weight) for the Phase 2 model to replace.

| Driver | Score | Direction | Weight | dP(Bear) pp | dP(Bull) pp | Evidence (date) | Conf |
|---|---|---|---|---|---|---|---|
| Regulatory clarity | +1 | improving | 0.14 | -5.6 | +1.7 | GENIUS effective 2027-01-18; OCC rule 2026-10-21; CLARITY failed 2026-09-15 | [High] |
| End-user demand | -1 | stable | 0.14 | -5.6 | +1.7 | Supply flat 12 months to 2026-10-14; payments about 6% of demand (JPM, 2025-07) | [Moderate] |
| Bank capital treatment | -1 | stable | 0.10 | -4.0 | +1.2 | Basel review, no date (2026-02-25) | [Moderate] |
| Interoperability | 0 | improving | 0.09 | -3.6 | +1.1 | Agora to real-value testing, undated (2026-05-27) | [Low] |
| Political durability | 0 | stable | 0.09 | -3.6 | +1.1 | CLARITY reset; midterm result unverified | [Low] |
| Institutional custody | +1 | improving | 0.08 | -3.2 | +1.0 | DTC no-action 2025-12-11; DTCC plan 2026-05-04 | [Moderate] |
| Technical maturity | 0 | improving | 0.08 | -3.2 | +1.0 | Limited production trades only | [Low] |
| Incumbent incentives | 0 | stable | 0.08 | -3.2 | +1.0 | HK licences to banks; BUIDL about $2B | [Low] |
| Geopolitical competition | +1 | improving | 0.07 | -2.8 | +0.8 | EP digital euro mandate 416-169 (2026-07-09) | [Moderate] |
| Interest-rate level | -1 | deteriorating | 0.07 | -2.8 | +0.8 | Hike to 3.75%-4.00% 2026-09-16 | [Moderate] |
| Treasury market effects | 0 | stable | 0.06 | -2.4 | +0.7 | TBAC 2026-11-03 minutes mention only | [Moderate] |

Fact: Weighted score is -0.02. Inference: this sits at neutral, consistent with a 50/43 Bear/Base split in 2030 and a more Base-leaning 2035. [Low]

Inference: Rates cut both ways. Higher yields raise issuer float income and tokenized Treasury appeal but weaken the crypto leverage that drove supply growth (StanChart calls the stall cyclical, 2026-10-14). [Moderate]

### 5. Forecast reconciliation (see `data/forecasts.csv`)

| Forecaster | Vintage | Metric | Horizon | Value | Interest flag |
|---|---|---|---|---|---|
| Standard Chartered | 2026-10-14 | Stablecoins | 2030 | $2.0T (was 2028) | Bank, digital assets |
| Citi Institute | 2026-06-01 | Tokenized assets (bear/base/bull) | 2030 | $2.7T / $5.5T / $8.2T | [Interested source] |
| Citi Institute | 2026-06-01 | Stablecoins | 2030 | $1.9T | [Interested source] |
| McKinsey | 2024 | Tokenized, ex-crypto | 2030 | about $2T ($1-4T) | [Interested source] |
| BCG and Ripple | 2025-04-07 | Tokenized, ex-crypto and CBDC | 2033 | $18.9T (2030: $9.4T) | [Interested source] |
| BCG and ADDX | 2022 | Illiquid assets tokenized | 2030 | $16.1T | [Interested source] |
| Bernstein | 2025 | Stablecoins | 2035 | $4T | Single secondary source |
| JPMorgan | 2025-07 | Stablecoins | 2028 | $0.5T | Bank, Kinexys |
| TBAC | 2025 | Stablecoins | 2028 | $2T | Via BIS WP 1270 |
| 21.co | not found | NA | NA | NA | Gap |

Fact: Forecasts differ because of metric (stablecoins vs securities), scope (McKinsey excludes stablecoins and deposits; Citi counts securities on chain; BCG/Ripple excludes crypto and CBDC), vintage, and sponsor. Citi's present market of about $17B differs from RWA.xyz distributed $39.4B and represented $396B, so even the starting point is contested. [Moderate]

Fact on N8 (forecast cuts): StanChart delayed 2028 to 2030 (2026-10-14). JPMorgan cut to $500B by 2028 (2025-07). BCG's 2030 figure fell from $16.1T (2022) to $9.4T (2025), though scope differs. Citi's 2030 base is $5.5T and was not cut. N8 is supported for stablecoins, mixed for tokenized assets. [Low]

Inference: My range (method: scenario CAGR mixtures from observed levels, weighted by the probabilities above).

| Metric | P10 | Median | P90 |
|---|---|---|---|
| S 2030 | $0.38T | $0.55T | $1.3T |
| T 2030 | $0.06T | $0.12T | $0.45T |
| S 2035 | $0.5T | $1.1T | $3.5T |
| T 2035 | $0.15T | $0.6T | $3.0T |

Inference: My S 2030 median is a quarter of StanChart's and my T 2030 median is about 2% of Citi's base. Citi's figure counts a different universe, so the gap partly reflects definition, not only judgment. [Low]

### 6. Historical analogs (see `data/analog_curves.csv`)

| Analog | Years to 10% | Years to 50% | Value captor | Lesson | Conf |
|---|---|---|---|---|---|
| Pix (2020-11) | Not found | about 4.6 (50.9% of retail transactions, H1 2025; 54.7% H2 2025) | Central bank utility; fintechs and banks distribute; card and TED fees lost | Public mandate plus free pricing, not technology, drove speed | [Moderate] |
| UPI (2016) | Not found | Not found; 85.5% of digital volume by H2 2025 (about 9.6 years) | NPCI and wallet apps; banks lost fees | Share of volume far exceeds share of value (UPI 9.5% by value) | [Moderate] |
| M-Pesa (2007) | Not found | 40% of adults in about 2.5 years; about two-thirds later | Mobile operator | Entrant with distribution and an unbanked market wins fast | [Low] |
| EMV US (2015) | Not found | about 3.5 years to 99% of volume | Networks and issuers | A liability shift forced migration in years | [Low] |
| US MMFs (1971) | Not computed | Not computed; $4B (1977) to $185B (1981); $7.98T 2026 | Fund sponsors | Regulatory arbitrage (Reg Q) created demand; took a decade to scale | [Low] |
| T+1 US (2024-05-28) | NA | Mandated | Incumbent utilities | Rule change delivers speed without DLT | [Unverified] |
| SWIFT, FX e-trading, bank cloud | NA | NA | Incumbents or hyperscalers | Not verified this session | [Unverified] |
| Failed consortia | NA | Never reached | None | TradeLens (4 years to shutdown), we.trade (2022), ASX CHESS (about 6 years, cancelled 2022-11) | [High] |

Inference: Fast analogs share a mandate, a subsidy, or an unmet need (unbanked, high card fees). Tokenization has none of the three in the US and EU retail context, which argues against a 2030 Bull. It does have a regulatory clock (T+1 2027, GENIUS 2027). [Moderate]

Inference: Current tokenized Treasuries are 0.18% of US MMF assets about 2.6 years after BUIDL. Reaching 10% of MMF assets would need 50x growth. [Low]

## Gaps and unresolved

| Gap | Effect |
|---|---|
| Search limit hit after 28 searches; not searched: 21.co, Kinexys, Canton and Fnality volumes, UK DIGIT, mBridge, Fed payment account, bank cloud, FX e-trading | W measure has no series; interop and technical scores low confidence |
| McKinsey and BCG primary reports not read | Forecast values secondary |
| Midterm election result (2026-11-03) and third digital euro trilogue (2026-09-30) outcomes | Political durability and EU timeline scores |
| Pre-2025 timeline rows are training knowledge | Marked `unverified` |
| Stablecoin total differs by source ($295B to $309B) | Use DefiLlama range |

## Files written

`/home/user/Grotesque-Sublime/research/ws/ws3.md`, `timeline.csv`, `data/driver_tree.csv`, `data/analog_curves.csv`, `data/forecasts.csv`, `ws/search_log_ws3.md`.
