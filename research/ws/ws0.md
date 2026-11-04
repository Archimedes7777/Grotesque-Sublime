# WS0: Is it actually happening? Adoption data and the null hypothesis

## Summary

Fact: USD stablecoin supply is $295.1B (2026-11-04, DefiLlama API), 3.0% below 2025-10-31 ($304.4B) and 6.5% below the 2026-05-17 peak ($315.5B). The 2024-10 to 2025-10 surge (+77%) has stopped for 12 months.

Fact: Organic payments are small. McKinsey/Artemis put real 2025 stablecoin payments at $0.39T annualized against $35T reported volume (about 1.1%). Visa's adjusted series is 19% of raw ($12.0T vs $63.0T, Jan to Aug 2026) and is about 46x the McKinsey payments figure. Methods disagree by an order of magnitude.

Fact: Tokenized Treasuries and MMFs are $14.25B distributed (RWA.xyz, 2026-11-04), 0.18% of US MMF assets ($7.90T, ICI 2026-10-28), and fell 4.1% in 30 days.

Fact: Broadridge DLR reports about $359B per day (Sept 2026), flat since January. Kinexys reports over $7B per day (June 2026), equal to the daily average of RTP, with no use-case split. Both are issuer claims.

Inference: Verdicts. H0 is retained for retail CBDC and for tokenized securities ex-cash (outside private credit); contested for stablecoin payments, stablecoin as offshore dollar, tokenized cash-equivalents, and wholesale DLT repo; wholesale CBDC has no usable data. No segment meets the rejection test (at or above 1% with eight quarters of faster growth and identifiable organic use). [Moderate]

Inference: Where it is real: Tron and Ethereum USDT dollar plumbing, DLR repo, B2B stablecoin payments in Asia. Pilot theater: bank-chain volumes without disclosure, tokenized equities, most CBDCs. Coverage is incomplete because the search budget was cut off (see Gaps).

## Key numbers

| Metric | Value | Date | Source | Confidence |
|---|---|---|---|---|
| USD stablecoin supply | $295.1B | 2026-11-04 | DefiLlama API (sum of list $295.6B) | [High] |
| Stablecoin supply, peak | $315.5B | 2026-05-17 | DefiLlama API; matches press report of same peak | [High] |
| Stablecoin supply change, 12 months | -3.0% | 2025-10-31 to 2026-11-04 | DefiLlama API | [High] |
| USDT / USDC supply | $177.8B / $71.3B (60.1% / 24.1%) | 2026-11-04 | DefiLlama API | [Moderate] |
| Stablecoins on Tron / Ethereum | $94.1B / $138.4B (31.9% / 46.9%) | 2026-11-04 | DefiLlama API | [Moderate] |
| Real stablecoin payments | $0.39T annualized (B2B $226B) | Dec 2025 annualized | McKinsey/Artemis via search summary | [Moderate] |
| Visa adjusted volume Jan to Aug | $12.0T (raw $63.0T) | 2026-08-31 | Aggregator relay of Visa/Allium [Interested source] | [Low] |
| Tokenized Treasuries and MMFs | $14.25B distributed | 2026-11-04 | RWA.xyz | [Moderate] |
| Share of US MMF assets | 0.18% | 2026-11 | RWA.xyz and ICI ($7.90T, 2026-10-28) | [Moderate] |
| Tokenized private credit | $13B to 14B active (Figure dominant) | 2026-Q1 to Q3 | eco.com, Blockworks via search | [Low] |
| Kinexys daily volume | over $7B | 2026-06-29 | CoinDesk citing JPMorgan [Interested source] | [Low] |
| Broadridge DLR daily / monthly | $359B / $7.5T | 2026-09 | Search summary, Kaiko (June) [Interested source] | [Low] |
| FedNow Q3 2026 | 6.38M payments, $370.9B | 2026-09-30 | Fed Financial Services via search snippet | [Moderate] |
| RTP Q3 2026 | 150M payments, $621B | 2026-09-30 | The Clearing House | [Moderate] |
| ACH 2025 | 35.19B payments, $93.0T | 2025 | Nacha | [High] |
| CHIPS | over $2T per day | undated | The Clearing House | [Moderate] |
| US MMF assets | $7.90T | 2026-10-28 | ICI | [High] |
| e-CNY cumulative | 3.48B txns, CNY 16.7T | 2025-11-30 | PBoC via secondary | [Low] |

## Body

### 1. Method and limits

Fact: Supply data were pulled directly from the DefiLlama stablecoin API on 2026-11-04 and parsed locally (Source: DefiLlama, stablecoincharts and stablecoins endpoints, 2026-11-04, https://stablecoins.llama.fi/stablecoincharts/all).

Fact: The shared web search quota ran out after 11 searches. Several load-bearing items are therefore from search summaries or aggregators and are tagged [Low]. Dashboards were read, not model-built.

Inference: Treat all issuer-reported volumes (Visa, JPMorgan, Broadridge) as claims, not measurements. [High]

### 2. Stablecoin supply and composition (tests N2)

| Label | Date | Total | USDT | USDC | On Tron | On Ethereum |
|---|---|---|---|---|---|---|
| Fact | 2023-10-31 | $124.0B | $84.7B | $24.3B | $45.7B | $64.9B |
| Fact | 2024-10-31 | $172.3B | $120.4B | $34.8B | $60.7B | $83.4B |
| Fact | 2025-04-30 | $239.9B | $148.9B | $62.0B | $71.0B | $125.2B |
| Fact | 2025-10-31 | $304.4B | $183.3B | $75.5B | $78.1B | $163.4B |
| Fact | 2026-05-31 | $312.3B | $188.2B | $75.9B | $90.2B | $160.1B |
| Fact | 2026-11-04 | $295.1B | $178.2B | $70.9B | $94.1B | $138.4B |

(Source: DefiLlama API, 2026-11-04; full monthly series in data/adoption_stablecoin_supply.csv. USD billion.)

Fact: Press reports match the DefiLlama peak of $315.5B on 2026-05-17 and $301.6B on 2026-10-28 (Source: KuCoin News flash, 2026-10-28, https://www.kucoin.com/news/flash/stablecoin-supply-drops-2-1b-in-2026-surpassed-1t-growth-in-2025) [SEO-shaped aggregator, used as a cross-check only].

Fact: Within 2026, Ethereum stablecoin supply fell from $163.4B (2025-10-31) to $138.4B while Tron rose from $78.1B to $94.1B (DefiLlama, 2026-11-04). USDT is 60.1% of supply and the Tron share rose from 25.7% to 31.9%.

Inference: Dollar demand growth is shifting toward the Tron/USDT offshore-dollar channel while the Ethereum, DeFi, and regulated-issuer channel shrinks. This is consistent with N2 but does not prove it, since chain-level issuer splits and holder data were not retrieved. [Low]

Fact: Non-fiat-backed assets (crypto-backed and algorithmic in DefiLlama's tags) total about $25.7B, 8.7% of supply. USDS, DAI, USDe are $15.8B (DefiLlama, 2026-11-04).

Gap: Correlation with crypto market cap and exchange-held share were not computed (no price series or exchange-wallet data retrieved). N2 is therefore partly tested.

### 3. Volume: raw, adjusted, and payments (tests N1)

| Label | Measure | Value | Period | Source |
|---|---|---|---|---|
| Fact | McKinsey/Artemis reported volume | up to $35T | 2025 | McKinsey via search summary, 2026-02 |
| Fact | McKinsey/Artemis real payments | $0.39T (B2B $226B, C2C $77B, C2B $76B, B2C $11B, cards $4.5B) | Dec 2025 annualized | McKinsey, 2026-02 |
| Fact | Visa raw volume | $63.0T | Jan to Aug 2026 | OneBullEx relaying Stablecoin Insider and Allium, 2026-09-27 [Interested source: Visa] |
| Fact | Visa adjusted volume | $12.0T | Jan to Aug 2026 | same |
| Fact | Visa adjusted, single month | $1.79T (June), $1.1T (May) | 2026 | Crypto Briefing, 2026-07-06 |
| Fact | Visa adjusted, H1 | $8.82T | H1 2026 | Crypto Briefing, 2026-07-06 |

Fact: Visa's method removes bot and wash activity and, after a label expansion, same-entity transfers. The label set and filter criteria are not published (OneBullEx, 2026-09-27). Visa's own dashboard returned no values to a fetch (2026-11-04).

Inference: Adjusted/raw is 19% (12.0/63.0). McKinsey's payments/reported is about 1.1% (0.39/35). Payments proper are therefore a low single digit to low tens of percent of any raw figure depending on method, and the Visa adjusted series still includes non-payment activity (treasury movement, DeFi, exchange flows) at roughly 46x the McKinsey payments number (annualized $18T vs $0.39T, mismatched periods). [Low]

Fact: The reported Visa trailing-12-month figure of $10.2T (to June 2026) cannot coexist with H1 2026 at $8.82T and June 2025 alone at about $0.795T. It is an inconsistent relay; excluded from conclusions (Crypto Briefing, 2026-07-06).

Fact: Artemis separately reported crypto-card spend above P2P stablecoin transfers (about $15B vs $11B per month run rate, January 2026) and a 2025 edition of B2B $76B, P2P $19B, card $18B annualized, which do not reconcile with McKinsey's card figure of $4.5B (search summary of Artemis reports, 2026-01).

Inference: N1 is supported: most counted volume is not payments. But the claim that organic payments are small relative to supply is only half-supported, because McKinsey's $0.39T annualized is still 1.3x the average $295B supply. B2B growth of 733% y/y (McKinsey, 2026-02) is real growth from a low base. [Moderate]

### 4. Tokenized cash equivalents, credit, and securities (tests N3, N9)

| Label | Asset | Value | Date | Source |
|---|---|---|---|---|
| Fact | Tokenized US Treasury funds, distributed | $14.25B (-4.14% 30d), 123 assets, 85,870 holders | 2026-11-04 | RWA.xyz |
| Fact | Represented (non-distributed) | $0.088B | 2026-11-04 | RWA.xyz |
| Fact | USDY (Ondo) | $2.40B | 2026-11-04 | RWA.xyz |
| Fact | USYC (Circle) | $2.24B | 2026-11-04 | RWA.xyz |
| Fact | BUIDL | $1.97B | 2026-11-04 | RWA.xyz |
| Fact | BENJI plus iBENJI | $2.70B | 2026-11-04 | RWA.xyz |
| Fact | US money market fund assets | $7.90T (retail $3.11T) | 2026-10-28 | ICI |
| Fact | Private credit, active loans | about $13B to 14B | Q1 to Q3 2026 | eco.com and Cryptonews via search [SEO-shaped] |
| Fact | Total RWA ex-stablecoins | $38B to 39B (RWA.xyz) vs $46.3B (Token Terminal) | 2026-09 to 10 | OneBullEx, 2026-10-26 |

Inference: Penetration of US MMF assets is 0.18%, in the contested band (0.1% to 1%). The 30-day decline of 4.1% and flat supply from stablecoin data indicate that growth is stalling in the latest month. Eight quarters of faster growth could not be tested without history. [Low]

Fact: BUIDL ($1.97B) appears in DefiLlama's stablecoin list and in RWA.xyz's Treasury category (both 2026-11-04), so headline totals double-count unless netted.

Gap: N3 (holder composition, top-holder concentration, DAO and stablecoin-reserve recycling) is not testable: RWA.xyz per-product holder data is login-gated and no disclosure was retrieved. Circle's USYC at $2.24B is issuer-linked, which makes recycling plausible but unproven. [Unverified]

Inference: Private credit is the largest non-Treasury category, but Figure's HELOCs on Provenance, a permissioned chain, dominate (70% to 92% depending on metric). Against roughly $2T US private credit (Blockworks title figure, not verified) penetration is about 0.65%. This is a single-issuer, permissioned-chain result, which supports N9 on chain choice. [Low]

Gap: Tokenized equities, bonds (DIVA/SDX-style), and funds were not retrieved. No fee-revenue series for Ethereum L1 or L2s was retrieved (N9 revenue half untested).

### 5. Wholesale DLT and tokenized deposits (tests N4)

| Label | Platform | Metric | Value | Date | Source |
|---|---|---|---|---|---|
| Fact | Kinexys | average daily volume | over $7B | 2026-06-29 | CoinDesk citing JPMorgan [Interested source] |
| Fact | Kinexys | cumulative | over $4T | 2026-06-29 | same |
| Fact | Broadridge DLR | average daily repo | $359B (Sep), $357B (Jun), $365B (Jul), $384B (Dec 2025) | 2026 | Kaiko; search summary [Interested source] |
| Fact | Broadridge DLR | monthly | $7.5T (Sep) | 2026-09 | Pluang via search summary |
| Fact | CHIPS | average daily value | over $2T | undated | The Clearing House |
| Fact | RTP | average daily value | $7B | 2026-10 | The Clearing House |

Inference: Kinexys at $7B per day is 0.35% of CHIPS daily value and equal to RTP's daily average. Annualized at about 250 business days it is about $1.75T. Neither a use-case split nor intra-group share was disclosed, so N4 cannot be accepted or rejected. Independent analysts say public ledgers show a much smaller footprint (Coindoo, via search summary). [Low]

Inference: DLR volume is flat in 2026 (Jan $365B, Sep $359B, Dec 2025 $384B, so -6.5% since December). The one DLT segment with large absolute numbers shows no growth in nine months. Penetration of US repo cannot be stated because a verified denominator was not retrieved. If US daily repo is in the low trillions the share would be above 1%, but this is [Unverified] and the volume counts notional including rolls (assumption). [Low]

Gap: Canton (outside DLR), Partior, Fnality, DTCC collateral and Project Ion volumes were not retrieved. Data unavailable for this session.

### 6. CBDCs (tests N7)

| Label | CBDC | Metric | Value | Date | Source |
|---|---|---|---|---|---|
| Fact | e-CNY | cumulative | 3.48B txns, CNY 16.7T | 2025-11-30 | PBoC via secondary [Low] |
| Fact | e-CNY | cumulative | 4.3B txns | 2026-09-30 | Xinhua via The Paypers [Unverified] |
| Fact | mBridge | cumulative settlement | $55.5B, e-CNY about 95% | approx 2026 | Atlantic Council via search [Low] |
| Fact | e-CNY | policy | interest-bearing deposit-style features from 2026 | 2025-12-29 | gov.cn headline via search [Low] |

Inference: e-CNY at CNY 16.7T over several years is far below 1% of Chinese annual payment flows (denominator not retrieved) and the move to interest-bearing status suggests that adoption needed a design change. [Low]

Gap: eNaira, Sand Dollar, digital euro, and Agora volumes were not retrieved. From prior knowledge only, retail CBDC use in Nigeria and the Bahamas is very low; do not use for conclusions. [Unverified]

### 7. Non-DLT comparators (tests N5, G6)

| Label | Rail | Q3 2026 or latest | Notes |
|---|---|---|---|
| Fact | FedNow | 6.38M payments, $370.9B; Q2 5.00M, $274.7B | Q3 +27.6% count q/q, +35.0% value; over 1,800 participants (July 2026) |
| Fact | RTP | 150M payments, $621B; 1,417 participants; cap $10M | daily average $7B (Oct 2026) |
| Fact | ACH | 35.19B payments, $93.0T (2025) | +4.9% count, +7.9% value y/y; Same Day ACH growing (Nacha Q3 headline, 2026-10-28) |
| Fact | CHIPS | over $2T per day | undated |

(Sources: Federal Reserve Financial Services via search snippet, 2026-10-20; Clearing Post, 2026-08-18; The Clearing House, 2026-10; Nacha, 2026-10-28.)

Inference: FedNow plus RTP settle about $0.99T per quarter, about $4.0T annualized, roughly 10x the McKinsey real stablecoin payments figure (mixed geography, US only vs global). US instant rails already outscale organic stablecoin payments, which supports N5 on the volume test. FedNow counts are small (6.4M in Q3 vs RTP 150M) but growing 28% q/q. [Low]

Inference (G6): ISO 20022 and T+1 are live and are the incumbent modernization path; this session did not retrieve SWIFT gpi speed, remittance price, or T+1 data. Incumbent capture of gains is plausible but unquantified. [Unverified]

### 8. Base rate of failure and abandonment (G4, G12, N6)

Gap: The queries on we.trade, Marco Polo, TradeLens, and ASX CHESS replacement were not executed before the search quota ended, so no fetched source exists in this session.

Inference: From prior knowledge, flagged [Unverified] and not to drive conclusions: we.trade wound up in 2022; TradeLens (Maersk/IBM) announced wind-down in 2022-11 with end in 2023-Q1; Marco Polo network (R3 Corda) ceased in 2023; ASX wrote off its CHESS replacement and scrapped the project in 2022 to 2024. WS3 or the lead should verify with dates before citing. The survival-bias point stands in structure: the enterprise wave of 2016 to 2020 shows a high failure rate, and the current wave's volume disclosures (Kinexys, DLR) are mostly issuer-reported.

### 9. Dashboard disagreement (G13)

| Label | Comparison | Spread |
|---|---|---|
| Fact | DefiLlama chart $295.14B vs list sum $295.58B (2026-11-04) | 0.15% |
| Fact | Aggregator 2026-10-19 about $306B vs DefiLlama about $305B | within 1% |
| Fact | RWA total: RWA.xyz $38B to 39B vs Token Terminal $46.3B | about 20% |
| Fact | Private credit: $7.99B distributed vs $13B to 14B active vs $37.55B represented | 4.7x |
| Fact | Visa raw $63.0T vs adjusted $12.0T | 5.3x |
| Inference | Visa adjusted annualized vs McKinsey payments | about 46x |
| Fact | BUIDL counted in both stablecoin and Treasury totals | $1.97B |

Inference: Supply data agree across sources; adoption and volume data do not. The spread grows with the degree of judgement in the metric definition. Use supply and MMF totals as anchors and treat volume as a range, with McKinsey as the floor and Visa adjusted as a ceiling. [Moderate]

### 10. Penetration table

| Label | Numerator | Denominator | Penetration | Date |
|---|---|---|---|---|
| Inference | Tokenized MMF/Treasury $14.25B | US MMF $7.90T | 0.18% | 2026-11 |
| Inference | Real stablecoin payments $0.39T | US ACH value $93.0T | 0.42% | 2025 |
| Inference | Visa adjusted annualized $18T | US ACH value $93.0T | 19% (not payments) | 2026 |
| Inference | Kinexys $7B per day | CHIPS $2T per day | 0.35% | 2026-06 |
| Inference | Stablecoin real payments | global payments (McKinsey) | 0.02% | 2025 |
| Inference | Private credit tokens $13B | US private credit $2T | 0.65% | 2026 |

All [Low] because denominators are mismatched in scope or geography. Full calculations in data/adoption_penetration.csv.

### 11. Null hypothesis tests

| Label | Claim | Result | Evidence | Confidence |
|---|---|---|---|---|
| Inference | N1 wash and trading dominate | Supported | adjusted 19% of raw; payments about 1% of reported | [Moderate] |
| Inference | N2 supply driven by leverage and offshore demand | Partly supported | 12 months flat; Tron share 32%; correlation not run | [Low] |
| Inference | N3 tokenized Treasuries recycle crypto cash | Untested | holder data gated | [Unverified] |
| Inference | N4 bank DLT substitutes internal transfers | Untested | no split disclosed | [Low] |
| Inference | N5 fast rails deliver the benefits | Supported on volume | FedNow plus RTP about 10x real stablecoin payments | [Low] |
| Inference | N6 enterprise wave failed | Not tested in session | prior knowledge only | [Unverified] |
| Inference | N7 retail CBDC stalled | Weakly supported | e-CNY redesign; others not retrieved | [Low] |
| Inference | N8 forecasts are cut | Not tested | no vintages retrieved | [Unverified] |
| Inference | N9 token value accrual weak | Partly supported | permissioned-chain private credit; fees untested | [Low] |
| Inference | N10 regulation caps advantage | Not tested | GENIUS yield rule and Basel not retrieved | [Unverified] |

### 12. Verdict per segment (decision rule applied)

| Label | Segment | Verdict | Basis | Thesis status |
|---|---|---|---|---|
| Inference | Stablecoin payments | Contested | 0.42% of US ACH (contested band) but 0.02% of global payments (retained band); fast growth from a low base; supply flat 12 months [Low] | Real but small |
| Inference | Stablecoin as offshore dollar | Contested | $295B supply, USDT 60%, Tron 32%; growth has stopped 12 months, so the eight-quarter test fails recently [Low] | Real |
| Inference | Tokenized cash-equivalents | Contested | 0.18% of MMF; down 4.1% in 30 days; recycling untested [Low] | Early, stalling |
| Inference | Tokenized securities ex-cash | Retained (private credit contested) | equities, bonds not measured; private credit about 0.65% and dominated by one issuer on a permissioned chain [Low] | Mostly pilot |
| Inference | Wholesale DLT settlement | Contested | DLR $359B per day, flat in 2026, issuer-reported; Kinexys $7B per day unsplit [Low] | Real in repo, unproven elsewhere |
| Inference | Retail CBDC | Retained | e-CNY redesign; eNaira and Sand Dollar not retrieved [Low] | Pilot theater outside China |
| Inference | Wholesale CBDC | Data unavailable | only mBridge $55.5B cumulative [Low] | Unknown |

Inference: H0 as stated (below 1% migration through 2030) is not rejected for any segment; the rejection test requires 8 quarters of faster growth that this session could not construct and 1% penetration that no verified series reaches. The 12-month flat supply is the single most important fact against the thesis momentum. [Moderate]

Recommendation: Downstream workstreams should cite supply, MMF, ACH, and FedNow/RTP figures at their stated confidence, treat Visa and issuer volumes as claims, and re-run G4, G12, and G13 searches before final synthesis. Kill criterion: if supply regains $315B and DLR or Kinexys disclose independent external-flow splits, revisit stablecoin payments and wholesale DLT verdicts. [Moderate]

## Gaps and unresolved

| Gap | Impact |
|---|---|
| Search quota exhausted after 11 searches; 29 planned remain | Items below unresolved |
| Fedwire annual value, SWIFT messages, CPMI cross-border, World Bank remittance prices | Legacy denominators for wholesale and remittance penetration missing |
| Failed consortia (we.trade, Marco Polo, TradeLens, ASX CHESS) with dated sources | G4, G12, N6 untested |
| BUIDL, BENJI, OUSG holder composition | N3 untested |
| Canton, Partior, Fnality, DTCC volumes | Wholesale DLT incomplete |
| eNaira, Sand Dollar, digital euro, Agora | Retail and wholesale CBDC incomplete |
| Ethereum and L2 fee revenue; RWA chain split permissioned vs public | N9 untested |
| GENIUS yield prohibition, Basel treatment | N10 untested |
| Forecast vintages | N8 untested |
| Eight-quarter growth series for tokenized Treasuries and DLR | Decision rule cannot be fully applied |
| Primary Visa, Artemis, McKinsey pages (503 or JS-only) | Volume figures [Low] |
| FedNow quarterly table from Fed page (fetch truncated) | Q3 figures from search snippet |

## Files written

- /home/user/Grotesque-Sublime/research/ws/ws0.md
- /home/user/Grotesque-Sublime/research/ws/search_log_ws0.md
- /home/user/Grotesque-Sublime/research/data/adoption_stablecoin_supply.csv
- /home/user/Grotesque-Sublime/research/data/adoption_stablecoin_volume.csv
- /home/user/Grotesque-Sublime/research/data/adoption_tokenized_rwa.csv
- /home/user/Grotesque-Sublime/research/data/adoption_wholesale_dlt.csv
- /home/user/Grotesque-Sublime/research/data/adoption_cbdc.csv
- /home/user/Grotesque-Sublime/research/data/adoption_legacy_rails.csv
- /home/user/Grotesque-Sublime/research/data/adoption_penetration.csv
- /home/user/Grotesque-Sublime/research/data/adoption_dashboard_disagreement.csv
