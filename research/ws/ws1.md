# WS1: What is changing: the landscape map

Date: 2026-11-04. Data table: `data/landscape.csv` (59 rows). Search was capped at 24 working queries because the shared web search budget ran out; unsearched areas are marked [Unverified].

## Summary

Fact: Real settlement migration exists but is small against legacy rails. Tokenized Treasuries are $14.25B (2026-11-04) against $7.90T of US money market fund assets (2026-10-28), about 0.18% (Inference, High). Stablecoins are $284B to $296B depending on tracker, about 3.6% to 3.7% of MMF assets (Inference, Moderate).

Fact: Wholesale activity is concentrated in a few operator-reported numbers: Broadridge DLR $8.0T in July 2026 (about $365B per day), Kinexys over $4T cumulative (about $7B per day, secondary). Both are self-reported gross notional [Interested source].

Fact: The regulatory path is now dated. OCC finalized its GENIUS Act rule on 2026-10-21, effective 2027-01-18. The European Parliament voted 416 to 169 on 2026-07-09 to open digital euro talks. The SEC approved Nasdaq tokenized securities rules on 2026-03-18, but settlement stays T+1 through NSCC/DTC.

Fact: Programmability is mostly not live in settlement. Agora (conditional triggers, atomic multi-currency) is a prototype (BIS, 2026-05-27). Swift's ledger settles finally through existing systems. Tempo's Machine Payments Protocol is live (2026-03-18).

Inference [Moderate]: The thesis is real for stablecoins, repo and tokenized cash-like funds; pilot theater for tokenized equities ($3.89B, mostly wrapped), retail CBDCs and most bank deposit tokens (no independent volume).

Gaps: bank-issued stablecoins, Fidelity, Goldman and BNY funds, SDX, HKEX, Canton, Partior, Pix, ISO 20022, CCIP, and conventional MMF expense ratios (G7) could not be verified.

## Key numbers

| Metric | Value | Date | Source | Confidence |
|---|---|---|---|---|
| Global stablecoin value (RWA.xyz) | $284.42B | 2026-11-04 | app.rwa.xyz | [Moderate] |
| Global stablecoin supply (DefiLlama via CoinMarketCap) | $295.9B, lowest since 2025-09 | 2026-11-03 | coinmarketcap.com/academy | [Low] secondary |
| USDC circulation | $73.9B | 2026-09-30 | The Block, Circle Q3 | [Moderate] [Interested source] |
| USDT liabilities | $183.50B | 2026-09-30 | Cryptobriefing, 247wallst on attestation | [Moderate] |
| Tokenized Treasuries (distributed) | $14.25B, 85,870 holders | 2026-11-04 | app.rwa.xyz/treasuries | [Moderate] |
| BUIDL AUM | $1.97B | 2026-11-04 | app.rwa.xyz | [Moderate] |
| US MMF total assets | $7.90T | 2026-10-28 | ici.org | [High] |
| Tokenized stocks | $3.89B, 4.61M holders | 2026-11-04 | app.rwa.xyz/stocks | [Moderate] |
| Tokenized credit (distributed) | $8.27B | 2026-11-04 | app.rwa.xyz/private-credit | [Moderate] |
| Broadridge DLR | $8.0T per month; $365B per day | 2026-07 | broadridge.com release 2026-08-10 | [Moderate] [Interested source] |
| Visa stablecoin settlement run rate | $25B annualized | 2026-10-27 | secondary (KuCoin) | [Moderate] [Interested source] |
| UPI | 25.47B transactions | 2026-10 | Inc42 citing NPCI | [Moderate] |
| FedNow Q2 2026 | 4.998M payments, $274.7B | 2026-06-30 | PaymentsJournal | [Moderate] |
| Retail CBDCs launched | 3 (BS, JM, NG); 41 pilots; 146 exploring | 2026-05 | atlanticcouncil.org | [Moderate] |
| mBridge cumulative | $55.49B, 4,047 txns | 2025-11 | PYMNTS citing Atlantic Council | [Low] |

## Body

### 1. Source quality and method

Fact: Primary pages fetched: Atlantic Council tracker, RWA.xyz (four pages), Broadridge release, OCC Bulletin 2026-50, BIS Agora page, Securitize Q2 release, ICI weekly MMF data. No fetched page tried to instruct the agent.
Fact: Many search hits were SEO-shaped explainers (eco.com, stablecoininsider.org, KuCoin flash news, castlelabs.io). They are used only where nothing better exists, tagged [Low], and flagged [SEO-shaped] below.
Inference [High]: Trackers disagree by 3% to 80% on the same item (stocks $2.76B to $4.9B; stablecoins $284B to $316B). Compare only inside one source.

### 2. CBDCs

| Label | Item | Status and figure | Constraint | Source |
|---|---|---|---|---|
| Fact | Tracker totals | 146 exploring, 77 advanced, 41 pilots, 3 launched (BS, JM, NG), 2026-05 | No volume data for launched three | atlanticcouncil.org/cbdctracker, 2026-05 |
| Fact | e-CNY | 3.4B transactions, about 16.7T RMB cumulative to 2025-12; reclassified as deposit liability 2026-01 | Uncertain plans | Atlantic Council, 2026-05 |
| Fact | Digital euro | Plenary 416 to 169 to 22 on 2026-07-09; trilogue; aim to finish 2026 | Council negotiation; holding cap | sofiaglobe.com, 2026-07-09 [Moderate] |
| Fact | US | Only G20 member not exploring | Legal basis not verified here | Atlantic Council, 2026-05 [Low] |
| Fact | mBridge | $55.49B cumulative to 2025-11; Saudi exit reported 2026-09-20; BIS left 2024-10 | Geopolitics | PYMNTS, 2026-09-21 [Low] |
| Fact | Agora | Prototype report 2026-05-27, 7 central banks, 40+ firms | No production timeline | bis.org/publ/othp110.pdf [High] |

Inference [Moderate]: CBDCs offer no investable route. Value for investors is indirect (rule-setting for stablecoins and bank tokens).

### 3. Stablecoins

| Label | Item | Status and figure | Constraint | Source |
|---|---|---|---|---|
| Fact | USDC | $73.9B quarter end, flat YoY; reserve yield 3.5%, down 61bp; Arc public mainnet 2026-09-16 | Rate-sensitive float income | The Block, 2026-11-04 [Interested source] |
| Fact | USDT | $183.50B liabilities, $191.45B assets, buffer $7.95B; BTC holdings $8.37B | Outside GENIUS path; USAT is the US product | Cryptobriefing 2026-10-31; BeInCrypto [Moderate] |
| Fact | USAT | Ethereum 2026-01-27, Celo 2026-07-29, Anchorage Digital Bank | Single secondary source | eco.com [SEO-shaped] [Low] |
| Fact | PYUSD | About $2.70B, peak $4.214B 2026-03-05 | Falling | metamask.com price page, 2026-11-03 [Low] |
| Fact | RLUSD | About $2.49B (late 2026-09), conflicting $177M tracker | Tracker disagreement | KuCoin, 2026-09 [Low] |
| Fact | USDG | About $3.4B (mid 2026-08) | Distribution via yield sharing | spark.money [Low] |
| Fact | GENIUS Act OCC rule | Final 2026-10-21, effective 2027-01-18; FDIC rule not final; BSA/AML rule pending | Rule gaps | occ.gov Bulletin 2026-50 [High] |
| Fact | Hong Kong | HKMA press release "Granting of stablecoin issuer licences" 2026-04-10 | Names not retrieved | hkma.gov.hk [Low] |
| Fact | Bank-issued stablecoins | None verified | NA | gap |

Inference [Moderate]: Total supply peaked near $322B in May 2026 and fell about 8% since. Growth is not monotonic.

### 4. Tokenized deposits and wholesale infrastructure

| Label | Item | Status and figure | Constraint | Source |
|---|---|---|---|---|
| Fact | Kinexys and JPMD | Over $4T cumulative (2026-10-19), about $7B per day secondary; JPMD on Ethereum for approved institutions | Self-reported, platform-wide | coindoo.com, the-businesstime.com [Low] |
| Fact | Citi Token Services | 7 live markets, 2026-09 | No volume | eco.com [SEO-shaped] [Low] |
| Fact | HSBC | More than $28B payments by 2026-06, 5 markets | Single source | tabinsights.com [Low] |
| Fact | Swift ledger | 17 banks, initial live use 2026-07-09; final settlement via existing systems | Stack unresolved (Besu vs Linea) | coindesk.com 2026-07-09 [Moderate] |
| Fact | Broadridge DLR | $8.0T in July 2026, $365B per day, up 28% YoY | Gross notional; operator source | broadridge.com 2026-08-10 [Interested source] |
| Fact | Fnality sterling | Controlled live payments since 2023-12; USD and EUR pending | Approvals | fnality.com [Moderate] |
| Fact | Partior, Canton, Euroclear, Clearstream, Agora successors | Not verified | NA | gap |

Inference [Moderate]: Wholesale DLT is real mainly in repo and bank-to-bank deposit tokens. Independent volume data does not exist for Kinexys, Citi or HSBC; WS0 should treat them as unaudited.

### 5. Tokenized MMFs and Treasuries, and fees (G7)

| Label | Product | AUM (2026-11-04 unless noted) | Access | Source |
|---|---|---|---|---|
| Fact | Ondo USDY | $2.40B | Non-US persons [Unverified] | app.rwa.xyz/treasuries |
| Fact | Circle USYC | $2.24B | Institutional | app.rwa.xyz/treasuries |
| Fact | BlackRock BUIDL | $1.97B | Qualified purchasers, $5M minimum (secondary, Low) | app.rwa.xyz/treasuries |
| Fact | Franklin iBENJI plus BENJI | $1.71B plus $0.98B | Eligible investors | app.rwa.xyz/treasuries |
| Fact | WisdomTree WTGXX | $1.06B (2026-10) | App and DeFi | pixelwebsolutions.com [Low] |
| Fact | Ondo OUSG | $0.32B (2026-10) | Qualified purchasers | pixelwebsolutions.com [Low] |

Fact: FOBXX net expense ratio 0.20% (0.15% management fee), net assets $686.6M at 2026-08-31 (altstreet.investments, [SEO-shaped] [Low]). BUIDL fee is quoted at 0.50% by one source and 0.20% to 0.50% by another [Low].
Fact: Tokenized Treasury 7-day APY 3.58% (RWA.xyz, 2026-11-04). Distributed value fell 4.14% in 30 days.
Inference [Low]: G7 is unresolved. No conventional MMF expense ratio was retrieved (search cap). Do not state fee compression until WS4 or a later pass pulls ICI or fund prospectus fees.
Inference [High]: Tokenized Treasuries are about 0.18% of MMF assets ($14.25B over $7.90T).

### 6. Tokenized securities and RWA venues

| Label | Item | Status and figure | Constraint | Source |
|---|---|---|---|---|
| Fact | Tokenized stocks | $3.89B, 4.61M holders; bStocks $1.6B, Ondo $914.9M, xStocks $627.1M, Securitize $262.7M | Mostly wrapped or synthetic | app.rwa.xyz/stocks, 2026-11-04 |
| Fact | Ondo | Renamed Ondo Stocks 2026-07 (one source) | Rename unconfirmed | castlelabs.io [Low] |
| Fact | Robinhood | About $148M on-chain | EU only [Unverified] | castlelabs.io [Low] |
| Fact | Securitize | NYSE listing 2026-07-02 (SECZ); tokenized AUM $4.3B at 2026-06-30; Q2 revenue $14.4M, net loss $21.7M | Revenue small vs AUM | prnewswire.com 2026-08-12 [Interested source] |
| Fact | Nasdaq | SEC approval 2026-03-18; T+1 via NSCC/DTC; equity tokens expected Q2 2027 (secondary) | No on-chain settlement | coindesk.com 2026-03-18 |
| Fact | DTC pilot | No-action letter 2025-12-11; three-year pilot; free of value; launch unconfirmed | Primary launch proof missing | fintechanddigitalassets.com [Moderate] |
| Fact | Tokenized credit | $8.27B distributed; represented assets far larger (Figure HELOC $26.06B) | Definitions | app.rwa.xyz/private-credit |
| Fact | Gold | XAUT $3.0B, PAXG $1.7B | Custody terms | app.rwa.xyz |
| Fact | RWA headline | Distributed $39.40B vs represented $395.97B | Represented is off-chain record | app.rwa.xyz |

Inference [Moderate]: "Tokenized RWA" headlines are 10x inflated if represented assets are counted. Use distributed value for scenario measure T.

### 7. Payment rails and card networks

| Label | Item | Figure | Source |
|---|---|---|---|
| Fact | UPI | 25.47B transactions, INR 31.53 lakh crore, 2026-10 | Inc42 citing NPCI, 2026-11-01 |
| Fact | FedNow | Q2 2026 4.998M payments, $274.7B; over 1,800 institutions | PaymentsJournal [Moderate] |
| Fact | RTP | About 142M transactions, $576B, Q2 2026 | Single secondary [Low] |
| Fact | Visa | $25B annualized stablecoin settlement run rate, 10x YoY (2026-10-27); $3.5B at 2025-11-30 | KuCoin, Visa claim [Interested source] |
| Fact | Mastercard | BVNK $1.8B deal closed 2026-08-03; BVNK about $30B annualized volume | bvnk.com press, 2026-08-03 |
| Fact | Stripe and Shopify | USDC on Base for Shopify merchants in 34 countries | stripe.com newsroom (date approx 2025-06) |
| Fact | Pix, ISO 20022 | Not verified | gap |

Inference [Moderate]: Fast-payment rails are 100x to 1000x larger than stablecoin card settlement. UPI alone is about 25B transactions per month.

### 8. Chains and interoperability

Fact: Tempo mainnet launched 2026-03-18 with the Machine Payments Protocol; validators Stripe, Visa, Zodia; one source says the launch set was permissioned (coindesk.com 2026-03-18) [Moderate].
Fact: Arc public mainnet launched 2026-09-16, 11 founding validators, about $1.5B on chain late 2026-10, ARC token presale $182M (Circle Q3 call, [Interested source], [Low]).
Fact: Securitize BUIDL and STAC span Ethereum, Solana and other public chains (Securitize release, 2026-08-12).
Inference [Low]: Public, permissioned and hybrid designs are all in use; Chainlink CCIP, Hedera, XRPL, Stellar, Plasma and Solana were not searched and carry [Unverified] rows.

### 9. Programmability: live versus whitepaper

| Label | System | Live | Whitepaper or prototype | Source |
|---|---|---|---|---|
| Fact | Agora | None | Atomic multi-currency settlement; smart contracts with compliance and conditional triggers | bis.org 2026-05-27 |
| Fact | Swift ledger | 24/7 tokenized deposit transfers | Final settlement still on legacy systems | coindesk.com 2026-07-09 |
| Fact | Nasdaq and DTC | Representation only | DvP absent; DTC service is free of value | coindesk, fintechanddigitalassets |
| Fact | Tempo | Machine Payments Protocol (agent payments, link WS8) | NA | coindesk 2026-03-18 |
| Fact | Broadridge DLR | Intraday repo settlement on ledger | Fnality real-time repo link [Unverified] | broadridge.com |
| Fact | Visa and Mastercard | Stablecoin settlement between institutions | 24/7 settlement via Mastercard Move planned | bvnk.com |
| Inference | Kinexys and Citi | Programmable features claimed, not independently verified | NA | [Low] |

Recommendation [Low]: Treat "programmable money" as live mainly for repo, agent micropayment protocols and card settlement; treat conditional PvP and DvP as prototype until a production DvP is verified (query 19 not completed).

### 10. Survivorship (G12)

| Label | Item | Status | Source |
|---|---|---|---|
| Fact | Mastercard Zerohash investment | Scrapped 2026-05, replaced by BVNK | lookonchain.com [Low] |
| Fact | RealT, Remora Markets | Listed among RWA shutdowns in 2026 roundup (status: abandoned, snippet only) | coindesk.com 2026-08-09 [Low] |
| Fact | Ondo Global Markets | Renamed Ondo Stocks 2026-07 (status: renamed) | castlelabs.io [Low] |
| Fact | mBridge | Live; Saudi Arabia exited, BIS exited 2024 | PYMNTS 2026-09-21 [Low] |
| Fact | we.trade, Marco Polo, TradeLens, ASX CHESS replacement | Believed abandoned from memory only | [Unverified] |

Inference [Moderate]: Exits are frequent (100+ crypto project shutdowns in H1 2026 per roundup), supporting survivorship caution.

## Gaps and unresolved

- Bank-issued stablecoins, Fidelity FDIT, Goldman and BNY tokenized MMF, SDX, HKEX, Canton volumes, Partior, Euroclear, Clearstream, ECB Pontes and Appia.
- Conventional MMF expense ratios for G7; BUIDL fee conflict.
- Pix, ISO 20022 status, Chainlink CCIP, Hedera, XRPL, Stellar, Plasma.
- CLARITY Act and Anti-CBDC Act status (searches refused after budget cap).
- Primary Visa and Fed FedNow Q3 figures (pages did not render).
- Production DvP examples (query 19).

## Files written

- `/home/user/Grotesque-Sublime/research/ws/ws1.md`
- `/home/user/Grotesque-Sublime/research/data/landscape.csv`
- `/home/user/Grotesque-Sublime/research/ws/search_log_ws1.md`
