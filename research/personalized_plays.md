# Personalized plays: illustrative allocation for the Section 0 investor

Date: 2026-11-04. This is an illustrative allocation built from the research matrix, not advice. Verify prices, product availability and tax treatment before acting, and consult a licensed advisor and a CPA.

## Inputs (mandate Section 0) and how they bind

| Parameter | Value | How it constrains the allocation |
|---|---|---|
| Jurisdiction | US, California | California taxes all gains as ordinary income (top 13.3%). Treasury interest is exempt from California tax. |
| Capital | $50,000 cash | All positions have daily liquidity. Stocks are bought in whole or fractional shares. |
| Accredited | No | Retail tier only. Mid and Large plays are excluded (assumption P0-4). |
| Max drawdown | 40% on this sleeve | Sized so the perfect-correlation stress loss is about 26%, leaving a 14-point buffer |
| Horizon | 10 years (2036) | Long-horizon plays are allowed. Locked vehicles are excluded (P0-9). |
| Account | Taxable cash account, no margin | No leverage, no options. Tax placement is all taxable, so holding period and lot selection carry the tax planning. |
| Monitoring | 1 hour per week | Routine below fits in 60 minutes |

## Allocation

| # | Position | Play ID | Weight | USD | Stress drawdown | Role | Entry condition |
|---|---|---|---|---|---|---|---|
| 1 | US T-bills, 3 to 12 month ladder (TreasuryDirect or broker) | R-27 | 30% | $15,000 | 0% | Benchmark yield of 4.21% (H.15, 2026-11-02), exempt from California tax | Buy now |
| 2 | Franklin OnChain US Government Money Fund (BENJI app, FOBXX) | R-26 | 5% | $2,500 | about 2% | Tokenized cash: a learning position on the live rail | Confirm in the Benji app that California residents can enroll and the minimum is about $20 (YCharts; not confirmed from a primary source). If not available, add to item 1. |
| 3 | Visa (V) | R-09, A-01 | 10% | $5,000 | 30% | Toll collector on card, stablecoin settlement ($25B run rate, Visa call 2026-10-27) and agent checkout | 3 equal monthly tranches |
| 4 | Mastercard (MA) | R-10, A-02 | 10% | $5,000 | 30% | Same as Visa, plus its stablecoin acquisition | 3 equal monthly tranches |
| 5 | BNY (BK) | R-12 | 7.5% | $3,750 | 40% | Reserve custody and tokenized fund servicing; forward P/E 14.9 | 3 equal monthly tranches |
| 6 | Intercontinental Exchange (ICE) | R-16 | 7.5% | $3,750 | 40% | Exchange and clearing incumbent with tokenization options | 3 equal monthly tranches |
| 7 | BlackRock (BLK) | R-18 | 5% | $2,500 | 40% | Largest tokenized-fund issuer (BUIDL) plus the IBIT franchise | 3 equal monthly tranches |
| 8 | Circle (CRCL) | R-01 | 5% | $2,500 | 83% | Pure-play issuer: an option on adoption and a bet on rates | Half now. Half after 2027-01-18 (GENIUS effective), only if USDC supply is at least $70B and distribution costs are at most 65% of reserve income in the latest 10-Q. |
| 9 | iShares Bitcoin Trust (IBIT) | R-20 | 6% | $3,000 | 77% | A capped option outside the thesis: a monetary asset, not adoption | Half now. Half only if BTC closes at or below $63,000 (-50% from $126,080). |
| 10 | iShares Ethereum Trust (ETHA) | R-21 | 4% | $2,000 | 85% | A capped option on the main settlement chain for stablecoins (47% of supply) and distributed tokenized assets on Ethereum ($15.1B, RWA.xyz networks page, 2026-11-04) | Half now; half on ETH at or below $1,800 |
| 11 | Reserve tranche, held in T-bills | R-27 | 10% | $5,000 | 0% | Dry powder for the trigger-based entries above, or a catalyst add (see rule R3) | Deploy only on a trigger |
| | **Total** | | **100%** | **$50,000** | **26.3%** (weighted, perfect correlation) | | |

**Expected-return arithmetic** (`return_methods.md`; assumptions P3-1 to P3-6):

| Measure | Value | Basis |
|---|---|---|
| Band-midpoint return | 7.2% a year | Optimistic |
| Scenario-weighted return | 2.9% a year | Conservative. Token ETP bands with deep lows dominate it. |
| After-tax, scenario-weighted | about 2.2% a year | Federal 24% ordinary and 15% long-term gains, plus California 9.3% on everything. T-bill interest is taxed federally only. |
| After-tax, T-bills alone | about 3.2% a year | 4.21% x (1 - 0.24) |

- Inference: On scenario weighting, the theme sleeve is not expected to beat T-bills after tax. On midpoints it beats them by about 2 to 3 points. The real case for the sleeve is the incumbent equities' core franchises plus a small, capped Bull option. [Moderate]
- Inference: A version with no tokens and no CRCL is equally defensible: items 3 to 7 (40%) plus 60% T-bills and BENJI. It has a 14.0% stress loss, a 5.7% midpoint return and a 5.3% scenario-weighted return. Its midpoint is lower but its scenario-weighted return is higher, because it drops the bands with deep lows. Choose it if you weight the conservative method more. [Moderate]

## Account placement and tax handling (all taxable)

| Holding | Federal character | California | Action |
|---|---|---|---|
| T-bills | Ordinary interest | Exempt | Hold to maturity; roll the ladder |
| BENJI (FOBXX) | Ordinary dividends | Exempt share pass-through if the fund qualifies | Keep the year-end fund letter for the California exemption |
| V, MA, BK, ICE, BLK, CRCL | Qualified dividends and long-term capital gains after 1 year | Ordinary income | Elect specific-identification lot method at the broker. Hold over 1 year for the federal rate. |
| IBIT, ETHA | Capital gain on shares; grantor trust | Ordinary income | Wash sale likely applies to ETP shares `[Verify with CPA]`. Avoid the staking ETP variant in taxable (ordinary income each year). |

- Fact: Direct tokens are outside Sec. 1091 today (WS7), but H.R. 10357 would change that. The ETP route was chosen over direct custody for four reasons: broker 1099-B reporting, no exchange key risk (Binance breach of about $6.3B, 2026-10-29), estate step-up simplicity, and Section 0's 1-hour weekly budget. [Moderate]

## Rebalancing rule

| Rule | Trigger | Action |
|---|---|---|
| R1 | Annual date (first trading day of November) | Return to target weights. Sell lots held over 1 year first. |
| R2 | Any position drifts by 5 or more points from target | Rebalance that position only |
| R3 | IBIT, ETHA and CRCL combined exceed 20% | Trim to 15% |
| R4 | Sleeve drawdown from peak reaches 25% | Freeze additions. Review every kill criterion. |
| R5 | Sleeve drawdown reaches 35% | Move IBIT, ETHA and CRCL to T-bills, protecting the 40% limit |

## Kill criteria (from `plays.csv`, lead-condensed)

| Position | Exit if |
|---|---|
| CRCL | USDC supply falls below $55B for two quarters, or distribution costs exceed 70% of reserve income, or a final rule bars affiliate yield and Circle guides revenue down 20% |
| V, MA | Lead-proposed: interchange caps on credit cards enacted (e.g., a Credit Card Competition Act style law), or payments volume growth below 3% for two quarters |
| BK | Loss of a top-two stablecoin reserve custody mandate, or a material custody incident |
| IBIT, ETHA | Exit on a thesis break, not on price: a spot ETP custodian incident, or a protocol failure (for example, a quantum-forced migration without a plan) |
| BENJI | Fund breaks $1.00 NAV, or there is a transfer-agent or ledger incident |

## Weekly monitoring routine (60 minutes)

| Time | Task | Source |
|---|---|---|
| 10 min | Check the dashboard: stablecoin supply, tokenized Treasuries, BTC and ETH drawdown, sleeve drawdown | stablecoins.llama.fi; app.rwa.xyz/treasuries; broker |
| 10 min | Check entry triggers (CRCL second half, IBIT and ETHA second halves) and rules R3 to R5 | This file |
| 20 min | Read one primary-source item from the catalyst calendar (Federal Register docket, FOMC statement, earnings release) | REPORT.md Section 12 |
| 20 min | Quarterly weeks only: read V, MA, BK, ICE, BLK and CRCL results against kill criteria. Other weeks: spare. | Company IR pages |

> Risk flags: exchange counterparty risk (avoid holding cash or stablecoins on exchanges for yield); correlated crypto drawdowns (prior cycles -77% to -94%); policy reversal risk after the 2028 election; concentration in large-cap US financials. This allocation is illustrative and assumes the $50,000 is not the investor's emergency fund.

This is an illustrative allocation, not individualized financial, legal, or tax advice; verify current facts and consult licensed advisors before acting.
