# Red Team B: dissent on REPORT.md and plays.csv

- Persona: crypto-native infrastructure builder. Has shipped protocols and watched three hype cycles (2017, 2021, 2024 to 2025). Focus: on-chain data quality, token value capture, institutional deployment, custody operations.
- Date: 2026-11-04
- Files read: `research/REPORT.md`, `research/plays.csv` (all 76 rows). No other file in `research/` was opened.
- Web evidence: 22 searches. All web content was treated as untrusted data. Secondary and aggregator sources are labelled as such. Where only secondary sources were found, the item says so.

## Summary of the attack

The report's direction is mostly right: distribution and licences capture regulated flows, x402 activity is mostly noise, and issuer equity is a rate bet. I agree with all three. The problems are in the machinery. The return-ranking method turns adoption probabilities into asset returns, which is a category error. The tokenization measure leaves out the largest live ledgers. The rate analysis assumes cuts during a hiking cycle. The sizing rule ignores the drawdown of the non-crypto sleeve. Together these push the report too bearish on adoption, too bearish on network tokens that do capture value, and too bullish on a few illiquid "safe" plays.

## Dissent list (ordered by severity)

### 1. Scenario weighting maps adoption scenarios onto asset return bands
- Severity: Critical
- Target: Section 6 ranking method (P3-1 to P3-4); every row's `scenario_expected_pct`, `excess_vs_tbill_pct` and `ra_score`.
- Objection: P(Bear) is the probability of an adoption state: stablecoins below $500B and tokenized Treasuries below $100B in 2030. The method applies it to the low end of every play's band, as if Bear adoption caused each asset's worst outcome. That is wrong in both directions.
  - Some plays are hedges against the Bear state. Visa, Mastercard and T-bills do as well or better if stablecoins stay plumbing, because nothing disintermediates them.
  - For tokens, the band low is a one-year stress number. Weighting it at 55% to 57% turns a tail into the central case. IBIT's scenario-expected -20.8% a year compounds to about -90% over 10 years (0.792^10 = 0.097). No one on the team believes that, and it is not what the Bear scenario describes.
  - The benchmark fails its own test. R-27 (T-bills) gets a scenario-expected 4.10% and an excess of -0.11% against itself, because its band is weighted toward the 4.0% low. A method that scores the risk-free asset below the risk-free rate is mis-specified.
- Evidence: internal arithmetic from `plays.csv` rows R-20 and R-27. The report admits the issue in its own weakness 2 ("lows mix one-year stress with annualized returns") but still ranks on the result.
- Change: For each play, estimate a return conditional on each scenario, using a consistent horizon (for example 5-year annualized). Do not reuse band low, mid and high. Mark explicitly which plays are long Bear (V, MA, T-bills, BK) and which are long Bull (CRCL, tokens). Until then, drop `scenario_expected_pct` and `ra_score` from the ranking and say so.

### 2. The tokenization measure (T) leaves out the ledgers that are actually live
- Severity: Critical
- Target: Executive summary, Section 4 (scenario bands, falsifiers), weakness 3 (no W series), L-04, M-06.
- Objection: T is RWA.xyz *distributed* tokenized Treasuries at $14.25B. It excludes the permissioned, represented ledgers where institutions actually deploy.
  - RWA.xyz shows about $372B of represented value on Canton, with zero distributed, as of about 2026-08. That is 26x the report's T.
  - Broadridge DLR averages $357B to $368B a day in repo every month of 2026, $7T to $9T a month. The report itself cites $359B a day.
  - DTCC's tokenization service ran live production trades on Canton and Besu on 2026-07-15, under a December 2025 SEC no-action letter.
  The report's Base scenario says "Ledgers carry a minority of wholesale flows." On these numbers, that may already be true for repo. Meanwhile the Bear probability rests on S and T only. Represented assets are not settlement in central bank money, and DTC gives the tokens no collateral value in its own risk management. That is a real caveat, but it argues for reporting represented and distributed separately, not for leaving represented out.
- Evidence:
  - RWA.xyz Canton network page, https://app.rwa.xyz/networks/canton (snapshot about 2026-08; via search summary)
  - RWA.xyz framework post, https://app.rwa.xyz/blog/a-new-framework-for-tokenized-assets-distributed-and-represented
  - Broadridge June 2026 release via CFOtech, https://cfotech.news/story/broadridge-dlr-repo-hits-usd-7-5-trillion-in-june; Broadridge May 2026 release, https://www.broadridge.com/press-release/2026/broadridges-dlr-platform-achieves-220-percent-year-over-year-growth-in-may [Interested source]
  - DTCC Canton test, The Block, https://www.theblock.co/post/383009/dtcc-onchain-treasury-test-canton-network-sec-greenlight
  - Everstake on the 2026-07-15 live trades, https://everstake.one/resources/blog/dtccs-first-live-tokenized-trades-on-canton [secondary]
- Change: Add a W series built from DLR, Kinexys and Canton represented value, and report T in two forms, T-distributed and T-represented. Restate the scenario definitions so it is clear which T each one uses. Re-run the model. If Bear stays defined on T-distributed, rename it "public-chain tokenization stays niche" so readers do not take it to mean "ledgers stay niche."

### 3. The rate analysis assumes cuts during a hiking cycle
- Severity: Critical
- Target: Section 5 (the "100 bp cut" fact), R-01, R-36, Section 12 catalyst calendar, the benchmark.
- Objection: The FOMC raised the target range 25 bp to 3.75% to 4.00% on 2026-09-16. It held on 2026-10-28 with two dissents in favour of a hike, and markets price a December hike. Every rate sensitivity in the report is framed as a cut: the "100 bp cut removes $739M" line, R-36's band of -30 to +20, and the kill criterion "two cuts priced." The 3-month bill at 4.21%, above the top of the target range, is consistent with a hike being priced, which the report does not mention. The rate direction changes three conclusions:
  - (a) Issuer float income rises in a hike, so CRCL's rate leverage now points up.
  - (b) Higher policy rates raise the opportunity cost of holding a zero-yield stablecoin. That is the main reason supply shrank in 2022, and it explains the current flat supply better than "demand is flat" does (see item 4).
  - (c) The hurdle rate is a moving target.
- Evidence: Admiral Markets, "FOMC October 2026: Fed Holds Rates in a 10-2 Vote as Markets Price a December Hike," https://admiralmarkets.com/analytics/traders-blog/fomc-october-2026-fed-holds-rates; securities.io, https://www.securities.io/fomc-holds-federal-funds-target-range-as-two-members-dissent/ (both 2026-10-28, secondary).
- Change: Make the rate sensitivities symmetric, plus and minus 100 bp. Model stablecoin supply as rate-elastic. Re-centre R-36 and redo the R-01 bear case, which assumes a 3.0% reserve yield.

### 4. A momentum model run at a cyclical trough produces a structural Bear call
- Severity: Critical
- Target: Executive summary probabilities, Section 4 model ("measured momentum drives the result more than any single policy driver").
- Objection: S is a stock that moves with the crypto cycle and with rates. Today's 12-month reading (-3.0%) comes at a joint trough:
  - BTC is down 20% over the year and about 37% from its high.
  - The Fed is hiking.
  - The largest exchange theft on record ($6.3B, Binance, 2026-10-29) happened six days before the snapshot.
  In 2022 to 2023, supply fell about a third and then roughly tripled. Bear requires S below $500B in 2030, about 14% a year from $295B. That is below the 36-month rate (33%) and below every four-year window since 2019. A model whose most powerful input is trailing momentum will be most bearish exactly at troughs. That is pro-cyclical forecasting, and it is how analysts missed the 2023 to 2025 recovery. Also check the peak figure: DefiLlama-sourced coverage puts the total stablecoin peak at $322.4B on 2026-05-26, against the report's $315.5B USD-only peak on 2026-05-17. The report should say which series it uses.
- Evidence:
  - Binance $6.3B breach: Kitco, https://www.kitco.com/news/off-the-wire/2026-10-30/where-binances-63-billion-breach-ranks-cryptos-biggest-hacks-and (2026-10-30); BleepingComputer, https://bleepingcomputer.com/news/security/binance-links-63-billion-crypto-theft-to-compromised-devops-laptop
  - Stablecoin peak: Crypto Briefing, https://cryptobriefing.com/stablecoin-market-record-322-billion/ (2026-05) [secondary]
- Change: Replace trailing 12-month momentum with a cycle-adjusted measure: growth over a full cycle, or growth regressed on BTC drawdown and the policy rate. At minimum, present the "drivers only, no momentum" run (54/35/11) as co-lead, and state that the 12-month variant is measured at a trough.

### 5. The sizing rule ignores the drawdown of the rest of the sleeve
- Severity: High
- Target: Section 7 sizing warning ("0.45 x 90% = 40.5%").
- Objection: The 45% cap assumes the other 55% of the sleeve has zero drawdown. But the report's own recommended incumbents (V, MA, BK, BLK, ICE) carry 30% to 40% stress drawdowns in `plays.csv`, and they fall together with crypto in a liquidity stress. If the remainder sits in incumbents at a 35% drawdown, a 40% limit allows x(0.90) + (1 - x)(0.35) ≤ 0.40, so x ≤ 9%. If the remainder is half T-bills and half incumbents, x ≤ 31%. Also, a correlated stress year is when issuer and exchange equities drop 80% to 92% *and* the private marks (M-01 to M-05, stress set at 70%) cannot be sold.
- Evidence: `plays.csv` `stress_drawdown_pct` column; the report's own Section 7.
- Change: Size on a joint stress across all holdings, with private and locked positions counted at a full loss for liquidity purposes. Publish a table of maximum crypto weight for each mix of the remainder.

### 6. The top-five tables contradict the report's own scores
- Severity: High
- Target: Executive summary "Top five plays per tier."
- Objection:
  - Retail #1 (R-27 plus R-26 BENJI) has negative excess (-0.11 and -0.54). BENJI scores -0.27, below V and MA (0.121).
  - Mid #3 to #5 (M-02 at -0.096, M-01 at -0.142, M-04 at -0.132) rank above M-10 (-0.043), M-07 (-0.063) and M-03 (-0.110), which score better and are not listed.
  - Large #1 (L-03, -0.27) ranks above L-02 (0.024). L-06 and L-05 have no score, and L-05 is tagged Unverified.
  A ranking that overrides its own score without saying why is judgment presented as method.
- Evidence: `plays.csv` `ra_score` column.
- Change: Either rank by score, or label the table "lead judgment" and give a one-line reason for each override. Remove Unverified rows (L-05) from any top-five list.

### 7. "Distribution wins" is the thesis, yet the issuer ranks above the distributor
- Severity: High
- Target: Executive summary retail #5 (R-01), R-02, A-04, L-09, Section 11.
- Objection: The report's own evidence says Circle pays 62% of reserve income to distribution partners, mostly Coinbase. It also says the OCC final rule dropped the affiliate-yield presumption, which strengthens distributors' bargaining power. Coinbase books about $307M a quarter in stablecoin revenue, about $1.2B a year and about 23% of TTM revenue, with no issuer licence risk. Yet CRCL is a retail top-five play and COIN is not. On the report's own logic, COIN is the cleaner "USDC economics" exposure and CRCL is the squeezed party. Two counterweights:
  - (a) COIN carries trading-cycle beta.
  - (b) A Base token could move Base sequencer revenue (about $78M in 2025, secondary) off Coinbase's income statement. Polymarket put a 2026 launch at 69% (May 2026, secondary), and JPMorgan estimated up to $34B of value.
- Evidence:
  - The Block on Base token exploration, https://www.theblock.co/post/370668/coinbase-incubated-base-network-beginning-to-explore-native-token-creator-jesse-pollak-says (2025-09)
  - JPMorgan estimate via The Block, https://www.theblock.co/amp/post/376134/coinbases-base-token-could-be-worth-34-billion-jpmorgan-says
  - Polymarket odds and sequencer revenue via AMBCrypto, https://ambcrypto.com/base-is-exploring-native-token-launch-is-2026-the-year/ (2026-05) [secondary]
- Change: Explain why CRCL is ranked above COIN, or swap them. Add "Base token launch with sequencer revenue routed to the token" to COIN's key risks. Correct the Section 5 claim that "Base's sequencer margin accrues to Coinbase equity": it does today, and that may change.

### 8. "Network tokens capture little" generalizes from Ethereum and ignores the counterexamples
- Severity: High
- Target: Section 5 Public L1 and L2 row, Section 11 "Network tokens" row, R-20 to R-30.
- Objection: The value-capture test uses Ethereum's fee revenue ($127M in H1 2026) as the archetype. Two networks contradict the generalization:
  - Tron hosts 32% of stablecoins and earned about $3.5B in 2025 (CoinGecko via secondary), far above Ethereum. It also shows the fragility of this kind of capture: 27 Super Representatives voted a 60% base-fee cut on 2025-08-29, which shows that fee capture can be switched off by a concentrated validator set.
  - Hyperliquid routes about 99% of perp fees, roughly $0.8B to $1.06B annualized in mid-2026, into HYPE buybacks, and US-listed HYPE ETPs now exist. Buybacks are falling, though: from $317M in Q3 2025 to $192M in Q1 2026.
  The right conclusion is "capture is real where the chain or app owns order flow or a dominant stablecoin corridor, and fragile because governance can change it." "Capture is weak" is too broad.
- Evidence:
  - Tron revenue: Bit2Me, https://news.bit2me.com/en/Tron-surpasses-its-rivals-in-net-revenue/ ; CoinDesk Research, https://www.coindesk.com/research/tron-network-q3-2025 [secondary]
  - Hyperliquid: Allium, https://allium.so/reports/hyperliquid-hype-onchain-research ; KuCoin flash on buybacks, https://www.kucoin.com/news/flash/hyperliquid-buybacks-exceed-1-16b-as-hype-surpasses-62 [Interested source]
  - HYPE ETPs: etf.com, https://www.etf.com/sections/news/hype-token-etfs-what-hyperliquid-and-whether-thyp-bhyp-or-hypg-worth-buying (2026)
- Change: Rewrite the value-capture row with a per-chain fee and buyback table (ETH, TRX, SOL, HYPE, BNB). Add TRX and HYPE as small-option or watch rows, with governance-concentration and US-access warnings.

### 9. The Canton plays (L-04, M-06) rest on the wrong base rate and stale facts
- Severity: High
- Target: L-04, M-06, Section 4 consortium analog.
- Objection: L-04 scores a Canton stake against the we.trade and TradeLens failures (scenario-expected -63.6%). Its kill criterion, "No volume within 24 months," is already moot: DLR, the DTCC tokenization pilot and $372B of represented value all run on Canton or Daml. M-06 says no 2026 valuation was found. Digital Asset raised about $355M to $365M at a $2B valuation, led by a16z crypto, in May 2026. Canton Coin (CC) traded at about $5B to $6B of market cap in May 2026, more than the equity, which raises its own question of what the token captures. The genuine Canton risk is concentration: Rosa and Roubini (2026-05) found that a large share of Canton activity is a single application (DLR). That is a different risk from consortium failure.
- Evidence:
  - The Block, https://theblock.co/post/409168/canton-digital-asset-additional-10-million-funding-same-2-billion-equity-valuation-expanding-round-365-million
  - Cointelegraph, https://cointelegraph.com/news/company-canton-network-raises-300m-2-billion-valuation (2026-05)
  - Rosa and Roubini, https://rosa-roubini.com/wp-content/uploads/2026/05/Canton-RS-21May26.pdf (2026-05-21)
- Change: Re-price L-04 and M-06 from the 2026 round. Replace the base rate with "single-application concentration." Treat CC as a separate token row that needs an emissions and burn analysis (see item 17) before any recommendation.

### 10. M-08, tokenized private credit, is the mid-tier #1 only because its drawdown is understated
- Severity: High
- Target: M-08, executive summary mid #1.
- Objection: M-08 has the best mid-tier score (0.169) because its stress drawdown is set at 15%. Private credit NAVs are appraisal-smoothed, so a 15% figure understates economic loss in a credit event. Third-party notes and RWA.xyz describe ACRED with:
  - quarterly redemption, which the report's `liquidity` field correctly says
  - interval-fund gates of about 5% a quarter
  - a $50,000 minimum
  - full exit possibly taking 6 to 12 months or more in stress
  - on-chain AUM of only about $35M to $50M, so the token has no meaningful secondary liquidity
  The on-chain wrapper adds smart-contract and transfer-agent risk and no liquidity. At a 30% drawdown the score halves to about 0.085, below V and MA.
- Evidence:
  - RWA.xyz ACRED page, https://app.rwa.xyz/assets/apollo-diversified-credit-securitize-fund
  - Third-party note, https://product-onepagers.vercel.app/acred.html (2026-03) [informal, secondary]
- Change: Set stress at 25% to 35% and treat the gate as a liquidity haircut. Demote M-08 from #1. Compare it with buying the underlying fund through conventional channels, which removes the wrapper risk.

### 11. Private-secondary marks are not like-for-like, and Ripple is an XRP proxy
- Severity: High
- Target: M-01, M-02, M-03, M-04, M-05, A-06, R-38.
- Objection: "Discount to tender" or "53% below Series E" compares a preferred-share primary price, which carries liquidation preference, with indicative common-share secondary quotes. Those quotes are often for SPV units that carry a second layer of fees and carry and sit behind a right of first refusal. Kraken marks found range from $20B (November 2025 and May 2026 rounds) through $13.3B (Deutsche Boerse) and $12.2B (June secondary) to the report's $9.93B on Forge. That spread tells you how far the marks disagree, not that you are getting a bargain. Kraken confirmed a confidential S-1 but paused the IPO in March 2026. For Ripple, funds estimate that at least 90% of net asset value is XRP. M-02 is therefore a levered, illiquid XRP position stacked on R-24, with a correlated drawdown.
- Evidence:
  - Kraken filing and valuations, KuCoin flash, https://www.kucoin.com/news/flash/kraken-confirms-confidential-ipo-filing-despite-market-challenges ; Dextools, https://www.dextools.io/news/kraken-20-billion-valuation-ipo-reap-bitnomial-june-2026 [secondary]
  - Ripple: Unchained, https://unchainedcrypto.com/are-investors-in-ripples-500-million-raise-just-buying-discounted-xrp/ (2025-11); Finance Magnates, https://financemagnates.com/cryptocurrency/news/ripple-holds-over-70b-in-xrp-why-is-ripples-equity-valued-at-3b-novogratz
- Change: For each secondary, record the share class, SPV fee layers, ROFR and transfer restrictions. Model M-02 as XRP beta times a discount factor, and cap combined R-24 plus M-02 exposure. Keep M-01 conditional on a primary round or S-1, not on a Forge print.

### 12. New-issuer economics (L-01, L-02) assume Circle's margin and stable supply
- Severity: High
- Target: L-01, L-02, L-08, Section 11 breakeven of $2.65B.
- Objection: L-01's breakeven uses Circle's 42.7% RLDC margin. A new issuer has to outbid Circle for distribution: partner-network models such as USDG pass most reserve income back to partners. At a 20% margin, breakeven is $40M / (3.54% x 20%) = $5.65B of supply. At 10%, it is $11.3B. L-02 values a target at Circle's 24 cents per dollar of supply. But sub-scale supply is usually rented: it is incentive-paid or concentrated in a few large holders, and it leaves after the deal. Tether's USAT shows how hard onshore distribution is. Even with the Tether brand and an Anchorage charter, it reached only about $176M of supply roughly seven months after its 2026-01-27 launch (single aggregator source for the August figure).
- Evidence:
  - The Block on the first USAT attestation, https://www.theblock.co/post/391762/anchorage-usat-reserve-17-6-million-assets-backing-tether-us-stablecoins
  - The Block on USAT supply, https://www.theblock.co/news/markets/2026-05-28-tethers-usat-supply-grows-540-month-over-month-latest-attestation-shows-402933 (2026-05-28)
  - DIA on the August figure, https://www.diadata.org/map/global-stablecoins/stablecoin/usat/ [secondary]
- Change: Run L-01 at RLDC margins of 10%, 20% and 43%. In L-02, discount acquired supply for holder concentration and model a 30% to 50% post-deal outflow in the base case.

### 13. The stablecoin-chain wave is under-modelled, and the Arc presale carries a refund contingency
- Severity: High
- Target: Section 2, R-01, L-10, R-21, R-28, R-29.
- Objection: Tempo mainnet launched on 2026-03-18 and has passed $1B of rolling 30-day transfers, mostly enterprise payouts (single secondary source). Arc is in mainnet beta. Plasma's XPL fell about 95% from its September 2025 high, with stablecoin TVL collapsing ahead of unlocks. The lesson: issuer-owned and processor-owned chains move value to equity (Stripe, Circle), payment-chain tokens without captive flow go to near zero, and Ethereum and Tron lose stablecoin settlement share. None of this appears in the ETH or SOL bands. Separately, the ARC presale was $222M at a $3B FDV (May 2026). The report says $242M, which needs reconciling. Coverage describes investor repayment rights tied to the proof-of-stake transition by 2028-05-08. If that is right, part of the $182M of presale revenue Circle recognized in Q3 is contingent. And L-10's "unlock terms unknown" understates the problem: the presale's vesting schedule is undisclosed.
- Evidence:
  - Tempo: Crypto Briefing, https://cryptobriefing.com/tempo-1b-stablecoin-transfer-volume/ (2026-08) [secondary]; crypto.news, https://crypto.news/stripe-and-paradigms-tempo-mainnet-goes-live-for-machine-payments/
  - Plasma: Plasma deep-dive, https://portfolio-indiebuidl.vercel.app/blog/plasma_xpl_payfi [secondary]
  - Arc presale: Cointelegraph, https://cointelegraph.com/news/circle-raise-222-million-arc-token-presale-3-billion (2026-05); DeFiPrime, https://defiprime.com/arc-tokenomics-circle-whitepaper [secondary]
- Change: Add a chain-share forecast for stablecoin settlement by venue (ETH, Tron, Solana, Base, Arc, Tempo), and use it to haircut the ETH and SOL bands. Check the ARC repayment terms against Circle's 10-Q and treat the presale revenue as possibly refundable in R-01's valuation.

### 14. Staking ETPs carry a liquidity mismatch the report does not mention
- Severity: High
- Target: R-22, R-23, M-10.
- Objection: ETHE is 71% staked, per the report. Ethereum's validator exit queue reached about 850,000 ETH in early October 2026, about 13 days to exit, after one large provider exited as a precaution. The entry queue has run 40 to 52 days. A staking ETP that faces a redemption wave either holds an unstaked buffer, which drags yield, or relies on liquidity providers and lets the price discount to NAV widen. The report's stress drawdown and liquidity field ("daily") do not reflect this. The same applies more mildly to SOL, which has epoch-based unstaking.
- Evidence:
  - EdgeX news on the 2026 high, https://pro.edgex.exchange/en-US/news/article/ethereum-validator-exit-queue-hits-2026-high
  - Crypto Briefing, https://cryptobriefing.com/ethereum-exit-queue-eases-metamask-exits/ (2026-10-05) [secondary]
- Change: For staking ETPs, record the staked share, liquidity buffer policy and historical NAV premium or discount in stress. Downgrade the liquidity field to "daily, with a stress discount."

### 15. Custody and self-custody operations are missing; freeze risk survives self-custody
- Severity: Medium
- Target: R-28, R-29, R-30 (direct tokens "via Coinbase or Kraken"), R-31, Section 6 Binance paragraph.
- Objection: The direct-token rows put retail holdings on exchanges, while the report's own risk table gives an 80% chance of a theft above $500M. There is no guidance on:
  - hardware wallets or multisig
  - inheritance and recovery planning
  - address-poisoning and approval-drain attacks
  - physical coercion risk
  - the fact that moving coins to self-custody breaks 1099-DA basis reporting, which covers only units held in the same account
  The Binance incident also shows a point the report misses: Tether froze about $1.57B and Circle about $800M of linked funds. Issuer freeze power applies in self-custody too, which is useful against theft and a counterparty risk for any holder. And Binance covered losses from its own funds ($6.34B set aside). The relevant tail risk for a US Coinbase customer is bankruptcy treatment of custodial assets without CLARITY, not theft at an offshore exchange.
- Evidence: Khaleej Times on the freezes, https://khaleejtimes.com/business/cryptocurrency/crypto-exchange-binance-freezes-assets-after-63-billion-security-breach (2026-10-30); YourStory, https://yourstory.com/2026/10/binance-63-billion-impact-security-breach-freezes-3-billion-crypto-assets
- Change: Add a custody section. For most retail investors, the ETP (R-20 to R-24) should dominate direct holding unless they self-stake or need on-chain use. Score direct tokens below the ETP on the same asset. Re-target the R-32 counterparty paragraph to custodial bankruptcy risk.

### 16. DeFi convergence: self-custody is not the only route to on-chain yield
- Severity: Medium
- Target: R-32, R-33 ("Only route to on-chain yield above zero for a US individual").
- Objection: Since September 2025, Coinbase has offered in-app USDC lending through Morpho vaults on Base to US customers outside New York. The yield is variable (launch top rate 10.8%). Separately, it pays USDC rewards of 4.1%, or 4.5% for Coinbase One members (launch-period figures). This is the convergence pattern that matters: DeFi risk delivered through a regulated front end, with the platform taking a share. R-33's claim is false, and R-32 and R-33 have no rates at all.
- Evidence: The Block, https://www.theblock.co/post/371281/coinbase-usdc-onchain-lending (2025-09-18); Blockworks, https://blockworks.co/news/coinbase-usdc-onchain
- Change: Add a row for platform-intermediated DeFi lending, with smart-contract, curator and liquidity risk. Fetch current rates before quoting any. Fix R-33's wording.

### 17. Token unlocks and emissions are absent from every token row
- Severity: Medium
- Target: R-21 to R-24, R-28 to R-30, A-08, L-10, and any CC, HYPE or TRX additions.
- Objection: None of the token theses has a supply-side column:
  - LINK: The Chainlink Reserve held about 5.86M LINK by 2026-09-10, about $66M at $11.35, or 0.8% of market cap. The report's condition, "only if buybacks accrue," is technically met but immaterial. It is also dwarfed by scheduled releases from non-circulating supply (not verified in this session).
  - XPL: unlocks drove the collapse.
  - ARC: vesting is undisclosed.
  - HYPE: team unlocks are ongoing.
  - CC: emissions are continuous.
  - SOL: inflation dilutes holders who do not stake.
  Missing this is how most 2021 to 2025 token positions lost money even when usage grew.
- Evidence: KuCoin flash on the Chainlink Reserve, https://www.kucoin.com/news/flash/chainlink-adds-92-000-link-to-strategic-reserve-total-holdings-reach-5-67-million (2026-08) [secondary]; Arc and Plasma sources in item 13.
- Change: Add `net_supply_change_12m_pct` and `next_major_unlock` columns. Treat net dilution as a negative return input in every token band.

### 18. Missing plays, and one missing avoid list
- Severity: Medium
- Target: Section 6 matrix, Section 11.
- Objection: Four investable names are missing, along with one category that needs an explicit avoid:
  - Broadridge (BR): the most direct listed exposure to a live wholesale ledger (DLR, about $360B a day). Its purity is low because DLR is small relative to BR's revenue, but it is purer than JPM's exposure to Kinexys.
  - WisdomTree (WT) and WTGXX: WTGXX is retail-accessible on WisdomTree Prime. That contradicts R-26's claim that BENJI is the "only clearly retail-open tokenized MMF." It got SEC relief for 24/7 trading at a constant $1 via USDC (2026-02) and is now a deposit rail on Prime (2026-08). WisdomTree's tokenized AUM was $770M at end-2025, a higher share of the firm than BlackRock's or Franklin's.
  - HYPE ETPs and TRX: as sized options (item 8).
  - Explicit avoid for digital asset treasury companies: many trade below 1.0x mNAV, and Strategy's basic mNAV was reported at 0.74x on 2026-08-25. These names appear in retail portfolios as "crypto exposure," so the report should address them.
- Evidence:
  - WisdomTree: ThinkAdvisor, https://www.thinkadvisor.com/amp/2026/02/24/wisdomtree-gets-sec-nod-for-tokenized-money-fund-to-trade-247/ ; WisdomTree blog, https://www.wisdomtree.com/onchain/insights/blog/wtgxx-is-now-a-transfer-method ; Markets Media, https://www.marketsmedia.com/wisdomtree-has-breakout-year-in-tokenized-funds/
  - Treasury companies: CoinMarketCap Academy, https://coinmarketcap.com/academy/article/bitcoin-treasury-companies-losing-financing-edge-2026 [secondary]; uktaxdrag tracker, https://uktaxdrag.co.uk/mnav-explained [secondary]
- Change: Add BR, WT, WTGXX, HYPE ETP and TRX rows, and a "DATs: avoid at mNAV below 1.2x" row. Correct R-26's "only" claim.

### 19. The wrong hurdle for long-horizon equities, and pre-tax ranking for a California reader
- Severity: Medium
- Target: R-09 to R-19, A-01, A-02, R-27, retail #2 and #4.
- Objection: V and MA bands of 7% to 10% a year sit below the 10% S&P long-run figure that R-27 itself cites, and V and MA are already about 2% to 3% of SPY. Ranking a 10-year equity against a 3-month bill flatters every incumbent. The relevant question for retail is whether an overweight beats the index. Also, T-bill interest is exempt from California tax, while equity gains are taxed at up to 13.3% in California. The ranking is pre-tax.
- Evidence: `plays.csv` R-27 detail and R-09/R-10 bands; report Section 8.
- Change: Benchmark equity plays against SPY (and 10-year Treasuries). Show after-tax excess for the California reader the report assumes.

### 20. Supply is not usage, and chain attribution is mis-read
- Severity: Medium
- Target: Section 1, Section 5 ("Ethereum 47%, Tron 32%"), A-04 ("Base carried over 99% of agentic stablecoin volume").
- Objection: Supply share counts where tokens sit, and a large part of Ethereum-chain USDT and USDC is exchange and treasury inventory. Tron dominates retail emerging-market transfer counts. Base's 99% share of agentic volume is an artifact of the x402 facilitator defaulting to Base, not evidence that agents prefer Base. The report notes a 46x gap between adjusted payment measures, then uses supply as its only demand signal.
- Evidence: internal; Tron report in item 8.
- Change: Add S2, adjusted payment volume (excluding CEX-internal transfers, bots and same-entity flows), alongside supply. Report chain share by transfer count and adjusted volume, not only by supply.

### 21. The ETH value-capture test stops at fee revenue
- Severity: Medium
- Target: R-21, R-22, R-28, Section 11.
- Objection: Ethereum cut L1 fees by design (blobs, gas-limit increases). Fee-based DCF therefore says little about ETH's price, which is driven by its role as collateral and monetary asset: ETF holdings, treasury-company holdings, DeFi collateral. The report's "value capture unproven" is right on cash flows and silent on the actual price driver. Separately, a holder who does not stake (ETHA) is diluted by net issuance that a staker is not. The report ranks ETHA and ETHB with near-identical bands, but the spread between them is structural, not 2.5 points of noise.
- Evidence: report WS4 figure ($127M H1 2026).
- Change: State that ETH bands are monetary-premium bets with no link to the adoption scenarios. Show the ETHA versus ETHB gap as staking yield minus fee minus tax drag.

### 22. Base and L2 economics are stale
- Severity: Medium
- Target: Section 5 L1 and L2 row, A-04.
- Objection: In February 2026, Base announced it is moving off the OP stack to its own "base/base" stack, which removes the Superchain revenue share and changes the "leak to L2s" framing for OP. Combined with the token question in item 7, the L2 picture in the report reads as written for 2024.
- Evidence: AMBCrypto, https://ambcrypto.com/base-is-exploring-native-token-launch-is-2026-the-year/ (2026-05) [secondary]
- Change: Update the row. Note that OP and other shared-sequencer revenue models lose their largest contributor.

### 23. Thirteen unpriced rows and invented event bands dilute the matrix
- Severity: Low
- Target:
  - unpriced rows: R-32, R-33, M-06, M-12, L-05, L-06, L-07, L-08, L-10, A-05, A-06, A-07
  - event and distressed rows: R-07, R-34 to R-38
  - A-03
- Objection: Rows with no band cannot be ranked and inflate the count of plays from 75. The event rows use bands of plus or minus 10% to 15% chosen by assumption. A-03's band is the 52-week range, which is not a return model.
- Change: Move unpriced rows to a watch list. Drop the event rows from investment recommendations, or present them as catalysts.

### 24. The geography rows are off-theme
- Severity: Low
- Target: G-01 to G-07, Section 10.
- Objection: The report concedes that these are macro bets with a thin link to programmable money. Keeping them in the same matrix invites readers to treat them as theme exposure.
- Change: Move them to an appendix. Keep NU and MELI only as Pix and distributor analogs.

### 25. Tax items stated with more confidence than they deserve
- Severity: Low
- Target: Section 8 (wash sale on spot ETPs), R-22 and R-23 (UBTI note).
- Objection: Spot BTC and ETH ETPs are grantor trusts. Practitioners disagree on whether Sec. 1091 reaches shares when the trust's holders are treated as owning a non-security asset directly. Calling it "likely applies" picks one side. The "UBTI unresolved" note for staking ETPs in an IRA also needs a cited authority. Passive staking rewards in a grantor trust are not obviously income from an unrelated trade or business.
- Change: Tag both items [Contested] and `[Verify with CPA]`, and present both readings.

## Where the report is right (for balance)

- x402 and "agentic" token activity is mostly noise. The A-08 avoid stands.
- Issuer equity is a rate-times-adoption bet, and distribution takes the majority of float economics.
- The weak onshore uptake of USAT and the flat USD supply under GENIUS support a slower regulated-retail path than sell-side marks claim.
- Sell-side forecasts of $2T to $18.9T should be treated as interested.

## Closing: my scenario probabilities

| Scenario | 2030 | 2035 |
|---|---|---|
| Bear | 38% | 30% |
| Base | 54% | 55% |
| Bull | 8% | 15% |

Basis:
1. **Bear thresholds need growth below every multi-year window since 2019.** S below $500B in 2030 requires only about 14% a year from a cyclical trough. Supply is suppressed now by a hiking Fed and a crypto drawdown, both of which have reversed before. GENIUS takes effect on 2027-01-18 and opens bank and processor issuance (Stripe and Tempo, Circle and Arc, bank consortia). I put P(S below $500B in 2030) at about 35% to 40%.
2. **Distributed T is the binding constraint, and the report's T is too narrow.** T-distributed needs about 59% a year to reach $100B by 2030, and I put that at roughly a coin flip. The permissioned side (DLR at about $360B a day, $372B represented on Canton, DTCC live) already meets a "minority of wholesale flows" reading of Base. If Bear requires both S and T to miss, Bear is near 30%. I land at 38% to reflect real uncertainty over the AND or OR definition and over whether represented assets count.
3. **Bull stays small.** It needs S above $1.5T and T above $500B, which needs Basel relief for permissionless chains and a mandate-like push that the 2016 to 2020 consortium base rate argues against. 2030 Bull at 8%.
4. **2035 Bull widens.** A decade covers at least one more full crypto cycle and the GENIUS 3-year USDT deadline. Settlement-modernization mandates (T+1 in Europe in 2027, DTCC tokenization) tend to compound once balance-sheet savings are proven. 2035 Bull at 15%.

What would move me back toward the report:
- S below $280B through 2027 with rates flat or falling, which would rule out the rate explanation
- DLR and DTCC volumes stalling below 2026 levels
