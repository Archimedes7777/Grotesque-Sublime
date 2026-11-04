# Shared schema (binding on all agents)

Date: 2026-11-04. Any agent that finds an entity not listed here uses the naming pattern below and flags it as `[New entity]` in its file.

## 1. Labeling and confidence rules

- Every paragraph or table row in a workstream body begins with, or has a column for, one of: **Fact**, **Inference**, **Recommendation**.
  - Fact: directly stated by a cited source. Carries `(Source: publisher, title or doc ID, YYYY-MM-DD, URL)`.
  - Inference: your reasoning from one or more facts. Carries a confidence tag.
  - Recommendation: an action. Carries a confidence tag and a kill criterion where relevant.
- Confidence tags:
  - `[High]`: two or more independent primary or top-tier sources agree, or the claim is a direct reading of law or audited filings; low sensitivity to assumptions.
  - `[Moderate]`: one primary source, or two secondary sources; or an inference that depends on one material assumption.
  - `[Low]`: single secondary source, interested source, or an inference resting on several assumptions.
  - `[Unverified]`: could not confirm with a fetched source in this session. Do not use as a driver of conclusions.
  - `[Single source]`: a number that drives a conclusion but has only one source.
  - `[Interested source]`: the source has a financial stake in the thesis (issuer, token foundation, VC, consultancy selling implementation, exchange). Place next to the citation.
  - `[SEO-shaped]`: content farm or affiliate-marketing source. Avoid; if used, flag.
- Dates: ISO `YYYY-MM-DD`. Money: USD unless stated, with "as of" date. Write `$1.2B (2026-09-30)`.
- No em dashes. Prose blocks no longer than four lines.

## 2. Controlled vocabulary

### 2.1 Instrument types (`instrument_type`)

| Canonical value | Definition | Not to be confused with |
|---|---|---|
| `payment_stablecoin` | Fiat-referenced token redeemable at par, backed by reserves, issued by a non-bank or bank subsidiary (GENIUS Act "permitted payment stablecoin issuer" in US; MiCA "e-money token" in EU) | tokenized deposit |
| `offshore_stablecoin` | Fiat-referenced token not issued under a US or EU regime (e.g., USDT as of research date unless verified otherwise) | |
| `synthetic_dollar` | Dollar-tracking token backed by derivatives or crypto collateral (e.g., USDe, DAI/USDS) | payment_stablecoin |
| `tokenized_deposit` | Deposit liability of a regulated bank represented on a ledger; holder is a bank depositor | stablecoin |
| `tokenized_mmf` | Share of a registered or private money market or Treasury fund recorded on a ledger | stablecoin |
| `tokenized_treasury` | Direct or fund-wrapped US Treasuries on a ledger (RWA.xyz category) | |
| `tokenized_private_credit` | Loans or credit fund interests on a ledger | |
| `tokenized_equity` | Share or economic-exposure token of a listed or private company. Sub-type required: `native` (legal share on ledger), `wrapped` (SPV or custodial receipt), `synthetic` (derivative) | |
| `tokenized_bond` | Debt security issued natively or represented on a ledger | |
| `tokenized_fund` | Non-MMF fund shares on a ledger | |
| `tokenized_commodity` | Gold, other commodity tokens | |
| `tokenized_real_estate` | Title, SPV, or REIT units on a ledger | |
| `rcbdc` | Retail CBDC | |
| `wcbdc` | Wholesale CBDC | |
| `network_token` | Native token of a public chain or protocol (ETH, SOL, LINK, XRP, etc.) | |

### 2.2 Canonical entity names (use the left column only)

| Canonical | Aliases to map |
|---|---|
| Kinexys (JPMorgan) | JPM Coin, Onyx, JPMD, Kinexys Digital Payments, Kinexys Digital Assets |
| Citi Token Services | Citi tokenized deposits |
| BNY | BNY Mellon |
| HSBC Orion | HSBC tokenization platform; HSBC Tokenised Deposit Service (list separately as product) |
| BlackRock BUIDL | BlackRock USD Institutional Digital Liquidity Fund |
| Franklin BENJI | Franklin OnChain U.S. Government Money Fund (FOBXX), Benji Investments |
| Circle | Circle Internet Group, CRCL; products USDC, EURC, CPN, Arc |
| Tether | USDT, USAT if launched |
| Paxos | USDP, PYUSD issuer, USDG issuer, Paxos Trust |
| Ripple | RLUSD, Ripple Payments, Hidden Road acquisition (Ripple Prime) |
| Digital Asset (Canton) | Canton Network, Digital Asset Holdings, Canton Coin (CC) |
| Chainlink | Chainlink Labs, CCIP, LINK |
| SWIFT | Swift |
| DTCC | DTCC Digital Assets, Project Ion, DTCC Collateral AppChain |
| SDX | SIX Digital Exchange |
| Fnality | Fnality International, Fnality Payment System (FnPS) |
| Partior | |
| Project Agora | Project Agorá (BIS) |
| mBridge | Project mBridge |
| Tempo | Stripe and Paradigm payment chain |
| Base | Coinbase L2 |
| Arc | Circle L1 |
| Securitize | |
| Ondo | Ondo Finance, Ondo Global Markets, OUSG, USDY |
| GENIUS Act | Guiding and Establishing National Innovation for U.S. Stablecoins Act (Public Law number to be verified) |
| CLARITY Act | Digital Asset Market Clarity Act; Senate market structure bill (record exact Senate title) |
| MiCA | Markets in Crypto-Assets Regulation (EU) 2023/1114 |
| e-CNY | Digital renminbi, e-CNY |
| Digital euro | |

Pattern for new entities: legal or brand name as used in the entity's most recent primary filing, parent in parentheses.

### 2.3 Rails (`rail`)

`ach`, `fedwire`, `chips`, `swift_gpi`, `fednow`, `rtp`, `card_visa`, `card_mastercard`, `pix`, `upi`, `sepa_inst`, `target2`, `dtc_nscc`, `euroclear`, `clearstream`, `public_chain`, `permissioned_chain`, `hybrid_chain`.

### 2.4 Chains (`chain`)

`ethereum`, `base`, `arbitrum`, `optimism`, `polygon`, `solana`, `avalanche`, `canton`, `hedera`, `xrpl`, `stellar`, `tron`, `bnb`, `aptos`, `sui`, `tempo`, `arc`, `plasma`, `stable`, `ton`, `kinexys_private`, `other:<name>`.

### 2.5 Jurisdictions (`jurisdiction`)

ISO 3166 alpha-2, with `US-CA` for California, `EU` for EU-level law, `INTL` for BIS, FSB, FATF, IOSCO, Basel.

### 2.6 Value-chain layers (`layer`)

`issuance`, `reserve_mgmt`, `custody`, `settlement_clearing`, `tokenization_platform`, `l1_l2_infra`, `validators_staking`, `oracles_data`, `compliance_identity`, `wallets_distribution`, `exchanges_ats`, `treasury_software`, `insurance`, `legal_audit`, `tax_reporting`, `payments_network`, `asset_management`, `banking`.

### 2.7 Status (`status`)

`live`, `pilot`, `design`, `paused`, `cancelled`, `banned_by_law`, `announced`, `renamed`, `abandoned`.

### 2.8 Tiers and horizons

- Tier: `Retail` (non-accredited, public markets), `Mid` (accredited, $250k to $5M deployable), `Large` ($5M and up, institution).
- Horizon (from 2026-11-04): `Short` (to 2027-11), `Medium` (2027-11 to 2029-11), `Long` (2029-11 to 2036-11).

## 3. Scenario definitions (provisional thresholds; WS3 may recalibrate with stated reason)

Measures: S = global fiat-backed stablecoin supply; T = tokenized RWA ex-stablecoins (RWA.xyz-style definition: Treasuries, MMFs, private credit, bonds, equities, commodities, funds; excludes stablecoins); W = share of a named legacy wholesale flow (repo, collateral, cross-border bank-to-bank) settled on DLT.

| Scenario | 2030 | 2035 | Narrative anchor |
|---|---|---|---|
| Bear | S < $600B; T < $150B; W < 0.5% | S < $1T; T < $500B; W < 1% | Stablecoins remain crypto-trading and offshore-dollar plumbing. Tokenization stays a pilot niche. Incumbent rails modernize without DLT. |
| Base | S $600B to $2T; T $150B to $1.5T; W 0.5% to 3% | S $1T to $4T; T $0.5T to $5T; W 1% to 10% | Regulated stablecoins become a mainstream payment and treasury instrument. Tokenized MMFs and Treasuries are standard collateral. Wholesale DLT handles a meaningful minority of repo and collateral. |
| Bull | S > $2T; T > $1.5T; W > 3% | S > $4T; T > $5T; W > 10% | Programmable ledgers become a primary settlement layer for securities and cross-border payments; major exchanges run 24/7 tokenized venues; agentic payments material. |

Assignment rule: a scenario "occurs" if at least two of the three measures fall in its band.

## 4. CSV column specifications

All CSVs: UTF-8, comma-separated, header row, ISO dates, one fact per row, no merged cells. Every CSV has `source_url` and `source_date`. Use `NA` for not available; never blank.

### `data/adoption_<series>.csv`
`series_id, metric, instrument_type, entity, chain, jurisdiction, date, value, unit, method_note, source_name, source_url, source_date, interested_source (Y/N), confidence`

### `timeline.csv` (WS3)
`date, date_precision (day|month|quarter|year), event, category (law|rule|go_live|central_bank|launch|etf|ipo|other), jurisdiction, entity, status (occurred|scheduled|expected|speculative), impact (low|med|high), scenario_signal (bear|base|bull|neutral), source_url, source_date, confidence`

### `institutions.csv` (WS2)
`entity, parent, entity_type (central_bank|regulator|bank|asset_manager|market_infra|payments|crypto_native|tech|consortium), jurisdiction, public_private, ticker, role (rule_setter|rail_builder|issuer|distributor|reserve_holder|custodian), shipped, announced, revenue_or_aum_tied, metric_date, exposure_route, exposure_purity (high|med|low), source_url, source_date, confidence`

### `plays.csv` (WS5 master; WS8 writes `data/plays_ws8.csv`, WS9 writes `data/plays_ws9.csv` with the same columns)
`play_id, vehicle, ticker_or_route, layer, thesis, tier, horizon, return_band_annual_pct (low to high), return_method (comps|revenue_pool_share|base_rate_analog|yield|reverse_dcf), return_method_detail, valuation_snapshot (metric and date), key_risk, catalyst, catalyst_date, kill_criterion, liquidity (daily|weekly|quarterly|locked), min_investment_usd, accredited_required (Y/N), regulatory_exposure (low|med|high), tax_character, account_placement, crowding (low|med|high), confidence, source_ws, source_url, source_date`

### `risks.csv` (WS6)
`risk_id, category (regulatory|technical|financial|market|operational|structural), risk, probability_5y (low|med|high and pct), severity (1 to 5), plays_hit (play_id list or layer), early_warning_signal, signal_data_source, signal_url, threshold_trigger, source_url, source_date, confidence`

### `tax_matrix.csv` (WS7)
`vehicle_class, example, federal_character, holding_period_rule, wash_sale_applies (Y/N/Unclear with date), income_timing, reporting_form, pfic_risk (Y/N), qsbs_eligible (Y/N/NA), sec1256 (Y/N), ca_conformity (conforms|diverges with note), taxable_ok, trad_ira_ok, roth_ok, 401k_window_ok, notes, verify_with_cpa (Y/N), source_url, source_date, confidence`

### `jurisdictions.csv` (WS9)
`jurisdiction, cbdc_status, cbdc_name, stablecoin_regime, tokenized_securities_framework, key_law_or_reg, adoption_metric, adoption_value, adoption_date, dominant_players, capital_controls, foreign_investor_tax_note, us_investor_access_route, return_outlook (outsized|neutral|loss_risk), rationale, source_url, source_date, confidence`

### `scenario_results.csv` (Phase 2)
`run, scenario, probability_2030, probability_2035, driver, driver_delta, prob_shift, note`

## 5. File structure for each `ws/wsN.md`

```
# WSN: <title>
## Summary            (300 words max)
## Key numbers        (table: metric | value | date | source | confidence)
## Body               (6,000 words max; sections per brief; F/I/R labels)
## Gaps and unresolved
## Files written
```
