# Research Mandate v2: Programmable Ledgers, Digital Money, and the Investment Map

You are the research lead for a multi-phase, multi-agent investigation. Today's date is in the environment. Treat the current state of law, products, prices, institutions, and roles as unknown until verified by search. Training data is stale for this subject. Verify before asserting.

## 0. Investor parameters (fill in or keep defaults)

| Parameter | Value |
|---|---|
| Home jurisdiction (federal, state) | US, California |
| Deployable capital, personal case | $50,000, cash on hand (not currently invested) |
| Accredited investor status | No |
| Risk tolerance (max tolerable drawdown on this sleeve) | 40% |
| Liquidity need (earliest date capital may be needed) | None stated; 10-year horizon (~2036) |
| Existing exposure to the theme (tickers, tokens, funds) | None |
| Account types available (taxable, IRA, Roth, 401k brokerage window) | Taxable brokerage, cash account (no margin) |
| Constraints (no leverage, no direct token custody, ESG, etc.) | None stated |
| Time available per week for monitoring | 1 hour |

If a field is blank, state the assumption you use in `assumptions.md` and proceed. The personalized section (Phase 3, file `personalized_plays.md`) uses this table. The three canonical tiers (Retail, Mid, Large) are always produced regardless.

## 1. Operating rules

1. Work in the current directory. Create `./research/`, `./research/data/`, `./research/ws/`. Every artifact is a file. Nothing lives only in chat.
2. Phase 0 must finish before any workstream launches. It produces the shared schema that all agents use.
3. Subagents: one per workstream, launched concurrently. Each brief is self-contained: paste the workstream section, Section 1 (these rules), `schema.md`, and the relevant block of `queries.md`. Agents do not see each other's output. If your environment lets you choose a model per subagent, use the strongest available model for synthesis, verification, and red team, a mid-tier model for workstream collection, and the cheapest model for source triage and deduplication.
4. Source hierarchy, highest first: central bank and BIS publications, legislation and regulator releases (Federal Register, SEC, CFTC, OCC, FDIC, Treasury, FSB, FATF, IOSCO, EU Official Journal, UK HMT/FCA/BoE, MAS, HKMA, FINMA), audited filings (10-K, 10-Q, 20-F, annual reports, prospectuses), earnings call transcripts, consortium technical papers, peer-reviewed or NBER/IMF/BIS working papers, major financial press (FT, WSJ, Bloomberg, Reuters), then everything else. Crypto-native media, project blogs, and foundation posts are acceptable for product facts only, never for market sizing, adoption, or return claims.
5. Every factual claim carries an inline source and the source's publication date. Every number that drives a conclusion is cross-checked against a second independent source or flagged `[Single source]`.
6. Confidence tags on every inference and recommendation: `[High]`, `[Moderate]`, `[Low]`. Anything unverified: `[Unverified]`. Within every section, label paragraphs or table rows as Fact, Inference, or Recommendation.
7. State every assumption and judgment call in `assumptions.md` as you go. Do not ask the user questions. Make the reasonable call and record it.
8. Search discipline: log every query and the URLs used to `search_log.md`. Use the search tool's extended or deep mode for niche, recent, or numeric facts. Fetch full documents for anything load-bearing, never rely on snippets. Per workstream budget: 40 searches and 20 full fetches. Stop when the marginal search stops changing the workstream summary.
9. Context discipline: each workstream file begins with `## Summary` (300 words max) and `## Key numbers` (a table). Body is capped at 6,000 words. Raw data goes to CSV files in `./research/data/` with a source URL column, not into prose.
10. Ownership rules to prevent duplication: WS2 owns institution and regulator facts. WS9 owns non-core jurisdictions. WS4 owns value chain economics and references WS2 by institution name without re-researching. WS5 owns plays and references WS4 layers. WS7 owns tax. WS8 owns agentic payments. All others link rather than repeat.
11. No em dashes anywhere. Tables for comparisons and data. Prose blocks no longer than four lines. Numbers carry units and dates.
12. Reject promotional framing. When a source has a financial interest in the thesis (issuer, venture fund, token foundation, consultancy selling implementation), say so next to the citation. Flag SEO-shaped sources.
13. Red team is mandatory and runs twice (Phase 5 and Phase 6). Dissent is preserved verbatim in the report.
14. Final sentence of `REPORT.md`: this is research, not individualized financial, legal, or tax advice, and the reader should verify current facts and consult licensed advisors before acting.

## 2. Core question

Is the global financial system moving toward programmable ledgers (tokenized deposits, tokenized securities, stablecoins, CBDCs, DLT settlement, unified ledgers, agent-initiated payments) in a way that materially changes where value accrues? If so: how likely is each stage, on what timeline, driven by whom, and what positions could a retail investor, a mid-scale investor (accredited, roughly $250k to $5M deployable), and a large-scale investor (family office, fund, institution, $5M and up) take now, across short (0 to 12 months), medium (1 to 3 years), and long (3 to 10 years) horizons, to capture the largest risk-adjusted after-tax return? Who is set to benefit most, and what does it take to be among them?

## 3. Phase 0: Mandate critique and shared schema (before any research)

Write these files:

1. `plan.md`: a critique of this mandate. List ambiguities, missing questions, overlapping scopes, and anything a skeptical portfolio manager would ask that this document does not. Add each gap you find to the relevant workstream brief before launching it. This step is recursive: the mandate improves itself before execution.
2. `schema.md`: controlled vocabulary (canonical names for every instrument type, rail, chain, institution, and jurisdiction so agents do not produce "JPM Coin" and "Kinexys" as separate entities), the exact column specs for every CSV deliverable in Section 6, the confidence tag definitions, and the Fact/Inference/Recommendation labeling rule.
3. `queries.md`: 10 to 20 seed queries per workstream, including exact terms that must be searched (named laws, named projects, named consortia, named data series). Mark queries whose results are expected to have changed in the last 12 months.
4. `null_hypothesis.md`: the strongest case that this entire theme is narrative with little real settlement migration. WS0 is assigned to test it.

## 4. Phase 1: Workstreams (concurrent subagents)

### WS0. Is it actually happening? Hard adoption data and the null hypothesis
- Pull dated, sourced time series: stablecoin supply and on-chain transaction volume (separating wash and bot volume with method stated), tokenized Treasury and MMF AUM, tokenized private credit AUM, tokenized deposit transaction volume where disclosed, DLT settlement volumes at named consortia, CBDC transaction volumes where published (e-CNY, Sand Dollar, eNaira, others), card-network stablecoin settlement volumes, FedNow and RTP volumes as the non-DLT comparator.
- Compare each to the legacy rail it claims to displace (ACH, Fedwire, CHIPS, SWIFT, correspondent banking, DTCC settlement, money market fund AUM, remittance flows). Report penetration as a percentage, dated.
- Test `null_hypothesis.md` against the data. State explicitly where the thesis is real, where it is pilot theater, and where the data is unavailable.
- Save every series to `./research/data/adoption_*.csv`.

### WS1. What is changing: the landscape map
Taxonomy and current status table for every major rail and instrument:
- Retail and wholesale CBDC by jurisdiction (live, pilot, design, paused, banned by law).
- Fiat-backed stablecoins (USDC, USDT, PYUSD, bank-issued, consortium-issued), tokenized deposits (JPMorgan Kinexys, Citi Token Services, others), tokenized money market funds (BlackRock BUIDL, Franklin BENJI, Fidelity, Goldman, others), tokenized Treasuries and repo.
- Tokenized securities and real-world assets (equities, bonds, private credit, real estate, funds, commodities) and the venues (Securitize, Ondo, SIX Digital Exchange, Nasdaq, DTCC digital initiatives, Broadridge DLR, HKEX, Robinhood and Kraken tokenized equities, others).
- Wholesale settlement infrastructure (BIS Project Agorá, mBridge, Fnality, Partior, Canton Network, Regulated Liability Network successors, SWIFT tokenization and connector work, DTCC, Euroclear, Clearstream).
- Competing and complementary payment rails (FedNow, RTP, Pix, UPI, SEPA Instant, ISO 20022 migration status, Visa and Mastercard stablecoin settlement, Stripe and Shopify stablecoin products, PayPal, card-network tokenized-asset programs).
- Public versus permissioned versus hybrid chains and the interoperability layer (Chainlink CCIP, SWIFT connectors, Ethereum and its L2s, Solana, Avalanche subnets, Canton, Hedera, XRP Ledger, Stellar, Base, Tempo or other payment-specific chains).
- Programmability specifically: what "programmable money" means in each system (conditional payments, delivery-versus-payment, payment-versus-payment, escrow, embedded compliance, agent-initiated payments). Note which features are live versus whitepaper.
For each row: what it is, who runs it, live or pilot, volume or AUM with date and source, access route for an investor, and the single constraint holding it back.

### WS2. Who: institutions, governments, regulators, and the political map (core jurisdictions)
- Central banks and treasuries: Fed, US Treasury, ECB (digital euro), Bank of England, PBoC (e-CNY), BIS and the Innovation Hub, MAS, HKMA, BoJ, SNB. Current stance, stated timeline, political constraint on each.
- Legislators and regulators: US stablecoin law (GENIUS Act or successor) and its implementing rules and effective dates, US market structure legislation status, anti-CBDC legislation status, SEC and CFTC posture and any joint framework, OCC and FDIC guidance on custody and tokenized deposits, Basel Committee crypto capital standard and revisions, FASB fair value accounting, UCC Article 12 adoption by state, EU MiCA implementation and the digital euro legislative file, UK stablecoin regime and Digital Securities Sandbox, Hong Kong stablecoin ordinance, Singapore, Japan.
- Private institutions ranked by exposure: JPMorgan, Citi, BNY, State Street, Goldman, Morgan Stanley, HSBC, Standard Chartered, DBS, BlackRock, Franklin Templeton, Fidelity, Invesco, WisdomTree, VanEck, Apollo, KKR, Hamilton Lane, DTCC, SWIFT, Visa, Mastercard, Stripe, PayPal, Coinbase, Circle, Tether, Ripple, Paxos, Anchorage, Fireblocks, Securitize, Ondo, Chainlink Labs, Digital Asset (Canton), R3, Nasdaq, ICE, CME, Robinhood, Kraken, Galaxy, Bullish, Figure, Gemini.
- For each: what they have shipped, what they have announced, revenue or AUM tied to it (dated), public or private, and how an investor gets exposure.
- Power map: who sets rules, who builds rails, who issues instruments, who distributes to end users, who holds reserves. Deliver as a table and as a Mermaid diagram in the markdown.

### WS3. When and how likely: timeline and scenario analysis
- Dated milestone table, past and forward: legislation, rule effective dates, consortium go-lives, central bank decision points, issuer launches, ETF decisions. Output `timeline.csv`.
- Three scenarios through 2030 and 2035: Bear, Base, Bull as defined in `schema.md`. For each: narrative, probability with stated basis, three leading indicators with the exact data series or docket to watch, and the falsifier.
- Driver tree: list the 8 to 12 drivers that determine which scenario occurs (regulatory clarity, bank capital treatment, institutional custody availability, interoperability standards, retail demand, Treasury market effects, geopolitical competition, technical maturity, incumbent incentives). Score each driver's current state and direction, dated. This feeds the Phase 2 model.
- Reconcile market-size forecasts (BCG, McKinsey, Standard Chartered, Citi, Bernstein, 21.co, RWA.xyz, Boston Consulting, any 2025 and 2026 updates) and explain why they differ. Give your own range with method.
- Historical analogs with adoption curves and who captured value: SWIFT, equity and FX electronification, T+1, money market fund rise, M-Pesa, Pix, UPI, EMV chip migration, cloud adoption by banks.

### WS4. Where value accrues: value chain economics and who benefits
- Value chain map: issuance, reserve management and float income, custody, settlement and clearing, tokenization platforms, blockchain infrastructure (L1, L2, validators, staking, sequencers), oracles and data, compliance and identity (KYC, AML, travel rule, digital ID), wallets and distribution, exchanges and ATS venues, treasury and cash management software, insurance, legal and audit, tax and reporting software.
- For each layer: current revenue pool (dated), margin structure, who is winning, moat type (network effect, regulatory license, balance sheet, distribution, switching cost), and whether the layer commoditizes. Deliver a layer-by-layer table with a "pricing power 2030" judgment and confidence tag.
- Who loses: correspondent banks, remittance firms, card interchange, legacy custodians, FX intermediaries, transfer agents, bank deposit franchises if disintermediated. Quantify fee pools at risk with source.
- Macro and geopolitical effects: stablecoin reserve demand for Treasuries and its short-end effect, dollar dominance versus e-CNY and mBridge, sanctions enforcement and evasion, monetary policy transmission, bank funding stability, privacy politics, tax automation.
- Token versus equity value capture: for each public chain used by institutions, assess whether institutional flow accrues to the token (fees, burn, staking yield) or leaks to intermediaries' equity. Show the mechanism and the numbers.
- Additional topics: digital identity standards (eIDAS 2.0, mobile driver's licenses, verifiable credentials), tokenized carbon and energy, tokenized real estate and title, DeFi and TradFi convergence (Aave, Sky, Uniswap, Morpho institutional products), post-quantum cryptography timelines for ledgers, legal finality and settlement law, deposit insurance treatment of tokenized deposits, custody rule changes (SAB 121 rescission and successors), prime brokerage for digital assets, ETF and ETP wrappers including staking in ETFs, smart contract insurance.

### WS5. The plays: investment map by tier and horizon
Produce `plays.csv` per `schema.md`. Columns: Vehicle, Ticker or access route, Layer, Thesis (one line), Tier (Retail, Mid, Large), Horizon (Short, Medium, Long), Return band with method (comps, revenue pool share, base-rate from WS3 analogs; never a bare number), Key risk, Catalyst, Kill criterion, Liquidity, Regulatory exposure, Tax character (from WS7, fill after merge), Confidence.

Minimum coverage:
- Retail: public equities with direct exposure (exchanges, issuers, custodians, payment networks, asset managers, banks with disclosed tokenization revenue), listed ETFs and ETPs (spot crypto, tokenization and blockchain equity, staking), tokenized money market funds open to retail, direct network tokens with the WS4 value-capture test applied, and the stablecoin yield question (where retail can and cannot legally earn it, dated).
- Mid-scale: Reg D and Reg S private placements in infrastructure, venture and growth funds focused on this layer (name them, with minimums), tokenized private credit funds, validator and staking operations, pre-IPO secondaries in named private companies (Circle-class, Kraken-class, Securitize-class, whichever remain private), structured notes.
- Large-scale: direct stakes in settlement consortia, anchor positions in tokenized fund launches, becoming an issuer or distributor, bank partnerships, infrastructure build-or-buy, sovereign engagement, and the operational requirements (licenses, custody, compliance staffing, capital) to be a participant rather than a spectator.
- Short horizon: event-driven catalysts with dates, with explicit crowding and valuation notes.
- Valuation reality check: current multiples of each named public equity versus growth, where the thesis is already priced in, and which trades are crowded. Pull multiples from filings or a reputable data source, dated.
- The picks-and-shovels fallacy: which infrastructure layers commoditize and which hold pricing power.

### WS6. Risks, limitations, and warning signals
- Regulatory and political (reversal, stablecoin yield bans, state and federal divergence, EU and US divergence, anti-CBDC movements).
- Technical (smart contract failure, bridge exploits, key management, oracle manipulation, finality and reorg risk, throughput, post-quantum).
- Financial (depegs, reserve quality, run dynamics, issuer concentration, custodian counterparty risk, rehypothecation).
- Market (bubble dynamics, token unlock schedules, wash-traded volume, narrative-driven sources, research conflicts of interest).
- Operational (custody errors, tax complexity, fraud targeting retail).
- Structural (bank disintermediation backlash, privacy backlash, walled-garden fragmentation).
- For each: probability, severity, which plays it hits hardest, early warning signal, and the data source for that signal. Output `risks.csv`.

### WS7. Tax treatment by vehicle and tier (US federal plus California, with notes for other jurisdictions in WS9)
- For every vehicle class in WS5: tax character (ordinary, qualified dividend, long-term capital gain, collectibles rate, interest), holding period rules, wash sale applicability as of today (verify current law for digital assets), staking and airdrop income timing, tokenized MMF distributions, stablecoin yield character, PFIC exposure for offshore funds and some tokens, QSBS eligibility for private infrastructure equity, Section 1256 treatment where applicable, broker reporting (Form 1099-DA and its phase-in), cost-basis method elections, estate treatment, and California conformity or divergence on each.
- Account placement: which vehicles belong in taxable, traditional IRA, Roth IRA, or a 401k brokerage window, and which are prohibited or impractical in each.
- Mid and large tiers: fund structures, carried interest, UBTI for tax-exempt investors, opportunity zone interaction, trust structures, state residency planning.
- Output `tax_matrix.csv` and a one-page summary. Flag every item with `[Verify with CPA]` where the rule changed in the last 24 months.

### WS8. Agentic payments: AI agents as transacting parties
- Protocols and products, each verified as live, renamed, or abandoned: Coinbase x402, Visa Intelligent Commerce and Trusted Agent Protocol, Mastercard Agent Pay, Stripe agentic commerce products and any Stripe-affiliated payment chain, Google Agent Payments Protocol, PayPal agent tools, Skyfire, Nevermined, any bank or card-network successor programs.
- Mechanics: how an agent is identified (Know Your Agent, verifiable credentials, delegated authority scopes), how it holds funds (stablecoin wallets, virtual cards, tokenized deposits), how merchants verify it, and what settlement rail each uses.
- Economics: who captures fees, how micropayment economics differ from card economics, whether stablecoins or cards win agent-to-merchant flows, and the implications for interchange pools.
- Regulation: liability for agent-initiated transactions, consumer protection, AML treatment, EU and US positions.
- Timeline and adoption data if any exists. Investable exposure by tier. Add rows to `plays.csv` with WS8 as the source tag.

### WS9. Expanded geography
- Jurisdictions beyond WS2: Brazil (Drex, Pix), Mexico, Argentina, Colombia, Nigeria, Kenya, South Africa, Ghana, UAE (VARA, ADGM, DIFC), Saudi Arabia, Bahrain, Qatar, Switzerland and Liechtenstein, India (digital rupee, UPI, tax regime), South Korea, Australia, Canada, Turkey, Kazakhstan, Russia (digital ruble and sanctions context), Cambodia (Bakong), Thailand, Indonesia, Philippines.
- For each: CBDC status, stablecoin regime, tokenized securities framework, adoption data where available, the dominant local players, capital controls and FX rules affecting foreign investors, tax treatment of foreign investors in local vehicles, and the access route for US investors (ADRs, ETFs, local brokers, restrictions).
- Identify the three jurisdictions most likely to produce outsized returns for a foreign investor and why, and the three most likely to produce losses through capital controls or regulatory reversal.
- Output `jurisdictions.csv`.

## 5. Phase 2 through Phase 6

### Phase 2: Quantitative scenario model
- Using the WS3 driver tree and WS0 data, write `scenario_model.py` (Python, standard libraries plus pandas and numpy). Inputs: driver scores and weights, adoption series, analog adoption curves. Outputs: scenario probabilities, a sensitivity table showing which drivers move the probabilities most, and a tornado-style ranking. Keep the model simple and inspectable. Document every weight in `assumptions.md`. Save `scenario_results.csv`.
- For each play in `plays.csv`, state the return band method and show the arithmetic in `return_methods.md`.

### Phase 3: Synthesis
- Read every `./research/ws/*.md` Summary and Key numbers section first, then the bodies only where needed.
- Merge WS7 tax character into `plays.csv`. Merge WS8 and WS9 plays.
- Write `REPORT.md` per Section 6.
- Write `personalized_plays.md` using Section 0: a sized allocation across the plays that fits the stated capital, drawdown tolerance, liquidity date, account types, and constraints, with position sizes, entry conditions, account placement by tax character, a rebalancing rule, and a monitoring routine that fits the stated weekly time. State that this is an illustrative allocation, not advice.

### Phase 4: Verification
- A fresh agent extracts the 30 most load-bearing claims from `REPORT.md` (numbers, legal status, dates, roles), re-fetches each source, and confirms or corrects. Output `verification.md` with pass, fail, or unresolved per claim. Fix every fail in the report.

### Phase 5: Red team, two independent agents
- Agent A persona: skeptical macro economist and bank regulator. Agent B persona: crypto-native infrastructure builder who has watched three hype cycles. Each sees only `REPORT.md` and `plays.csv`. Each attacks the thesis, the probabilities, the value-capture claims, and every play. Each writes a numbered dissent with severity ratings.
- Also write `external_review_packet.md`: a self-contained version of the executive summary, scenario probabilities, and plays matrix, formatted for pasting into a different vendor's frontier model with the instruction "attack this thesis and these positions, list the ten strongest objections with evidence." The user may run this manually and drop the response at `./research/external_dissent.md`. If that file exists when Phase 6 runs, incorporate it.

### Phase 6: Revision and second red team
- Revise the report. Record every change in `changelog.md`.
- Re-run one red-team agent on the diff only. Incorporate. Finalize.

## 6. Deliverables in `./research/`

| File | Content |
|---|---|
| `REPORT.md` | Executive summary (one page, answer first: is it happening, how likely, who wins, top five plays per tier with confidence). Condensed sections per workstream. "Who benefits most and how to be among them." Scenario model results. Dissent and Weaknesses, verbatim from both red teams and any external dissent. Monitoring plan with dated catalyst calendar and indicator dashboard. Disclaimer. |
| `plays.csv`, `plays.xlsx` | Full plays matrix. The xlsx has one sheet per tier and a summary sheet with filters. |
| `personalized_plays.md` | Section 0 allocation. |
| `timeline.csv`, `institutions.csv`, `jurisdictions.csv`, `risks.csv`, `tax_matrix.csv`, `scenario_results.csv` | As specified. |
| `scenario_model.py`, `return_methods.md` | Inspectable model and arithmetic. |
| `sources.md` | Every source with URL, date, and interest or bias note. |
| `search_log.md`, `assumptions.md`, `verification.md`, `changelog.md`, `external_review_packet.md` | Process records. |
| `ws/ws0.md` through `ws/ws9.md` | Raw workstream outputs, unedited. |
| `data/*.csv` | Raw series with source URL column. |

Quality bar before finishing: every probability has a stated basis and a falsifier. Every play has a kill criterion, a return method, and a tax character. No claim about current law, product, price, or role rests on training data alone. Verification pass has zero unresolved fails on legal status or dates. Both red-team dissents appear verbatim. `REPORT.md` has been re-read end to end and every vague, promotional, or undated passage fixed.

Begin with Phase 0.
