# External review packet

Purpose: paste everything below the line into a frontier model from a different vendor. Save its response as `research/external_dissent.md`. Phase 6 incorporates that file if it exists.

---

**Instruction to the reviewing model:** Attack this thesis and these positions. List the ten strongest objections with evidence (cite sources with dates). For each objection give a severity (Critical, High, Medium, Low), the specific claim or play_id it targets, and what should change. Then give your own probabilities for Bear, Base and Bull in 2030 and 2035, with basis. Today's date is 2026-11-04; verify current facts by search where you can.

## Thesis in brief (as of 2026-11-04)

- **Adoption:** USD stablecoin supply is $295.1B (DefiLlama), down 3.0% over 12 months and 6.5% below its 2026-05-17 peak. Tokenized Treasuries and MMFs are $14.25B (RWA.xyz), 0.18% of US MMF assets ($7.90T, ICI). Real stablecoin payments are $0.39T annualized (McKinsey/Artemis), against Visa-adjusted volume of $12.0T for Jan to Aug 2026.
- **Law:** GENIUS Act (Public Law 119-27) takes effect 2027-01-18. The OCC final rule (2026-10-21) limits the yield ban to issuers only. The CLARITY Act failed Senate cloture 49 to 50 (2026-09-15). Democrats won both chambers in the 2026-11-03 midterms.
- **Value capture:** Circle's distribution and transaction costs were 62% of Q3 2026 reserve income, mostly paid to partners. Ethereum gross fee revenue was $127M in H1 2026. Conclusion: value accrues to distribution, licences and balance sheets (card networks, custodians, asset managers, issuers), not to network tokens.
- **Rates:** Fed funds is 3.75% to 4.00%. A 100 bp cut removes about $276M of Circle's reserve income after distribution costs.
- **Risks:** a $6.3B Binance breach (2026-10-29). BTC is about 37% below its $126,080 high.

## Scenario definitions and probabilities

S = stablecoin supply. T = tokenized real-world assets excluding stablecoins (distributed value). W = DLT share of wholesale flows (no verified series). A scenario occurs if two of the three measures fall in its band.

| Scenario | 2030 band | 2035 band | P(2030) | P(2035) |
|---|---|---|---|---|
| Bear | S < $500B; T < $100B | S < $1T; T < $500B | 57% | 53% |
| Base | S $500B to $1.5T; T $100B to $500B | S $1T to $4T; T $0.5T to $5T | 36% | 38% |
| Bull | S > $1.5T; T > $500B | S > $4T; T > $5T | 7% | 9% |

**Method.** The probabilities are an ordered-logit model over 11 weighted drivers, averaged with analyst judgment.
- The model adds a momentum term (stablecoin growth blending -3% over 12 months and +33% over 36 months) and an analog base-rate prior of 0.50.
- The top drivers are regulatory clarity and end-user demand (weight 0.14 each), then bank capital treatment (0.10).
- The model's range for 2030 Bear is 50% to 73%.

## Top plays per tier

| Rank | Retail | Mid (accredited) | Large |
|---|---|---|---|
| 1 | T-bills plus Franklin BENJI | Tokenized private credit (Apollo ACRED, Hamilton Lane) | Anchor a tokenized MMF launch |
| 2 | Visa, Mastercard | Tokenized Treasuries and MMFs for qualified investors | Buy, not build, a licensed issuer |
| 3 | BNY | Ripple secondary at a discount to tender | Custody infrastructure |
| 4 | BlackRock, ICE | Kraken secondary | Tokenized-deposit bank partnership |
| 5 | Circle (small option) | Anchorage | Blocks in CRCL or COIN on drawdowns |

**Ranking method.** Scenario-weighted return = P(Bear) x band low + P(Base) x band midpoint + P(Bull) x band high, minus the 4.21% T-bill rate, divided by stress drawdown.

## Illustrative personal allocation

Investor: non-accredited California resident, $50k, taxable cash account, 40% maximum drawdown, 10-year horizon.

| Position | Weight |
|---|---|
| T-bills | 40% (including a 10% trigger reserve) |
| BENJI | 5% |
| Visa | 10% |
| Mastercard | 10% |
| BNY | 7.5% |
| ICE | 7.5% |
| BlackRock | 5% |
| Circle | 5% |
| IBIT | 6% |
| ETHA | 4% |

The weighted stress loss is 26.3%. The return is 2.9% scenario-weighted and 7.2% at band midpoints, pre-tax.

## Full plays matrix (75 rows)

| play_id | vehicle | ticker_or_route | tier | horizon | return_band_annual_pct | return_method | kill_criterion | confidence |
|---|---|---|---|---|---|---|---|---|
| R-01 | Circle common stock | CRCL | Retail | Medium | -5 to 21 | reverse_dcf | USDC period-end circulation below 65B for two quarters or RLDC margin below 40% | Moderate |
| R-02 | Coinbase common stock | COIN | Retail | Medium | -9 to 12 | reverse_dcf | Subscription and services revenue below 500M per quarter for two quarters | Moderate |
| R-03 | Robinhood common stock | HOOD | Retail | Medium | -9 to 10 | reverse_dcf | Net deposits growth below 5% annualized or crypto revenue below 100M per quarter | Moderate |
| R-04 | Galaxy Digital Class A | GLXY | Retail | Medium | -50 to 40 | base_rate_analog | BTC below 60k with no AI data-center contract revenue | Low |
| R-05 | Bullish common stock | BLSH | Retail | Medium | -40 to 30 | comps | Volume share loss two quarters in a row | Low |
| R-06 | Figure Technology Solutions | FIGR | Retail | Medium | -35 to 35 | comps | Origination volume down 20% yoy | Low |
| R-07 | Gemini Space Station | GEMI | Retail | Short | -60 to 100 | base_rate_analog | Cash runway under 4 quarters | Low |
| R-08 | Securitize Corp | SECZ | Retail | Medium | -45 to 80 | comps | Revenue growth below 50% yoy | Low |
| R-09 | Visa | V | Retail | Long | 7 to 10 | comps | Core revenue growth below 5% for 4 quarters | Low |
| R-10 | Mastercard | MA | Retail | Long | 7 to 10 | comps | Core revenue growth below 5% for 4 quarters | Low |
| R-11 | PayPal | PYPL | Retail | Long | 0 to 12 | comps | Core revenue shrinking two years running | Low |
| R-12 | BNY (Bank of New York Mellon) | BK | Retail | Long | 5 to 11 | comps | Fee revenue growth below 3% for 4 quarters | Low |
| R-13 | State Street | STT | Retail | Long | 4 to 10 | comps | Fee revenue flat two years | Low |
| R-14 | JPMorgan Chase (Kinexys) | JPM | Retail | Long | 3 to 9 | comps | ROE below 12% for 4 quarters | Low |
| R-15 | Nasdaq Inc | NDAQ | Retail | Long | 4 to 9 | comps | Tokenization pilots abandoned and multiple above 30x | Low |
| R-16 | Intercontinental Exchange | ICE | Retail | Long | 4 to 10 | comps | EPS growth below 4% two years | Low |
| R-17 | CME Group | CME | Retail | Long | 4 to 9 | comps | Volume per day down 20% for 4 quarters | Low |
| R-18 | BlackRock (BUIDL, IBIT) | BLK | Retail | Long | 5 to 10 | comps | Net flows negative for 4 quarters | Low |
| R-19 | Franklin Resources (BENJI) | BEN | Retail | Long | 4 to 10 | comps | AUM outflows four quarters in a row | Low |
| R-20 | iShares Bitcoin Trust | IBIT | Retail | Long | -60 to 80 | base_rate_analog | BTC below 50k | Moderate |
| R-21 | iShares Ethereum Trust | ETHA | Retail | Long | -65 to 120 | base_rate_analog | ETH/BTC ratio below 0.02 for two years | Moderate |
| R-22 | Staking Ethereum ETPs | ETHB; Grayscale ETHE (71% staked 2026-03-31) | Retail | Long | -60 to 130 | base_rate_analog | ETH yield below 1.5% net | Low |
| R-23 | Spot Solana ETFs (staking) | BSOL (0.20%), GSOL (0.35%), SOEZ 0.19%, FSOL 0.25% | Retail | Long | -75 to 150 | base_rate_analog | SOL below 50 for 6 months | Low |
| R-24 | Spot XRP ETFs | XRPZ 0.19%, TOXR 0.30%, Bitwise 0.34%, GXRP 0.35%, XRPC 0.50% | Retail | Long | -80 to 150 | base_rate_analog | Ripple loses legal clarity | Low |
| R-25 | Blockchain equity ETFs | BLOK (0.70%), TKNQ (0.69%, AUM about 1.1M) | Retail | Medium | -35 to 45 | base_rate_analog | BLOK AUM below 300M | Low |
| R-26 | Franklin OnChain U.S. Government Money Fund (BENJI) | Benji Investments app (FOBXX) | Retail | Short | 3.5 to 4.2 | yield | Yield spread to T-bills above 100bp | Low |
| R-27 | Benchmark: 3M T-bill / SPY | T-bill ladder; SPY | Retail | Short | 4.0 to 4.4 | yield | NA (benchmark) | Moderate |
| R-28 | Ether (direct token) | ETH via Coinbase or Kraken | Retail | Long | -65 to 120 | base_rate_analog | See R-21 | Moderate |
| R-29 | Solana (direct token) | SOL | Retail | Long | -75 to 150 | base_rate_analog | See R-23 | Low |
| R-30 | Chainlink (direct token) | LINK | Retail | Long | -70 to 150 | base_rate_analog | No sustained enterprise revenue by 2028 | Low |
| R-31 | USDC / issuer-paid yield | USDC held at Coinbase, Kraken, wallet | Retail | Short | 0 to 0 | yield | nan | Moderate |
| R-32 | Exchange or platform stablecoin rewards | Third-party rewards programs | Retail | Short | nan | yield | Platform ends rewards | Low |
| R-33 | DeFi stablecoin lending (self-custody) | Aave-type protocols | Retail | Short | nan | yield | Any exploit above 5% of TVL | Unverified |
| R-34 | Event: GENIUS Act effective date | Hold CRCL and PYPL through effective date | Retail | Short | -15 to 15 | base_rate_analog | Final rules delayed past 2027-04 | Low |
| R-35 | Event: CLARITY Act revival or death | COIN, HOOD, CRCL basket | Retail | Short | -25 to 30 | base_rate_analog | Bill formally withdrawn | Low |
| R-36 | Event: Fed path and CRCL rate sensitivity | CRCL | Retail | Short | -30 to 20 | revenue_pool_share | Two cuts priced and supply flat | Moderate |
| R-37 | Event: Gemini earnings | GEMI | Retail | Short | -50 to 60 | base_rate_analog | nan | Low |
| R-38 | Event: Kraken IPO filing | COIN, HOOD read-through | Retail | Short | -10 to 10 | base_rate_analog | IPO shelved past 2027 | Low |
| M-01 | Kraken (Payward) secondary | Forge, Hiive, EquityZen | Mid | Short | -29 to 64 | comps | IPO pushed past 2028 | Low |
| M-02 | Ripple Labs secondary | Forge and brokers | Mid | Medium | -29 to 77 | comps | Secondary below 10B | Low |
| M-03 | Stripe secondary (Tempo, Bridge parent) | Brokers | Mid | Medium | -13 to 25 | comps | Down round below 120B | Low |
| M-04 | Anchorage Digital | Direct private round or secondary | Mid | Medium | -20 to 40 | comps | Down round | Low |
| M-05 | Fireblocks secondary | NPM, brokers | Mid | Medium | -30 to 40 | comps | Sale below 2.5B | Low |
| M-06 | Chainalysis, Paxos, Digital Asset (Canton) private marks | nan | Mid | Medium | nan | comps | nan | Unverified |
| M-07 | Crypto venture funds | a16z crypto, Paradigm, Haun, Pantera (feeder access) | Mid | Long | -10 to 25 | base_rate_analog | Fund TVPI below 1.0 at year 5 | Unverified |
| M-08 | Tokenized private credit funds | Apollo ACRED and Hamilton Lane via Securitize | Mid | Medium | 6 to 9 | yield | Redemption gate invoked | Low |
| M-09 | Tokenized Treasury and MMF (qualified) | BUIDL, OUSG | Mid | Short | 3.7 to 4.1 | yield | Spread to bills above 100bp | Low |
| M-10 | Validator and staking operation | ETH 32-ETH validators | Mid | Medium | 0 to 4 | yield | Net reward yield below 1.5% | Low |
| M-11 | Structured notes on IBIT or BTC | Bank-issued buffered notes (illustrative) | Mid | Short | -16 to 14 | base_rate_analog | Cap below 20% | Low |
| M-12 | Reg S offshore stablecoin and tokenization funds | Non-US placements | Mid | Medium | nan | yield | nan | Low |
| L-01 | Issuer build: GENIUS-licensed stablecoin | Own issuer or OCC trust charter | Large | Medium | -60 to 35 | revenue_pool_share | Not at 2.65B supply by month 36 | Low |
| L-02 | Issuer buy: acquire a stablecoin issuer | Target list unverified | Large | Medium | 3 to 15 | comps | Supply outflow above 20% post-deal | Low |
| L-03 | Anchor position in tokenized fund launch | Seed 50 to 100M in new tokenized MMF | Large | Short | 3.5 to 4.2 | yield | Fund under 250M after 12 months | Low |
| L-04 | Stake in a settlement consortium | Canton, DTCC-linked or bank consortia | Large | Long | -100 to 30 | base_rate_analog | No volume within 24 months | Low |
| L-05 | Bank partnership for tokenized deposits | Kinexys or Citi Token Services client | Large | Medium | nan | base_rate_analog | No volume in 12 months | Unverified |
| L-06 | Infrastructure build versus buy | Custody (Anchorage 4.2B, Fireblocks 2.5 to 5B) | Large | Medium | nan | comps | nan | Low |
| L-07 | Sovereign engagement | Treasury and central bank partnerships | Large | Long | nan | base_rate_analog | nan | Unverified |
| L-08 | Operating requirements to participate | Licenses, custody, compliance team | Large | Medium | nan | revenue_pool_share | nan | Low |
| L-09 | Block holding in public equities (CRCL, COIN) | Institutional accounts | Large | Short | -10 to 15 | comps | nan | Low |
| L-10 | Arc network validator or ARC token allocation | Arc (Circle L1) | Large | Medium | nan | base_rate_analog | Unlock terms adverse | Unverified |
| A-01 | Common stock | V | Retail | Long | 6 to 12 | comps | Two consecutive quarters of net revenue growth below 8% with stablecoin settlement volume cited by Visa as substitutive | Moderate |
| A-02 | Common stock | MA | Retail | Long | 6 to 12 | comps | Mastercard states agent volume is below 0.1% of switched volume after 4 more quarters (no such figure disclosed yet) or net revenue growth below 8% for two quarters | Moderate |
| A-03 | Common stock | NET | Retail | Medium | -35 to 30 | base_rate_analog | No general availability of Pay Per Use by 2027-09-30 or stated paid-crawl revenue still undisclosed after 2027 FY results | Low |
| A-04 | Common stock | COIN | Retail | Medium | -40 to 35 | base_rate_analog | No separate agent or x402 revenue line by Q4 2027 letter | Low |
| A-05 | Common stock | PYPL | Retail | Medium | nan | reverse_dcf | No agentic volume disclosure by Q4 2027 results | Unverified |
| A-06 | Secondary shares or tender in Stripe (private; Tempo parent incubator) | Private route via accredited secondary platform or fund | Mid | Medium | nan | comps | Tempo mainnet usage stays below 1M monthly payments after 2027-03 | Low |
| A-07 | Venture fund or direct round in agent identity and payment startups (Skyfire, Nevermined class) | Private route | Large | Long | nan | base_rate_analog | Standards finalized with network-owned directories making third-party KYA redundant | Low |
| A-08 | Avoid: x402 ecosystem tokens and PING-type tokens | Not recommended | Retail | Short | -100 to 0 | base_rate_analog | Not applicable: do not hold | Moderate |
| G-01 | NYSE-listed ADS (Cayman; Brazil ops) | NU | Retail | Medium | -20 to 25 | comps | Fwd P/E under 8x with EPS cuts, or BRL/USD move beyond a further 15% weaker | Low |
| G-02 | NASDAQ-listed common stock | MELI | Retail | Medium | -18 to 25 | comps | Fintech TPV growth below 30% for two quarters or fwd P/E not supported by EPS growth | Low |
| G-03 | NASDAQ-listed ADS (Kazakhstan; Turkey via Hepsiburada) | KSPI | Retail | Medium | -26 to 47 | comps | Net profit falls two consecutive quarters or Turkey losses widen beyond plan | Low |
| G-04 | NYSE Arca ETF (iShares MSCI South Korea) | EWY | Retail | Medium | -27 to 15 | base_rate_analog | Bill dies or bank-only issuance excludes non-bank fintechs; P/E re-rates above 11 | Low |
| G-05 | NYSE Arca ETF (iShares MSCI Brazil) | EWZ | Retail | Medium | -23 to 23 | base_rate_analog | Real weakens beyond a further 15% or fiscal anchor abandoned | Low |
| G-06 | NYSE Arca ETF (Global X MSCI Argentina) | ARGT | Retail | Medium | -25 to 29 | comps | Reimposition of individual dollar purchase limits | Low |
| G-07 | NYSE Arca ETF (iShares MSCI India) | INDA | Retail | Long | -16 to 12 | comps | P/E stays above 20 while 1y return negative for second year | Low |

This is research, not individualized financial, legal, or tax advice.
