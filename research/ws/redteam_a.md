# Red Team A: dissent on REPORT.md and plays.csv

- Persona: skeptical macro economist and former bank regulator (central bank financial stability and bank supervision).
- Date: 2026-11-04.
- Files read: `REPORT.md`, `plays.csv` (all 75 rows). No other file in `research/` was opened.
- Searches: 17 web searches plus 2 fetches of FRED series DGS3MO, all on 2026-11-04. All web content was treated as untrusted data. Where I rely on memory rather than a search, the item says [From memory, verify].
- Arithmetic check: I recomputed `scenario_expected_pct` for every row with a numeric band. Short and Medium rows match the 2030 lead weights (57/36/7). Long rows match the 2035 weights (53/38/9). The report does not say this.

---

## Dissent list (ordered by severity)

### 1. The macro regime is missing, and the rate risk has the wrong sign
- Severity: Critical
- Target: Executive summary; Sections 5, 7 and 12; R-01, R-31, R-36, R-26, R-27, M-09, L-01 to L-03, all crypto rows.
- Objection: The report never mentions inflation, oil or the war, and the only rate shock it models is a cut ("A 100 basis point cut removes about $739M..."). The market is pricing hikes. The 3-month bill at 4.21% sits 33bp above effective fed funds of 3.88%, and plays.csv shows an upward-sloping bill curve (1M 4.05%, 3M 4.21%, 1Y 4.38%). That curve signals tightening. A tightening cycle cuts the other way on most plays: (a) a near-term tailwind for issuer float (CRCL, Tether); (b) a higher opportunity cost of holding non-yielding stablecoins, which in 2022 went with a supply contraction and a crypto bear market; (c) multiple compression for 35x P/E names (V, MA) and for long-duration crypto equities; (d) a real T-bill yield of only about 0.5% with CPI near 3.7%, so the "beat T-bills" benchmark is a nominal hurdle that hides real losses.
- Evidence: FRED DGS3MO, last value 4.21 on 2026-11-02, about 4.16 to 4.28 since late September (https://fred.stlouisfed.org/data/DGS3MO.txt, fetched 2026-11-04). Fed held at 3.75% to 4.00% on 2026-10-28 on a 10 to 2 vote, with both dissents for a hike and a December hike priced (secondary: https://admiralmarkets.com/analytics/traders-blog/fomc-october-2026-fed-holds-rates; https://investinglive.com/central-banks/fomc-decision-oct-28/, searched 2026-11-04). September CPI reported at 3.7% on Iran-war energy costs (secondary aggregator, verify against BLS: https://www.itiger.com/hans/news/1155128098; https://www.cbsnews.com/news/iran-war-economic-impact-gas-prices-inflation-2026/). Post-election coverage attributes Democratic gains partly to the Iran war and gas prices (https://www.cbsnews.com/live-updates/senate-election-results-2026/).
- Change: Add a macro-regime section covering inflation, the policy path, term premium and the real hurdle. Rerun R-36 and the CRCL bands for +100bp as well as -100bp. Add a supply-response term to the float arithmetic, because supply tends to fall when the opportunity cost rises. Show real returns next to nominal ones.

### 2. Scenario weighting applies an adoption state to plays whose returns do not depend on adoption
- Severity: Critical
- Target: Section 6 ranking method; every row with a numeric band. The clearest cases are R-27, R-26, R-09 to R-19, A-01, A-02, R-20 to R-24, R-28 to R-30 and G-01 to G-07.
- Objection: The method gives each row P(Bear) x band low + P(Base) x midpoint + P(Bull) x band high. That assumes adoption Bear maps to each play's worst outcome. For incumbents the mapping runs backwards: if stablecoins stay crypto plumbing, Visa, Mastercard and BNY keep their franchises, and that is their good state. For T-bills the band reflects rates, not adoption. For BTC the report itself says the row is "not a ledger-infrastructure bet." The result is absurd: the benchmark (R-27) scores 4.10%, below its own 4.21% hurdle. Weights also change silently with horizon (Long rows use 2035 weights).
- Evidence: My recomputation from plays.csv. For R-27: 0.57 x 4.0 + 0.36 x 4.2 + 0.07 x 4.4 = 4.10. R-09 (Long) reproduces only with 53/38/9. R-01 (Medium) reproduces only with 57/36/7.
- Change: Give each play a return conditional on each scenario, rather than mapping low, mid and high to Bear, Base and Bull. Plays not driven by adoption should get a macro distribution. Document the horizon rule.

### 3. The risk-adjusted score is invalid, and the top-five table does not follow it
- Severity: Critical
- Target: Section 6 ranking; executive summary top-five table; ra_score column.
- Objection: (a) Dividing a negative excess return by drawdown rewards high drawdown. R-31 (no-yield USDC, 2% drawdown) scores -2.105, BENJI scores -0.27, and COIN scores -0.088, so COIN "beats" a cash-like fund. This is the known failure of Sharpe-type ratios with a negative numerator. (b) The numerator mixes one-year bands (R-20 says "wider for 1y") with 10-year annualized bands (R-09), and the denominator is a peak-to-trough figure with no horizon. (c) The ranking departs from the score without saying so. L-03 is Large #1 at -0.27 while L-02 scores +0.024. L-05 and L-06 are ranked although they have no computed return. Mid #3 to #5 (M-02 -0.096, M-01 -0.142, M-04 -0.132) rank above M-07 (-0.063) and M-03 (-0.110). Retail #5 CRCL (-0.033) has an expected return below T-bills.
- Evidence: plays.csv ra_score, scenario_expected_pct and return_mid_pct columns.
- Change: Restate every band as an annualized expected excess return over one common horizon, paired with a drawdown over that same horizon. Rank on expected excess return with a drawdown cap, not on the ratio. Label the top-five table as judgment where it overrides the score.

### 4. Incumbent stress drawdowns are too small, and the sizing warning assumes the rest of the sleeve is cash
- Severity: Critical
- Target: R-09, R-10, A-01, A-02 (30%); R-11 to R-19 (40%); the Section 7 sizing warning.
- Objection: In 2008 to 2009 the custody and bank names in this list fell far more than 40%: State Street about -80%, BNY about -65% to -70%, JPMorgan about -70%, BlackRock about -60%. The card networks fell more than 30%: Mastercard about -60%, Visa about -50% from its 2008 high [From memory, verify against price history]. The Section 7 rule (0.45 x 90% = 40.5%) assumes the other 55% of the sleeve has zero drawdown. If that 55% is the recommended incumbents at their own 40% stress, the sleeve is at 40% before any crypto is added. In a correlated stress year, any crypto allocation breaches the limit.
- Change: Set incumbent stress from 2008 to 2009 and 2022 history (50% to 80%). Restate the sizing rule as a portfolio sum, with correlations near 1 in stress.

### 5. The scenario probabilities show more precision than the method supports, and the scenario definitions are incomplete
- Severity: High
- Target: Executive summary table; Section 4.
- Objection: (a) The headline 57/36/7 carries no confidence tag, although the variants run from 50% to 73% Bear. (b) The "lead estimate" averages a model with a midterm override and a WS3 judgment that disagree by 29 points on 2035 Bear (67 vs 38). An average of two estimates that far apart hides the disagreement. (c) The 2030 bands were recalibrated after the data were seen, which moves the goalposts. (d) The report never says how mixed outcomes are classified (for example S above $500B with T below $100B), so the three states may not be exhaustive. (e) The 2035 bands are "unchanged" but are not shown.
- Change: Show the bands in full with a rule for mixed states. Report ranges such as "Bear 50% to 70%" instead of point estimates. Show the model and the judgment separately.

### 6. The model is a crypto-cycle extrapolation presented as an adoption forecast
- Severity: High
- Target: Section 4 model; Bear leading indicators.
- Objection: The report says "measured momentum drives the result more than any single policy driver." Stablecoin supply is pro-cyclical with crypto prices and inversely related to rates. The 12-month window samples a BTC -20% year in a tightening cycle. The 36-month window starts from the post-FTX trough. Picking a window is picking a point in the cycle. No macro driver appears: no crypto market capitalization, no rate differential, no offshore dollar demand (EM FX stress, such as Brazil's 2026-10-26 move).
- Change: Model S on crypto market capitalization, the policy rate and an EM FX stress index, then report probabilities conditional on those paths. Drop raw momentum as the dominant term.

### 7. No disorderly scenario: run dynamics, lender of last resort and fire sales are missing
- Severity: High
- Target: Sections 4, 5 and 7; R-01, R-31, R-36, R-26, M-09, L-01 to L-03, L-09; the USDT risk row.
- Objection: The three scenarios are all orderly, and Bear lumps "flat" together with "collapse." Stablecoins are run-prone liabilities with no lender of last resort. The Fed's proposed payment account excludes discount window access, pays no interest and caps balances. The report cites BIS WP 1270 only for the inflow effect and tags it [High]. The paper also finds that outflows move yields two to three times as much as inflows, and that effects are much larger when bills are scarce. Precedents the report omits: USDC's depeg in March 2023 with $3.3B stuck at SVB; the wind-down of BUSD after the NYDFS order of February 2023; Terra in May 2022 [From memory, verify]. Each of them reshaped regulation and market share overnight.
- Evidence: BIS WP 1270 and the Banque de France copy of the February 2026 revision: 2.5bp to 3.5bp for a 2 standard deviation inflow (about $3.5B), outflows two to three times larger, 5bp to 8bp under bill scarcity (https://www.bis.org/publ/work1270.htm; https://www.banque-france.fr/system/files/2026-02/Stablecoins-and-safe-asset-prices.pdf, searched 2026-11-04). Payment account terms: CRS Insight IN12722, 2026-08-04 (https://www.everycrsreport.com/reports/IN12722.html).
- Change: Add a fourth "disorderly" state (my estimate is 10% to 15% over five years) with a mapping for each play. Correct the BIS magnitudes and add the asymmetry. Model reserve fire sales in a Treasury market that is already stressed, as in March 2020.

### 8. Fed account access is the most important structural lever, and the report omits it
- Severity: High
- Target: Sections 3 and 12; L-01, L-02, M-04, R-01, R-12, R-14.
- Objection: Whether issuers settle in central bank money, and on what terms, decides issuer economics, the narrow-bank question and how far bank deposits drain. The Fed proposed a limited "payment account" in 2026. It covers Fedwire, NSS and FedNow, with balance caps, no interest and no discount window, and the target date is Q4 2026. Kraken received a 12-month pilot limited master account in March 2026. None of this is in the regulatory table or the catalyst calendar.
- Evidence: https://www.everycrsreport.com/reports/IN12722.html (2026-08-04); https://www.americanbanker.com/payments/news/fed-skinny-accounts-take-early-heat-from-crypto-fintechs (searched 2026-11-04).
- Change: Add the payment account to Section 3 and to the calendar, and state its effect on the issuer breakeven and on bank plays.

### 9. Deposit franchise economics are not analyzed, so the bank and custody plays are mis-specified
- Severity: High
- Target: Sections 5 and 11; R-12, R-13, R-14, L-05.
- Objection: (a) The bank lobby's fight over yield comes from deposit economics. Converting a deposit into a stablecoin moves it, and the system-wide loss depends on where reserves sit: bank deposits, bills bought from banks, or bills bought from money funds holding Fed RRP. (b) Issuer cash held at banks is wholesale, non-operational deposits from financial entities. Under the LCR those carry very high run-off assumptions, so they add little to a bank's stable funding or net interest income. (c) Reserve custody fees are a few basis points on about $74B, which is immaterial to BNY's revenue. BNY at #3 retail is a value pick with a thin thematic link, not a toll collector. (d) The TBAC "$6.6T at risk" figure is the stock of transactional deposits, not a forecast, and bank lobbyists use it.
- Evidence: Secondary coverage of TBAC, 2025-04-30 (https://cryptoslate.com/?p=493876; https://finadium.com/?p=150357, searched 2026-11-04). LCR outflow treatment [From memory, verify in 12 CFR 249].
- Change: Add a short section on deposit flows and bank funding. Restate the BNY, STT and JPM theses as value positions with a stated thematic share of revenue.

### 10. Capital rules are misstated, and the custody enabler is missing
- Severity: High
- Target: Section 3 (Basel row, tagged [High]); Section 4 Bull indicator; R-12, R-13, M-04, L-06.
- Objection: Calling the Basel crypto standard "in force 2026-01-01" holds only in some jurisdictions. Reports from November 2025 said the US Fed and the Bank of England would not apply it as written, and the EU left out the permissionless-chain provisions. What matters for US bank custody was SEC SAB 121 and its rescission by SAB 122 in January 2025 [From memory, verify], which the report omits.
- Evidence: https://coincentral.com/basel-committee-reconsiders-crypto-capital-rules-after-us-uk-pushback/ ; https://www.ledgerinsights.com/basel-committee-considering-revisiting-bank-crypto-rules-re-stablecoins-report/ (searched 2026-11-04).
- Change: Lower the confidence on the Basel row to [Moderate] and give status by jurisdiction. Add SAB 122 and the US agencies' crypto statements.

### 11. The Treasury clearing mandate is missing, and the infrastructure analogs suffer from survivorship bias
- Severity: High
- Target: Section 4 analogs; Sections 1 and 2 (Broadridge DLR, wholesale DLT); R-16, R-17, M-09, L-03, L-04.
- Objection: The biggest mandated change in the dollar funding market is under way: central clearing of cash Treasuries by 2026-12-31 and of repo by 2027-06-30. It will absorb dealers' operational budgets in 2026 and 2027, which may crowd out DLT projects. It will also raise demand for mobile collateral, which is where tokenized MMF shares could fit. The analog section counts only failed voluntary consortia (we.trade, TradeLens, CHESS). The better base rate is that infrastructure moves when supervisors force a reduction in risk: CLS after Herstatt-type risk, central clearing of OTC derivatives after 2009, and US T+1 in 2024. That makes the regulatory agenda, not voluntary adoption, the main driver.
- Evidence: https://www.sifma.org/explore-issues/treasury-clearing ; https://www.thetradenews.com/sec-extends-us-treasury-clearing-compliance-deadline-in-bid-to-help-firms-implement-necessary-risk-management-changes/ (searched 2026-11-04).
- Change: Add both dates to the calendar. Rebuild the analog set to include mandated successes, and state which mandates could plausibly arrive for ledgers.

### 12. Interchange legislation, a real risk to the #2 retail pick, is missing
- Severity: High
- Target: R-09, R-10, A-01, A-02; Section 5 fee pools; Section 11.
- Objection: The thesis treats V and MA as safe incumbents and lists only stablecoin substitution as the key risk. The President endorsed the Credit Card Competition Act on 2026-01-13. Visa fell 4.5% and Mastercard 3.8% that day. A Democratic Congress makes a populist, bipartisan swipe-fee bill more likely, not less. The DOJ debit monopolization suit against Visa (filed September 2024) is also omitted [From memory, verify status]. All four kill criteria are revenue-based and would trigger only after the damage.
- Evidence: https://www.bloomberg.com/news/articles/2026-01-13/trump-targets-card-swipe-fees-after-lambasting-interest-rates ; https://www.durbin.senate.gov/newsroom/press-releases/durbin-marshall-reintroduce-the-credit-card-competition-act ; https://www.pymnts.com/credit-cards/2026/president-donald-trump-endorses-legislation-lower-credit-card-swipe-fees/ (searched 2026-11-04).
- Change: Add a legislative kill criterion (for example, CCCA passing either chamber) and a low band that includes interchange compression. Reconsider V and MA at #2.

### 13. The midterm override puts too much weight on politics, and the politics may still change
- Severity: High
- Target: Executive summary "Why Bear leads"; the model's midterm override; R-35.
- Objection: GENIUS is law. A Democratic Congress cannot repeal it over a veto, and many Senate Democrats voted for it (it passed the Senate 68 to 30 in June 2025) [From memory, verify]. The election mostly affects CLARITY, which drives token and exchange plays. It has much less effect on regulated stablecoin payments and tokenized cash, yet the Bear state is defined on S and T. Building the override into the model and then averaging with a judgment that also reflects the election probably double-counts it. The results are also still moving: coverage on 2026-11-04 shows uncalled races and conflicting seat counts.
- Evidence: CBS live results, "Democrats win control" (https://www.cbsnews.com/live-updates/senate-election-results-2026/). Time's live page reports 54 seats, which conflicts with other outlets (https://time.com/article/2026/11/03/midterm-elections-2026-key-races-live-results-polls-latest-news-updates/). Kalshi priced Democratic Senate control at 62% on 2026-10-15 (https://news.kalshi.com/p/who-will-control-the-senate-2026). All searched 2026-11-04.
- Change: Apply the political override to CLARITY-dependent plays (COIN, HOOD, tokens, R-35), not to the stablecoin supply (S) and tokenized assets (T) scenario probabilities. Re-run once the seat counts are final. My view is that this makes the report too bearish on adoption by about 5 to 10 points of Bear.

### 14. "The thesis is not priced in" contradicts the report's own valuation numbers
- Severity: High
- Target: Section 6 valuation inference; R-01 to R-03, R-34 to R-36, L-09, A-04.
- Objection: A 68% to 83% drawdown from a peak measures sentiment, not value. Anchoring on the peak is a bias. The report's own reverse DCFs need 16.1% (CRCL), 17.0% (COIN) and 18.3% to 21.0% (HOOD) revenue CAGR for ten years just to earn 10%. With forward P/Es of 60.8 and 104.5, and HOOD at 15.1x EV/S, the market is pricing a recovery.
- Change: Rewrite the inference to say the names are priced for recovery, and keep each as an option only if it is sized for an 80% to 90% loss.

### 15. M-08 tokenized private credit: the #1 Mid pick uses yield as its return during a gating wave
- Severity: High
- Target: M-08 (and the Mid #1 slot).
- Objection: The return is the T-bill plus a 2.5 to 4.0 point credit spread less fees. That is yield, not expected return, because it ignores defaults and loss given default. The 15% stress drawdown reflects smoothed NAV marks, and that smoothing is why M-08 has the best ra_score in the tier. "Quarterly" liquidity overstates reality: in 2026 the large private credit sponsors capped withdrawals at about 5% a quarter while requests ran at 10% to 16% or more. Apollo, the sponsor named in this row, is among them. The token wrapper adds nothing to the economics.
- Evidence: CRS Insight IN12674, 2026-04-02 (https://www.everycrsreport.com/reports/IN12674.html); Apollo capped withdrawals at 5% against 11% of requests (https://investinglive.com/stock-market-update/private-credit-stress-apollo-cap-fund-withdrawals-at-5-redemption-requests-surge-to-11-20260323/amp); Carlyle at 15.7% of requests (https://rallies.ai/news/carlyle-private-credit-fund-sees-157-redemptions-caps-redemptions-at-5). All searched 2026-11-04.
- Change: Subtract expected loss (1% to 3% a year in a downturn), set stress at 25% to 35% with a gating haircut, set liquidity to "gated," and take it out of #1.

### 16. Issuer build and buy economics (L-01, L-02) assume incumbent distribution terms and sticky float
- Severity: High
- Target: L-01, L-02, L-08; the $2.65B breakeven in Section 11.
- Objection: The breakeven uses Circle's 42.7% RLDC margin. A new entrant has to buy distribution at a much higher pass-through. In the Hyperliquid USDH contest, Paxos, Ethena and Frax bid 95% to 100% of reserve yield. At 90% pass-through the breakeven becomes $40M / (3.54% x 10%), about $11.3B, more than four times the report's figure. Float is not sticky: BUSD shrank to almost nothing within months of its regulatory order. L-02 earns 4.2% before growth, below the 4.21% hurdle, yet ranks #2. A change of control needs regulatory approval, and the $40M opex figure is unsourced.
- Evidence: https://www.theblock.co/post/370570/native-markets-team-wins-hyperliquid-usdh-stablecoin-bid-eyes-test-phase-within-days ; https://hashtalks.substack.com/p/the-usdh-bidding-war-how-hyperliquid (searched 2026-11-04).
- Change: Show breakeven at 40%, 70% and 90% pass-through and at policy rates of 2.5%, 3.5% and 4.5%. Add supply attrition after acquisition. Drop L-02 from the top five.

### 17. "Only federally chartered crypto bank" is out of date, and the licence moat is commoditizing
- Severity: Medium
- Target: M-04, L-06, Section 5 custody row, Section 11.
- Objection: On 2025-12-12 the OCC conditionally approved national trust charters for Circle, Ripple, BitGo, Fidelity Digital Assets and Paxos. BitGo met its conditions the same day. Coinbase, Bridge and Crypto.com have applied. The scarcity premium in M-04's $4.2B mark, and the report's "licences are the moat," are both shrinking.
- Evidence: https://www.axios.com/2025/12/12/banks-crypto-occ-charters ; https://www.steptoe.com/en/news-publications/occ-conditionally-approves-five-national-trust-bank-charter-applications.html (searched 2026-11-04).
- Change: Correct M-04. Count charter holders and applicants. Treat licences as table stakes rather than a moat.

### 18. The same security appears in several rows with different bands, and some data conflict
- Severity: Medium
- Target: R-09/A-01 (V), R-10/A-02 (MA), R-02/A-04/L-09/R-35 (COIN), R-01/R-34/R-36 (CRCL), R-11/A-05 (PYPL), M-03/A-06 (Stripe).
- Objection: V is 7 to 10 in one row and 6 to 12 in another. COIN has three bands (-9 to 12, -40 to 35, -10 to 15). A-06 says Stripe's valuation was "not retrieved," while M-03 uses a $159B tender. A-01 puts V at about $396 after hours on 2026-10-27, while Section 6 shows $433.90 on 2026-11-04, a 9.6% move in a week that the report does not explain. Counting 75 "plays" inflates breadth.
- Change: Keep one row per security, with sub-theses recorded as notes, and reconcile the prices.

### 19. Internal number conflicts between REPORT.md and plays.csv
- Severity: Medium
- Target: Sections 1, 2, 5, 7 and 12; R-01, R-18, R-26, R-36.
- Objection: (a) A 100bp cut after distribution: the report says $276M and R-36 says $316M. (b) Distribution costs are "62% of reserve income" in the report and "about 57% of revenue" in R-01. (c) The risk trigger "distribution costs above 62%" is already at the current level, while the dashboard uses 65%. (d) BENJI AUM: $2.7B in the report versus "700 to 760M" in R-26. (e) BUIDL: $1.97B versus "over 2.87B" in R-18. (f) The dashboard's Bull trigger ($400B) sits inside the 2030 Bear band (below $500B), and the Bear indicator ($350B) differs from the dashboard's Bear trigger ($280B). (g) R-35's detail computes +0.6% expected, but its scenario column shows -11.25%.
- Change: Pick one figure for each item, explain differences in definition, and align the thresholds with the scenario bands.

### 20. Tokenized MMF rows (R-26, M-09, L-03) are dominated by T-bills but ranked first
- Severity: Medium
- Target: R-26, M-09, L-03; Retail #1 and Large #1.
- Objection: These rows yield 3.5% to 4.1% against 4.21% for bills, with fees, onboarding and chain operational risk on top. A 24/7 token redeemable against T+0 or T+1 underlying assets creates a liquidity mismatch once the shares are reused as collateral. The 2% stress figure ignores operational failure. California treats MMF dividends as exempt only if at least 50% of the fund's assets are US obligations at each quarter end, and repo usually does not count. So "CA exempt share for US-obligation portion" may be wrong for FOBXX [From memory, Verify with CPA]. An anchor of $50M to $100M in a new fund (L-03) concentrates the fund's redemption risk on the anchor.
- Change: Present these as learning or operational positions, not return plays. Rank T-bills alone at Retail #1. Verify the California 50% test.

### 21. Sanctions are an underweighted channel
- Severity: Medium
- Target: Sections 2, 7 and 10; G-03, the USDT risk row, R-20 to R-24, R-28 to R-30.
- Objection: In wartime, sanctions enforcement on offshore dollar rails (USDT on Tron, OTC desks, Section 311 actions) becomes more likely, and that cuts both ways for the offshore dollar thesis. For KSPI, the secondary-sanctions risk was a specific, documented short-seller allegation that moved the stock about 20% in one day and led to law-firm investigations, not a matter of "perception." The report does not mention US secondary-sanctions authority over foreign financial institutions (EO 14114) [From memory, verify].
- Evidence: https://www.rferl.org/a/kaspi-bank-kazakhstan-toqaev-lomtadze-kim-nasdaq-culper/33131206.html ; https://www.intellinews.com/short-seller-argues-nasdaq-listed-kazakh-fintech-heavyweight-kaspi-misled-market-over-russia-links-344492 (searched 2026-11-04).
- Change: Add a sanctions risk row with its trigger and the plays it affects. Raise G-03's stress drawdown.

### 22. Geography plays are weakly linked to the theme, misclassified and selectively chosen
- Severity: Medium
- Target: G-01 to G-07; Section 10.
- Objection: EWY, EWZ, ARGT and INDA are tagged with vehicle_class "blockchain_equity_etf_1940" and layers such as "exchanges_ats" and "banking." Those labels are wrong. Section 10 lists Argentina among likely losses, yet G-06 gives ARGT a +2% midpoint. The Brazil claim ("real fell about 12%") reads as an intraday figure. Trading Economics shows a move from about 5.045 to a 5.60 intraday low, then a recovery to about 5.40, roughly 7% on the day. Kazakhstan is included while HK, Singapore, the UK, Japan and the EU are unverified, which is selection bias toward easy-to-find tickers.
- Evidence: https://tradingeconomics.com/brazil/currency/news/595076 (searched 2026-11-04).
- Change: Fix the classifications, state Brazil's move both intraday and at the close, and label the G rows as macro trades outside the theme.

### 23. Theft and hack probabilities are too low given the report's own data
- Severity: Medium
- Target: Section 7 risk row (80%); R-02, R-03, R-32, R-33, R-28 to R-30.
- Objection: The report records about $8.6B of hacks in 2026, including a $6.3B incident on 2026-10-29. Incidents above $500M occurred in at least three of the last five years. A Poisson rate of about 0.6 a year gives roughly a 95% chance of at least one in five years, not 80%.
- Change: Raise it to 90% to 95% and model severity rather than occurrence.

### 24. Private-market marks are anchored on the most favorable price
- Severity: Medium
- Target: M-01, M-02, M-03, M-04, M-05, L-06, A-06.
- Objection: M-02 assumes Ripple "reverts" to a $50B tender. A tender is a price the company sets, so it is not a market anchor, and Ripple's equity largely tracks its XRP holdings (XRP is down 40% over a year). M-01 compares a Forge price for common shares with a Series E preferred mark that sits above it in the liquidation stack. M-05 uses a bid that was reportedly denied. Treating the gap to the highest mark as upside builds survivorship into the numbers.
- Change: Treat the secondary price as fair value, value the preference stack, and treat Ripple as XRP beta.

### 25. Adoption denominators are inconsistent, and source capture is understated
- Severity: Low
- Target: Section 1; executive summary.
- Objection: Measuring stablecoins against MMF assets assumes they are savings. For payments, the relevant base is M1 or transactional deposits, where stablecoins are about 1.6% of deposits. "Tokenized Treasuries" includes offshore products that are not MMFs. Broadridge's $359B a day counts intraday repo legs and should be compared with SOFR volumes, not left standing alone. Kinexys should be compared with JPMorgan's total daily payment flows, roughly $10T, rather than with RTP [From memory, verify]. Several rows cite bare domains (https://www.benzinga.com/ in M-06, M-07, L-04, L-05, L-07, L-08) or SEO and single-blog pages (eco.com, cryptoetf.today, defirate, nadcab, biggo, ambcrypto, stellagent).
- Change: Use comparators that match each use. Replace placeholder citations or mark those rows Unverified.

### 26. Forecasts are labeled as facts, and one cited magnitude is off
- Severity: Low
- Target: Section 5.
- Objection: "Fact: Fee pools at risk... 1% to 4% at risk" is a forecast. "Fact: A 100bp cut removes $739M" is a static calculation with no supply response. The BIS figures (0.7bp on impact, 4bp at 10 days) do not match either version of WP 1270 (2bp to 2.5bp in May 2025, 2.5bp to 3.5bp in February 2026, state-dependent), yet they carry a [High] tag.
- Change: Relabel these as Inference and cite the February 2026 revision.

### 27. Remaining rows: event trades, unpriced rows and avoid rows
- Severity: Low
- Target: R-04 to R-08, R-25, R-32 to R-38, M-06, M-07, M-10 to M-12, L-04, L-05, L-07, L-08, L-10, A-03, A-05, A-07, A-08, R-20 to R-24, R-28 to R-30.
- Objection: (a) Event rows (R-34 to R-38) are one- to eight-week trades sized on implied volatility. They have no stated edge and do not belong in a structural investment map. (b) About 13 rows have no computed return (R-32, R-33, M-06, M-12, L-05 to L-08, L-10, A-05 to A-07, plus the partial A-03). They should be listed as watchlist items, not counted as plays. (c) A-03's band is just the 52-week range, which is not a return method. (d) The token and ETP rows are weighted by adoption state although the report says they are not adoption bets (see item 2). The grantor-trust look-through on spot ETPs may cut against "wash sale likely applies" [Verify with CPA]. (e) M-11 structured notes and M-10 validators carry issuer-credit and slashing risk that the bands ignore. The avoid calls (A-08, L-04, R-04 to R-08 by implication) look right.
- Change: Split the matrix into Investable, Watchlist and Avoid. Give the remaining rows proper methods.

---

## Coverage map (play_id to dissent items)

| play_ids | Items |
|---|---|
| R-01, R-34, R-36 | 1, 2, 3, 7, 14, 18, 19 |
| R-02, R-03, R-35, L-09, A-04 | 2, 3, 6, 13, 14, 18, 19, 23 |
| R-04 to R-08, R-25 | 2, 3, 14, 27 |
| R-09, R-10, A-01, A-02 | 1, 2, 4, 12, 18 |
| R-11, A-05 | 2, 4, 18, 27 |
| R-12, R-13, R-14 | 2, 4, 9, 10 |
| R-15 to R-19 | 2, 4, 11, 19 |
| R-20 to R-24, R-28 to R-30 | 2, 6, 21, 23, 27 |
| R-26, R-27, M-09, L-03 | 1, 2, 3, 7, 11, 19, 20 |
| R-31 to R-33 | 1, 3, 23, 27 |
| R-37, R-38 | 27 |
| M-01 to M-05, L-06, A-06 | 17, 18, 24 |
| M-06, M-07, M-10 to M-12 | 25, 27 |
| M-08 | 15 |
| L-01, L-02, L-08 | 8, 16 |
| L-04, L-05, L-07, L-10 | 11, 25, 27 |
| A-03, A-07, A-08 | 27 |
| G-01 to G-07 | 2, 21, 22 |

---

## Closing: my probability estimates

I put 2030 at Bear 48% / Base 47% / Bull 5%, and 2035 at Bear 40% / Base 50% / Bull 10%. These use the report's 2030 bands, with the reading that Bear means both S and T are below the floors. The report's Bear weight is too high for two reasons. Its momentum term samples a crypto drawdown during a tightening cycle. Its midterm override hits stablecoins and tokenized cash, which mostly depend on a statute already in force (GENIUS) and on supervisory plumbing still being built (Fed payment accounts, OCC charters, Treasury clearing, which creates collateral demand), not on CLARITY. From $295B, reaching $500B of stablecoins by 2030 needs about 14% a year. That is achievable without a crypto boom if regulated distribution grows, so I give S about a 45% chance of reaching the Base floor. T needs about 63% a year to reach $100B, so I give it about 25%. Those two are correlated. I cut Bull below the report's 7% because $1.5T by 2030 needs about 50% annual growth during a hawkish, high-oil regime that has historically been hostile to crypto liquidity. Inside my Bear weight I hold 10% to 15% for a disorderly path (a run, a large theft or a sanctions shock followed by a regulatory clampdown). The report does not model that state, and it matters more for play selection than the gap between Bear and Base. On value capture I am more bearish than the report: distribution pass-through and charter commoditization will keep issuer and custodian take rates falling. On incumbents I am more cautious than the report: interchange legislation and realistic stress drawdowns make V, MA, BK and STT ordinary equity risk, not safe proxies for the theme.
