# WS7: Tax treatment by vehicle and tier (US federal plus California)

Date: 2026-11-04. Not individualized tax advice. Search budget: 13 searches ran, then a shared limit blocked further searches; several items are therefore `[Unverified]` and listed in Gaps. Secondary sources (law-firm and accounting alerts) are used where irs.gov text was unreadable.

## Summary

Fact: Direct crypto is still property. The wash sale rule (Sec 1091) still reaches only "stock or securities" and its text has no digital asset language (Cornell US Code, read 2026-11-04). H.R. 10357 (Digital Asset Tax Certainty Act) passed Ways and Means 38 to 5 on 2026-09-16 and would apply wash sale rules to digital assets, but it has no floor vote and is not law. [High] `[Verify with CPA]`

Fact: Form 1099-DA reports gross proceeds for sales after 2025, and basis only for covered units bought after 2025 and held in the same custodial account (IRS instructions, reviewed 2026-04-30). Staking rewards are not on the form. [High]

Fact: Rev. Proc. 2025-31 (2025-11-10) was superseded on 2026-10-06 by Rev. Proc. 2026-20; staking inside a qualifying single-asset grantor trust ETP is allowed, with net rewards distributed or sold within 60 days after quarter end. Holders still owe ordinary income on rewards (inference). [Moderate] `[Verify with CPA]`

Fact: QSBS for stock issued after 2025-07-04 is 50, 75, 100 percent at 3, 4, 5 years, with a $15M cap and $75M asset test (Sec 1202 text). California does not conform. [High federal, Moderate CA]

Recommendation for the personal case ($50k, taxable cash account, Retail tier): prefer spot ETPs or direct tokens held over one year, record specific identification, avoid staking and yield products in taxable, and do not rely on wash sale loopholes surviving past a lame-duck bill. [Moderate]

## Key numbers

| Metric | Value | Date | Source | Confidence |
|---|---|---|---|---|
| 2026 LTCG 0% ceiling, single | $49,450 | 2025-10 (Rev. Proc. 2025-32) | IRS IRB 2025-45 sec 4.03 | High |
| 2026 LTCG 15% ceiling, single | $545,500 | same | same | High |
| 2026 LTCG 0% and 15% ceilings, MFJ | $98,900 and $613,700 | same | same | High |
| 2026 estate basic exclusion | $15,000,000 | 2025-10 | IRS newsroom, 2026 inflation adjustments | High |
| QSBS cap, stock issued after 2025-07-04 | $15M or 10x basis; indexed after 2026 | 2026-11-04 | Cornell, 26 USC 1202(b) | High |
| QSBS asset test | $75M | 2026-11-04 | Cornell, 26 USC 1202(d) | High |
| Form 1099-DA stablecoin optional aggregate | $10,000 gross proceeds | 2026-04-30 | IRS i1099da | Moderate |
| Staking ETP reward distribution deadline | 60 days after quarter end | 2026-10-06 | McDermott on Rev. Proc. 2026-20 | Moderate |
| H.R. 10357 committee vote | 38 to 5 | 2026-09-16 | House Ways and Means release | High |
| CA top rate on capital gains | 13.3% as ordinary income | 2026-11-04 | secondary (FBT Gibbons, TSCPA) | Moderate |
| CA DFAL licensing operative | 2026-07-01 | 2026-07-01 | MoFo, others (secondary) | Moderate |
| Rev. Proc. 2026-20 effective | Tax years ending on or after 2026-10-06; 6-month transition | 2026-10-06 | KPMG, McDermott | Moderate |

## Body

### 1. Federal rules verified today

| Label | Item | Finding | Source and date | Conf |
|---|---|---|---|---|
| Fact | Property status | Digital assets are property; sale for dollars gives capital gain or loss; holding period starts day after acquisition | IRS FAQ, reviewed 2026-06-29, https://www.irs.gov/individuals/international-taxpayers/frequently-asked-questions-on-digital-asset-transactions | High |
| Fact | Specific ID | Unhosted wallets: identify units by transaction date. Broker custody after 2025: use broker identifiers or a standing order in place beforehand. Otherwise first-in first-out | Same IRS FAQ | High |
| Fact | Rev. Proc. 2024-28 | One-time allocation of unused basis to wallets holding units on 2025-01-01. Window closed. Wallet-by-wallet tracking is the going rule | TaxAdviser 2024-10 and RSM 2024 (secondary) | Moderate |
| Fact | Wash sale | Sec 1091 covers "stock or securities" and options on them. No digital asset text | https://www.law.cornell.edu/uscode/text/26/1091 | High |
| Fact | Staking income | Income at fair market value when dominion and control is gained (Rev. Rul. 2023-14). Paschall, T.C. Memo. 2026-46, held Cardano rewards taxable in 2021 on Sec 61 grounds without relying on the ruling | TaxAdviser 2026-09-30 | Moderate |
| Fact | Jarrett | IRS refunded 2019 Tezos tax without conceding. No merits decision found | TaxAdviser 2026-09-30 and secondary | Low |
| Fact | Airdrops and forks | Income when taxpayer has dominion and control (Rev. Rul. 2019-24). Hard fork without new asset is not income | IRS FAQ 2026-06-29 | High |
| Fact | Form 1099-DA | Proceeds for sales after 2025; basis for covered units after 2025. Noncovered units: broker may add voluntarily (box 9). Staking, lending, liquidity provider transactions exempt under Notice 2024-57 | IRS i1099da, 2026-04-30 | High |
| Fact | Backup withholding | No backup withholding for 2025 and 2026 sales; 2027 relief for TIN-matched payees (Notice 2025-33). W-9 collection from 2026-01-01 | RSM, KPMG, 2025-06 (secondary) | Moderate |
| Fact | Sec 1256 | Regulated futures contracts and nonequity options get 60/40 and year-end mark-to-market. Text has no digital asset language | https://www.law.cornell.edu/uscode/text/26/1256 | High |
| Fact | Sec 408(m) | Collectible list is art, rugs, antiques, metals, gems, stamps, coins, alcohol, other tangible property the Treasury specifies. No digital asset mention | https://www.law.cornell.edu/uscode/text/26/408 | High |
| Inference | Crypto in IRAs | Not a listed collectible and intangible, so not a deemed distribution under Sec 408(m). Prohibited transaction rules still bind self-directed custody | Analysis of text above | Moderate |
| Fact | OZ 2.0 | For investments after 2026-12-31: deferral to 5 years, 10% basis step-up (30% rural), basis equals FMV after 30-year hold. Old 5/7-year step-ups end with 2026-12-31 inclusion | https://www.law.cornell.edu/uscode/text/26/1400Z-2 | Moderate |
| Fact | Estate | 2026 basic exclusion $15,000,000 | IRS newsroom (OBBBA adjustments) | High |
| Fact | Step-up | Sec 1014 step-up applies to inherited property including crypto | Training knowledge, not fetched | `[Unverified]` |

### 2. Staking ETPs: Rev. Proc. 2025-31 to 2026-20

| Label | Point | Detail | Source | Conf |
|---|---|---|---|---|
| Fact | Original | Rev. Proc. 2025-31 issued 2025-11-10: 14 conditions, trust must be on a national exchange and follow SEC staking rules, custodians direct staking | Ropes and Gray 2025-11; RSM | Moderate |
| Fact | Replacement | Rev. Proc. 2026-20 issued 2026-10-06 supersedes it. Changes: multiple custodians allowed, SEC disclosure must be in an effective registration statement, slashing indemnity narrowed to provider-controllable events, rewards (new units or fees) distributed in kind or sold within 60 days after quarter end | McDermott, 2026-10 (secondary); KPMG 2026-10-06 | Moderate |
| Fact | Timing | Effective for tax years ending on or after 2026-10-06; existing trusts have six months and may rely on 2025-31 until then | KPMG; McDermott | Moderate |
| Fact | Scope | Single-asset trusts; RSM says diversified baskets are not covered. IRS gives no view on ECI, UBTI, forks, airdrops | RSM 2026; McDermott | Moderate |
| Inference | Holder tax | Grantor trust holder is taxed on a pro rata share of rewards as ordinary income when the trust gains dominion, plus capital gain on share sale. A held ETP is not 1099-DA reporting; 1099-B and a trust statement (2027-03-15 for 2026) apply | Inference from grantor trust rules and i1099da | Low |
| Recommendation | Taxable account | Treat staking ETP distributions as ordinary income at federal plus CA rates; prefer non-staking ETP in taxable if only price exposure is wanted [Moderate] `[Verify with CPA]` | n/a | Moderate |

### 3. Pending legislation (as of 2026-11-04)

| Label | Item | Status | Source | Conf |
|---|---|---|---|---|
| Fact | H.R. 10357 Digital Asset Tax Certainty Act | Passed Ways and Means 38 to 5 on 2026-09-16. Applies wash sale and constructive sale rules, mark-to-market for dealers and traders, charitable simplification, mining and staking clarification, voluntary disclosure program. Effective dates not stated on committee release | https://waysandmeans.house.gov/2026/09/16/historic-digital-asset-tax-legislation-advances-to-keep-america-the-crypto-capital-of-the-world/ | High |
| Fact | Floor and Senate | House out until after election; Senate companion ADAPT Act (Daines, Lummis, Moreno, Scott) introduced; advocacy group sees lame-duck package as a path | Crypto Council for Innovation 2026-10-02 `[Interested source]` | Low |
| Fact | Draft features | PARITY discussion draft (2025-12-20): 30-day wash sale window, $200 de minimis for regulated payment stablecoins, 5-year staking deferral election, Sec 475 election, Sec 1058 lending. Lummis S.2207: $300 per transaction and $5,000 per year | BDO 2026-01-22 | Moderate |
| Fact | Bill identity | One secondary source says wash sale applies to dispositions after 2026-09-14 and another names H.R. 9172. Neither confirmed | search result 2026-11-04 | `[Unverified]` |
| Inference | Odds | Enactment before end-2026 is uncertain; loss-harvesting windows for direct crypto may close with an effective date earlier than enactment | Inference | Low |

### 4. California

| Label | Item | Finding | Source | Conf |
|---|---|---|---|---|
| Fact | Rate | Capital gains taxed as ordinary income, top 13.3% | FBT Gibbons; TSCPA (secondary) | Moderate |
| Fact | QSBS | California does not conform to Sec 1202 (R&TC 18152 cited by FBT Gibbons) | https://fbtgibbons.com/section-1202-and-qsbs-a-survey-of-states-that-dont-conform-to-the-federal-treatment/ | Moderate |
| Fact | MMF exempt interest | R&TC 17145: fund must hold 50% or more of assets in obligations exempt for CA individuals at each quarter end; only the exempt percentage of dividends passes through (SBE decisions) | https://california.public.law/codes/revenue_and_taxation_code_section_17145 | Moderate |
| Fact | DFAL | Licensing operative 2026-07-01 (AB 1934); NMLS applications opened 2026-03-09; firms with a completed application on file may operate pending decision; SB 97 (2026-06-30) reportedly removed DFAL stablecoin provisions | MoFo, ADR, Eastern Herald (secondary) | Low |
| Inference | Platform use | CA residents should use venues licensed or with pending DFAL applications; no direct income tax effect | n/a | Moderate |
| Fact | FTB crypto stance | FTB pages returned HTTP 403; conformity to Rev. Rul. 2023-14 and wash sale assumed to follow federal | n/a | `[Unverified]` |

### 5. Vehicle table (full detail in `tax_matrix.csv`)

| Vehicle class | Character | Wash sale | Place in | Label | Verify |
|---|---|---|---|---|---|
| US common stock | Qualified dividend, LTCG | Y | Any | Fact | N |
| Spot ETP, grantor trust | Capital gain on shares; no dividends | Unclear | Taxable, Roth best | Inference [Moderate] | Y |
| Spot ETP with staking | Ordinary rewards plus capital | Unclear | IRA or Roth | Inference [Moderate] | Y |
| Blockchain equity ETF | Dividends and capital | Y | Any | Fact | N |
| Futures crypto ETF | RIC dividends or K-1 60/40 | Y or Unclear | IRA or Roth | Inference [Low] | Y |
| Direct token | Capital gain | N today | Taxable | Fact [High] | Y |
| Staking, airdrops | Ordinary at receipt | N | Taxable | Fact [High] | Y |
| Stablecoin held | Capital (near zero) | N | Taxable | Inference [Moderate] | Y |
| Stablecoin yield | Ordinary | N | IRA or Roth if possible | Inference [Low] | Y |
| Tokenized MMF (registered) | Ordinary dividends; CA exempt share | Y | Taxable ok | Fact [Moderate] | Y |
| Tokenized MMF (offshore) | PFIC likely | Unclear | Not Retail | Inference [Low] | Y |
| Tokenized Treasuries | Ordinary interest | Unclear | By structure | Inference [Low] | Y |
| Private credit | K-1 interest, UBTI | Unclear | Not Retail | Inference [Low] | Y |
| Offshore fund | PFIC | N | Avoid | Fact [Moderate] | Y |
| Wrapped tokenized equity | Unclear | Unclear | Avoid | Inference [Low] | Y |
| QSBS private | LTCG with Sec 1202 | Y | Taxable | Fact [High] | Y |
| VC LP | K-1; Sec 1061 | NA | Taxable | Inference [Low] | Y |
| Validator business | Ordinary plus SE tax | N | Entity | Inference [Low] | Y |
| Structured notes | Per prospectus | Y | Any | Inference [Low] | Y |
| CME futures and options | Sec 1256 60/40 | N | Taxable margin | Fact [High] | Y |

### 6. Mid and large tiers

| Label | Topic | Note | Conf |
|---|---|---|---|
| Inference | Carried interest Sec 1061 | Three-year holding for carry gains; not re-verified for 2025 and 2026 law changes | `[Unverified]` |
| Inference | UBTI | IRS gives no view on staking UBTI or ECI (Rev. Proc. 2026-20). Debt-financed fund income creates UBTI for IRAs. Use blockers | Moderate |
| Fact | OZ 2.0 | New investments after 2026-12-31 defer to 5 years with 10% step-up; designation mechanics under Sec 1400Z-1 not verified | Moderate |
| Inference | Trusts | Grantor trusts pass through and keep step-up; non-grantor trusts hit top brackets at low income. DAPT and CA trustee residency rules need counsel | Low |
| Inference | State residency | CA taxes residents on worldwide income; leaving requires a documented change of domicile. Whether a California wealth tax measure is pending was not verified | `[Unverified]` |
| Fact | Estate | $15M exclusion in 2026; step-up reduces embedded gain tax on heirs | Moderate |

### 7. Account placement for the personal case

Recommendation: Only a taxable cash account is available. Ranked by tax efficiency: (1) spot non-staking ETP or direct token held over one year, (2) US common stock, (3) tokenized registered government MMF with CA-exempt percentage, (4) staking ETP or stablecoin yield only if income is accepted at ordinary rates. [Moderate]

Recommendation: Use specific identification at the broker; avoid transfers into a custodian that would make units noncovered; keep a ledger for every wallet. [High]

Recommendation: Do not rely on a direct-crypto wash sale gap beyond a lame-duck bill; harvest only with a clear exit date. `[Verify with CPA]` [Moderate]

### 8. Lookup for the lead

The mapping from vehicle class to `tax_character` and `account_placement` strings is in `data/tax_lookup.csv`. Use the string verbatim.

## Personal case one-page summary

| Item | Position |
|---|---|
| Profile | California resident, non-accredited, $50k, taxable cash account |
| Federal LTCG rate | Likely 15% if taxable income is above $49,450 (single) and below $545,500; 0% below the first figure |
| NIIT | 3.8% above the MAGI threshold; check |
| California | Ordinary rates, up to 13.3%; no QSBS; MMF exempt percentage only |
| Best vehicles | Spot ETP or direct token held over 1 year; stock |
| Worst for taxable | Staking ETP, stablecoin yield, offshore funds, wrapped tokenized equity |
| Records | 1099-DA gross proceeds in 2026 forms; basis only for covered units; track the rest |
| Wash sale | Not applicable to direct crypto today; H.R. 10357 pending |
| Items to confirm with CPA | Staking ETP holder income, ETP wash sale, tokenized MMF domicile, CA FTB treatment |

## Gaps and unresolved

| Gap | Why |
|---|---|
| DOL 401k crypto status after 2025 rescission and executive order | Search blocked; `[Unverified]` |
| FTB (CA) guidance on crypto and Pub 1001 | HTTP 403 |
| Rev. Proc. 2026-20 primary text | PDF unreadable; relies on KPMG, McDermott, RSM |
| Sec 1061, Sec 1014, Sec 1297, Sec 1202(e) exclusions text | Not fetched; training basis |
| Tokenized MMF and Treasury product domiciles | No offering documents read |
| Stablecoin yield and tokenized equity character | No authority located |
| H.R. 10357 effective dates and bill identity conflicts | Congress.gov blocked |
| Whether futures ETFs are RICs or partnerships | Prospectuses not read |
| CA wealth tax measure and exit rules | Search blocked |

## Files written

`/home/user/Grotesque-Sublime/research/ws/ws7.md`, `/home/user/Grotesque-Sublime/research/tax_matrix.csv`, `/home/user/Grotesque-Sublime/research/data/tax_lookup.csv`, `/home/user/Grotesque-Sublime/research/ws/search_log_ws7.md`
