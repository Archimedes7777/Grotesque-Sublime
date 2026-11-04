# Personalized plays: illustrative allocation for the Section 0 investor

Date: 2026-11-04. Version 2.1, revised after the red teams and the second-pass review (changelog C6, D9 to D12). This is an illustrative allocation built from the research matrix, not advice. Verify prices, product availability and tax treatment before acting, and consult a licensed advisor and a CPA.

## Inputs (mandate Section 0) and how they bind

| Parameter | Value | How it constrains the allocation |
|---|---|---|
| Jurisdiction | US, California | California taxes all gains as ordinary income (top 13.3%). Treasury interest is exempt from California tax. |
| Capital | $50,000 cash | All positions have daily liquidity |
| Accredited | No | Retail tier only (P0-4) |
| Max drawdown | 40% on this sleeve | Sized on the sum of weight x stress drawdown, assuming correlation near 1 in stress |
| Horizon | 10 years (2036) | Long-horizon equities allowed; locked vehicles excluded |
| Account | Taxable cash account, no margin | All taxable. Holding period and lot selection carry the tax planning. |
| Monitoring | 1 hour per week | Routine below fits in 60 minutes |

## Recommended: Option A, incumbent core

| # | Position | Play ID | Weight | USD | Stress | Central return | Entry |
|---|---|---|---|---|---|---|---|
| 1 | US T-bills, 3 to 12 month ladder | R-27 | 45% | $22,500 | 0% | 4.21% | Buy now |
| 2 | Reserve tranche in T-bills | R-27 | 10% | $5,000 | 0% | 4.21% | Deploy only on the triggers below |
| 3 | Franklin BENJI (FOBXX) | R-26 | 5% | $2,500 | 2% | 3.85% | Confirm California eligibility and the minimum in the Benji app; otherwise add to item 1 |
| 4 | Visa (V) | R-09 | 10% | $5,000 | 50% | 8.50% | 3 equal monthly tranches |
| 5 | Mastercard (MA) | R-10 | 10% | $5,000 | 60% | 8.50% | 3 equal monthly tranches |
| 6 | BNY (BK) | R-12 | 7.5% | $3,750 | 65% | 8.00% | 3 equal monthly tranches |
| 7 | BlackRock (BLK) | R-18 | 5% | $2,500 | 60% | 7.50% | 3 equal monthly tranches |
| 8 | Intercontinental Exchange (ICE) | R-16 | 7.5% | $3,750 | 80% | 7.00% | 3 equal monthly tranches |
| | **Total** | | **100%** | **$50,000** | **25.0%** | **5.71%** | |

**Reserve triggers** (deploy $2,500 per trigger, at most twice):
- (a) Any of V, MA, BK falls 25% from its purchase price with its kill criterion intact.
- (b) USD stablecoin supply exceeds $350B (DefiLlama) and tokenized Treasuries exceed $30B (RWA.xyz). In that case, fund the Option B options.

## Alternative: Option B, core plus capped options

Option B moves 10 points from item 1 into four options:

| Position | Play ID | Weight | USD | Stress | Central return | Role |
|---|---|---|---|---|---|---|
| Circle (CRCL) | R-01 | 2.5% | $1,250 | 83% | 2.41% | Issuer float leverage (panel-weighted scenarios) |
| Coinbase (COIN) | A-04 (lower of R-02, A-04) | 2.5% | $1,250 | 92% | -6.78% | Distributor; Base-token risk |
| iShares Bitcoin Trust (IBIT) | R-20 | 2.5% | $1,250 | 77% | -4.92% | Monetary-asset option, not adoption |
| iShares Ethereum Trust (ETHA) | R-21 | 2.5% | $1,250 | 85% | 1.45% | Settlement chain for 47% of stablecoins |

| Measure | Option A | Option B |
|---|---|---|
| Stress loss | 25.0% | 33.4% |
| Central return | 5.71% | 5.09% |

- Inference: Option B lowers the central estimate and raises stress. Choose it only if you want exposure to the Bull tail (8% in 2030, 11% in 2035) and accept that cost. One central per ticker is used, taking the lower of duplicate rows. [Moderate]

**After-tax arithmetic**

Assumption P3-6: federal 24% ordinary and 15% long-term gains, plus California 9.3% on everything. Treasury interest is federally taxed only.

| Measure | Value |
|---|---|
| Option A, after tax | about 0.60 x (4.2 x 0.76) + 0.40 x (8.0 x 0.757) = about 4.3% a year |
| T-bills alone, after tax | 4.21 x 0.76 = 3.2% a year |
| Real return | About +0.6 points for Option A and about -0.5 points for T-bills alone. This is ex post, against trailing headline CPI of 3.7%, and assumes today's bill rate persists. A 10-year breakeven inflation rate was not retrieved; check FRED T10YIE. |
| Second benchmark | The 10-year Treasury at 4.91% (H.15, 2026-11-02) suits the 10-year horizon. Option A's central return beats it by about 0.8 points pre-tax. |

- Inference: The excess over T-bills comes mainly from the incumbents' core franchises, not from the theme. That is the honest finding of this research. [Moderate]

## Account placement and tax handling (all taxable)

| Holding | Federal character | California | Action |
|---|---|---|---|
| T-bills | Ordinary interest | Exempt | Hold to maturity; roll the ladder |
| BENJI (FOBXX) | Ordinary dividends | Exempt portion if the fund qualifies | Keep the year-end fund letter |
| V, MA, BK, BLK, ICE (and CRCL, COIN in Option B) | Qualified dividends; long-term gains after 1 year | Ordinary income | Elect specific-identification lots; hold over 1 year for the federal rate |
| IBIT, ETHA (Option B) | Capital gain on grantor-trust shares | Ordinary income | Wash sale likely applies to ETP shares `[Verify with CPA]`. Avoid staking variants in taxable. |

## Rebalancing rule

| Rule | Trigger | Action |
|---|---|---|
| R1 | Annual (first trading day of November) | Return to target weights, selling lots held over 1 year first |
| R2 | Any position 5 or more points from target | Rebalance that position |
| R3 | Equity plus option weight exceeds its target by 5 points (45% for A, 55% for B) | Trim to target |
| R4 | Sleeve drawdown reaches 25% | Freeze additions; review kill criteria |
| R5 | Sleeve drawdown reaches 35% | Sell Option B positions to T-bills first, then trim equities to protect the 40% limit |

## Kill criteria

| Position | Exit if |
|---|---|
| V, MA | A credit card routing mandate (Credit Card Competition Act) or a direct interchange cap enacted, or payments volume growth below 3% for two quarters |
| BK | Loss of a top-two stablecoin reserve custody mandate, or a material custody incident |
| BLK, ICE | Tokenized-fund or venue franchise lost to a new entrant, shown by two consecutive quarters of share loss in their disclosures |
| CRCL (B) | USDC below $55B for two quarters, or distribution costs above 70% of reserve income |
| COIN (B) | A Base token routes sequencer revenue away from Coinbase, or stablecoin revenue falls 30% year on year |
| IBIT, ETHA (B) | Custodian incident or protocol failure. Price alone is not a kill criterion. |
| BENJI | NAV below $1.00, or a transfer-agent or ledger incident |

## Weekly monitoring routine (60 minutes)

| Time | Task | Source |
|---|---|---|
| 10 min | Check the dashboard: stablecoin supply, tokenized Treasuries, sleeve drawdown, Fed and CPI | stablecoins.llama.fi; app.rwa.xyz/treasuries; broker |
| 10 min | Check reserve triggers and rules R3 to R5 | This file |
| 20 min | Read one primary-source item from the catalyst calendar | REPORT.md Section 12 |
| 20 min | In earnings weeks, read the holdings' results against kill criteria; otherwise spare | Company IR pages |

> **Risk flags:**
> - Correlated drawdowns: in 2008 to 2009 the incumbents in this list fell 50% to 80% [Unverified history].
> - Rates: higher rates compress the 35x multiples of V and MA.
> - Exchange counterparty risk: do not hold cash or stablecoins on exchanges for yield.
> - Policy reversal risk after 2028.
> - This allocation assumes the $50,000 is not the investor's emergency fund.

This is an illustrative allocation, not individualized financial, legal, or tax advice; verify current facts and consult licensed advisors before acting.
