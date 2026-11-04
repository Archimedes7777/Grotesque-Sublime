# WS4: Where value accrues, value chain economics and who benefits

Date: 2026-11-04. Search budget: 18 of 40 searches completed, then the shared web-search limit blocked three more; 19 of 20 fetches used (one failed with HTTP 503). Layers and topics without a fetched source are marked [Unverified].

## Summary

Fact: the clearest value capture today is in float income and distribution, not in blockchains. Circle earned $657.6M of reserve income in Q3 2026 and paid $409.2M (62%) in distribution and transaction costs. Tether reported about $1.5B net operating profit for Q3 2026 with no comparable revenue share disclosed.

Fact: public-chain fee revenue is small next to issuer float. Ethereum gross revenue was $127M in H1 2026 (down 69% year on year); Solana REV was $140.8M in H1 2026; Canton burned $155M of fees in Q3 2026. ETH burn offset only 2.1% of issuance in the ledger to 2026-10-09.

Inference [Moderate]: institutional flow leaks to intermediary equity (issuers, distributors, custodians, asset managers) rather than to network tokens. Base is the cleanest example: no token, Coinbase keeps the sequencer margin.

Inference [Low]: stablecoin issuer earnings are rate-sensitive. A 100 bp cut removes about $739M gross reserve income from Circle (about $276M after distribution, roughly half of ex-ARC annualized adjusted EBITDA) and $1.3B to $1.8B from Tether (22% to 31% of its run-rate profit). The Fed raised to 3.75% to 4.00% in September 2026 and held on 2026-10-28, so near-term risk is a pause, not cuts.

Fact: fee pools at risk are modest against the pools. Cross-border revenue is about $293B (McKinsey); my estimate of loss by 2030 is 1% to 4%. Bank-deposit outflow estimates range from $182B (Citi low) to $908B, versus a White House CEA baseline of about $300B stablecoin share. Several topics (identity, PQC, legal finality, insolvency remoteness, geopolitics) were not researched and are listed as gaps.

## Key numbers

| Metric | Value | Date | Source | Confidence |
|---|---|---|---|---|
| Circle total revenue and reserve income | $864.9M (17% YoY); $182M is ARC token presale | 2026-09-30 | Circle Q3 release via investingnews.com, cross-checked with The Block 2026-11-04 | [High] |
| Circle reserve income, return rate | $657.6M (-8% YoY); 3.5% (-61 bp YoY) | 2026-09-30 | same | [High] |
| Circle distribution and transaction costs | $409.2M (62% of reserve income, 47% of total revenue) | 2026-09-30 | same | [High] |
| Circle USDC, period end and average | $73.9B; $73.3B | 2026-09-30 | same | [High] |
| Circle adjusted EBITDA (new definition) | $316.7M, of which ARC presale about $182M | 2026-09-30 | same | [Moderate] |
| Tether Q3 net operating profit | about $1.5B; YTD about $4.5B; excess reserves $7.95B | 2026-09-30 | BDO attestation via Crypto Briefing 2026-10-30 [Interested source: issuer data] | [Low] |
| Tether Treasury exposure; supply | about $132.4B; about $184B | 2026-09-30 | same | [Low] |
| Coinbase stablecoin revenue | $307M Q3 2026 (+5% QoQ); avg USDC on platform $22B | 2026-09-30 | Coinbase Q3 call coverage 2026-10-29 | [Moderate] |
| Coinbase stablecoin revenue Q2 2026 | $292.1M; corporate balance income $65.8M reclassified | 2026-06-30 | SEC 10-Q (coin-20260630) | [High] |
| Tokenized RWA distributed, Ethereum | $15.13B | 2026-11-04 | RWA.xyz networks page | [Moderate] |
| Tokenized Treasuries and MMFs | $14.68B; BUIDL $2.17B | 2026-10-16 | RWA.xyz via FinanceFeeds | [Moderate] |
| Fed funds target range | 3.75% to 4.00% | 2026-10-28 | federalreserve.gov FOMC statement | [High] |
| BIS stablecoin to T-bill effect | $3.5B inflow: -0.71 bp impact, about -4 bp at 10 days | data to 2026-03 | BIS Working Paper 1270 | [High] |
| Cross-border payments revenue pool | $293B on $191T flows | 2024 | McKinsey via search summary (page fetch failed) | [Moderate] |
| US card swipe fees all-in | $198.25B | 2025 | Merchants Payments Coalition citing Nilson [Interested source] | [Low] |

## Body

### 1. Layer table

Labels: each row is Inference unless the pool column is a cited Fact. Full detail and URLs in `data/value_chain.csv`.

| Layer | Revenue pool (dated) | Winner | Moat | Commoditizes | Pricing power 2030 | Confidence |
|---|---|---|---|---|---|---|
| issuance | Circle $2.63B reserve income run-rate; Tether about $6.0B profit run-rate (2026-Q3) | Tether (profit), Circle (scale, low retention) | balance sheet, distribution | Partial | med | [Low] |
| reserve_mgmt | about $10B gross float pool (supply x 3.5%) | issuers themselves | balance sheet | Y | low | [Low] |
| custody | State Street fee revenue about $11B (FY2025, all servicing); BNY $14.3B fees | bank custodians | balance sheet, licence, switching | Partial | med | [Moderate] |
| settlement_clearing | no dated pool found | DTCC, Euroclear; Canton emerging | licence, network | N | high | [Low] |
| tokenization_platform | about $22M to $73M (fees on $14.68B AUM) | BlackRock, Franklin, Ondo, Circle USYC | brand, switching | Y | low | [Low] |
| l1_l2_infra | about $1.3B across four chains (mixed periods) | Canton, Solana, Ethereum, Base | network effect | Y | low | [Low] |
| validators_staking | Lido about $590M trailing 1y gross (scope ambiguous) | Lido, exchanges | scale | Y | low | [Low] |
| oracles_data | not researched | Chainlink (unverified) | network | Partial | med | [Unverified] |
| compliance_identity | not researched | not verified | licence, data | Partial | med | [Unverified] |
| wallets_distribution | Circle distribution about $1.64B run-rate; Coinbase stablecoin about $1.23B | Coinbase | distribution | N | high | [Moderate] |
| exchanges_ats | Coinbase about $4.9B revenue run-rate (cyclical) | Coinbase, Kraken, Robinhood | network, licence | Partial | med | [Low] |
| treasury_software | not researched | not verified | switching | Partial | med | [Unverified] |
| insurance | Nexus Mutual fees $3.3M trailing 1y; rest not researched | not verified | balance sheet | N | med | [Unverified] |
| legal_audit | not researched | Big Four, BDO | licence | N | med | [Unverified] |
| tax_reporting | not researched (WS7) | not verified | switching | Partial | med | [Unverified] |
| payments_network | $198B US swipe all-in (2025) | Visa, Mastercard | network, licence | N | med | [Low] |
| asset_management | same $22M to $73M tokenized-fund fee pool | BlackRock, Franklin | brand, distribution | Y | low | [Low] |
| banking | deposit stock at risk, not revenue | JPMorgan, Citi, BNY | balance sheet, deposit insurance | N | med | [Low] |

Inference [Moderate]: the pricing-power split is distribution and regulated balance sheets high, protocol and fund-wrapper layers low. Circle's 62% payout to partners is the single strongest datapoint.

### 2. Issuer economics (G3, G5)

Fact: Circle Q3 2026 reserve income $657.6M, distribution and transaction costs $409.2M, total distribution, transaction and other costs $411.6M, operating expenses $245M (+16%), 5% workforce reduction (Source: Circle Q3 release via investingnews.com and The Block, 2026-11-04).

Fact: Coinbase stablecoin revenue was $307M in Q3 2026 and $292.1M in Q2 2026; the 10-Q does not disclose amounts paid to Circle or the revenue-share percentage (Source: SEC 10-Q for 2026-06-30; Q3 call coverage 2026-10-29). The Coinbase share of Circle's $409M is therefore not verified.

Inference [Moderate]: Circle distribution cost share of reserve income fell from 62.9% (Q3 2025: $447.2M over $711.2M) to 62.2% (Q3 2026). Retention is about 37%, so reserve rate moves hit Circle at about 0.37 of face.

Rate sensitivity arithmetic, per 100 bp lower reserve yield (Inference [Low]; assumes full pass-through to reserves, constant supply, constant payout ratio):

| Item | Circle | Tether |
|---|---|---|
| Reserve base | $73.9B USDC (2026-09-30) | $132.4B Treasuries, or $184B total |
| Gross income change | $73.9B x 1.00% = -$739M per year | -$1.32B (Treasuries only) to -$1.84B (all supply) |
| Retained after distribution | x 0.374 = -$276M | no disclosed payout: assume about 100% |
| Baseline | ex-ARC adj. EBITDA about ($316.7M - $182M) x4 = $540M | Q3 profit $1.5B x4 = $6.0B |
| Share of baseline | about -51% | -22% to -31% |

Recommendation [Low]: for WS5, treat Circle earnings as a levered short-rate bet. Kill criterion: USDC supply growth above about 40% a year (company guidance) offsetting each 100 bp cut. Also note the ex-ARC baseline treats the whole presale as margin, which is my assumption.

Inference [Low]: Tether keeps more of the float than regulated issuers because no revenue-share disclosure exists; profit per supply dollar is about 3.3% against Circle's roughly 1.3% retained. Tether is an interested source and the BDO attestation was read only through press.

### 3. Who loses: fee pools at risk

Detail and sources in `data/fee_pools_at_risk.csv`.

| Pool | Annual revenue | Share at risk 2030 | Label and tag |
|---|---|---|---|
| Cross-border payments (McKinsey) | $293B (2024) | 1% to 4% | Inference [Low] |
| US card swipe fees all-in | $198.25B (2025) | 0.5% to 2% | Inference [Low] |
| Bank deposits | stock, not revenue | 1% to 5% of about $17.6T implied | Inference [Low] |
| Custody (State Street proxy) | about $11B (FY2025) | 0% to 3% | Inference [Low] |
| Remittance, transfer agents, FX, correspondent banking | not obtained | NA | [Unverified] |

Fact: McKinsey puts low-value cross-border flows at about 10% of volume and one third of the revenue pool (Source: McKinsey cross-border payments, via search summary, 2025).

Fact: World Bank RPW average remittance cost is 6.36%; banks 14.99%, digital 4.59% (Source: World Bank RPW Issue 54 via secondary summary, 2026-04). Inference [Moderate]: the price gap is where disruption concentrates, but I lack a volume figure to size it.

Fact: incumbent custodians grew in 2025: State Street fee revenue about $11B (+9%) and BNY fee revenue $14.3B versus $13.4B in 2024 (+7%). Northern Trust launched a tokenized MMF share class (Source: company annual reports and press, 2026). Inference [Low]: displacement is not yet visible in filings.

### 4. Macro and geopolitical

Fact: BIS Working Paper 1270 finds a $3.5B (2 standard deviation) stablecoin inflow lowers 3-month T-bill yields about 0.71 bp on impact and about 4 bp within 10 days, with no spillover to longer maturities and larger effects under stress (Source: BIS, 2025-05-28, data to March 2026). A secondary summary says redemptions raise yields two to three times as much; not verified.

Inference [Moderate]: with Tether holding about $132B of Treasuries exposure, the issuer sector is a structural short-end buyer, but the yield effect is small in normal conditions and matters mainly in run or stress.

Fact: White House CEA (April 2026, page dated 2026-09-15) estimates a stablecoin yield ban would add $2.1B of bank lending at a 1.7% deposit share and $11.1B at 10%; the extreme stacked case is $531B (4.4% of loans). The $6.6T TBAC "at risk" figure appears via CRS and Forbes summaries; I could not fetch the TBAC source [Unverified]. Outflow forecasts: Standard Chartered up to $500B by 2028; Citi $182B to $908B by 2030 (Source: The Block 2026-01-27; Bloomberg 2026-01-27).

Fact: Fed held at 3.75% to 4.00% on 2026-10-28 (10 to 2, both dissenters wanted a hike); September 2026 raised by 25 bp per secondary press (Source: federalreserve.gov, 2026-10-28). Inference [Low]: rising-rate risk raises issuer income near term, and the reverse is the larger long-run concern.

Not researched, [Unverified]: dollar dominance versus e-CNY and mBridge, sanctions evasion and enforcement, privacy politics, tax automation. WS2 and WS6 should cover them.

### 5. Token versus equity value capture

Full numbers in `data/token_value_capture.csv`. Chain-level figures exclude app fees; DefiLlama "chain" totals include app fees and so overstate token capture.

| Chain | Annual fee revenue (basis) | RWA on chain (2026-11-04) | Accrues to | Mechanism and reasoning |
|---|---|---|---|---|
| ethereum | about $254M (H1 2026 x2) | $15.13B distributed | mixed | Burn offsets 2.1% of issuance; token value is collateral and staking demand, not fees |
| solana | about $282M (REV H1 x2) | $4.92B | mixed | 72% of Q2 REV to validators, 26% to holders |
| base | about $130M sequencer (H1 x2) | $0.64B | equity | No token; Coinbase keeps margin |
| avalanche | about $3M gas (1 day x365) | $1.50B distributed; $11.4B represented | mixed | Mostly equity of issuers; token fee link not verified |
| stellar | about $0.5M | $4.11B | equity | Fees negligible; issuer and anchor equity |
| xrpl | about $0.17M | $0.64B distributed; $5.0B represented | equity | Fees negligible |
| canton | about $621M (Q3 burn x4) | $349B represented (repo notional) | mixed | Burn is real but minted rewards offset it and flow to apps and operators |
| polygon | about $23M (1 day x365) | $0.48B distributed | equity | Fee mechanism not verified |
| arbitrum | about $5M (1 day x365) | $1.12B | equity | ARB fee claim not verified |

Inference [Moderate]: tokenized-RWA holders pay the asset manager (0.15% to 0.50%) and the issuer; chain fees on $14.68B of tokenized Treasuries are trivial, so institutional use of public chains does not translate into token cash flow. The exception is Canton, where fees scale with synchronizer traffic, and the burn is still partly offset by minting [Low].

Caveat: RWA.xyz "represented" values (Canton $349B) are not comparable with "distributed" values; do not rank chains on them.

### 6. Additional topics (brief)

| Topic | Note | Tag |
|---|---|---|
| Custody rules | Fact: SAB 122 (2025-01-23) rescinded SAB 121; custodians now apply contingency-loss rules; it removes an accounting barrier but not operational ones (Source: NatLawReview and XBRL.org summaries, 2025). No 2026 bank launches found | [Moderate] |
| Tokenized MMF fees (G7) | Fact: BENJI 0.20% (0.15% in one guide), BUIDL 0.50% per third-party guides; tokenized Treasuries $14.68B (2026-10-16). No fee-trend source found, so compression is not demonstrated | [Low] |
| Other additional topics | eIDAS 2.0, PQC, tokenized carbon, real estate, DeFi convergence, deposit insurance, legal finality, prime brokerage, staking ETFs, smart contract insurance: not researched | [Unverified] |

### 7. Counterfactual (G6) and G11

Inference [Low]: the 2025 custodian filings and the Northern Trust tokenized share class support a "incumbents absorb tokenization" reading, because fee revenue grew 7% to 9% while they adopted the wrapper. Evidence is thin and covers one year.

G11 (legal enforceability of tokenized title, reserve insolvency remoteness): not researched [Unverified].

## Gaps and unresolved

- Coinbase's share of Circle's $409M distribution costs (neither the Circle release nor the 10-Q excerpt gave it).
- Tether primary attestation not read; supply differs between DefiLlama ($177.8B) and the attestation ($184B).
- McKinsey and TBAC primary pages not read (HTTP 503; not found).
- Chain fee scope: DefiLlama totals mix app fees; token burn mechanics for AVAX, XLM, XRP, POL, ARB unverified.
- Not researched: oracles, compliance and identity, treasury software, insurance, legal and audit, tax; remittance and correspondent volumes; geopolitics; G11; most additional topics.
- Three queries (staking ETFs, GENIUS Act rules, small-chain fees) were blocked by the web-search limit.

## Files written

- `/home/user/Grotesque-Sublime/research/ws/ws4.md`
- `/home/user/Grotesque-Sublime/research/data/value_chain.csv`
- `/home/user/Grotesque-Sublime/research/data/fee_pools_at_risk.csv`
- `/home/user/Grotesque-Sublime/research/data/token_value_capture.csv`
- `/home/user/Grotesque-Sublime/research/ws/search_log_ws4.md`
