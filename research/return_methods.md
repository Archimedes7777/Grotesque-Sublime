# Return methods and arithmetic per play

Each row gives the workstream's stated method and arithmetic (verbatim from `return_method_detail`), then the lead's v2 central estimate.

Lead formula (v2): read the band as roughly the 10th to 90th percentile of annual returns. sigma = (high - low) / 2.563; central = midpoint - sigma^2 / 2 (compounding drag). Excess = central - 4.21% (3M T-bill constant maturity, H.15, 2026-11-02). Plays are ranked within tier on excess; stress drawdown is shown separately (assumptions.md P6-1 to P6-3).

Retired v1 method: scenario-weighting of band low, mid and high by Bear, Base and Bull probabilities. Both red teams showed it maps adoption states onto assets whose returns do not depend on adoption (changelog C1).

Caution: bands are workstream judgment, not calibrated distributions.


## R-01 Circle common stock (CRCL), Retail, Medium

- Band: -5 to 21 percent per year. Method: reverse_dcf.
- Workstream arithmetic (WS5): Price implies 10y rev CAGR 16.1%: mcap 19.52B x1.10^10 / 20x P/E = 2.53B NI; /20% margin = 12.7B rev vs 2.85B TTM ex-presale. Scenarios: bear USDC 120B x3.0% = 3.6B res inc, NI 0.75B x15 = 11.2B (-5.4%/yr); base 300B x3.5% NI 2.19B x20 = 43.8B (+8.4%/yr); bull 750B NI 5.47B x25 = 136.7B (+21.5%/yr)
- Lead central estimate: mid = (-5 + 21) / 2 = 8; sigma = 26 / 2.563 = 10.1%; central = 8 - 10.1^2 / 200 = 7.49%; excess 3.28 pts; stress 83%; tier rank 7.0

## R-02 Coinbase common stock (COIN), Retail, Medium

- Band: -9 to 12 percent per year. Method: reverse_dcf.
- Workstream arithmetic (WS5): Price implies 10y rev CAGR 17.0%: mcap 40.21B x1.10^10 /20x = 5.21B NI; /20% = 26.1B rev vs 5.44B TTM. Scenarios: bear rev flat 5.44B NI 1.09B x15 = 16.3B (-8.6%/yr); base 10% CAGR NI 2.82B x20 = 56.4B (+3.4%/yr); bull 26B NI 5.2B x25 = 130B (+12.5%/yr)
- Lead central estimate: mid = (-9 + 12) / 2 = 1.5; sigma = 21 / 2.563 = 8.2%; central = 1.5 - 8.2^2 / 200 = 1.16%; excess -3.05 pts; stress 92%; tier rank 23.0

## R-03 Robinhood common stock (HOOD), Retail, Medium

- Band: -9 to 10 percent per year. Method: reverse_dcf.
- Workstream arithmetic (WS5): Price implies 10y rev CAGR 18.3 to 21.0%: mcap 78.91B x1.10^10 /25x = 8.19B NI; /30% = 27.3B rev vs 5.08B TTM. Scenarios: bear 5% CAGR NI 2.07B x15 = 31B (-8.9%/yr); base 12% NI 4.73B x20 = 94.7B (+1.8%/yr); bull 18% NI 7.98B x25 = 199B (+9.7%/yr)
- Lead central estimate: mid = (-9 + 10) / 2 = 0.5; sigma = 19 / 2.563 = 7.4%; central = 0.5 - 7.4^2 / 200 = 0.23%; excess -3.98 pts; stress 92%; tier rank 26.0

## R-04 Galaxy Digital Class A (GLXY), Retail, Medium

- Band: -50 to 40 percent per year. Method: base_rate_analog.
- Workstream arithmetic (WS5): Beta to BTC of 1.26 for COIN (Nadcab, mid-2026) as analog; BTC 1y -20.4%: 1.26 x -20.4% = -26% central drawdown case; +/-1 sigma 30-day vol 68 to 90% gives wide band
- Lead central estimate: mid = (-50 + 40) / 2 = -5; sigma = 90 / 2.563 = 35.1%; central = -5 - 35.1^2 / 200 = -11.17%; excess -15.38 pts; stress 80%; tier rank 46.0

## R-05 Bullish common stock (BLSH), Retail, Medium

- Band: -40 to 30 percent per year. Method: comps.
- Workstream arithmetic (WS5): mcap 3.51B / rev 300.7M = 11.7x sales vs COIN EV/S 7.03; re-rate to 7x sales on flat revenue = 2.1B (-40%); 12x on +25% revenue = 4.5B (+28%)
- Lead central estimate: mid = (-40 + 30) / 2 = -5; sigma = 70 / 2.563 = 27.3%; central = -5 - 27.3^2 / 200 = -8.73%; excess -12.94 pts; stress 80%; tier rank 45.0

## R-06 Figure Technology Solutions (FIGR), Retail, Medium

- Band: -35 to 35 percent per year. Method: comps.
- Workstream arithmetic (WS5): mcap 5.23B / rev 619M = 8.4x sales, P/E 27.2; at 6x sales on +20% revenue (743M) = 4.5B (-14%); at 10x on +35% (836M) = 8.4B (+60%) over 1y
- Lead central estimate: mid = (-35 + 35) / 2 = 0; sigma = 70 / 2.563 = 27.3%; central = 0 - 27.3^2 / 200 = -3.73%; excess -7.94 pts; stress 80%; tier rank 37.0

## R-07 Gemini Space Station (GEMI), Retail, Short

- Band: -60 to 100 percent per year. Method: base_rate_analog.
- Workstream arithmetic (WS5): Price 2.70 vs 52w high 17.77 = -84.8%; options-like payoff: 0.4x (-60%) if burn continues, 2x (+100%) if acquired or recovers
- Lead central estimate: mid = (-60 + 100) / 2 = 20; sigma = 160 / 2.563 = 62.4%; central = 20 - 62.4^2 / 200 = 0.51%; excess -3.70 pts; stress 80%; tier rank 25.0

## R-08 Securitize Corp (SECZ), Retail, Medium

- Band: -45 to 80 percent per year. Method: comps.
- Workstream arithmetic (WS5): mcap 1.39B / rev 66.77M = 20.8x sales; at 10x on 2x revenue (133M) = 1.33B (-4%); at 20x on 3x (200M) = 4.0B (+188%) over 3y = +42%/yr; bear 5x on flat = 0.33B (-76% total)
- Lead central estimate: mid = (-45 + 80) / 2 = 17.5; sigma = 125 / 2.563 = 48.8%; central = 17.5 - 48.8^2 / 200 = 5.61%; excess 1.40 pts; stress 80%; tier rank 17.0

## R-09 Visa (V), Retail, Long

- Band: 7 to 10 percent per year. Method: comps.
- Workstream arithmetic (WS5): P/E 35.2 to exit 28 with EPS +10%/yr (assumption): 1.10^10 x 28/35.2 = 2.06x = 7.5%/yr plus 0.8% yield = 8.3%
- Lead central estimate: mid = (7 + 10) / 2 = 8.5; sigma = 3 / 2.563 = 1.2%; central = 8.5 - 1.2^2 / 200 = 8.49%; excess 4.28 pts; stress 50%; tier rank 3.0

## R-10 Mastercard (MA), Retail, Long

- Band: 7 to 10 percent per year. Method: comps.
- Workstream arithmetic (WS5): P/E 35.1 to 28 with EPS +11% (assumption): 1.11^10 x 28/35.1 = 2.27x = 8.5%/yr plus 0.5% = 9.0%
- Lead central estimate: mid = (7 + 10) / 2 = 8.5; sigma = 3 / 2.563 = 1.2%; central = 8.5 - 1.2^2 / 200 = 8.49%; excess 4.28 pts; stress 60%; tier rank 3.0

## R-11 PayPal (PYPL), Retail, Long

- Band: 0 to 12 percent per year. Method: comps.
- Workstream arithmetic (WS5): P/E 11.5 exit 11: EPS +3%/yr gives 1.03^10 x 11/11.5 = 1.29x = 2.6%/yr; EPS +8% gives 2.06x = 7.5%/yr; plus buybacks to about 12% (assumptions)
- Lead central estimate: mid = (0 + 12) / 2 = 6; sigma = 12 / 2.563 = 4.7%; central = 6 - 4.7^2 / 200 = 5.89%; excess 1.68 pts; stress 80%; tier rank 16.0

## R-12 BNY (Bank of New York Mellon) (BK), Retail, Long

- Band: 5 to 11 percent per year. Method: comps.
- Workstream arithmetic (WS5): P/E 16.8 trailing, 14.9 fwd; EPS +6%/yr and flat multiple 1.06^10 = 1.79x = 6.0%/yr plus 2.0% yield (assumptions) = 8%
- Lead central estimate: mid = (5 + 11) / 2 = 8; sigma = 6 / 2.563 = 2.3%; central = 8 - 2.3^2 / 200 = 7.97%; excess 3.76 pts; stress 65%; tier rank 5.0

## R-13 State Street (STT), Retail, Long

- Band: 4 to 10 percent per year. Method: comps.
- Workstream arithmetic (WS5): P/E 14.05 flat; EPS +5%/yr = 1.05^10 = 1.63x = 5%/yr plus 3% yield (assumptions) = 8%
- Lead central estimate: mid = (4 + 10) / 2 = 7; sigma = 6 / 2.563 = 2.3%; central = 7 - 2.3^2 / 200 = 6.97%; excess 2.76 pts; stress 80%; tier rank 9.0

## R-14 JPMorgan Chase (Kinexys) (JPM), Retail, Long

- Band: 3 to 9 percent per year. Method: comps.
- Workstream arithmetic (WS5): P/E 14.7 exit 13; EPS +6%: 1.06^10 x 13/14.7 = 1.58x = 4.7%/yr plus 2% yield = 6.7%
- Lead central estimate: mid = (3 + 9) / 2 = 6; sigma = 6 / 2.563 = 2.3%; central = 6 - 2.3^2 / 200 = 5.97%; excess 1.76 pts; stress 70%; tier rank 15.0

## R-15 Nasdaq Inc (NDAQ), Retail, Long

- Band: 4 to 9 percent per year. Method: comps.
- Workstream arithmetic (WS5): P/E 29.9 exit 25; EPS +9%: 1.09^10 x 25/29.9 = 1.98x = 7.1%/yr plus 1.2% yield = 8.3%
- Lead central estimate: mid = (4 + 9) / 2 = 6.5; sigma = 5 / 2.563 = 2.0%; central = 6.5 - 2.0^2 / 200 = 6.48%; excess 2.27 pts; stress 65%; tier rank 12.0

## R-16 Intercontinental Exchange (ICE), Retail, Long

- Band: 4 to 10 percent per year. Method: comps.
- Workstream arithmetic (WS5): P/E 23.7 flat; EPS +8%: 1.08^10 = 2.16x = 8%/yr plus 1.2% yield (assumptions) = 9%
- Lead central estimate: mid = (4 + 10) / 2 = 7; sigma = 6 / 2.563 = 2.3%; central = 7 - 2.3^2 / 200 = 6.97%; excess 2.76 pts; stress 80%; tier rank 9.0

## R-17 CME Group (CME), Retail, Long

- Band: 4 to 9 percent per year. Method: comps.
- Workstream arithmetic (WS5): P/E 25.1 flat; EPS +7%: 1.07^10 = 1.97x = 7%/yr plus 2% yield (assumptions) = 9%
- Lead central estimate: mid = (4 + 9) / 2 = 6.5; sigma = 5 / 2.563 = 2.0%; central = 6.5 - 2.0^2 / 200 = 6.48%; excess 2.27 pts; stress 70%; tier rank 12.0

## R-18 BlackRock (BUIDL, IBIT) (BLK), Retail, Long

- Band: 5 to 10 percent per year. Method: comps.
- Workstream arithmetic (WS5): P/E 27.9 exit 23; EPS +9%: 1.09^10 x 23/27.9 = 1.95x = 6.9%/yr plus 2% yield = 8.9%
- Lead central estimate: mid = (5 + 10) / 2 = 7.5; sigma = 5 / 2.563 = 2.0%; central = 7.5 - 2.0^2 / 200 = 7.48%; excess 3.27 pts; stress 60%; tier rank 8.0

## R-19 Franklin Resources (BENJI) (BEN), Retail, Long

- Band: 4 to 10 percent per year. Method: comps.
- Workstream arithmetic (WS5): P/E 22.9 exit 18; EPS +5%: 1.05^10 x 18/22.9 = 1.28x = 2.5%/yr plus 4.5% yield = 7% (assumptions)
- Lead central estimate: mid = (4 + 10) / 2 = 7; sigma = 6 / 2.563 = 2.3%; central = 7 - 2.3^2 / 200 = 6.97%; excess 2.76 pts; stress 65%; tier rank 9.0

## R-20 iShares Bitcoin Trust (IBIT), Retail, Long

- Band: -60 to 80 percent per year. Method: base_rate_analog.
- Workstream arithmetic (WS5): BTC 1y -20.4% and YTD -10.0% (CMC 2026-11-04); prior cycle drawdowns near -75% widely reported (unverified here); 0.25x (-13%/yr over 10y) to 3x (+11%/yr) endpoints; wider for 1y
- Lead central estimate: mid = (-60 + 80) / 2 = 10; sigma = 140 / 2.563 = 54.6%; central = 10 - 54.6^2 / 200 = -4.92%; excess -9.13 pts; stress 77%; tier rank 39.0

## R-21 iShares Ethereum Trust (ETHA), Retail, Long

- Band: -65 to 120 percent per year. Method: base_rate_analog.
- Workstream arithmetic (WS5): ETH 1y -25.5% YTD -19.9% (CMC); ETHA 1y -32.6%; 0.2x (-15%/yr 10y) to 4x (+15%/yr 10y)
- Lead central estimate: mid = (-65 + 120) / 2 = 27.5; sigma = 185 / 2.563 = 72.2%; central = 27.5 - 72.2^2 / 200 = 1.45%; excess -2.76 pts; stress 85%; tier rank 21.0

## R-22 Staking Ethereum ETPs (ETHB; Grayscale ETHE (71% staked 2026-03-31)), Retail, Long

- Band: -60 to 130 percent per year. Method: base_rate_analog.
- Workstream arithmetic (WS5): Same ETH price band as R-21 plus staking yield (rate unverified, assumed 2.5 to 3.5%) less 0.25% fee: central +2.5% above ETHA
- Lead central estimate: mid = (-60 + 130) / 2 = 35; sigma = 190 / 2.563 = 74.1%; central = 35 - 74.1^2 / 200 = 7.52%; excess 3.31 pts; stress 85%; tier rank 6.0

## R-23 Spot Solana ETFs (staking) (BSOL (0.20%), GSOL (0.35%), SOEZ 0.19%, FSOL 0.25%), Retail, Long

- Band: -75 to 150 percent per year. Method: base_rate_analog.
- Workstream arithmetic (WS5): SOL 1y -38.8% YTD -25.5% (CMC); BSOL 1y -47.4%; 0.15x (-17%/yr over 10y) to 5x (+17%/yr)
- Lead central estimate: mid = (-75 + 150) / 2 = 37.5; sigma = 225 / 2.563 = 87.8%; central = 37.5 - 87.8^2 / 200 = -1.03%; excess -5.24 pts; stress 85%; tier rank 33.0

## R-24 Spot XRP ETFs (XRPZ 0.19%, TOXR 0.30%, Bitwise 0.34%, GXRP 0.35%, XRPC 0.50%), Retail, Long

- Band: -80 to 150 percent per year. Method: base_rate_analog.
- Workstream arithmetic (WS5): XRP 1.298, 1y -39.9%, YTD -30.9% (CMC); 0.1x (-20%/yr) to 4x (+15%/yr over 10y)
- Lead central estimate: mid = (-80 + 150) / 2 = 35; sigma = 230 / 2.563 = 89.7%; central = 35 - 89.7^2 / 200 = -5.27%; excess -9.48 pts; stress 85%; tier rank 40.0

## R-25 Blockchain equity ETFs (BLOK (0.70%), TKNQ (0.69%, AUM about 1.1M)), Retail, Medium

- Band: -35 to 45 percent per year. Method: base_rate_analog.
- Workstream arithmetic (WS5): BLOK 1y -25.6% (2026-11-04); basket beta ~1.0 to 1.3 vs BTC; 1.2 x -20% = -24% central, +/-1 sigma 30%
- Lead central estimate: mid = (-35 + 45) / 2 = 5; sigma = 80 / 2.563 = 31.2%; central = 5 - 31.2^2 / 200 = 0.13%; excess -4.08 pts; stress 75%; tier rank 28.0

## R-26 Franklin OnChain U.S. Government Money Fund (BENJI) (Benji Investments app (FOBXX)), Retail, Short

- Band: 3.5 to 4.2 percent per year. Method: yield.
- Workstream arithmetic (WS5): 3M CMT 4.21% (H.15 2026-11-02) less assumed 0.2 to 0.7% fee = 3.5 to 4.0%; fund-level yield not fetched
- Lead central estimate: mid = (3.5 + 4.2) / 2 = 3.85; sigma = 0.7 / 2.563 = 0.3%; central = 3.85 - 0.3^2 / 200 = 3.85%; excess -0.36 pts; stress 2%; tier rank 18.0

## R-27 Benchmark: 3M T-bill / SPY (T-bill ladder; SPY), Retail, Short

- Band: 4.0 to 4.4 percent per year. Method: yield.
- Workstream arithmetic (WS5): 3M 4.21%, 1M 4.05%, 1Y 4.38% (H.15 2026-11-02); SPY 1y +13.5%, YTD +13.4% (SPY 767.38); S&P long-run about 10% nominal is commonly cited, not fetched
- Lead central estimate: mid = (4 + 4.4) / 2 = 4.2; sigma = 0.4 / 2.563 = 0.2%; central = 4.2 - 0.2^2 / 200 = 4.20%; excess 0.00 pts; stress 0%; tier rank NA

## R-28 Ether (direct token) (ETH via Coinbase or Kraken), Retail, Long

- Band: -65 to 120 percent per year. Method: base_rate_analog.
- Workstream arithmetic (WS5): ETH 2,404.81; 1y -25.5%; see R-21 arithmetic; add staking if self-staked
- Lead central estimate: mid = (-65 + 120) / 2 = 27.5; sigma = 185 / 2.563 = 72.2%; central = 27.5 - 72.2^2 / 200 = 1.45%; excess -2.76 pts; stress 85%; tier rank 21.0

## R-29 Solana (direct token) (SOL), Retail, Long

- Band: -75 to 150 percent per year. Method: base_rate_analog.
- Workstream arithmetic (WS5): SOL 94.44; 1y -38.8%; see R-23
- Lead central estimate: mid = (-75 + 150) / 2 = 37.5; sigma = 225 / 2.563 = 87.8%; central = 37.5 - 87.8^2 / 200 = -1.03%; excess -5.24 pts; stress 85%; tier rank 33.0

## R-30 Chainlink (direct token) (LINK), Retail, Long

- Band: -70 to 150 percent per year. Method: base_rate_analog.
- Workstream arithmetic (WS5): LINK 11.35; 1y -20.4%; 30d -18.5%; 0.2x to 4x endpoints over 10y
- Lead central estimate: mid = (-70 + 150) / 2 = 40; sigma = 220 / 2.563 = 85.8%; central = 40 - 85.8^2 / 200 = 3.16%; excess -1.05 pts; stress 85%; tier rank 19.0

## R-31 USDC / issuer-paid yield (USDC held at Coinbase, Kraken, wallet), Retail, Short

- Band: 0 to 0 percent per year. Method: yield.
- Workstream arithmetic (WS5): GENIUS Act bars issuer interest or yield to holders (Latham tracker); Circle reserve return 3.54% (Q3 2026) retained by Circle vs 4.21% 3M bill; holder spread is -4.21pp opportunity cost
- Lead central estimate: mid = (0 + 0) / 2 = 0; sigma = 0 / 2.563 = 0.0%; central = 0 - 0.0^2 / 200 = 0.00%; excess -4.21 pts; stress 2%; tier rank 29.0

## R-32 Exchange or platform stablecoin rewards (Third-party rewards programs), Retail, Short

- Band: nan percent per year. Method: yield.
- Workstream arithmetic (WS5): Rate not verified in session; benchmark 4.21% 3M CMT. CLARITY text bans yield paid solely for holding; bona fide activity incentives allowed (CoinDesk 2026-05-01); bill stalled 49-50 cloture 2026-09-15
- Lead central estimate: No band asserted by workstream; not scored.

## R-33 DeFi stablecoin lending (self-custody) (Aave-type protocols), Retail, Short

- Band: nan percent per year. Method: yield.
- Workstream arithmetic (WS5): Rate not verified; any yield must be compared to 4.21% bill; add smart-contract loss probability
- Lead central estimate: No band asserted by workstream; not scored.

## R-34 Event: GENIUS Act effective date (Hold CRCL and PYPL through effective date), Retail, Short

- Band: -15 to 15 percent per year. Method: base_rate_analog.
- Workstream arithmetic (WS5): Regulatory-clarity events usually priced in; +/-15% range = 1 sigma of one-month move for CRCL (30d vol 89.9% / sqrt(12) = 26% monthly; half-weight assumption)
- Lead central estimate: mid = (-15 + 15) / 2 = 0; sigma = 30 / 2.563 = 11.7%; central = 0 - 11.7^2 / 200 = -0.69%; excess -4.90 pts; stress 83%; tier rank 32.0

## R-35 Event: CLARITY Act revival or death (COIN, HOOD, CRCL basket), Retail, Short

- Band: -25 to 30 percent per year. Method: base_rate_analog.
- Workstream arithmetic (WS5): Market-structure bill odds cited at 7 to 9% (defirate, single source); passage +25% on COIN/HOOD analog vs no-action -10%; probability-weighted 0.08 x 30 + 0.92 x -2 = +0.6%
- Lead central estimate: mid = (-25 + 30) / 2 = 2.5; sigma = 55 / 2.563 = 21.5%; central = 2.5 - 21.5^2 / 200 = 0.20%; excess -4.01 pts; stress 92%; tier rank 27.0

## R-36 Event: Fed path and CRCL rate sensitivity (CRCL), Retail, Short

- Band: -30 to 20 percent per year. Method: revenue_pool_share.
- Workstream arithmetic (WS5): 73.9B USDC x 1.00% = 739M gross per year; RLDC margin 42.7% = 316M, about 24% of TTM RLDC 1.29B (3.03B x 42.7%); fed funds held at 3.75 to 4.00%
- Lead central estimate: mid = (-30 + 20) / 2 = -5; sigma = 50 / 2.563 = 19.5%; central = -5 - 19.5^2 / 200 = -6.90%; excess -11.11 pts; stress 83%; tier rank 43.0

## R-37 Event: Gemini earnings (GEMI), Retail, Short

- Band: -50 to 60 percent per year. Method: base_rate_analog.
- Workstream arithmetic (WS5): 1-day move +/-25% typical for microcap with -85% drawdown (assumption); position sized at 1% of sleeve
- Lead central estimate: mid = (-50 + 60) / 2 = 5; sigma = 110 / 2.563 = 42.9%; central = 5 - 42.9^2 / 200 = -4.21%; excess -8.42 pts; stress 80%; tier rank 38.0

## R-38 Event: Kraken IPO filing (COIN, HOOD read-through), Retail, Short

- Band: -10 to 10 percent per year. Method: base_rate_analog.
- Workstream arithmetic (WS5): IPO supply of a direct comp historically weighs on peers; +/-10% assumption
- Lead central estimate: mid = (-10 + 10) / 2 = 0; sigma = 20 / 2.563 = 7.8%; central = 0 - 7.8^2 / 200 = -0.30%; excess -4.51 pts; stress 92%; tier rank 31.0

## M-01 Kraken (Payward) secondary (Forge, Hiive, EquityZen), Mid, Short

- Band: -29 to 64 percent per year. Method: comps.
- Workstream arithmetic (WS5): Entry 9.93B (Forge); exit 6.0B (-40%) over 1.5y = -29%/yr; exit 21B (Series E) = 2.11x over 1.5y = +64%/yr
- Lead central estimate: mid = (-29 + 64) / 2 = 17.5; sigma = 93 / 2.563 = 36.3%; central = 17.5 - 36.3^2 / 200 = 10.92%; excess 6.71 pts; stress 75%; tier rank 2.0

## M-02 Ripple Labs secondary (Forge and brokers), Mid, Medium

- Band: -29 to 77 percent per year. Method: comps.
- Workstream arithmetic (WS5): Entry 15.96B; reversion to 50B tender = 3.13x over 2y = +77%/yr; halving to 8B = -29%/yr
- Lead central estimate: mid = (-29 + 77) / 2 = 24; sigma = 106 / 2.563 = 41.4%; central = 24 - 41.4^2 / 200 = 15.45%; excess 11.24 pts; stress 75%; tier rank 1.0

## M-03 Stripe secondary (Tempo, Bridge parent) (Brokers), Mid, Medium

- Band: -13 to 25 percent per year. Method: comps.
- Workstream arithmetic (WS5): Tender mark 159B (2026-02-24); exit 175B in 2y = +5%/yr; 120B = -13%/yr; 250B = +25%/yr
- Lead central estimate: mid = (-13 + 25) / 2 = 6; sigma = 38 / 2.563 = 14.8%; central = 6 - 14.8^2 / 200 = 4.90%; excess 0.69 pts; stress 75%; tier rank 6.0

## M-04 Anchorage Digital (Direct private round or secondary), Mid, Medium

- Band: -20 to 40 percent per year. Method: comps.
- Workstream arithmetic (WS5): Mark 4.2B (Tether 100M, 2026-02-05); IPO at 6B in 2y = +20%/yr; 2.8B = -18%/yr
- Lead central estimate: mid = (-20 + 40) / 2 = 10; sigma = 60 / 2.563 = 23.4%; central = 10 - 23.4^2 / 200 = 7.26%; excess 3.05 pts; stress 75%; tier rank 4.0

## M-05 Fireblocks secondary (NPM, brokers), Mid, Medium

- Band: -30 to 40 percent per year. Method: comps.
- Workstream arithmetic (WS5): NPM 5.86/share (2026-10-07) and reported Visa 2.5B bid (denied, V News 2026-10) imply 2.5 to 5B vs 8B 2022 round: -69% to -38%
- Lead central estimate: mid = (-30 + 40) / 2 = 5; sigma = 70 / 2.563 = 27.3%; central = 5 - 27.3^2 / 200 = 1.27%; excess -2.94 pts; stress 75%; tier rank 9.0

## M-06 Chainalysis, Paxos, Digital Asset (Canton) private marks (nan), Mid, Medium

- Band: nan percent per year. Method: comps.
- Workstream arithmetic (WS5): Not priced; skipped until a dated source is found
- Lead central estimate: No band asserted by workstream; not scored.

## M-07 Crypto venture funds (a16z crypto, Paradigm, Haun, Pantera (feeder access)), Mid, Long

- Band: -10 to 25 percent per year. Method: base_rate_analog.
- Workstream arithmetic (WS5): Venture net IRR dispersion: median about 10%, top quartile 20 to 25% (general VC base rate, unverified); minimums not found
- Lead central estimate: mid = (-10 + 25) / 2 = 7.5; sigma = 35 / 2.563 = 13.7%; central = 7.5 - 13.7^2 / 200 = 6.57%; excess 2.36 pts; stress 75%; tier rank 5.0

## M-08 Tokenized private credit funds (Apollo ACRED and Hamilton Lane via Securitize), Mid, Medium

- Band: 6 to 9 percent per year. Method: yield.
- Workstream arithmetic (WS5): 4.21% 3M bill + 2.5 to 4.0pp credit spread (assumption) = 6.7 to 8.2% gross, less fees about 0.5 to 1% = 6 to 9%
- Lead central estimate: mid = (6 + 9) / 2 = 7.5; sigma = 3 / 2.563 = 1.2%; central = 7.5 - 1.2^2 / 200 = 7.49%; excess 3.28 pts; stress 30%; tier rank 3.0

## M-09 Tokenized Treasury and MMF (qualified) (BUIDL, OUSG), Mid, Short

- Band: 3.7 to 4.1 percent per year. Method: yield.
- Workstream arithmetic (WS5): 3M 4.21% less fee 0.2 to 0.5% (assumption) = 3.7 to 4.0%
- Lead central estimate: mid = (3.7 + 4.1) / 2 = 3.9; sigma = 0.4 / 2.563 = 0.2%; central = 3.9 - 0.2^2 / 200 = 3.90%; excess -0.31 pts; stress 2%; tier rank 7.0

## M-10 Validator and staking operation (ETH 32-ETH validators), Mid, Medium

- Band: 0 to 4 percent per year. Method: yield.
- Workstream arithmetic (WS5): 32 ETH x 2,404.81 = 76,954 capital per validator; rewards assumed 3% = 2,309/yr gross minus ops and slashing risk; principal moves with ETH price
- Lead central estimate: mid = (0 + 4) / 2 = 2; sigma = 4 / 2.563 = 1.6%; central = 2 - 1.6^2 / 200 = 1.99%; excess -2.22 pts; stress 80%; tier rank 8.0

## M-11 Structured notes on IBIT or BTC (Bank-issued buffered notes (illustrative)), Mid, Short

- Band: -16 to 14 percent per year. Method: base_rate_analog.
- Workstream arithmetic (WS5): Illustrative terms (assumed): 2y, 20% buffer, cap 30% = +14%/yr; IBIT -50% means -30% = -16%/yr
- Lead central estimate: mid = (-16 + 14) / 2 = -1; sigma = 30 / 2.563 = 11.7%; central = -1 - 11.7^2 / 200 = -1.69%; excess -5.90 pts; stress 40%; tier rank 10.0

## M-12 Reg S offshore stablecoin and tokenization funds (Non-US placements), Mid, Medium

- Band: nan percent per year. Method: yield.
- Workstream arithmetic (WS5): Ondo USDY excludes US persons per secondary source; not an option for US investor
- Lead central estimate: No band asserted by workstream; not scored.

## L-01 Issuer build: GENIUS-licensed stablecoin (Own issuer or OCC trust charter), Large, Medium

- Band: -60 to 35 percent per year. Method: revenue_pool_share.
- Workstream arithmetic (WS5): Breakeven supply = 40M opex (assumed) / (3.54% x 42.7%) = 2.65B; at 5B: 177M reserve income x 42.7% = 75.6M RLDC minus 40M = 35.6M on 100M build (assumed) = 36%; at 1B loss 25M
- Lead central estimate: mid = (-60 + 35) / 2 = -12.5; sigma = 95 / 2.563 = 37.1%; central = -12.5 - 37.1^2 / 200 = -19.37%; excess -23.58 pts; stress 80%; tier rank 4.0

## L-02 Issuer buy: acquire a stablecoin issuer (Target list unverified), Large, Medium

- Band: 3 to 15 percent per year. Method: comps.
- Workstream arithmetic (WS5): Buy 5B supply at 24c = 1.2B; RLDC 75.6M minus 25M opex = 50.6M = 4.2%/yr before growth; needs 15% supply growth for double digits
- Lead central estimate: mid = (3 + 15) / 2 = 9; sigma = 12 / 2.563 = 4.7%; central = 9 - 4.7^2 / 200 = 8.89%; excess 4.68 pts; stress 80%; tier rank 1.0

## L-03 Anchor position in tokenized fund launch (Seed 50 to 100M in new tokenized MMF), Large, Short

- Band: 3.5 to 4.2 percent per year. Method: yield.
- Workstream arithmetic (WS5): 4.21% 3M less 0.2 to 0.7% fee; plus negotiated fee rebate
- Lead central estimate: mid = (3.5 + 4.2) / 2 = 3.85; sigma = 0.7 / 2.563 = 0.3%; central = 3.85 - 0.3^2 / 200 = 3.85%; excess -0.36 pts; stress 2%; tier rank 2.0

## L-04 Stake in a settlement consortium (Canton, DTCC-linked or bank consortia), Large, Long

- Band: -100 to 30 percent per year. Method: base_rate_analog.
- Workstream arithmetic (WS5): Base rate from plan.md G4 failures: most stakes written off (-100%); success case 3x over 10y = +12%/yr; blend 25% success x 3x = 0.75x = -3%/yr
- Lead central estimate: mid = (-100 + 30) / 2 = -35; sigma = 130 / 2.563 = 50.7%; central = -35 - 50.7^2 / 200 = -47.86%; excess -52.07 pts; stress 80%; tier rank 5.0

## L-05 Bank partnership for tokenized deposits (Kinexys or Citi Token Services client), Large, Medium

- Band: nan percent per year. Method: base_rate_analog.
- Workstream arithmetic (WS5): Return is cost saving; no verified fee data
- Lead central estimate: No band asserted by workstream; not scored.

## L-06 Infrastructure build versus buy (Custody (Anchorage 4.2B, Fireblocks 2.5 to 5B)), Large, Medium

- Band: nan percent per year. Method: comps.
- Workstream arithmetic (WS5): Fireblocks implied 2.5 to 5.0B vs 8B (-38 to -69%); buy before the multiple recovers
- Lead central estimate: No band asserted by workstream; not scored.

## L-07 Sovereign engagement (Treasury and central bank partnerships), Large, Long

- Band: nan percent per year. Method: base_rate_analog.
- Workstream arithmetic (WS5): Return not computed; depends on mBridge and Agora outcomes
- Lead central estimate: No band asserted by workstream; not scored.

## L-08 Operating requirements to participate (Licenses, custody, compliance team), Large, Medium

- Band: nan percent per year. Method: revenue_pool_share.
- Workstream arithmetic (WS5): Opex assumed 40M per year used in L-01; no sourced staffing data
- Lead central estimate: No band asserted by workstream; not scored.

## L-09 Block holding in public equities (CRCL, COIN) (Institutional accounts), Large, Short

- Band: -10 to 15 percent per year. Method: comps.
- Workstream arithmetic (WS5): Block of 1B in COIN is 2.5% of 40.21B mcap; slippage assumed 2 to 4%
- Lead central estimate: mid = (-10 + 15) / 2 = 2.5; sigma = 25 / 2.563 = 9.8%; central = 2.5 - 9.8^2 / 200 = 2.02%; excess -2.19 pts; stress 92%; tier rank 3.0

## L-10 Arc network validator or ARC token allocation (Arc (Circle L1)), Large, Medium

- Band: nan percent per year. Method: base_rate_analog.
- Workstream arithmetic (WS5): Token lockup terms not found; no return computed
- Lead central estimate: No band asserted by workstream; not scored.

## A-01 Common stock (V), Retail, Long

- Band: 6 to 12 percent per year. Method: comps.
- Workstream arithmetic (WS8): Fiscal 2026 net revenue $46B up 15% (Visa 8-K 2026-10-27). Assume revenue growth fades to 10 to 12% a year, EPS growth about 12 to 14% with buybacks, multiple flat: low 6 = 10% growth minus 4 points multiple compression; high 12 = 13% EPS growth minus 1 point. Agentic adds 0 in the base case.
- Lead central estimate: mid = (6 + 12) / 2 = 9; sigma = 6 / 2.563 = 2.3%; central = 9 - 2.3^2 / 200 = 8.97%; excess 4.76 pts; stress 50%; tier rank 1.0

## A-02 Common stock (MA), Retail, Long

- Band: 6 to 12 percent per year. Method: comps.
- Workstream arithmetic (WS8): Q3 2026 net revenue growth 14% (consistent across secondary summaries, 2026-10-29); assume 11 to 13% revenue growth, EPS 12 to 14%, flat multiple, less 0 to 6 points for multiple compression: band 6 to 12. Revenue dollar figure conflicts across sources and is not used.
- Lead central estimate: mid = (6 + 12) / 2 = 9; sigma = 6 / 2.563 = 2.3%; central = 9 - 2.3^2 / 200 = 8.97%; excess 4.76 pts; stress 60%; tier rank 1.0

## A-03 Common stock (NET), Retail, Medium

- Band: -35 to 30 percent per year. Method: base_rate_analog.
- Workstream arithmetic (WS8): High-multiple infrastructure equity: 52-week range $158.83 to $370.35 implies roughly -40% to +40% annual swings around the $264.63 print (MarketBeat). Band is the 52-week range relative to current: low = 158.83/264.63 - 1 = -40%, rounded to -35; high = 370.35/264.63 - 1 = +40%, haircut to 30 for mean reversion. Not a forecast of agentic revenue.
- Lead central estimate: mid = (-35 + 30) / 2 = -2.5; sigma = 65 / 2.563 = 25.4%; central = -2.5 - 25.4^2 / 200 = -5.72%; excess -9.93 pts; stress 70%; tier rank 41.0

## A-04 Common stock (COIN), Retail, Medium

- Band: -40 to 35 percent per year. Method: base_rate_analog.
- Workstream arithmetic (WS8): Q3 2026 total revenue $1.22B down year over year, trading revenue down 44% (secondary), stablecoin revenue $306.9M. Equity behaves as crypto beta; band set by assumed drawdown tolerance and prior-cycle swings: low -40 is the sleeve max drawdown; high 35 assumes crypto trading recovers. No agentic revenue assumed.
- Lead central estimate: mid = (-40 + 35) / 2 = -2.5; sigma = 75 / 2.563 = 29.3%; central = -2.5 - 29.3^2 / 200 = -6.78%; excess -10.99 pts; stress 92%; tier rank 42.0

## A-05 Common stock (PYPL), Retail, Medium

- Band: nan percent per year. Method: reverse_dcf.
- Workstream arithmetic (WS8): Not computed: no price or earnings retrieved this session (search budget exhausted). Do not use until WS5 supplies a reverse DCF.
- Lead central estimate: No band asserted by workstream; not scored.

## A-06 Secondary shares or tender in Stripe (private; Tempo parent incubator) (Private route via accredited secondary platform or fund), Mid, Medium

- Band: nan percent per year. Method: comps.
- Workstream arithmetic (WS8): Not computed: Stripe valuation and tender price not retrieved. Tempo valuation $5B (Oct 2025 Series A $500M) is the only dated anchor.
- Lead central estimate: No band asserted by workstream; not scored.

## A-07 Venture fund or direct round in agent identity and payment startups (Skyfire, Nevermined class) (Private route), Large, Long

- Band: nan percent per year. Method: base_rate_analog.
- Workstream arithmetic (WS8): Venture base rate: most seed-stage infrastructure startups return zero; no dated fund data retrieved, so no band is asserted.
- Lead central estimate: No band asserted by workstream; not scored.

## A-08 Avoid: x402 ecosystem tokens and PING-type tokens (Not recommended), Retail, Short

- Band: -100 to 0 percent per year. Method: base_rate_analog.
- Workstream arithmetic (WS8): Observed: Oct 2026 5.1M tx and $274k value (Fireblocks via secondary) versus 196M cumulative; $274k / 5.1M = $0.054 per transaction. Zero-revenue token base rate treated as total loss at the low end.
- Lead central estimate: mid = (-100 + 0) / 2 = -50; sigma = 100 / 2.563 = 39.0%; central = -50 - 39.0^2 / 200 = -57.61%; excess -61.82 pts; stress 85%; tier rank 47.0

## G-01 NYSE-listed ADS (Cayman; Brazil ops) (NU), Retail, Medium

- Band: -20 to 25 percent per year. Method: comps.
- Workstream arithmetic (WS9): Fwd EPS = 12.03/12.31 = $0.977. High: EPS +25% at constant 12.31x gives +25%. Low: multiple to 9x (EWZ fwd 8.14x to 9x range) and EPS +10%: 9*0.977*1.10=$9.67, -19.6%. EPS growth rates are my assumptions
- Lead central estimate: mid = (-20 + 25) / 2 = 2.5; sigma = 45 / 2.563 = 17.6%; central = 2.5 - 17.6^2 / 200 = 0.96%; excess -3.25 pts; stress 60%; tier rank 24.0

## G-02 NASDAQ-listed common stock (MELI), Retail, Medium

- Band: -18 to 25 percent per year. Method: comps.
- Workstream arithmetic (WS9): Fwd EPS = 1746.38/42.26 = $41.32. High: EPS +25% at constant 42.26x gives +25%. Low: multiple to 30x and EPS +15%: 30*41.32*1.15=$1425, -18.4%. Assumptions mine
- Lead central estimate: mid = (-18 + 25) / 2 = 3.5; sigma = 43 / 2.563 = 16.8%; central = 3.5 - 16.8^2 / 200 = 2.09%; excess -2.12 pts; stress 60%; tier rank 20.0

## G-03 NASDAQ-listed ADS (Kazakhstan; Turkey via Hepsiburada) (KSPI), Retail, Medium

- Band: -26 to 47 percent per year. Method: comps.
- Workstream arithmetic (WS9): Fwd EPS = 95.77/6.75 = $14.19. High: re-rate to 9x with EPS +10%: 9*14.19*1.10=$140.5, +46.7%. Low: 5x on flat EPS: $70.9, -25.9%
- Lead central estimate: mid = (-26 + 47) / 2 = 10.5; sigma = 73 / 2.563 = 28.5%; central = 10.5 - 28.5^2 / 200 = 6.44%; excess 2.23 pts; stress 60%; tier rank 14.0

## G-04 NYSE Arca ETF (iShares MSCI South Korea) (EWY), Retail, Medium

- Band: -27 to 15 percent per year. Method: base_rate_analog.
- Workstream arithmetic (WS9): Low: give back half of the 1y return of 54.63% = -27.3%. High: 15% earnings growth at constant P/E 7.61 (my assumption)
- Lead central estimate: mid = (-27 + 15) / 2 = -6; sigma = 42 / 2.563 = 16.4%; central = -6 - 16.4^2 / 200 = -7.34%; excess -11.55 pts; stress 60%; tier rank 44.0

## G-05 NYSE Arca ETF (iShares MSCI Brazil) (EWZ), Retail, Medium

- Band: -23 to 23 percent per year. Method: base_rate_analog.
- Workstream arithmetic (WS9): High: fwd P/E 8.14x to 10x = +22.8%. Low: P/E to 7x (-14.0%) plus real -10% = about -23%
- Lead central estimate: mid = (-23 + 23) / 2 = 0; sigma = 46 / 2.563 = 17.9%; central = 0 - 17.9^2 / 200 = -1.61%; excess -5.82 pts; stress 60%; tier rank 35.0

## G-06 NYSE Arca ETF (Global X MSCI Argentina) (ARGT), Retail, Medium

- Band: -25 to 29 percent per year. Method: comps.
- Workstream arithmetic (WS9): Low: fwd P/E 9.32 to 7 = -24.9%. High: to 12 = +28.8%
- Lead central estimate: mid = (-25 + 29) / 2 = 2; sigma = 54 / 2.563 = 21.1%; central = 2 - 21.1^2 / 200 = -0.22%; excess -4.43 pts; stress 60%; tier rank 30.0

## G-07 NYSE Arca ETF (iShares MSCI India) (INDA), Retail, Long

- Band: -16 to 12 percent per year. Method: comps.
- Workstream arithmetic (WS9): Low: P/E 20.20 to 17 = -15.8%. High: 12% earnings growth at constant P/E (assumption)
- Lead central estimate: mid = (-16 + 12) / 2 = -2; sigma = 28 / 2.563 = 10.9%; central = -2 - 10.9^2 / 200 = -2.60%; excess -6.81 pts; stress 60%; tier rank 36.0
