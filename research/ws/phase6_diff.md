# Phase 6 diff for second red-team pass

Unified diff of REPORT.md v1 (after Phase 4 fixes) against v2, main body only. The appendices are the verbatim red-team dissents and are excluded.

```diff
--- data/REPORT_v1.md	2026-11-04 20:29:21.238636791 +0000
+++ /tmp/claude-0/-home-user-Grotesque-Sublime/4b43f784-03b2-5e55-909a-96a2e34ca95f/scratchpad/report_v2_body.md	2026-11-04 20:34:30.730714570 +0000
@@ -1,238 +1,275 @@
 # Programmable Ledgers, Digital Money, and the Investment Map
 
-Research date: 2026-11-04. Status: v1 (Phase 3 synthesis). Revisions after verification and red team are logged in `changelog.md`.
+Research date: 2026-11-04. Status: v2, revised after Phase 4 verification and the Phase 5 red teams. Every change is logged in `changelog.md`; v1 is preserved at `data/REPORT_v1.md`.
 
 ## Executive summary
 
-**Is it happening?** Partly, and more slowly than the forecasts it is sold with.
+**Is it happening?** Yes, on regulated and permissioned rails. Barely, on public-chain tokenization. Not yet in payments or retail CBDCs.
 
-- Fact: USD stablecoin supply is $295.1B (DefiLlama API, 2026-11-04). It is 3.0% lower than 12 months ago and 6.5% below its 2026-05-17 peak of $315.5B.
-- Fact: Tokenized Treasuries and money funds are $14.25B (RWA.xyz, 2026-11-04) [Interested source]. That is 0.18% of US money fund assets of $7.90T (ICI, 2026-10-28).
-- Inference: No market segment passes the rejection test in `null_hypothesis.md`. Four segments are contested: stablecoin payments, the offshore dollar, tokenized cash and wholesale repo on ledgers. Retail CBDCs and tokenized securities outside cash remain mostly narrative. [Moderate]
+- Fact: USD stablecoin supply is $295.1B (DefiLlama API, 2026-11-04). It is 3.0% lower than 12 months ago, at a joint low in the crypto price and interest-rate cycle (Section 4A).
+- Fact: Tokenized Treasuries and money funds on public chains are $14.25B (RWA.xyz, 2026-11-04) [Interested source]. That is 0.18% of US money fund assets ($7.90T, ICI, 2026-10-28).
+- Fact: Assets recorded on permissioned ledgers are much larger. RWA.xyz counts $396B of represented value, mostly on Canton. Broadridge's DLR platform runs about $359B of repo a day (2026-09) [Interested source].
+- Inference: No market segment passes the rejection test in `null_hypothesis.md`. Wholesale repo on ledgers is the segment closest to passing, if self-reported operator volumes are accepted. [Moderate]
 
-**How likely?** Lead estimate, the average of the model and WS3's judgment:
+**How likely?** The lead estimate is a five-estimator panel: the model base run, the model's drivers-only run, WS3 judgment, Red Team A and Red Team B.
 
-| Scenario | 2030 | 2035 | What it means |
-|---|---|---|---|
-| Bear | 57% | 53% | Stablecoins stay crypto plumbing and an offshore dollar. Tokenization stays a niche. |
-| Base | 36% | 38% | Regulated stablecoins go mainstream. Tokenized Treasuries become standard collateral. Ledgers carry a minority of wholesale flows. |
-| Bull | 7% | 9% | Ledgers become a primary settlement layer. |
+| Scenario | 2030 | Panel range | 2035 | Panel range |
+|---|---|---|---|---|
+| Bear: public-chain tokenization and stablecoins stay niche | 51% | 38% to 64% | 46% | 30% to 67% |
+| Base | 42% | 28% to 54% | 43% | 26% to 55% |
+| Bull | 7% | 5% to 11% | 11% | 7% to 15% |
 
-- The model's variants put 2030 Bear between 50% and 73%. [Low]
-- Why Bear leads: the law is in place, but demand is flat. US market structure legislation failed cloture 49 to 50 (2026-09-15). Democrats won both chambers on 2026-11-03 (AP calls via CBS News, 2026-11-04), so that bill restarts in a new Congress. [Moderate]
+- Confidence: [Low]. Inside Bear sits a disorderly sub-path of about 10% over five years: a run, a large theft or a sanctions shock followed by a clampdown (Section 4B).
+- Fact: The binding constraints are demand and macro, not law. GENIUS is law (effective 2027-01-18). Market structure legislation failed cloture 49 to 50 (2026-09-15). Democrats won both chambers on 2026-11-03 (AP calls via CBS News, 2026-11-04).
+- Fact: The Fed raised its target range to 3.75% to 4.00% on 2026-09-16 and held on 2026-10-28. September CPI was 3.7% (secondary reports of BLS data, 2026-10-14). [Moderate]
 
-**Who wins?** Owners of three things: distribution, licences and balance sheets.
+**Who wins?** Owners of distribution, licences and balance sheets.
 
-- Fact: Circle's Q3 2026 distribution and transaction costs were $409.2M, 62% of its $657.6M reserve income (Circle Q3 2026 results, 2026-11-04). Most of this is paid to distribution partners such as Coinbase.
-- Fact: Public-chain fees are small. Ethereum gross revenue was $127M in H1 2026, down 69% year on year (WS4).
-- Inference: Institutional flow accrues to intermediary equity (issuers, distributors, card networks, custodians, asset managers) more than to network tokens. [Moderate]
+- Fact: Circle's distribution and transaction costs were 62% of its Q3 2026 reserve income ($409.2M of $657.6M, Circle Q3 2026). Ethereum gross fee revenue was $127M in H1 2026.
+- Inference: Tokens capture value only where a chain owns order flow or a dominant stablecoin corridor (Tron, Hyperliquid). That capture is fragile because governance can switch it off. [Moderate]
 
-**Top five plays per tier.** The benchmark is the 3-month T-bill at 4.21% constant-maturity yield (4.03% discount basis; Federal Reserve H.15, 2026-11-02).
+**Top five plays per tier.** Ranking is by central excess return over T-bills (4.21%, 3-month constant maturity, H.15, 2026-11-02), shown with stress drawdown. Rows marked (J) are judgment overrides of the score.
 
 | Rank | Retail | Mid (accredited) | Large ($5M and up) |
 |---|---|---|---|
-| 1 | T-bills, plus Franklin BENJI as a small tokenized-cash position (R-27, R-26) [Moderate] | Tokenized private credit funds (M-08) [Low] | Anchor position in a tokenized MMF launch (L-03) [Low] |
-| 2 | Visa and Mastercard (R-09, R-10, A-01, A-02) [Moderate] | Tokenized Treasuries and MMFs for qualified investors as collateral cash (M-09) [Low] | Buy a licensed stablecoin issuer rather than build one (L-02) [Low] |
-| 3 | BNY (R-12) [Low] | Ripple secondary at a discount to its tender price (M-02) [Low] | Custody infrastructure, build or buy (L-06) [Low] |
-| 4 | BlackRock and ICE (R-18, R-16) [Low] | Kraken secondary, only if the Forge mark is confirmed (M-01) [Low] | Tokenized-deposit partnership with Kinexys or Citi Token Services (L-05) [Unverified] |
-| 5 | Circle, sized as an option on adoption and rates (R-01) [Low] | Anchorage private round (M-04) [Low] | Block positions in CRCL or COIN only on drawdowns (L-09) [Low] |
+| 1 | Visa, Mastercard (R-09, R-10, A-01, A-02): +4.3 to +4.8 pts; stress 50% to 60% [Moderate] | Tokenized private credit, held through the conventional fund where possible (M-08): +3.3 pts; stress 30%; quarterly gates (J) [Low] | Buy a licensed issuer with distribution (L-02): +4.7 pts; stress 80% [Low] |
+| 2 | BNY (R-12): +3.8 pts; stress 65% [Low] | Ripple secondary (M-02): +11.2 pts. It is an XRP proxy (J) [Low] | Anchor a tokenized MMF launch (L-03): cash yield plus strategic access; -0.4 pts (J) [Low] |
+| 3 | BlackRock (R-18): +3.3 pts; stress 60% [Low] | Kraken secondary (M-01): +6.7 pts; mark disputed, Forge $9.93B vs Series E $21B [Low] | Custody build or buy (L-06): unscored (J) [Unverified] |
+| 4 | Circle (R-01): +3.3 pts; stress 83%; sized as an option [Low] | Anchorage (M-04): +3.1 pts [Low] | Digital Asset (Canton) equity or partnership, repriced from the 2026 round (M-06, L-04 revised) (J) [Low] |
+| 5 | ICE, State Street, Franklin (R-16, R-13, R-19): +2.8 pts; stress 65% to 80% [Low] | Venture funds (M-07): +2.4 pts; 10-year lockup [Unverified] | Tokenized-deposit partnership (L-05): unscored (J) [Unverified] |
+
+- Inference: Every crypto-native public equity except Circle scores below T-bills on central estimates (COIN, HOOD, GLXY, BLSH, FIGR, GEMI). So do token ETPs except staked ETH. Their case rests on the Bull tail and on token-price cycles, not on the adoption evidence. [Moderate]
 
-**Recommendation.** For the theme, prefer incumbents that capture the flows without depending on it. Treat issuers and token exposure as small options. The Bull case is real enough to own a little of, and not likely enough to build a portfolio on. [Moderate]
+**Recommendation.** For the theme, own the incumbents that collect tolls on the regulated path. Keep issuer, distributor and token exposure as small, capped options. Hold the rest in T-bills, which pay a real yield of about 0.5% against 3.7% CPI. [Moderate]
 
 ---
 
 ## 1. Adoption: what the data show (WS0)
 
-| Measure | Value | Date | Legacy comparator | Penetration | Source | Confidence |
+| Measure | Value | Date | Comparator | Penetration | Source | Confidence |
 |---|---|---|---|---|---|---|
-| USD stablecoin supply | $295.1B | 2026-11-04 | US MMF assets $7.90T | 3.7% | DefiLlama API; ICI | [High] |
+| USD stablecoin supply | $295.1B (peak $315.5B on 2026-05-17; the all-stablecoin series peaked at $322.4B on 2026-05-26) | 2026-11-04 | US MMF assets $7.90T | 3.7% | DefiLlama API; ICI; Crypto Briefing | [High] |
 | Real stablecoin payments | $0.39T annualized | 2025-12 | ACH $93.0T (2025) | 0.4% | McKinsey/Artemis via secondary [Interested source]; Nacha | [Moderate] |
 | Visa-adjusted stablecoin volume | $12.0T (raw $63.0T) | 2026-01 to 08 | | | Visa/Allium via secondary [Interested source] | [Low] |
-| Tokenized Treasuries and MMFs | $14.25B | 2026-11-04 | US MMF assets $7.90T | 0.18% | RWA.xyz [Interested source]; ICI | [Moderate] |
-| Tokenized stocks | $3.89B distributed | 2026-11-04 | | | RWA.xyz | [Moderate] |
+| Tokenized Treasuries and MMFs (distributed) | $14.25B | 2026-11-04 | US MMF assets | 0.18% | RWA.xyz [Interested source]; ICI | [Moderate] |
+| All tokenized assets excluding stablecoins (distributed) | $39.4B | 2026-11-04 | | | RWA.xyz | [Moderate] |
+| Represented assets (permissioned ledgers, mainly Canton) | $396B | 2026-11-04 | | | RWA.xyz | [Moderate] |
 | Broadridge DLR repo | about $359B per day | 2026-09 | | | Broadridge, self-reported [Interested source] | [Low] |
 | Kinexys | over $7B per day | 2026-06 | RTP about the same daily value | | JPMorgan via CoinDesk [Interested source] | [Low] |
 | FedNow plus RTP | about $0.99T | Q3 2026 | | | Federal Reserve; The Clearing House | [Moderate] |
 
-- Inference: The two adjusted measures of stablecoin payments differ by about 46x. Adoption claims built on any single dashboard are therefore unreliable. [High]
-- Inference: The comparison that matters is not ledger against ledger. Ledgers compete with fast conventional rails: FedNow, RTP, Pix and UPI (25.47B transactions in 2026-10, NPCI via Inc42). These deliver speed and 24/7 operation without new ledgers (null hypothesis N5). [Moderate]
+- Inference: Two adjusted measures of stablecoin payments differ by about 46x. Adoption claims built on any single dashboard are unreliable. [High]
+- Inference: Supply is a stock, not a usage measure. Supply on Tron and Ethereum reflects where balances are parked, not where payments occur.
+- Inference: Represented assets are records on a ledger, not settlement in central bank money. DTC gives tokenized positions no collateral value in its own risk management (Red Team B). [Moderate]
+- Inference: Fast conventional rails (FedNow, RTP, Pix, UPI) deliver speed and 24/7 operation without new ledgers. That is the counterfactual every DLT claim must beat. [Moderate]
 
 ## 2. Landscape (WS1)
 
 | Category | Status | Example and latest metric | Binding constraint |
 |---|---|---|---|
-| Payment stablecoins | Live | USDC $73.9B (2026-09-30, Circle Q3) | Demand outside crypto trading |
-| Offshore stablecoins | Live | USDT $177.8B (2026-11-04, DefiLlama) | Reserve quality: the Fed's FEDS Note (2026-04-08) puts only about 0.74x of liabilities in high-quality assets |
+| Payment stablecoins | Live | USDC $73.9B (2026-09-30, Circle Q3) | Demand outside crypto trading; opportunity cost when rates rise |
+| Offshore stablecoins | Live | USDT $177.8B (2026-11-04) | Reserve quality: about 0.74x of liabilities in high-quality assets (FEDS Note, 2026-04-08) |
 | Tokenized MMFs | Live | BUIDL $1.97B; BENJI and iBENJI $2.7B (RWA.xyz, 2026-11-04) | Small yield edge over conventional money funds |
-| Tokenized equities | Live, small | $3.89B; SEC innovation exemption 2026-09-17 to 2031-09-17 | Settlement still runs T+1 through NSCC/DTC (Nasdaq rules approved 2026-03-18) |
-| Wholesale DLT | Pilot to live | Agora is a prototype (BIS, 2026-05-27). Swift's ledger settles finally through existing systems (2026-07-09). | Interoperability and settlement finality in central bank money |
-| Retail CBDC | 3 launched, 41 pilots | Atlantic Council tracker, 2026-05 | Political opposition (US anti-CBDC bill); weak usage |
-| Agentic payments | Live, early | x402: $42M settled cumulatively; October 2026 run rate about $274k per month | Consumer protection and liability rules (WS8) |
-
-- Inference: Programmability is mostly prototype in settlement. Live conditional settlement and delivery-versus-payment exist only inside single-operator systems (Kinexys, DLR) or in DeFi. [Moderate]
+| Tokenized equities | Live, small | $3.89B; SEC innovation exemption 2026-09-17 to 2031-09-17 | Nasdaq tokenized trades still settle T+1 through NSCC/DTC |
+| Wholesale DLT | Live inside single operators | DLR and Kinexys are live. DTCC ran live tokenized trades on Canton and Besu on 2026-07-15 (secondary, per Red Team B). Agora is a prototype (BIS, 2026-05-27). | Interoperability; final settlement in central bank money |
+| Retail CBDC | 3 launched, 41 pilots | Atlantic Council, 2026-05 | Political opposition; weak usage |
+| Agentic payments | Live, early | x402: $42M settled cumulatively; about $274k in October 2026 | Consumer protection and liability rules (WS8) |
 
 ## 3. Who sets the rules and builds the rails (WS2)
 
 | Item | Status (2026-11-04) | Source | Confidence |
 |---|---|---|---|
 | GENIUS Act | Public Law 119-27, signed 2025-07-18, effective 2027-01-18 | govinfo | [High] |
-| OCC GENIUS final rule | Issued 2026-10-21. Dropped the presumption that affiliate or white-label yield is prohibited, so the ban binds issuers only. | OCC Bulletin 2026-50 | [High] |
-| Fed GENIUS rules | Proposed 2026-09-24. Comments close 2026-11-30. The proposal keeps an affiliate-yield presumption. | Federal Register via Arnold & Porter | [Moderate] |
-| CLARITY Act | Passed the House 294 to 134; Senate Banking Committee 15 to 9; cloture failed 49 to 50 (2026-09-15) | Latham tracker; Orrick | [High] |
-| 2026 midterms | AP called both chambers for Democrats | CBS News, NBC, Forbes live coverage, 2026-11-04 | [Moderate] (seat counts provisional) |
+| OCC GENIUS final rule | Issued 2026-10-21. Dropped the presumption that affiliate or white-label yield is prohibited. | OCC Bulletin 2026-50 via law-firm summaries | [Moderate] |
+| Fed GENIUS rules | Proposed 2026-09-24; comments close 2026-11-30; the proposal keeps an affiliate-yield presumption | Federal Register via Arnold & Porter | [Moderate] |
+| Fed payment accounts | Proposed limited-purpose account: no discount window, no interest, capped balances | CRS Insight IN12722 (2026-08-04), per Red Team A | [Moderate] |
+| CLARITY Act | Passed the House 294 to 134; Senate Banking 15 to 9; cloture failed 49 to 50 (2026-09-15); must be reintroduced in the 120th Congress | Latham; Orrick | [High] |
+| 2026 midterms | AP called both chambers for Democrats | CBS News, NBC, Forbes, 2026-11-04 | [Moderate] (seat counts provisional) |
 | SEC tokenized-stock exemption | Release 34-106402, expires 2031-09-17 | SEC; Sidley | [Moderate] |
-| Basel crypto standard | In force 2026-01-01; under targeted review, with an update due by end 2026 | BIS, 2026-10-01 | [High] |
+| Basel crypto standard | In force 2026-01-01; targeted review, with an update due by end 2026 | BIS, 2026-10-01 | [High] |
 | Digital euro | Parliament voted 416 to 169 to open trilogue (2026-07-09); ECB target 2029 | Secondary | [Moderate] |
-| MiCA | Transition period for crypto service providers ended 2026-07-01 | Secondary | [Moderate] |
+
+- Inference: Access to Fed accounts is the structural lever for issuers. Without a discount window, a stablecoin issuer remains a run-prone, narrow-bank-like liability. [Moderate]
 
 ```mermaid
 flowchart TD
-  Congress[Congress: GENIUS Act law; CLARITY restarts in 120th Congress] --> Regs[OCC, FDIC, Fed, NCUA, Treasury]
+  Congress[Congress: GENIUS law; CLARITY restarts in 120th Congress] --> Regs[OCC, FDIC, Fed, NCUA, Treasury]
   Congress --> MktRegs[SEC and CFTC]
   Basel[Basel Committee] --> Regs
-  Regs --> Issuers[Issuers: Circle, Paxos, banks, Tether offshore]
+  Regs --> Issuers[Issuers: Circle, Paxos, banks; Tether offshore]
+  Regs --> FedAcct[Fed payment account access]
+  FedAcct --> Issuers
   MktRegs --> Venues[Venues: Nasdaq, Coinbase, Robinhood, Kraken]
   Issuers --> Reserves[Reserve custody: BNY, Treasuries, repo]
   Issuers --> Dist[Distribution: Coinbase, Stripe, Visa, Mastercard]
-  Rails[Rails: Fedwire, Kinexys, Canton, public chains] --> Issuers
+  Rails[Rails: Fedwire, Kinexys, Canton, DLR, public chains] --> Issuers
   Dist --> Users[End users]
   Venues --> Users
 ```
 
-- Gap: The UK, Hong Kong licensees, Singapore, Japan, the PBoC, the SNB and private-institution financials were not verified (search cap). `institutions.csv` rows tagged Unverified are placeholders.
+- Gap: The UK, Hong Kong licensees, Singapore, Japan, the PBoC and the SNB were not verified (search cap). `institutions.csv` rows tagged Unverified are placeholders.
+
+## 4. Scenarios, macro regime and model
+
+### 4A. Macro regime (added in v2)
+
+| Variable | Value | Date | Source | Effect on the theme |
+|---|---|---|---|---|
+| Fed target | 3.75% to 4.00%: hiked 2026-09-16, held 2026-10-28 with two dissents for a hike | 2026-10-28 | FOMC; secondary on the dissents | Raises issuer float income. It also raises the cost of holding non-yielding stablecoins, which shrank supply in 2022. |
+| 3-month T-bill | 4.21% (constant maturity), above effective fed funds of 3.88% | 2026-11-02 | H.15; FRED | Markets lean toward a hike |
+| CPI | 3.7% year on year | 2026-09 (released 2026-10-14) | Secondary reports of BLS | Real T-bill yield about 0.5% |
+| Geopolitics | Iran war energy shock; post-election coverage links it to gas prices | 2026-11-04 | CBS News | Risk-off pressure on crypto liquidity |
+
+- Inference: Rate sensitivity runs both ways. ±100 basis points moves Circle's gross reserve income by about ±$739M a year at $73.9B USDC (about ±$276M after distribution costs) before any supply response. Supply tends to fall when the opportunity cost rises, so a hike is less positive for issuers than this arithmetic shows. [Moderate]
+
+### 4B. Scenario definitions
 
-## 4. Timeline and scenarios (WS3, Phase 2 model)
+Measures: S = stablecoin supply; T = distributed tokenized assets excluding stablecoins; W = DLT share of wholesale flows. W is unmeasured, so classification uses S and T. A split outcome counts as Base.
 
-**Calibration.** WS3 recalibrated the 2030 bands: Bear S below $500B and T below $100B; Bull S above $1.5T and T above $500B. The schema's original Bull threshold needed T to grow 149% a year. 2035 bands are unchanged.
+| Scenario | 2030 band (WS3 recalibration) | 2035 band (schema) |
+|---|---|---|
+| Bear | S < $500B and T < $100B | S < $1T and T < $500B |
+| Base | Otherwise | Otherwise |
+| Bull | S > $1.5T and T > $500B | S > $4T and T > $5T |
 
-**Model results** (`scenario_model.py`, `scenario_results.csv`):
+- Inference: The 2030 bands were recalibrated after the current data were seen: the schema's Bull threshold needed 149% a year growth in T. That is a judgment call, flagged here.
+- Inference: Bear is defined on public-chain T, so it means "public-chain tokenization stays niche," not "ledgers stay niche." On represented assets, T is $435B and already in the 2030 Base band. [Moderate]
+- Disorderly sub-path: about 10% over five years (WS6 R22 7%; Red Team A 10% to 15%). It would shift market share and regulation abruptly. The plays hit hardest are CRCL, COIN, token ETPs and tokenized MMFs, through a temporary run.
 
-| Run | 2030 Bear / Base / Bull | 2035 Bear / Base / Bull |
+### 4C. Panel results
+
+| Estimator | 2030 Bear / Base / Bull | 2035 Bear / Base / Bull |
 |---|---|---|
 | Model base (blend growth, decay 0.8, midterm override) | 64 / 28 / 7 | 67 / 26 / 7 |
-| 36-month growth, decay 0.9 (most bullish variant) | 52 / 36 / 12 | 53 / 36 / 11 |
-| 12-month growth, decay 0.8 (most bearish variant) | 73 / 22 / 5 | 68 / 26 / 6 |
-| Drivers only, no momentum | 54 / 35 / 11 | 53 / 36 / 11 |
+| Model, drivers only (no momentum) | 54 / 35 / 11 | 53 / 36 / 11 |
 | WS3 judgment | 50 / 43 / 7 | 38 / 51 / 11 |
-| **Lead estimate** (model base and WS3 averaged) | **57 / 36 / 7** | **53 / 38 / 9** |
+| Red Team A | 48 / 47 / 5 | 40 / 50 / 10 |
+| Red Team B | 38 / 54 / 8 | 30 / 55 / 15 |
+| **Panel mean (lead)** | **51 / 42 / 7** | **46 / 43 / 11** |
+
+Model variants for 2030 Bear:
+
+| Variant | 2030 Bear |
+|---|---|
+| 12-month growth (measured at the trough) | 73% |
+| 36-month growth, decay 0.9 | 52% |
+| T including represented assets | 50% |
 
-- Inference: The two most influential drivers are regulatory clarity and end-user demand. Each moves 2030 Bear by about 3.6 points per notch on the scoring scale. Basel capital treatment and political durability come next. [Moderate]
-- Inference: Measured momentum drives the result more than any single policy driver. A return to the 36-month growth rate (33% a year for stablecoins) would move 2030 Bear down 9 to 12 points, depending on the decay assumption. [Moderate]
+- Inference: Momentum is pro-cyclical. The base model is most bearish at troughs, which is why it is one of five panel estimators and not the lead. [Moderate]
+- Inference: The most influential drivers are regulatory clarity and end-user demand, about 3.7 points of Bear each per notch. Bank capital treatment and political durability come next. [Moderate]
 
 **Leading indicators and falsifiers** (WS3):
 
 | Scenario | Indicator to watch | Falsifier |
 |---|---|---|
-| Bear | DefiLlama stablecoin supply below $350B on 2027-12-31 | Two measures above Base floors by 2028-12-31 |
+| Bear | DefiLlama stablecoin supply below $350B on 2027-12-31 | S above $500B or T above $100B by 2028-12-31 |
 | Base | RWA.xyz tokenized Treasuries above $30B on 2027-12-31; final FDIC and Fed GENIUS rules by 2027-07-18 | S below $400B and T below $60B on 2028-12-31 |
 | Bull | Stablecoins above $600B by 2028-06-30; Basel removes the penalty for permissionless chains | S below $600B on 2028-12-31 |
 
-**Forecast reconciliation.**
-- Fact: Sell-side marks include Standard Chartered at $2T of stablecoins by 2030 (moved from 2028), Citi at $5.5T tokenized by 2030 and BCG/Ripple at $18.9T by 2033. All come from parties with an interest in the thesis [Interested source].
-- Inference: These marks need 50% to 150% annual growth from today's levels. WS3's own range is about $450B to $1.1T of stablecoins and $100B to $300B of tokenized assets by 2030. [Low]
+**Forecasts.**
+- Fact: Sell-side marks include Standard Chartered at $2T of stablecoins by 2030 (moved from 2028), Citi at $5.5T tokenized by 2030 and BCG/Ripple at $18.9T by 2033. All come from interested parties [Interested source].
+- Inference: These marks need 50% to 150% a year. WS3's range is about $450B to $1.1T of stablecoins and $100B to $300B of distributed T by 2030. [Low]
 
 **Analogs.**
-- Inference: Pix and UPI reached mass adoption in three to four years because central banks mandated or subsidized them. Value went to distributors and users, not to the rail operators.
-- Inference: The 2016 to 2020 consortium wave (we.trade, TradeLens, ASX CHESS replacement) failed. The base rate for voluntary infrastructure migration without a mandate is poor. [Moderate]
+- Inference: Pix and UPI scaled in three to four years under central-bank mandate. Value went to distributors and users.
+- Inference: The 2016 to 2020 voluntary consortia (we.trade, TradeLens, ASX CHESS replacement) failed. The current wave differs in one way: live single-operator platforms (DLR, Kinexys, Canton) now exist. [Moderate]
 
-## 5. Where value accrues (WS4)
+## 5. Where value accrues (WS4, revised with red-team counterexamples)
 
 | Layer | Who wins | Pricing power 2030 | Confidence |
 |---|---|---|---|
-| Issuance and float | Tether (offshore), Circle (regulated); bank issuers entering | Medium. Float income falls with policy rates, and distribution partners take the majority. | [Moderate] |
+| Issuance and float | Tether (offshore), Circle; bank issuers and yield-sharing coalitions entering | Medium to low. Take rate is compressing (Open USD coalition, 2026-06-30). | [Moderate] |
 | Distribution and wallets | Coinbase, Stripe, card networks, Robinhood | High | [Moderate] |
-| Custody and reserves | BNY, State Street, Anchorage | Medium. Licences are the moat, but fees are compressing. | [Low] |
-| Settlement and clearing | DTCC, Broadridge, Canton, Kinexys | Medium | [Low] |
-| Public L1 and L2 chains | Ethereum (47% of stablecoins), Tron (32%), Base | Low for tokens. Base's sequencer margin accrues to Coinbase equity. | [Moderate] |
-| Tokenization platforms | Securitize, Ondo, Figure | Low to medium. The products commoditize; distribution decides the winners. | [Low] |
-
-- Fact: A 100 basis point cut removes about $739M of Circle's gross reserve income (about $276M after distribution costs) and $1.3B to $1.8B from Tether (WS4 arithmetic from Q3 2026 data).
-- Fact: The Fed target range is 3.75% to 4.00% (FOMC, 2026-10-28). [High]
-- Inference: Issuer equity is mainly a rate bet layered on an adoption bet. Its return should be judged on both. [Moderate]
-- Fact: Fee pools at risk by 2030 are modest. Cross-border revenue is $293B (McKinsey, 2024) [Interested source], with 1% to 4% at risk. US card swipe fees are $198B (2025, Nilson via the Merchants Payments Coalition) [Interested source], with 0.5% to 2% at risk.
-- Fact: Stablecoin inflows lower T-bill yields slightly: a $3.5B inflow lowers them about 0.7 basis points on impact and about 4 basis points at 10 days (BIS Working Paper 1270). [High]
-- Inference: The reserve demand matters for the front end of the Treasury curve at the margin, not for the system. [Moderate]
+| Custody and reserves | BNY, State Street, Anchorage | Medium. Licences are commoditizing as more charters are granted. | [Low] |
+| Settlement and clearing | DTCC, Broadridge, Digital Asset (Canton), Kinexys | Medium. Canton activity is concentrated in one application, DLR (Rosa and Roubini, 2026-05-21). | [Low] |
+| Public L1 and L2 tokens | Mixed: Ethereum fees low; Tron about $3.5B of revenue in 2025 (secondary); Hyperliquid routes most perp fees to buybacks | Low on average, high where the chain owns order flow. Fragile: Tron's validators cut base fees 60% on 2025-08-29. | [Moderate] |
+| Base (L2) | Coinbase equity today. A Base token, if launched, could move sequencer revenue to token holders. | Medium | [Low] |
+| Tokenization platforms | Securitize, Ondo, Figure | Low to medium; products commoditize | [Low] |
+
+- Fact: Stablecoin flows move T-bill yields. WS4 reads BIS Working Paper 1270 as about 0.7 basis points on impact for a $3.5B inflow. Red Team A cites the 2026-02 revision as 2.5 to 3.5 basis points for a two-standard-deviation inflow, with outflows two to three times larger and 5 to 8 basis points under bill scarcity. [Moderate, magnitudes contested]
+- Inference: The asymmetry matters in a run more than in growth.
+- Fact: Fee pools at risk by 2030 are modest. Cross-border revenue is $293B (McKinsey, 2024) [Interested source], with 1% to 4% at risk. US card swipe fees are $198B (2025) [Interested source], with 0.5% to 2% at risk. Interchange legislation is a larger risk to V and MA than stablecoins are (Red Team A item 12). [Moderate]
 
 ## 6. The plays (WS5, WS8, WS9; merged with WS7 tax)
 
-The matrix has 75 rows in `plays.csv` and `plays.xlsx`: Retail 51, Mid 13, Large 11. Every row has a return method, a kill criterion, a tax character and a stress drawdown.
+The matrix has 75 rows in `plays.csv` and `plays.xlsx`: Retail 51, Mid 13, Large 11. Each row has a band, a central estimate, a stress drawdown, a tier rank, a tax character and a kill criterion.
 
-**Ranking method** (assumptions P3-1 to P3-4).
-- Scenario-weighted return = P(Bear) x band low + P(Base) x band midpoint + P(Bull) x band high.
-- Risk-adjusted score = (scenario-weighted return minus 4.21%) / stress drawdown.
-- The band midpoint is shown as well. Wide bands score well on the midpoint and poorly on scenario weighting. That gap is itself the finding: those plays are bets on Bull or on token prices, not on the adoption evidence.
+**Method v2** (changelog C1, C2).
+- Central estimate: each workstream band is read as roughly the 10th to 90th percentile of annual returns. The central estimate is the midpoint minus σ²/2, where σ = (high - low) / 2.563. This is the compounding drag for volatile assets.
+- Ranking: plays are ranked within each tier by central excess return over 4.21%, with stress drawdown shown next to it. There is no ratio, because a ratio with a negative numerator ranks riskier assets higher.
+- Stress drawdowns are anchored on 2008 to 2009 for incumbents: V 50%, MA 60%, BK 65%, STT and ICE 80%, BLK 60% [Unverified history]. Crypto anchors are in `data/drawdowns.csv`.
+- Bands remain workstream judgment and mix one-year and multi-year framings. [Low]
 
-**Valuation check** (WS5, `data/valuations.csv`, stockanalysis.com, 2026-11-04):
+**Valuation check** (WS5, stockanalysis.com, 2026-11-04):
 
 | Ticker | Price | Market cap | Multiple | Note |
 |---|---|---|---|---|
-| CRCL | $76.51 | $19.5B | EV/S 5.9; forward P/E 60.8 | Reverse DCF needs about 16% revenue CAGR for a 10% return. About 74% below its 2025-06-23 intraday peak of $298.99 (83% at the 52-week low of $49.90). |
-| COIN | $151.86 | $40.2B | EV/S 7.0; forward P/E 104.5 | Q3 revenue down 35% year on year (10-Q) |
-| HOOD | $87.63 | $78.9B | EV/S 15.1; forward P/E 32.2 | The most richly priced crypto-exposed name. Crypto revenue fell 55%. |
-| V / MA | $433.90 / $670.43 | $807B / $584B | Trailing P/E about 35 | Agentic and stablecoin optionality is not priced as a separate driver |
+| CRCL | $76.51 | $19.5B | EV/S 5.9; forward P/E 60.8 | Reverse DCF needs about 16% revenue CAGR for a 10% return. About 74% below the $298.99 intraday peak of 2025-06-23. |
+| COIN | $151.86 | $40.2B | EV/S 7.0; forward P/E 104.5 | Q3 revenue down 35% year on year (10-Q). Stablecoin revenue about $307M a quarter. Risk: a Base token. |
+| HOOD | $87.63 | $78.9B | EV/S 15.1; forward P/E 32.2 | Richest multiple of the crypto-exposed names |
+| V / MA | $433.90 / $670.43 | $807B / $584B | Trailing P/E about 35 | Multiple-compression risk if rates keep rising |
 | BK | $151.55 | $102B | Forward P/E 14.9 | Reserve custody and tokenized fund servicing |
 
-- Inference: The thesis is not priced in at crypto equities after drawdowns of about 68% (COIN) to 74% (CRCL) from their peaks. But their reverse-DCF hurdles still assume crypto activity recovers. Card networks price in their core franchise, not the theme. [Moderate]
-- Inference: Picks-and-shovels caution applies. Tokenization platforms, custody and chain blockspace are commoditizing. Distribution, regulatory licences and balance sheet are the layers that hold pricing power. [Moderate]
+- Inference: Crypto equities are not cheap on their own reverse-DCF hurdles. Those hurdles assume a recovery in crypto activity, even after drawdowns of about 68% (COIN) to 74% (CRCL) from peaks. [Moderate]
+- Inference: CRCL ranks above COIN on WS5's bands despite the "distribution wins" thesis. COIN carries trading-cycle beta and the Base-token risk, while CRCL's band embeds float leverage. Treat the two as a paired "stablecoin economics" option rather than choosing one. [Low]
 
-**Stablecoin yield for US retail (2026-11-04).**
-- Fact: GENIUS bars issuers from paying interest. Exchange rewards are not barred by the statute or by the OCC final rule.
-- Fact: Coinbase advertised about 4.0% in Q1 2026 (third-party, eco.com) [SEO-shaped], and rates vary by account type (Coinbase help page).
-- Inference: That reward is a discretionary marketing payment, not a claim on reserves. It is taxed as ordinary income federally and in California. It carries exchange counterparty risk, as the Binance breach of about $6.3B on 2026-10-29 showed (Bloomberg, CNBC, 2026-10-29). It is not a substitute for a T-bill, which is state tax exempt. [Moderate]
+**Stablecoin yield for US retail.**
+- Fact: GENIUS bars issuers from paying interest. Exchange rewards are not barred by the statute or the OCC final rule. Coinbase rewards were about 4.0% in Q1 2026 (third-party, eco.com) [SEO-shaped].
+- Inference: That reward is a discretionary payment taxed as ordinary income, with exchange counterparty risk. Binance lost about $6.3B in a breach on 2026-10-29 (Bloomberg, CNBC). It is not a substitute for a T-bill, which is exempt from California tax. [Moderate]
 
 ## 7. Risks (WS6, `risks.csv`, 45 rows)
 
 | Risk | 5-year probability | Severity (1 to 5) | Hits hardest | Trigger |
 |---|---|---|---|---|
-| Single exchange or custodian theft above $500M | 80% | 4 | Exchange equities, retail on platforms | Any incident above $500M |
+| Single theft above $500M | 80% | 4 | Exchange equities, platform users | Any incident above $500M |
 | Crypto equities fall further than BTC | 85% | 4 | COIN, HOOD, CRCL | COIN drawdown above 2x BTC's on a 60-day basis |
-| BTC at or below $63,000 at some point | 70% | 4 | Token ETPs, crypto equities | BTC closes below $63,000 |
-| Yield-sharing coalitions compress issuer take rate by over 25% | 65% | 4 | CRCL | Distribution costs above 62% of reserve income |
-| Yield ban extended to exchanges and affiliates | 55% | 4 | CRCL, COIN | Any final rule or statute barring affiliate yield |
-| Policy reversal after 2028 | 35% | 4 | Agency-dependent plays | SEC majority change; reversal of the exemption |
-| USDT reserve event (USDT below $0.97 for more than 24 hours) | 10% | 5 | Whole stablecoin complex | USDT below $0.99 for 24 hours |
+| BTC at or below $63,000 at some point | 70% | 4 | Token ETPs, crypto equities | BTC close below $63,000 |
+| Issuer take rate falls over 25% | 65% | 4 | CRCL | Distribution costs above 62% of reserve income |
+| Yield ban extended to affiliates | 55% | 4 | CRCL, COIN | Final Fed rule keeps the presumption, or a statute |
+| Credit card interchange caps enacted | not estimated (added v2) | 4 | V, MA | Floor vote on a Credit Card Competition Act style bill |
+| Policy reversal after 2028 | 35% | 4 | Agency-dependent plays | Change in SEC majority |
+| Disorderly run on a top-two issuer | about 10% | 5 | Issuers, tokenized MMFs, token ETPs | Weekly supply drop above 5% for a top-two issuer |
 
-- Fact: Hack losses were $2.2B in 2024 and $3.4B in 2025 (Chainalysis) [Interested source]. In 2026 they are about $8.6B to $8.74B through 2026-10-31 (PeckShield, DefiLlama via Yahoo Finance). [Moderate]
-- Fact: Prior-cycle drawdowns were BTC -77% to -86%, ETH -82% to -94%, COIN -92% and HOOD -92% (`data/drawdowns.csv`; pre-2025 rows tagged Unverified).
+- Fact: Hack losses were $2.2B in 2024 and $3.4B in 2025 (Chainalysis) [Interested source]. In 2026 they are about $8.6B to $8.74B through 2026-10-31, including Binance.
 
-> Sizing warning: a sleeve with more than about 45% in crypto equities or tokens can breach a 40% drawdown limit in a correlated stress year (0.45 x 90% = 40.5%). Size on equity drawdown history (80% to 92%), not on BTC's.
+> **Sizing rule (v2):** sum, across all holdings, of weight times stress drawdown, assuming correlation near 1 in stress. With incumbents at 50% to 80% stress, a 40% loss limit leaves room for only about 40% in equities if the rest is cash. Crypto options must come out of that budget.
 
 ## 8. Tax (WS7, `tax_matrix.csv`)
 
 | Item | Status (2026-11-04) | Confidence |
 |---|---|---|
-| Wash sale rule (Sec. 1091) | Covers stock and securities only. Direct crypto is outside it. H.R. 10357 passed Ways and Means 38 to 5 (2026-09-16) but is not law. | [High] `[Verify with CPA]` |
-| Wash sale and spot ETP shares | ETP shares are securities, so the rule likely applies (lead inference) | [Low] `[Verify with CPA]` |
-| Form 1099-DA | Gross proceeds reported for sales on or after 2025-01-01 (TD 10000). Basis reported only for covered units acquired on or after 2026-01-01 and held in the same custodial account. | [High] |
-| Staking ETPs | Rev. Proc. 2026-20 (2026-10-06) superseded Rev. Proc. 2025-31. Rewards are ordinary income to holders. | [Moderate] `[Verify with CPA]` |
-| QSBS | Stock issued after 2025-07-04: 50%, 75%, 100% exclusion at 3, 4, 5 years; $15M cap. California does not conform. Secondary purchases do not qualify (Sec. 1202 requires original issuance). | [High] federal |
-| California | Taxes capital gains as ordinary income (top 13.3%). Treasury interest is exempt. | [Moderate] |
+| Wash sale (Sec. 1091) | Covers stock and securities only; direct crypto is outside it. H.R. 10357 passed Ways and Means 38 to 5 (2026-09-16) and is not law. | [High] `[Verify with CPA]` |
+| Wash sale and ETP shares | Likely applies, because ETP shares are securities (lead inference) | [Low] `[Verify with CPA]` |
+| Form 1099-DA | Gross proceeds reported for sales on or after 2025-01-01 (TD 10000). Basis reported for covered units acquired on or after 2026-01-01 in the same account. | [High] |
+| Staking ETPs | Rev. Proc. 2026-20 (2026-10-06) superseded Rev. Proc. 2025-31. Rewards are ordinary income. Source is secondary only. | [Moderate] `[Verify with CPA]` |
+| QSBS | Stock issued after 2025-07-04: 50%, 75%, 100% exclusion at 3, 4, 5 years; $15M cap. California does not conform. Secondary purchases do not qualify. | [High] federal |
+| California | Capital gains taxed as ordinary income (top 13.3%); Treasury interest exempt | [Moderate] |
 
 ## 9. Agentic payments (WS8)
 
-- Fact: All major payments incumbents have shipped agent products. Visa and Mastercard both say volumes are small (Q3 calls, 2026-10-28 and 2026-10-29). OpenAI shut ChatGPT Instant Checkout on 2026-03-20 (CNBC).
-- Inference: Cards win consumer checkout by agents over 1 to 3 years, because chargebacks and Regulation E and Z protections sit on card rails. Stablecoins win machine-to-machine micropayments, a pool worth about $3M a year at today's run rate. [Moderate]
+- Fact: Major payments incumbents have shipped agent products. Visa and Mastercard call volumes small (calls on 2026-10-28 and 2026-10-29). OpenAI shut ChatGPT Instant Checkout on 2026-03-20.
+- Inference: Cards win consumer agent checkout over 1 to 3 years. Stablecoins win machine-to-machine micropayments, a pool of about $3M a year today. [Moderate]
 
 ## 10. Geography (WS9)
 
-| Group | Jurisdictions | Basis | Confidence |
-|---|---|---|---|
-| Possible outsized returns | South Korea (EWY), Kazakhstan (KSPI), Brazil (EWZ, NU) | Low multiples plus a regulatory catalyst. Brazil's real fell about 12% on 2026-10-26 (Al Jazeera). | [Low] |
-| Likely losses | Argentina, Nigeria, Russia (not investable for US persons) | Capital controls, repatriation history, sanctions | [Low to Moderate] |
+| Group | Jurisdictions | Confidence |
+|---|---|---|
+| Possible outsized returns | South Korea, Kazakhstan, Brazil | [Low] |
+| Likely losses | Argentina, Nigeria, Russia (not investable for US persons) | [Low to Moderate] |
 
-- Inference: These are macro and equity bets with a thin link to programmable money. Under scenario weighting they score below T-bills. [Low]
+- Inference: These are macro bets with a thin link to the theme. Only KSPI scores above T-bills on central estimates. [Low]
 
 ## 11. Who benefits most, and how to be among them
 
-| Winner type | Why | How an investor participates | How a firm becomes one |
+| Winner type | Why | Investor route | Firm route |
 |---|---|---|---|
-| Distribution owners (Coinbase, Stripe, card networks) | They take the majority of float economics and set user defaults | Public equity: V, MA, COIN; private: Stripe | Own end-user relationships and wallet defaults |
-| Licensed balance sheets (BNY, large banks) | GENIUS, OCC charters and Basel favor regulated holders of reserves | BK, JPM | Obtain a charter, a reserve custody mandate and compliance at scale |
-| Large asset managers (BlackRock, Franklin) | Tokenized funds extend existing distribution at low marginal cost | BLK, BEN | Shelf registration plus transfer-agent tech |
-| Offshore float holders (Tether) | Highest rate times largest supply | Not investable | n/a |
-| Network tokens | Weak capture so far: fees are low and leak to L2s and intermediaries | ETH or SOL via ETP, as a small option | n/a |
+| Distribution owners | They take the majority of float economics | V, MA, COIN; Stripe (private) | Own user defaults and wallets |
+| Licensed balance sheets | GENIUS, OCC charters and Basel favor regulated reserve holders | BK, JPM | Charter, reserve custody, compliance at scale |
+| Large asset managers | Tokenized funds extend distribution at low marginal cost | BLK, BEN | Shelf registration plus transfer-agent tech |
+| Order-flow chains | Tron and Hyperliquid capture fees, but under concentrated governance | Small token option only; US access limited | n/a |
+| Offshore float holders | Highest rate times largest supply | Not investable (Tether) | n/a |
 
-- Recommendation: To be among the winners as an investor, own the toll collectors on the regulated path, and keep a small, sized option on the open-network path. As a firm, the minimum kit is a licence, reserve custody, distribution and a compliance team. WS5 rows L-01 to L-08 give a breakeven for an issuer of about $2.65B of supply against an assumed $40M a year of operating cost. [Low]
+- Recommendation: As an investor, own the toll collectors on the regulated path and keep small, capped options on the open-network path. As a firm, the minimum kit is a licence, reserve custody, distribution and compliance staff. WS5's issuer breakeven is about $2.65B of supply on an assumed $40M a year of operating cost. It assumes Circle-like distribution terms, which a new entrant will not get. [Low]
 
 ## 12. Monitoring plan
 
@@ -241,14 +278,14 @@
 | Date | Event | Watch for |
 |---|---|---|
 | 2026-11-30 | Fed GENIUS comment period closes | Whether the affiliate-yield presumption survives |
-| 2026-12-09 | FOMC | Rate path: issuer float income |
-| 2026-12-31 | Basel crypto review update due; EU digital euro target | Treatment of permissionless chains |
-| 2027-01-03 | 120th Congress convenes; CLARITY must be reintroduced | Democratic market-structure posture |
-| 2027-01-18 | GENIUS Act effective | Count of OCC-approved issuers |
-| 2027-07-18 | Target date for final FDIC and Fed rules | Rule finality |
-| 2027-10-11 | EU, UK, Switzerland move to T+1 | Settlement modernization without DLT |
+| 2026-12-09 | FOMC | A hike (priced): issuer income up, stablecoin supply pressure |
+| 2026-12-31 | Basel crypto review update due | Treatment of permissionless chains |
+| 2027-01-03 | 120th Congress convenes | Market structure and interchange bills |
+| 2027-01-18 | GENIUS Act effective | Count of approved issuers |
+| 2027-07-18 | Target date for final FDIC and Fed rules | Rule finality; Fed payment account terms |
+| 2027-10-11 | EU, UK, Switzerland move to T+1 | Modernization without DLT |
 | 2027-12-31 | WS3 test date | Stablecoins above $350B? Tokenized Treasuries above $30B? |
-| 2028-07-18 | GENIUS 3-year deadline for non-permitted stablecoins | USDT's US access path |
+| 2028-07-18 | GENIUS 3-year deadline | USDT's US access path |
 | 2028-11-07 | US presidential election | Durability of agency-made policy |
 
 **Indicator dashboard**
@@ -257,28 +294,38 @@
 |---|---|---|---|
 | USD stablecoin supply | stablecoins.llama.fi | Below $280B | Above $400B |
 | Tokenized Treasuries and MMFs | app.rwa.xyz/treasuries | Below $12B | Above $30B |
+| Represented value on Canton | app.rwa.xyz/networks/canton | Falling for two quarters | Above $600B |
 | Circle distribution cost ratio | Circle 10-Q | Above 65% | Below 55% |
 | BTC drawdown from $126,080 | CoinMarketCap | Below -50% | New high |
-| Monthly hack losses outside the largest incident | DefiLlama hacks | Above $1B | n/a |
-| Fed funds target | federalreserve.gov | n/a | n/a (affects issuer revenue) |
+| Fed target and CPI | federalreserve.gov; bls.gov | CPI above 4% with hikes | Cuts with CPI below 3% |
 
 ## 13. Dissent and weaknesses
 
-To be filled verbatim after the Phase 5 red team (see `ws/redteam_a.md`, `ws/redteam_b.md`).
+Both red-team dissents appear verbatim in Appendix A (macro economist and regulator) and Appendix B (crypto-native builder). The external review (`external_dissent.md`) was not supplied by the user at finalization. The packet is ready at `external_review_packet.md`.
+
+**How the report responded** (detail in `changelog.md`):
 
-Known weaknesses (lead):
-1. **Search caps cut evidence short.** Every workstream hit a per-agent search cap between 11 and 30 searches against a budget of 40. Many rows rest on secondary sources.
-2. **Return bands are uncalibrated.** Workstream bands are not calibrated distributions, and their lows mix one-year stress with annualized returns. Scenario weighting is therefore conservative for wide bands, and midpoints are optimistic.
-3. **No wholesale share measure.** There is no verified W series (share of wholesale flows on DLT). The scenario assignment rests on S and T only.
-4. **The model is judgment.** Its weights and slopes are stated in `assumptions.md` P2-1 to P2-12.
-
-## Sources and process
-
-- `sources.md` (279 unique URLs with bias notes)
-- `search_log.md`
-- `assumptions.md`
-- `verification.md`
-- `changelog.md`
-- `ws/ws0.md` to `ws/ws9.md` (raw workstream output)
+| Red-team item | Response |
+|---|---|
+| A2, B1: scenario weighting of bands is a category error | Accepted. Retired; replaced by a compounding-adjusted central estimate. |
+| A3: ratio score with a negative numerator | Accepted. Ranking now uses excess return with stress shown; judgment overrides are marked (J). |
+| A4, B5: stress too low; sizing rule assumes cash | Accepted. Incumbent stress raised to 2008 to 2009 levels; sizing restated as a portfolio sum. |
+| A1, B3: missing macro regime; rate sign | Accepted. Section 4A added; sensitivity now symmetric. |
+| B4, A6: momentum at the trough | Accepted in part. The model is one of five panel estimators; the trough caveat is stated. |
+| B2: represented assets excluded from T | Accepted in part. Bear is renamed; a represented variant is reported. T stays distributed for continuity. |
+| A7: no disorderly scenario | Accepted. Added as a sub-path of about 10%. |
+| B8: token capture counterexamples | Accepted. Tron and Hyperliquid added to Section 5. |
+| B7: CRCL above COIN | Accepted in part. Treated as a paired option. |
+| B10: M-08 drawdown | Accepted. Stress set to 30%; gates noted. |
+| A12: interchange legislation | Accepted. Added to risks and to V/MA kill criteria. |
+| A15, A16, B9, B11 to B25, A8 to A27 (others) | Logged in `changelog.md` as accepted, partially accepted, or not adopted, with reasons |
+
+**Residual weaknesses (lead):**
+1. **Search caps cut evidence short.** Every workstream hit a cap between 11 and 30 searches.
+2. **Bands are uncalibrated.** They are workstream judgment.
+3. **No W series.** There is no measured share of wholesale flows on ledgers.
+4. **The model is judgment.** Its weights are stated in `assumptions.md`.
+5. **Incumbent stress history is unverified.** The 2008 to 2009 figures are tagged [Unverified].
+
+---
 
-This is research, not individualized financial, legal, or tax advice, and the reader should verify current facts and consult licensed advisors before acting.
```

## personalized_plays.md diff
```diff
diff --git a/research/personalized_plays.md b/research/personalized_plays.md
index 5b6ae66..19d2bb1 100644
--- a/research/personalized_plays.md
+++ b/research/personalized_plays.md
@@ -1,88 +1,112 @@
 # Personalized plays: illustrative allocation for the Section 0 investor
 
-Date: 2026-11-04. This is an illustrative allocation built from the research matrix, not advice. Verify prices, product availability and tax treatment before acting, and consult a licensed advisor and a CPA.
+Date: 2026-11-04. Version 2, revised after the red teams (changelog C6). This is an illustrative allocation built from the research matrix, not advice. Verify prices, product availability and tax treatment before acting, and consult a licensed advisor and a CPA.
 
 ## Inputs (mandate Section 0) and how they bind
 
 | Parameter | Value | How it constrains the allocation |
 |---|---|---|
 | Jurisdiction | US, California | California taxes all gains as ordinary income (top 13.3%). Treasury interest is exempt from California tax. |
-| Capital | $50,000 cash | All positions have daily liquidity. Stocks are bought in whole or fractional shares. |
-| Accredited | No | Retail tier only. Mid and Large plays are excluded (assumption P0-4). |
-| Max drawdown | 40% on this sleeve | Sized so the perfect-correlation stress loss is about 26%, leaving a 14-point buffer |
-| Horizon | 10 years (2036) | Long-horizon plays are allowed. Locked vehicles are excluded (P0-9). |
-| Account | Taxable cash account, no margin | No leverage, no options. Tax placement is all taxable, so holding period and lot selection carry the tax planning. |
+| Capital | $50,000 cash | All positions have daily liquidity |
+| Accredited | No | Retail tier only (P0-4) |
+| Max drawdown | 40% on this sleeve | Sized on the sum of weight x stress drawdown, assuming correlation near 1 in stress |
+| Horizon | 10 years (2036) | Long-horizon equities allowed; locked vehicles excluded |
+| Account | Taxable cash account, no margin | All taxable. Holding period and lot selection carry the tax planning. |
 | Monitoring | 1 hour per week | Routine below fits in 60 minutes |
 
-## Allocation
+## Recommended: Option A, incumbent core
 
-| # | Position | Play ID | Weight | USD | Stress drawdown | Role | Entry condition |
+| # | Position | Play ID | Weight | USD | Stress | Central return | Entry |
 |---|---|---|---|---|---|---|---|
-| 1 | US T-bills, 3 to 12 month ladder (TreasuryDirect or broker) | R-27 | 30% | $15,000 | 0% | Benchmark yield of 4.21% (H.15, 2026-11-02), exempt from California tax | Buy now |
-| 2 | Franklin OnChain US Government Money Fund (BENJI app, FOBXX) | R-26 | 5% | $2,500 | about 2% | Tokenized cash: a learning position on the live rail | Confirm in the Benji app that California residents can enroll and the minimum is about $20 (YCharts; not confirmed from a primary source). If not available, add to item 1. |
-| 3 | Visa (V) | R-09, A-01 | 10% | $5,000 | 30% | Toll collector on card, stablecoin settlement ($25B run rate, Visa call 2026-10-27) and agent checkout | 3 equal monthly tranches |
-| 4 | Mastercard (MA) | R-10, A-02 | 10% | $5,000 | 30% | Same as Visa, plus its stablecoin acquisition | 3 equal monthly tranches |
-| 5 | BNY (BK) | R-12 | 7.5% | $3,750 | 40% | Reserve custody and tokenized fund servicing; forward P/E 14.9 | 3 equal monthly tranches |
-| 6 | Intercontinental Exchange (ICE) | R-16 | 7.5% | $3,750 | 40% | Exchange and clearing incumbent with tokenization options | 3 equal monthly tranches |
-| 7 | BlackRock (BLK) | R-18 | 5% | $2,500 | 40% | Largest tokenized-fund issuer (BUIDL) plus the IBIT franchise | 3 equal monthly tranches |
-| 8 | Circle (CRCL) | R-01 | 5% | $2,500 | 83% | Pure-play issuer: an option on adoption and a bet on rates | Half now. Half after 2027-01-18 (GENIUS effective), only if USDC supply is at least $70B and distribution costs are at most 65% of reserve income in the latest 10-Q. |
-| 9 | iShares Bitcoin Trust (IBIT) | R-20 | 6% | $3,000 | 77% | A capped option outside the thesis: a monetary asset, not adoption | Half now. Half only if BTC closes at or below $63,000 (-50% from $126,080). |
-| 10 | iShares Ethereum Trust (ETHA) | R-21 | 4% | $2,000 | 85% | A capped option on the main settlement chain for stablecoins (47% of supply) and distributed tokenized assets on Ethereum ($15.1B, RWA.xyz networks page, 2026-11-04) | Half now; half on ETH at or below $1,800 |
-| 11 | Reserve tranche, held in T-bills | R-27 | 10% | $5,000 | 0% | Dry powder for the trigger-based entries above, or a catalyst add (see rule R3) | Deploy only on a trigger |
-| | **Total** | | **100%** | **$50,000** | **26.3%** (weighted, perfect correlation) | | |
-
-**Expected-return arithmetic** (`return_methods.md`; assumptions P3-1 to P3-6):
-
-| Measure | Value | Basis |
+| 1 | US T-bills, 3 to 12 month ladder | R-27 | 45% | $22,500 | 0% | 4.20% | Buy now |
+| 2 | Reserve tranche in T-bills | R-27 | 10% | $5,000 | 0% | 4.20% | Deploy only on the triggers below |
+| 3 | Franklin BENJI (FOBXX) | R-26 | 5% | $2,500 | 2% | 3.85% | Confirm California eligibility and the minimum in the Benji app; otherwise add to item 1 |
+| 4 | Visa (V) | R-09 | 10% | $5,000 | 50% | 8.49% | 3 equal monthly tranches |
+| 5 | Mastercard (MA) | R-10 | 10% | $5,000 | 60% | 8.49% | 3 equal monthly tranches |
+| 6 | BNY (BK) | R-12 | 7.5% | $3,750 | 65% | 7.97% | 3 equal monthly tranches |
+| 7 | BlackRock (BLK) | R-18 | 5% | $2,500 | 60% | 7.48% | 3 equal monthly tranches |
+| 8 | Intercontinental Exchange (ICE) | R-16 | 7.5% | $3,750 | 80% | 6.97% | 3 equal monthly tranches |
+| | **Total** | | **100%** | **$50,000** | **25.0%** | **5.70%** | |
+
+**Reserve triggers** (deploy $2,500 per trigger, at most twice):
+- (a) Any of V, MA, BK falls 25% from its purchase price with its kill criterion intact.
+- (b) USD stablecoin supply exceeds $350B (DefiLlama) and tokenized Treasuries exceed $30B (RWA.xyz). In that case, fund the Option B options.
+
+## Alternative: Option B, core plus capped options
+
+Option B moves 10 points from item 1 into four options:
+
+| Position | Play ID | Weight | USD | Stress | Central return | Role |
+|---|---|---|---|---|---|---|
+| Circle (CRCL) | R-01 | 2.5% | $1,250 | 83% | 7.49% | Issuer float leverage |
+| Coinbase (COIN) | R-02 | 2.5% | $1,250 | 92% | 1.16% | Distributor; Base-token risk |
+| iShares Bitcoin Trust (IBIT) | R-20 | 2.5% | $1,250 | 77% | -4.92% | Monetary-asset option, not adoption |
+| iShares Ethereum Trust (ETHA) | R-21 | 2.5% | $1,250 | 85% | 1.45% | Settlement chain for 47% of stablecoins |
+
+| Measure | Option A | Option B |
 |---|---|---|
-| Band-midpoint return | 7.2% a year | Optimistic |
-| Scenario-weighted return | 2.9% a year | Conservative. Token ETP bands with deep lows dominate it. |
-| After-tax, scenario-weighted | about 2.2% a year | Federal 24% ordinary and 15% long-term gains, plus California 9.3% on everything. T-bill interest is taxed federally only. |
-| After-tax, T-bills alone | about 3.2% a year | 4.21% x (1 - 0.24) |
+| Stress loss | 25.0% | 33.4% |
+| Central return | 5.70% | 5.41% |
 
-- Inference: On scenario weighting, the theme sleeve is not expected to beat T-bills after tax. On midpoints it beats them by about 2 to 3 points. The real case for the sleeve is the incumbent equities' core franchises plus a small, capped Bull option. [Moderate]
-- Inference: A version with no tokens and no CRCL is equally defensible: items 3 to 7 (40%) plus 60% T-bills and BENJI. It has a 14.0% stress loss, a 5.7% midpoint return and a 5.3% scenario-weighted return. Its midpoint is lower but its scenario-weighted return is higher, because it drops the bands with deep lows. Choose it if you weight the conservative method more. [Moderate]
+- Inference: Option B lowers the central estimate and raises stress. Choose it only if you want exposure to the Bull tail (7% in 2030, 11% in 2035) and accept that cost. [Moderate]
+
+**After-tax arithmetic**
+
+Assumption P3-6: federal 24% ordinary and 15% long-term gains, plus California 9.3% on everything. Treasury interest is federally taxed only.
+
+| Measure | Value |
+|---|---|
+| Option A, after tax | about 0.60 x (4.2 x 0.76) + 0.40 x (8.0 x 0.757) = about 4.3% a year |
+| T-bills alone, after tax | 4.21 x 0.76 = 3.2% a year |
+| Real return (CPI 3.7%) | about +0.6 points for Option A; about -0.5 points for T-bills alone |
+
+- Inference: The excess over T-bills comes mainly from the incumbents' core franchises, not from the theme. That is the honest finding of this research. [Moderate]
 
 ## Account placement and tax handling (all taxable)
 
 | Holding | Federal character | California | Action |
 |---|---|---|---|
 | T-bills | Ordinary interest | Exempt | Hold to maturity; roll the ladder |
-| BENJI (FOBXX) | Ordinary dividends | Exempt share pass-through if the fund qualifies | Keep the year-end fund letter for the California exemption |
-| V, MA, BK, ICE, BLK, CRCL | Qualified dividends and long-term capital gains after 1 year | Ordinary income | Elect specific-identification lot method at the broker. Hold over 1 year for the federal rate. |
-| IBIT, ETHA | Capital gain on shares; grantor trust | Ordinary income | Wash sale likely applies to ETP shares `[Verify with CPA]`. Avoid the staking ETP variant in taxable (ordinary income each year). |
-
-- Fact: Direct tokens are outside Sec. 1091 today (WS7), but H.R. 10357 would change that. The ETP route was chosen over direct custody for four reasons: broker 1099-B reporting, no exchange key risk (Binance breach of about $6.3B, 2026-10-29), estate step-up simplicity, and Section 0's 1-hour weekly budget. [Moderate]
+| BENJI (FOBXX) | Ordinary dividends | Exempt portion if the fund qualifies | Keep the year-end fund letter |
+| V, MA, BK, BLK, ICE (and CRCL, COIN in Option B) | Qualified dividends; long-term gains after 1 year | Ordinary income | Elect specific-identification lots; hold over 1 year for the federal rate |
+| IBIT, ETHA (Option B) | Capital gain on grantor-trust shares | Ordinary income | Wash sale likely applies to ETP shares `[Verify with CPA]`. Avoid staking variants in taxable. |
 
 ## Rebalancing rule
 
 | Rule | Trigger | Action |
 |---|---|---|
-| R1 | Annual date (first trading day of November) | Return to target weights. Sell lots held over 1 year first. |
-| R2 | Any position drifts by 5 or more points from target | Rebalance that position only |
-| R3 | IBIT, ETHA and CRCL combined exceed 20% | Trim to 15% |
-| R4 | Sleeve drawdown from peak reaches 25% | Freeze additions. Review every kill criterion. |
-| R5 | Sleeve drawdown reaches 35% | Move IBIT, ETHA and CRCL to T-bills, protecting the 40% limit |
+| R1 | Annual (first trading day of November) | Return to target weights, selling lots held over 1 year first |
+| R2 | Any position 5 or more points from target | Rebalance that position |
+| R3 | Total equity and option weight exceeds 50% | Trim to 40% (A) or 50% (B) |
+| R4 | Sleeve drawdown reaches 25% | Freeze additions; review kill criteria |
+| R5 | Sleeve drawdown reaches 35% | Sell Option B positions to T-bills first, then trim equities to protect the 40% limit |
 
-## Kill criteria (from `plays.csv`, lead-condensed)
+## Kill criteria
 
 | Position | Exit if |
 |---|---|
-| CRCL | USDC supply falls below $55B for two quarters, or distribution costs exceed 70% of reserve income, or a final rule bars affiliate yield and Circle guides revenue down 20% |
-| V, MA | Lead-proposed: interchange caps on credit cards enacted (e.g., a Credit Card Competition Act style law), or payments volume growth below 3% for two quarters |
+| V, MA | Credit card interchange caps enacted (Credit Card Competition Act style), or payments volume growth below 3% for two quarters |
 | BK | Loss of a top-two stablecoin reserve custody mandate, or a material custody incident |
-| IBIT, ETHA | Exit on a thesis break, not on price: a spot ETP custodian incident, or a protocol failure (for example, a quantum-forced migration without a plan) |
-| BENJI | Fund breaks $1.00 NAV, or there is a transfer-agent or ledger incident |
+| BLK, ICE | Tokenized-fund or venue franchise lost to a new entrant, shown by two consecutive quarters of share loss in their disclosures |
+| CRCL (B) | USDC below $55B for two quarters, or distribution costs above 70% of reserve income |
+| COIN (B) | A Base token routes sequencer revenue away from Coinbase, or stablecoin revenue falls 30% year on year |
+| IBIT, ETHA (B) | Custodian incident or protocol failure. Price alone is not a kill criterion. |
+| BENJI | NAV below $1.00, or a transfer-agent or ledger incident |
 
 ## Weekly monitoring routine (60 minutes)
 
 | Time | Task | Source |
 |---|---|---|
-| 10 min | Check the dashboard: stablecoin supply, tokenized Treasuries, BTC and ETH drawdown, sleeve drawdown | stablecoins.llama.fi; app.rwa.xyz/treasuries; broker |
-| 10 min | Check entry triggers (CRCL second half, IBIT and ETHA second halves) and rules R3 to R5 | This file |
-| 20 min | Read one primary-source item from the catalyst calendar (Federal Register docket, FOMC statement, earnings release) | REPORT.md Section 12 |
-| 20 min | Quarterly weeks only: read V, MA, BK, ICE, BLK and CRCL results against kill criteria. Other weeks: spare. | Company IR pages |
-
-> Risk flags: exchange counterparty risk (avoid holding cash or stablecoins on exchanges for yield); correlated crypto drawdowns (prior cycles -77% to -94%); policy reversal risk after the 2028 election; concentration in large-cap US financials. This allocation is illustrative and assumes the $50,000 is not the investor's emergency fund.
+| 10 min | Check the dashboard: stablecoin supply, tokenized Treasuries, sleeve drawdown, Fed and CPI | stablecoins.llama.fi; app.rwa.xyz/treasuries; broker |
+| 10 min | Check reserve triggers and rules R3 to R5 | This file |
+| 20 min | Read one primary-source item from the catalyst calendar | REPORT.md Section 12 |
+| 20 min | In earnings weeks, read the holdings' results against kill criteria; otherwise spare | Company IR pages |
+
+> **Risk flags:**
+> - Correlated drawdowns: in 2008 to 2009 the incumbents in this list fell 50% to 80% [Unverified history].
+> - Rates: higher rates compress the 35x multiples of V and MA.
+> - Exchange counterparty risk: do not hold cash or stablecoins on exchanges for yield.
+> - Policy reversal risk after 2028.
+> - This allocation assumes the $50,000 is not the investor's emergency fund.
 
 This is an illustrative allocation, not individualized financial, legal, or tax advice; verify current facts and consult licensed advisors before acting.
```
