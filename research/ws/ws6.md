# WS6: Risks, limitations, and warning signals

## Summary
Fact: Risk is front-loaded in 2026. Hack losses reached about $8.6B to $8.74B for 2026 through 2026-10-31 versus $3.4B for 2025 and $2.2B for 2024, driven by one event, the Binance breach of about $6.3B on 2026-10-29. BTC sits 37% to 39% below its 2025-10-06 high of $126,080, and crypto equities fell further (COIN about -68%, CRCL about -74% from peak).

Fact: The US market-structure bill (CLARITY) failed cloture 49-50 on 2026-09-15. Stablecoin yield and ethics provisions were the obstacles. Agency rules stand in for statute and are reversible.

Inference [Moderate]: The five largest risks to the theme are (1) exchange and custodian compromise, (2) a crypto bear market that pushes BTC to $63,000 or lower, (3) a yield ban extended to exchanges and affiliates, (4) yield-sharing competition against USDC (Open USD), (5) equity beta above BTC. The tail risk is a USDT reserve event (Fed note: only about 0.74x of liabilities in high-quality assets).

Recommendation [Moderate]: For a sleeve with a 40% drawdown limit, size on equity drawdowns of 80% to 92% (COIN, HOOD, CRCL history), not on BTC. Kill criteria and thresholds are in `risks.csv` (45 rows).

Gap: The search budget was exhausted at 16 searches (shared limit), so several risks rest on judgment and are tagged `Unverified` or `Low`.

## Key numbers
| Metric | Value | Date | Source | Confidence |
|---|---|---|---|---|
| Crypto hack losses 2024 | $2.2B (303 incidents) | 2024-12-19 | Chainalysis (https://www.chainalysis.com/blog/crypto-hacking-stolen-funds-2025/) [Interested source: security vendor] | [Moderate] |
| Crypto theft 2025 | $3.4B through early Dec; Bybit $1.5B; DPRK $2.02B | 2025-12-18 | Chainalysis (https://www.chainalysis.com/blog/crypto-hacking-stolen-funds-2026/) [Interested source] | [Moderate] |
| Hack losses 2026 YTD | $8.6B (PeckShield) to $8.74B (DefiLlama via Yahoo); ex-Binance $2.38B | 2026-10-31 | https://finance.yahoo.com/markets/crypto/articles/crypto-hack-losses-hit-8-131017031.html | [Low] [Single source cluster] |
| Binance breach | about $6.3B; about 98% replaced by Binance | 2026-10-29 to 11-03 | Fortune (https://fortune.com/2026/10/30/what-we-know-about-binance-hack-biggest-crypto-heist); CryptoTicker 2026-11-03 | [Moderate] |
| FBI IC3 crypto-linked losses 2025 | $11.366B, 181,565 complaints, +22%; investment fraud $7.228B | 2026-04 | ASIS summary of IC3 (https://www.asisonline.org/security-management-magazine/latest-news/today-in-security/2026/april/cryptocurrency-scams/); primary PDF not parseable | [Moderate] |
| Stablecoin market cap | $317B (2026-04-06); $320B (May FSR); $300.9B (2026-10-01, FSB coverage) | 2026 | Fed FEDS Note 2026-04-08; Fed FSR 2026-05; secondary | [Moderate] (series differ) |
| USDT high-quality reserve ratio | about 0.74x of liabilities; total 1.04x. USDC 1.0x high quality | 2026-04-08 | https://www.federalreserve.gov/econres/notes/feds-notes/stablecoins-in-2025-developments-and-financial-stability-implications-20260408.html | [High] |
| CLARITY Senate cloture | 49-50 on 2026-09-15 (needs 60) | 2026-10-02 | Orrick; FinTech Weekly 2026-09-23 | [High] |
| BTC drawdown | -37% to -39% from $126,080 (2025-10-06); $79,913 | 2026-11-04 | CoinMarketCap MCP; Admiral Markets | [Moderate] |
| ETH, SOL | $2,405 and $94.45 | 2026-11-04 | CoinMarketCap MCP | [Moderate] |
| CRCL | $76.51 vs intraday peak about $299 (2025-06-23); 52-week low $49.90 | 2026-11-04 | StockAnalysis; CoinDesk mirror (single source for $299) | [Low] |
| USDC supply | $77.0B (2026-03-31) | 2026-07-31 | valueaddvc.com | [Low] [Single source] |

## Body

### 1. Regulatory and political
Fact: House passed H.R. 3633 294-134 on 2025-07-17. Senate Banking advanced it 15-9 on 2026-05-14. Cloture failed 49-50 on 2026-09-15 after ethics and yield disputes. (Source: Orrick 2026-10-02; FinTech Weekly 2026-09-23; CoinDesk 2026-05-01 for text.)

Fact: The Senate text bars exchanges and affiliates from paying yield on idle stablecoin balances but allows activity-based rewards, and directs Treasury to restrict rewards if deposit flight occurs at scale. Banks want stricter language. (Source: CoinDesk, 2026-05-01; American Banker, undated [Low].)

Fact: GENIUS Act signed 2025-07-18; effective at the earlier of 2027-01-18 or 120 days after final rules (Source: Latham tracker, page updated 2026-08). SEC proposed Regulation Crypto Assets on 2026-08-18 (comments closed 2026-10-20). CFTC sent a rule to OIRA on 2026-09-17. (Source: Orrick 2026-10-02.)

Inference [Moderate]: Agency rules cannot preempt state licensing the way CLARITY would, so state and federal divergence persists (R05). Agency rules reverse faster than statute, which makes the 2028 election the key political date (R02).

Gap: EU and US divergence, anti-CBDC status, and digital euro legislative status were not searched (R06, R07 tagged Unverified). The 2026-11-03 midterm result was not retrieved.

### 2. Technical, with dated incident data
| Year | Losses | Source and date | Notes |
|---|---|---|---|
| 2024 | $2.2B, 303 incidents | Chainalysis 2024-12-19 | DPRK $1.34B (61%) |
| 2025 | $3.4B (through early Dec) | Chainalysis 2025-12-18 | Bybit $1.5B; DPRK $2.02B; personal wallets $713M |
| 2025, Jan to Oct | $2.51B | Yahoo Finance, 2026-11 | Comparator for 2026 |
| 2026, Jan to Oct | $8.6B to $8.74B | PeckShield; DefiLlama via Yahoo, 2026-10-31 | Binance about $6.3B; ex-Binance $2.38B (-5% vs 2025) |

Fact: The Binance breach came from a compromised DevOps engineer laptop that reached a service container and submitted unauthorized withdrawals. Tether and Circle said they would freeze linked stablecoins; BTC and ETH fell about 3%; BNB fell 6.3% within an hour (one teaser). Binance says about 98% of losses are replaced; withdrawals reopen in phases. (Source: Fortune 2026-10-30; CryptoTicker 2026-11-03.) Attribution to North Korea is probable but unproven.

Fact: Other 2026 incidents: StablR multisig compromise 2026-05-24 (unbacked mint); Ostium oracle exploit about $18M (July); Balance Coin oracle manipulation 2026-07-22. (Source: BeInCrypto 2026-05; secondary roundup, [Low].) The late-October log shows no bridge exploits.

Inference [Moderate]: The dominant loss vector in 2025 and 2026 is operational (keys, access, supply chain), not contract bugs. Annual totals are not comparable across vendors (netting of recovered funds, scope) and vendors sell security services [Interested source].

Fact: NIST IR 8547 final posted 2026-10-27; the fetched pages did not show the deprecation dates (draft dated 2024-11-12). (Source: csrc.nist.gov.) Inference [Low]: post-quantum is a low-probability, severity-5 tail (R17).

### 3. Financial
Fact: Fed FSR (May 2026) lists stablecoins as runnable liabilities, says growth moderated, and says supply is concentrated in the two largest issuers. FEDS Note (2026-04-08) finds USDT holds about 0.74x of liabilities in Treasuries, repo and bank deposits and USDC holds 1.0x, and names three vulnerabilities: complex intermediation chains, vertical integration, integration with traditional finance. (Source: federalreserve.gov, 2026-05-28 and 2026-04-08.)

Fact: FSB note of 2026-10-12 says global stablecoin crisis-management frameworks are untested, that reserves and issuing affiliates can sit in different jurisdictions, and that attribution data are limited. Non-binding. IMF WP of 2026-10-02 finds stablecoin holdings rise about 75% within a year of currency crises (188 countries, $21.4T gross flows 2018 to 2025). IMF October 2026 GFSR headline risks were an AI-related correction and sovereign yields; its stablecoin content was not retrieved. (Source: fsb.org; imf.org.)

| Event | Date | Fact | Source |
|---|---|---|---|
| USDC depeg after SVB | 2023-03 | Study of contagion exists; price detail not retrieved this session | arXiv 2606.07442 (2026-06) |
| Terra/UST collapse | 2022-05 | Training memory [Unverified] | none |
| StablR EURR/USDR depeg | 2026-05-24 | Key compromise, mint and swap | BeInCrypto |
| Balance Coin | 2026-07-22 | Oracle manipulation, about -99.75% [Low] | secondary |
| Large fiat-backed tokens | 2026 to Aug | Stayed within about 0.1% of $1 [Low] | secondary roundup |
| Stablecoin supply dip | 2026-08 | About -$15B as redemptions exceeded issuance [Low] | secondary |

Fact: Open USD coalition (Stripe, Visa, BlackRock named; 140+ businesses) announced 2026-06-30, passes reserve yield to partners; CRCL fell 17.55% to $62.63 that day. (Source: Fortune 2026-06-30; Invezz.) Inference [Moderate]: at $77.0B USDC, each 100 bp of lower reserve yield cuts about $0.77B per year of gross reserve income, before distribution costs.

### 4. Market and drawdown base rates
See `data/drawdowns.csv`. Recovery months are measured from peak to a new high. Rows marked Unverified come from training memory and must be re-verified before sizing use.

| Asset | Cycle | Drawdown | Recovery | Confidence |
|---|---|---|---|---|
| BTC | 2025-26 (open) | about -39% to 2026-11-03 | not recovered | [Moderate] |
| BTC | 2021-22 | about -77% | 28 months | [Unverified] |
| BTC | 2017-18 | about -84% | 36 months | [Unverified] |
| ETH | 2025-26 (open) | -51% | not recovered | [Low] |
| ETH | 2021-22 | about -82% | 45 months | [Unverified] |
| SOL | 2025-26 (open) | -68% | not recovered | [Low] |
| SOL | 2021-22 | about -97% | about 36 months | [Unverified] |
| COIN | 2025-26 (open) | about -68% | not recovered | [Moderate] |
| COIN | 2021-22 | about -92% | about 51 months | [Low] |
| HOOD | 2025-26 (open) | about -44% | not recovered | [Moderate] |
| HOOD | 2021-22 | about -92% | about 46 months | [Low] |
| CRCL | since IPO | about -83% (peak $299 to $49.90); now about -74% | not recovered | [Low] |
| Blockchain equity ETF | all | NA, not retrieved | NA | [Unverified] |

Fact: COIN Q3-2026 transaction revenue fell 44% to $590M and HOOD crypto revenue fell 55% to $120M (Source: Benzinga and CryptoBriefing, 2026-10-30; secondary). COIN hit about $136 on 2026-10-30, lowest since February 2024.

Inference [Moderate]: Equities draw down 1.1x to 1.9x the BTC drawdown in this cycle. A 40% sleeve limit is breached by an unhedged single stock in any past cycle. Recommendation [Moderate]: cap any single crypto equity so an 85% fall costs at most the 40% sleeve limit (a position of at most 47% of the sleeve, judgment), and prefer diversified exposure. Kill criterion: BTC closes below $63,000 and the thesis is not re-underwritten.

Gap: Token unlock schedules, wash-volume method, research conflicts, and crypto-equity beta were not searched; R31 to R33 are structural judgments.

### 5. Operational and structural
Fact: IC3 2025 crypto-linked losses $11.366B (+22%), crypto investment fraud $7.228B, age 60+ $4.43B; total IC3 losses $20.877B (Source: ASIS and AARP summaries, 2026-04). Wallet drainers took $713M from 158,000 incidents in 2025 (Chainalysis).

Inference [Low]: Structural risks (bank backlash, privacy backlash, fragmentation, interoperability failure, incumbent modernization, token value-capture failure) are judgment-based and carry numeric triggers in `risks.csv` rows R40 to R45.

### 6. Risk register summary (top 12 by probability times severity)
| Risk id | Risk | Prob (5y) | Severity | Hits hardest |
|---|---|---|---|---|
| R10 | Exchange or custodian compromise above $500M | high 80% | 4 | crypto exchange equity, custody |
| R29 | BTC at or below $63,000 | high 70% | 4 | network tokens, ETFs |
| R30 | Crypto equity beta above BTC | high 85% | 4 | COIN, HOOD, CRCL |
| R25 | Yield-sharing competition | high 65% | 4 | stablecoin issuer equity |
| R03 | Yield ban on exchanges and affiliates | high 55% | 4 | CRCL, COIN |
| R02 | Post-2028 policy reversal | med 35% | 4 | exchange and issuer equity |
| R01 | No federal market-structure statute | med 35% | 3 | exchange equity, tokens |
| R23 | Issuer concentration event | med 25% | 4 | issuer equity |
| R20 | Reserve bank counterparty failure | med 20% | 4 | issuer equity, tokenized MMF |
| R19 | USDT reserve event | low 10% | 5 | all stablecoin plays |
| R22 | Stablecoin run | low 7% | 5 | issuer equity, MMF |
| R17 | Post-quantum break | low 3% | 5 | network tokens |

## Gaps and unresolved
- Search cap hit (16 searches, 19 fetches). Not covered: BIS 2026 annual report, tokenized fund incidents, Tether attestation (BDO) detail, bank lobby detail, EU MiCA and digital euro, anti-CBDC status, token unlocks, wash-trade method, crypto-equity beta, 2026 chain outages, blockchain equity ETF drawdown, midterm result.
- FBI IC3 primary PDF could not be parsed; figures from two secondary summaries.
- CRCL peak is single-source; sources conflict ($189.92 and $262.97 appear elsewhere).
- Pre-2025 drawdown rows are training memory (Unverified). Signal URLs are landing pages not fetched this session.

## Files written
`ws/ws6.md`, `risks.csv`, `data/drawdowns.csv`, `ws/search_log_ws6.md`
