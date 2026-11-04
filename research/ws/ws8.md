# WS8: Agentic payments, AI agents as transacting parties

## Summary

Fact: Every major payments incumbent has shipped an agent product, but measured agent volume is tiny or undisclosed. Visa's CEO called agentic volume "very small in the big scheme" (Visa Q4 FY26 call, 2026-10-28). Mastercard's CEO said volumes remain small (2026-10-29).

Fact: The only public on-chain series, x402, shows 196M cumulative transactions and $42M settled by 2026-11-01, but October 2026 was 5.1M transactions worth $274k, and Artemis attributes over 95% of activity to protocol signaling (secondary sources) [Low].

Fact: OpenAI shut Instant Checkout on 2026-03-20 after about six months; ACP survives as a discovery and token spec. This is the clearest failure datapoint.

Inference: Cards, not stablecoins, win agent-to-merchant consumer checkout in the 1 to 3 year window, because merchants, chargeback rights and Regulation E and Z protection sit on card rails [Moderate]. Stablecoins win machine-to-machine micropayments, but that pool is currently about $3M a year at the October 2026 run rate ($274k x 12) [Low].

Inference: No evidence yet that interchange pools shrink. Forecasts ($190B to $5T by 2030) are interested-party scenarios, not measurements.

Recommendation: Own the card networks and Cloudflare as low-cost options, avoid x402 tokens, treat private Stripe or Tempo exposure as Mid and Large only. All return bands are Low to Moderate confidence.

## Key numbers

| Metric | Value | Date | Source | Confidence |
|---|---|---|---|---|
| x402 cumulative transactions | 196M across 12 chains | 2026-11-01 | Fireblocks via agenteconomy.to, reported by Decrypt | [Low] secondary |
| x402 cumulative settled value | over $42M | 2026-11-01 | same | [Low] |
| x402 October 2026 | 5.1M tx, $274k ($0.054 per tx) | 2026-10 | Fireblocks via Decrypt | [Low] |
| x402 daily commercial volume | about $28,000 | 2026-03 | CoinDesk 2026-05-05 | [Moderate] |
| Share of x402 activity that is signaling | over 95% | 2026 | Artemis via Forkast/Yahoo 2026-08-04 | [Low] |
| Cloudflare HTTP 402 responses | about 1B per day | 2026-05-05 | CoinDesk | [Moderate] [Interested source] |
| Visa AI partners live | nearly 50, expected to double | 2026-10-27 | Visa call | [High] |
| Visa stablecoin settlement run rate | over $25B annualized (not agentic) | 2026-10-27 | Visa call | [High] |
| Instant Checkout scale at shutdown | about 30 Shopify merchants, about 200k Walmart products | 2026-03-20 | CNBC | [High] |
| Walmart conversion in ChatGPT vs own site | 3x lower | 2026-03-20 | CNBC | [Moderate] |
| Tempo valuation | $5B (Series A $500M) | 2025-10 | The Block 2026-03-18 | [Moderate] |
| Forecast US agent e-commerce 2030 | $190B to $385B (Morgan Stanley); $300B to $500B (Bain) | 2025 to 2026 | secondary summaries | [Low] Forecast |
| Forecast global agentic 2030 | $3T to $5T (McKinsey) | 2025-10 | secondary summaries | [Low] Forecast |

## Body

### 1. Protocol and product status (verified 2026-11-04)

Full table in `data/agentic_protocols.csv`. Labels: Fact unless stated.

| Product | Status | Evidence | Label |
|---|---|---|---|
| x402 (Coinbase) | live | Tracked on 12 chains; Base carried over 99% of agentic stablecoin volume in Q2 2026 per Artemis, cited in Coinbase's Q2 deck (sec.gov 8-K, 2026) | Fact [Moderate] |
| x402 Foundation | live | Launched under the Linux Foundation 2026-07-14 with 40 organizations, 17 premier members including Visa, Mastercard, Stripe, Google, AWS, Cloudflare, Coinbase, American Express, Solana Foundation (Forkast via Yahoo, 2026-08-04). Another source gives 2026-04-02 | Fact [Single source] |
| Visa Intelligent Commerce and Trusted Agent Protocol | live, early | BILL and Billtrust pilot "currently live" (Visa press release, 2026-10-20); TAP introduced 2025-10-14 (secondary) | Fact [High] |
| Visa Intelligent Commerce Connect | live | One integration for TAP, MPP, ACP and UCP, 2026-04-08 (secondary) | Fact [Low] |
| Mastercard Agent Pay | live, early | Agentic Tokens; Verifiable Intent contributed to FIDO 2026-04-28; Q3 call 2026-10-29 says volumes small | Fact [Moderate] |
| Stripe ACP, Shared Payment Tokens | live | Launched 2025-09-29 with OpenAI (Stripe newsroom) | Fact [Moderate] |
| ChatGPT Instant Checkout | abandoned 2026-03-20 | CNBC 2026-03-20: moved to merchant apps | Fact [High] |
| Tempo and MPP | live | Mainnet 2026-03-18; more than 100 directory services (The Block) | Fact [High] |
| Google AP2 | live, under standards | Donated to FIDO Alliance 2026-04-28; rolling out in Google products 2026-05-19 (secondary) | Fact [Moderate] |
| Google UCP | live | Announced with Shopify 2026-01-11 (secondary) | Fact [Moderate] |
| PayPal agentic commerce services | live, no volume disclosed | Launched 2025-10-28 (PayPal newsroom) | Fact [Moderate] |
| Cloudflare Pay Per Crawl | pilot (closed beta) | Beta since 2025-07-01; evolving to Pay Per Use, beta reported 2026-09-30 (secondary) | Fact [Moderate] |
| Skyfire, Nevermined | live, small | Vendor-sourced claims only | Fact [Low] [Interested source] |
| Amazon | blocks third-party agents | Amazon won a preliminary injunction 2026-03-10; Ninth Circuit reversed 2026-08-04, rehearing declined September (secondary) | Fact [Moderate] |
| Shopify | participant | Shop Pay named by Visa (2026-10-27) and Mastercard (2026-10-29) as live agent partner | Fact [High] |
| Adyen Agentic | live | Launched June 2026, works with Meta AI checkout (secondary) | Fact [Low] |
| American Express | follower | "Warming up in the bullpen" Q1 2026 (secondary) | Fact [Low] |

Not verified this session: Amazon first-party Buy for Me, Worldpay agent products, any renamed successor program. [Unverified]

### 2. Mechanics

| Layer | Card-network path | Stablecoin path | Label |
|---|---|---|---|
| Identity | Agent registered in Visa Agentic Directory; TAP signs requests with HTTP Message Signatures. Mastercard requires agent registration under its Acceptance Framework | Wallet address; Skyfire KYAPay uses signed JWTs; x402 needs no account | Fact [Moderate] |
| Delegated authority | Mastercard Verifiable Intent and Google AP2 signed mandates; both now in FIDO working groups | AP2 A2A x402 extension; MPP sessions cap funds up front | Fact [Moderate] |
| Funds | Network token (Agentic Token) on the cardholder's card; Stripe SPT bound to merchant and amount | Pre-funded USDC wallet; Tempo session escrow | Fact [Moderate] |
| Merchant verification | Directory lookup and signature check, replaces CAPTCHA (Visa 2026-10-20) | Payment payload verified by facilitator; no merchant identity step | Fact [Moderate] |
| Settlement | card_visa, card_mastercard, existing acquirer cycles | public_chain (Base, Solana) or tempo | Fact [Moderate] |

Inference: Identity is converging on FIDO plus card-network directories, which threatens standalone Know Your Agent vendors [Moderate]. A cited weakness: a preprint argues AP2 signs the transaction but not the decision (arXiv 2609.11757, 2026) [Low].

Fact: Mastercard's CEO said virtual card numbers as an intermediary are not a long-term solution; fully tokenized transactions are preferred (Q3 call, 2026-10-29).

### 3. Economics

Compute (Fact inputs, Inference outputs). Card: Stripe list 2.9% plus $0.30 (stripe.com/pricing, page shows copyright 2026, no date). Stablecoin: Stripe lists 1.5% in one place and 0.8% (rising 0.2 points after 2027-01-01) in another; no minimum shown. On-chain: Base about $0.01 per transfer (third-party comparison, September 2026; range $0.001 to $0.05 across sources), Solana about $0.0003.

| Payment | Card fee (2.9% + $0.30) | Fee % of payment | Stablecoin at Stripe 1.5% | On-chain gas Base $0.01 | Gas % of payment |
|---|---|---|---|---|---|
| $0.01 | $0.3029 | 3,029% | $0.00015 | $0.01 | 100% |
| $1.00 | $0.329 | 32.9% | $0.015 | $0.01 | 1.0% |

Inference: Cards cannot carry a $0.01 payment; even Base gas equals the payment unless batched, which is why MPP aggregates session payments into one settlement and Solana at $0.0003 (3% of $0.01) is the viable micropayment rail [Moderate]. At $1 the stablecoin saves about $0.31 versus card list price, but merchants lose chargeback rights and card rewards funding.

Fact: Observed x402 average ticket is $0.054 ($274k over 5.1M, October 2026), so the observed flow sits where only stablecoin economics work, and is worth about $3.3M annualized.

Inference: Fee capture today. Cards: issuers (interchange), networks (assessments), acquirers. Stablecoin x402: Coinbase facilitator and Base sequencer fees, issuer float (Circle). Cloudflare: platform fee as merchant of record. None disclosed. Interchange pools show no measured erosion; Visa and Mastercard both report double-digit growth (Visa FY26 net revenue $46B up 15%; Mastercard Q3 up 14%). [Moderate]

Inference: Winner by flow type [Moderate]: consumer shopping, cards (protection, rewards, existing merchants). B2B invoices, cards via Visa-BILL pilot, with ACH substitution risk to ACH. Machine micropayments (APIs, crawls), stablecoin. Stablecoin-linked cards (Visa: over 225 programs) blur the split.

### 4. Regulation and liability

| Topic | Position | Label |
|---|---|---|
| Regulation E | No CFPB guidance applying it to AI agents found as of August 2026 (secondary law and vendor blogs); unauthorized-transfer exclusion for a person the consumer gave access to may cover agent use; unresolved | Fact [Low] |
| Bank contract shift | Wells Fargo Online Access Agreement s15 deems agent actions authorized by the customer, effective 2026-11-24 (TechTimes 2026-11-03, not verified against bank text) | Fact [Single source] |
| Industry view | Consumer Bankers Association January 2026 white paper says application of Regulation E exceptions to agentic AI is unclear and merchants may face chargebacks (secondary description; PDF not machine-readable here) | Fact [Low] [Interested source] |
| Regulation Z, network chargeback rules | Not verified from primary text this session | [Unverified] |
| AML | Not researched: search budget exhausted. No FinCEN or FATF agent guidance verified | [Unverified] |
| EU PSD3 and PSR | Provisional deal 2025-11-27; no agent-specific provisions; strong customer authentication stays with the payer; application date disputed across sources | Fact [Moderate] |
| EU AI Act | Digital Omnibus Regulation (EU) 2026/1744 in force 2026-07-27; Annex III high-risk to 2027-12-02; Article 50 transparency unchanged. Payment-agent classification not addressed | Fact [Moderate] |
| US state law | Not researched | [Unverified] |
| Platform law | Ninth Circuit, 2026-08-04: user, not the agent vendor, accesses Amazon, favoring agents | Fact [Moderate] |

Inference: Liability is migrating to the consumer by contract while statute is silent. Expect a first CFPB or court test within 12 to 24 months [Low]. This favors card rails, where dispute rights are codified.

### 5. Adoption and forecasts

Measured: see Key numbers. Fact: neither Visa nor Mastercard discloses an agent transaction count or revenue; Coinbase excludes x402 from its payments volume and shows no agent revenue line (Q3 2026 deck, per sec-api analysis, 2026-10-30).

Forecasts (all Low, scenario-based, authors' definitions differ): Morgan Stanley $190B to $385B US by 2030 counts autonomous purchases only; Bain $300B to $500B US includes agent-influenced; McKinsey $3T to $5T global including B2B. Interested flags: Bain and McKinsey sell implementation; networks and vendors repeat these numbers. Inference: even $385B is under 2% of global card purchase volume order of magnitude, so interchange impact is second-order before 2030 [Low; global card volume not sourced this session].

Inference: Scenario signal for WS3: bear to base. Agentic payments are not yet "material" under the mandate threshold ($5B a year new revenue pool by 2030): at the October 2026 x402 run rate the pool is about $3M a year.

### 6. Investable exposure by tier

See `data/plays_ws8.csv`. Summary:

| ID | Play | Tier | Confidence |
|---|---|---|---|
| A-01 | Visa (V) | Retail | Moderate |
| A-02 | Mastercard (MA) | Retail | Moderate |
| A-03 | Cloudflare (NET) | Retail | Low |
| A-04 | Coinbase (COIN) | Retail | Low |
| A-05 | PayPal (PYPL), not scored | Retail | Unverified |
| A-06 | Stripe secondary or tender | Mid | Low |
| A-07 | Agent identity startups | Large | Low |
| A-08 | Avoid x402 tokens | Retail | Moderate |

Recommendation: For the $50k non-accredited case, agentic exposure is a rounding error inside A-01 and A-02; do not size a position on agentic grounds [Moderate]. Kill criteria in the CSV.

## Gaps and unresolved

- Search budget: the shared per-turn limit was exhausted after 24 searches; 14 fetches attempted (three 403 from mastercard.com, businesswire.com, cloudflare.com).
- AML treatment, US state law, Regulation Z and card network liability rules, Know Your Agent as a defined standard, Worldpay, Amazon Buy for Me: not verified.
- Primary documents not read: Coinbase decks, Visa 8-K, Mastercard 10-Q agentic text, CFPB, FIDO announcement, Cloudflare press release. Many statuses rest on secondary sources.
- x402 counts differ by tracker (Chainalysis cited 138M on Base vs 88M in agenteconomy.to); no wash adjustment method is verified.
- Stripe stablecoin fee page lists both 1.5% and 0.8%; actual applicable rate unclear.
- Valuations for PYPL, MA, V multiples, Stripe not retrieved; A-05 and A-06 have no band.
- Santander and Mastercard first live payment date and Visa TAP launch date from secondary snippets.

## Files written

- `/home/user/Grotesque-Sublime/research/ws/ws8.md`
- `/home/user/Grotesque-Sublime/research/data/plays_ws8.csv`
- `/home/user/Grotesque-Sublime/research/data/agentic_protocols.csv`
- `/home/user/Grotesque-Sublime/research/ws/search_log_ws8.md`
