# WS5: The plays: investment map by tier and horizon

Date: 2026-11-04. Rows in `plays.csv`: 60 (Retail 38, Mid 12, Large 10). Valuations in `data/valuations.csv`: 19 tickers. `tax_character` and `account_placement` are `TBD_WS7`.

## Summary

Fact: Crypto-linked equities have de-rated while the cash alternative pays 4.21% (3M Treasury, 2026-11-02). BTC is 79,875 (-20.4% 1y), Coinbase Q3 revenue fell 35% yoy, Robinhood crypto revenue fell 55%.

Inference: Reverse DCF puts CRCL at about 16% 10-year revenue CAGR and COIN at about 17% for a 10% return. That is above what a flat BTC market supports, below Circle's own 40% USDC growth target. Expected returns for most direct plays sit at or below the T-bill rate after risk. [Moderate]

Inference: Value goes to distribution, regulated charters and incumbent networks, not to commoditized plumbing. Circle pays about 57% of revenue to distribution partners; custody and ETF fees are in a fee war (0.19% to 0.50%). [Moderate]

Recommendation: For a $50k non-accredited California cash-account investor, the opportunity set is public equities, spot and staking ETFs, BENJI, and direct tokens. Judge every play against 4.21% bills. Mid and Large plays carry the real asymmetry but stale or missing marks. [Moderate]

Limits: The shared search budget ran out after 21 searches; ACRED and Hamilton Lane minimums, venture fund minimums, GENIUS rule detail and current stablecoin reward rates are open (see Gaps).

## Key numbers

| Metric | Value | Date | Source | Confidence |
|---|---|---|---|---|
| BTC price, 1y, YTD | 79,874.57; -20.4%; -10.0% | 2026-11-04 | CoinMarketCap MCP quote | Moderate |
| ETH, SOL, LINK, XRP | 2,404.81; 94.44; 11.35; 1.298 | 2026-11-04 | CoinMarketCap MCP quote | Moderate |
| 3M, 1Y, 10Y Treasury (CMT) | 4.21%; 4.38%; 4.91% | 2026-11-02 | Federal Reserve H.15 | High |
| Fed funds target, effective | 3.75% to 4.00%; 3.88% | 2026-10-28; 2026-11-02 | CNBC 2026-10-28; H.15 | High |
| SPY price, 1y and YTD return | 767.38; +13.5%; +13.4% | 2026-11-04 | stockanalysis.com compare | Moderate |
| CRCL price, mcap, EV/S | 76.51; 19.52B; 5.94 | 2026-11-04 | stockanalysis.com | Moderate |
| Circle Q3 revenue and reserve income | 864.9M (+17%, -7.7% ex ARC presale); 658M (-8%) | 2026-11-04 | Circle Q3 release via financefeeds, stocktitan | Moderate |
| USDC circulation, reserve return | 73.9B period end; 3.54% | Q3 2026 | Circle Q3 slides via investing.com | Moderate |
| COIN price, mcap, EV/S, fwd P/E | 151.86; 40.21B; 7.03; 104.5 | 2026-11-04 | stockanalysis.com | Moderate |
| Coinbase Q3 revenue, GAAP NI | 1,215.6M (-35% yoy); 718.7M | Q3 2026 | Coinbase 10-Q (sec.gov) | High |
| HOOD price, mcap, EV/S, fwd P/E | 87.63; 78.91B; 15.13; 32.2 | 2026-11-04 | stockanalysis.com | Moderate |
| Kraken Series E vs Forge | 21B post-money (2026-09-10) vs 9.93B | 2026-11-04 | forgeglobal.com [Interested source] | Low |
| CLARITY Senate cloture | 49-50, failed | 2026-09-15 | defirate, fintechweekly (secondary) | Moderate |

## Body

### 1. What a US retail investor can buy (G8: $50k, California, taxable cash account, no margin)

Label: Fact. Cash accounts permit long-only purchases of listed securities with settled cash. No margin, no short selling. Tokenized equities and OUSG/BUIDL-class funds are not available to this investor (non-US or qualified-purchaser only per eco.com 2026 guides, secondary).

| Category | Can buy today? | Examples (play_id) | Notes |
|---|---|---|---|
| Direct-exposure equities | Yes | CRCL, COIN, HOOD, GLXY, BLSH, FIGR, GEMI, SECZ (R-01 to R-08) | Fact: SECZ listed on NYSE 2026-07-02 (investing.com, 2026-07-01). Kraken is not listed. |
| Incumbent equities | Yes | V, MA, PYPL, BK, STT, JPM, NDAQ, ICE, CME, BLK, BEN (R-09 to R-19) | Low purity. |
| Spot and staking ETFs | Yes | IBIT 0.25%, ETHA 0.25%, ETHB 0.25%, BSOL 0.20%, GSOL 0.35%, XRP funds 0.19% to 0.50% (R-20 to R-24) | Fact: fees from stockanalysis ETF page and cryptoetf.today (blog, Low). |
| Tokenization and blockchain ETFs | Yes | BLOK 0.70% (AUM 873M), TKNQ 0.69% (AUM about 1.1M) (R-25) | BKCH not verified. Global X TOKN is Canadian-listed. |
| Tokenized MMF | Yes, narrow | Franklin BENJI via Benji app, $20 minimum (R-26) | Source is secondary (eco.com). Ondo USDY excludes US persons. |
| Network tokens | Yes (exchange custody) | ETH, SOL, LINK (R-28 to R-30) | WS4 owns value-capture test. |
| BUIDL, OUSG, ACRED, Kraken, Ripple, Stripe | No | M-rows | Accreditation or qualified-purchaser required. |
| Issuer-paid stablecoin yield | No | R-31 | GENIUS Act bars issuer yield. |

Recommendation: Do not treat this as an allocation. Phase 3 sizes the sleeve against the 40% drawdown limit. [Moderate]

### 2. Stablecoin yield: what US retail can and cannot do (dated 2026-11-04)

| Label | Statement | Source and date | Confidence |
|---|---|---|---|
| Fact | GENIUS Act (signed 2025-07-18) bars issuers from offering holders interest or yield. Effective on the earlier of 18 months after enactment (about 2027-01-18) or 120 days after final rules. | Latham & Watkins tracker, page updated 2026-08 (lw.com) | High |
| Fact | CLARITY compromise text (2026-05-01) bans yield paid solely for holding a payment stablecoin or economically equivalent to deposit interest, and allows incentives tied to bona fide activity. Treasury and CFTC rules due within one year of enactment. | CoinDesk 2026-05-01 | Moderate |
| Fact | CLARITY has not become law: Senate cloture failed 49-50 on 2026-09-15; no new vote scheduled as of 2026-10-22. | defirate.com; cryptoticker.io (secondary) | Moderate |
| Fact | Circle earns a 3.54% reserve return (Q3 2026) and keeps it; USDC holders receive none from Circle. 3M bill pays 4.21%. | Circle Q3 slides via investing.com 2026-11-04; H.15 2026-11-02 | Moderate |
| Unverified | Whether Coinbase and other platforms currently pay USDC rewards and at what rate (Coinbase page returned 403; search blocked). | NA | Unverified |
| Inference | Today the only legal yield routes for a US retail holder are third-party platform rewards (status unverified) and self-custody DeFi lending (smart-contract risk, tax friction). Both trail a T-bill on risk-adjusted terms. | Reasoning | Low |

### 3. Valuation reality check

Label: Fact (all rows). Source: stockanalysis.com pages fetched 2026-11-04; those pages state no as-of time except "market open" for statistics pages. Compare pages give no EV or growth, so EV/S is NA and mcap/revenue is shown separately. Confidence Moderate for statistics pages, Low for compare pages.

| Ticker | Price | Mcap | EV/S | P/E trailing | P/E fwd | Rev growth yoy | Mcap/Rev |
|---|---|---|---|---|---|---|---|
| CRCL | 76.51 | 19.52B | 5.94 | 43.1 | 60.8 | +17% Q3 (-7.7% ex presale) | 6.4x |
| COIN | 151.86 | 40.21B | 7.03 | n/m | 104.5 | -35% Q3 | 7.4x |
| HOOD | 87.63 | 78.91B | 15.13 | 40.4 | 32.2 | +12% Q3 | 15.5x |
| GLXY | 14.22 | 5.52B | NA | n/m | NA | NA | n/m (gross trading revenue 37.8B) |
| BLSH | 23.17 | 3.51B | NA | n/m | NA | NA | 11.7x |
| FIGR | 23.29 | 5.23B | NA | 27.2 | NA | NA | 8.4x |
| GEMI | 2.825 | 366M | NA | n/m | NA | NA | 1.8x |
| SECZ | 8.13 | 1.39B | NA | n/m | NA | NA | 20.8x |
| V | 433.90 | 806.8B | NA | 35.2 | NA | NA | 17.6x |
| MA | 670.43 | 584.1B | NA | 35.1 | NA | NA | 16.1x |
| PYPL | 60.25 | 50.1B | NA | 11.5 | NA | NA | 1.5x |
| BK | 151.55 | 102.0B | NA (EV negative) | 16.8 | 14.9 | NA | 4.6x |
| STT | 171.87 | 46.8B | NA | 14.1 | NA | NA | 3.0x |
| JPM | 349.68 | 928.6B | NA | 14.7 | NA | NA | 4.9x |
| NDAQ | 109.45 | 60.7B | NA | 29.9 | NA | NA | 10.5x |
| ICE | 174.07 | 97.3B | NA | 23.7 | NA | NA | 8.9x |
| CME | 306.55 | 109.7B | NA | 25.1 | NA | NA | 15.8x |
| BLK | 1,225.24 | 198.7B | NA | 27.9 | NA | NA | 7.0x |
| BEN | 33.64 | 17.1B | NA | 22.9 | NA | NA | 1.8x |

Note: COIN trailing P/E is n/m on stockanalysis although Q3 GAAP net income was 718.7M (mark-to-market gains); adjusted net profit was about 78M (KuCoin summary of the Q3 deck, Low).

| Label | Where it is priced in | Confidence |
|---|---|---|
| Inference | HOOD is priced for continued compounding (15x EV/S, 32x forward earnings) with crypto revenue falling 55%. Least margin of safety. | Moderate |
| Inference | CRCL at 60.8x forward earnings includes a one-off ARC presale (182M); Q3 revenue ex presale fell 7.7%. | Moderate |
| Inference | COIN at 104x forward earnings is priced on trough earnings; the multiple is a cycle artifact, so use EV/S 7.0x instead. | Low |
| Inference | V and MA at 35x are priced for 10% EPS growth; stablecoin disintermediation is not in the price either way. | Low |
| Inference | Crowded: spot BTC ETFs (IBIT AUM 62B, in outflows: -515M October, 2026-11-04 IBIT -405M per 24/7 Wall St). Uncrowded: GEMI (-85% from 52w high), SECZ (-27% YTD), SOL funds (-47% 1y). Cheap does not mean mispriced. | Low |

### 4. Reverse DCF (G1): what CRCL and COIN prices imply

Label: Inference. Method: equity value today grown at required return k for 10 years gives target equity value in 2036; divide by exit P/E to get required 2036 net income; divide by steady-state net margin to get required revenue; compare with TTM revenue. Assumptions (all [Low]): k 10%, exit P/E 20x, net margin 20%, no dilution, no interim cash flow.

| Step | CRCL | COIN |
|---|---|---|
| Mcap today | 19.52B | 40.21B |
| x 1.10^10 (2.594) | 50.6B | 104.3B |
| / 20x = required 2036 net income | 2.53B | 5.21B |
| / 20% margin = required 2036 revenue | 12.7B | 26.1B |
| TTM revenue base | 2.85B (3.03B less 0.18B presale) | 5.44B |
| Implied 10y revenue CAGR | 16.1% | 17.0% |
| Sensitivity: k 8% | 14.0% | 14.8% |
| Sensitivity: exit 25x | 13.5% | 14.4% |
| Sensitivity: exit 15x | 19.5% | 20.4% |
| CRCL translation | 12.7B x 0.96 / 3.5% = 347B USDC (16.7% CAGR from 73.9B) | |
| COIN translation vs forward NI | 5.21B vs 0.385B fwd NI (mcap / 104.5) = 29.8% NI CAGR | |

Inference: CRCL needs USDC near 347B at a 3.5% reserve rate, or 460B at 15x exit and lower rates. Circle's stated 40% CAGR target would exceed that, but the base case (300B, 15% CAGR) yields 8.4%/yr, below the 10% hurdle and about double the 4.21% bill. COIN at the base case (10% revenue CAGR) yields 3.4%/yr. [Low]

### 5. Beta (G2)

| Label | Item | Value | Source and date | Confidence |
|---|---|---|---|---|
| Fact | Beta to BTC / correlation: COIN | 1.26 / 0.75 | Nadcab Labs analysis, mid-2026 (secondary) | Low |
| Fact | HOOD to BTC | 0.96 / 0.58 | same | Low |
| Fact | CRCL to BTC | 1.18 / 0.55 | same | Low |
| Fact | 5Y beta to market: COIN 3.35, HOOD 2.53, BK 1.01 | as stated | stockanalysis.com 2026-11-04 | Moderate |
| Inference | Crypto equities behave as levered market and BTC beta; CRCL has lower BTC correlation but 90-day volatility near 104% (Nadcab). I could not run a regression: no price series fetched. | | | Low |

### 6. Benchmarks (G9)

| Benchmark | Value | Date | Source | Confidence |
|---|---|---|---|---|
| 1M, 3M, 6M, 1Y bill | 4.05%, 4.21%, 4.25%, 4.38% | 2026-11-02 | Fed H.15 | High |
| S&P 500 proxy SPY 1y | +13.5% (YTD +13.4%); P/E 24.0 | 2026-11-04 | stockanalysis.com | Moderate |
| S&P 500 long-run nominal | about 10% (commonly cited; not fetched) | NA | NA | Unverified |
| MMF yield | Not fetched; use 3M bill as proxy | NA | NA | Unverified |

Inference: Excess return hurdle for a crypto-linked equity is 4.21% plus equity risk premium; only the bull cases of CRCL (21.5%) and COIN (12.5%) clear a 10% S&P-like hurdle. [Low]

### 7. Token unlocks and lockups (G10)

| Label | Item | Status | Confidence |
|---|---|---|---|
| Fact | CRCL, FIGR, GEMI (2025 IPOs): standard 180-day lockups | Expired by 2026-11 (inference from IPO dates, not fetched) | Low |
| Fact | SECZ de-SPAC closed 2026-07-01, trading from 2026-07-02 | Sponsor and PIPE lockup terms not found | Unverified |
| Fact | COIN: arrangements to sell about 13.6M shares (about 2.2B) disclosed; stock fell 10.6% to 143.54 on 2026-10-30 | Single secondary source (AMBCrypto) | Low |
| Fact | ARC: 10B genesis mint; presale 242M total, 182M recognized Q3; PoS transition 2027 | Unlock schedule not found | Unverified |
| Gap | Network token unlock calendars (tokenomist.ai returned 403) | Open | Unverified |

### 8. Mid-scale (accredited) plays

| Label | Item | Evidence | Confidence |
|---|---|---|---|
| Fact | Kraken (Payward): Series E 100M at 61.47/share, 21B post-money, Nasdaq Ventures, 2026-09-10. Forge price 29.08, implied 9.93B, 2026-11-04. Deutsche Boerse secondary 13.3B (2026-04). IPO not before Q2 2027. [Interested source: Forge] | forgeglobal.com; crowdfundinsider 2026-09 | Low |
| Fact | Ripple: 50B tender (2026-03); Forge price 97.04, about 15.96B (2026-09-02). [Interested source: Forge] | Benzinga 2026-09 (via search; fetch 403) | Low |
| Fact | Stripe: 159B tender 2026-02-24; secondary 172 to 176B (blog, 2026-08) | Axios 2026-02-24 | Moderate |
| Fact | Anchorage: 4.2B with Tether 100M, 2026-02-05 | search summary, Bloomberg 2026-01-16 on funding seeking | Low |
| Fact | Fireblocks: 8B (2022-01); NPM 5.86/share (2026-10-07); Visa 2.5B bid reported and denied | NPM, V News | Low |
| Fact | Securitize is public (SECZ), no longer a secondary play | investing.com 2026-07-01 | Moderate |
| Unverified | Chainalysis, Paxos, Digital Asset valuations; ACRED and Hamilton Lane minimums; crypto VC fund minimums | Search blocked | Unverified |
| Inference | Private marks are 30 to 70% apart between tender, last round and secondary. Treat secondary entry as an option on an IPO; mid-tier edge is access, not price. | | Low |

Inference: Validator operation (M-10) needs 32 ETH x 2,404.81 = 76,954 per validator and earns an assumed 3%, below the T-bill on a risk-adjusted basis. [Low]

### 9. Large-scale plays and operating requirements

Inference: Issuer economics are scale-driven. At 3.54% reserve return and 42.7% RLDC margin, 40M of assumed annual opex (not sourced) breaks even at 2.65B supply (40M / (0.0354 x 0.427)). At 5B supply: 177M reserve income, 75.6M RLDC. [Low]

Inference: Buying scale costs about 24 cents per dollar of supply (Circle EV 17.82B / 73.9B USDC). Buying 5B for 1.2B yields about 4.2% before growth (L-02). [Low]

Fact: plan.md G4 lists failed consortia (we.trade, Marco Polo, ASX CHESS replacement, TradeLens). Applied as base rate in L-04. [Moderate]

| Requirement | Evidence in this session | Status |
|---|---|---|
| Licenses (GENIUS issuer, OCC trust, state MTL) | GENIUS effective by about 2027-01-18; detailed rules not verified | Gap |
| Custody and compliance staffing | Opex 40M assumed | Unverified |
| Capital | 100M build assumed in L-01 | Unverified |

### 10. Short-horizon catalysts (to 2027-11)

| Date | Event | Plays | Crowding and valuation note |
|---|---|---|---|
| 2026-11-12 | GEMI earnings (Yahoo) | R-07, R-37 | Low crowding; microcap, -85% from high |
| 2026-12-08 to 09 | FOMC; 100bp cut removes about 739M gross, 316M RLDC (24%) at CRCL | R-36, R-01 | Medium; CRCL fwd P/E 60.8 |
| 2026-12-31 | Lame-duck window for CLARITY; midterm results reported 2026-11-03 to 04 (unverified) | R-35 | High crowding in COIN, HOOD on policy |
| 2027-01-18 | GENIUS Act effective at latest | R-34, L-01 | Medium |
| 2027-02 | Q4 earnings: COIN, HOOD, CRCL | R-01 to R-03 | HOOD 32x fwd; COIN trough earnings |
| 2027 Q2 earliest | Kraken IPO | M-01, R-38 | Secondary 53% below mark |
| 2027 | Arc proof-of-stake transition | L-10 | Terms unknown |

### 11. The picks-and-shovels test

| Layer | Commoditizing or pricing power | Evidence | Confidence |
|---|---|---|---|
| custody | Commoditizing | ETF fees 0.19% to 0.50%; Fireblocks mark down from 8B to 2.5 to 5.9B | Low |
| tokenization_platform | Commoditizing | SECZ 20.8x sales, -27% YTD; TKNQ AUM 1.1M | Low |
| exchanges_ats | Cyclical | COIN revenue -35%; HOOD crypto -55% | Moderate |
| issuance | Pricing power only with distribution and scale | Circle keeps 43% of revenue after distribution; rate-exposed | Moderate |
| payments_network | Pricing power | V, MA at 35x earnings | Low |
| l1_l2_infra | Unproven (WS4) | SOL -39%, ETH -26% 1y | Low |
| compliance_identity | Unverified | No data collected | Unverified |

## Gaps and unresolved

| Gap | Status |
|---|---|
| ACRED and Hamilton Lane SCOPE minimums, VC fund minimums | Search blocked; minimums set NA |
| GENIUS final rules and OCC charters | Search blocked |
| Current platform stablecoin reward rates | Coinbase 403; open |
| Beta regression (G2) | No price series; used cited betas |
| Token unlock calendar (G10) | Tokenomist 403 |
| Chainalysis, Paxos, Digital Asset marks | None found |
| Midterm outcome and CLARITY effect | Headlines only, unverified |
| EV, growth for 13 tickers | Compare pages lack them; filings not fetched |
| BKCH, S&P 500 long-run return, MMF yields | Not verified |

## Files written

`research/plays.csv` (60 rows), `research/data/valuations.csv` (19 rows), `research/ws/ws5.md`, `research/ws/search_log_ws5.md`.
