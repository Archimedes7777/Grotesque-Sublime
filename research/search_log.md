# Search log (merged)
Merged from `ws/search_log_ws*.md` by the lead. Lead gap-fill searches are listed at the end.

---

## ws/search_log_ws0.md


Note: the shared web search limit (200 per turn across all agents) was exhausted after 11 successful searches, so the planned 40-search budget was not reachable. Gaps from this are listed in ws0.md. DefiLlama JSON endpoints were pulled with curl as a data API (no search engine used).

## Searches
| # | Query | Mode | URLs used |
|---|---|---|---|
| 1 | stablecoin total supply October 2026 DefiLlama USDT USDC market cap | extended | https://www.kucoin.com/news/flash/stablecoin-supply-drops-2-1b-in-2026-surpassed-1t-growth-in-2025 ; https://defillama.com/stablecoins/ethereum ; https://stablecoininsider.org/stablecoin-statistics-in-2026/ ; https://www.onebullex.com/news/articles/usdc-sheds-4-69b-in-30-days-as-stablecoin-market-cap-falls-to-300-36b-3 |
| 2 | RWA.xyz tokenized treasuries total value October 2026 | extended | https://www.stobox.io/reports/state-of-rwa-2026 ; https://app.rwa.xyz/treasuries ; https://www.onebullex.com/news/articles/tokenized-treasuries-slip-to-28-percent-of-46-3-billion-rwa-market-as-private-credit-grows-3 ; https://www.onebullex.com/news/articles/rwa-xyz-records-46-2-billion-tokenized-assets-across-36-chains-in-2026 |
| 3 | Visa Onchain Analytics adjusted stablecoin transaction volume 2026 | extended | https://cryptobriefing.com/visa-record-stablecoin-volume-june/ ; https://solanacompass.com/news/visa-onchain-analytics-reports-record-179-trillion-in-adjusted-stablecoin-volume-for-june-2026 ; https://www.onebullex.com/news/articles/visa-stablecoin-revision-drops-dollar-volume-to-12-trillion-as-transaction-count-holds-steady ; https://www.onebullex.com/news/articles/visa-expands-address-labeling-to-600-million-cutting-adjusted-stablecoin-volume-less-than-2-2 |
| 4 | Kinexys daily transaction volume 2026 JPMorgan | extended | https://www.coindesk.com/business/2026/06/29/j-p-morgan-broadens-blockchain-settlement-network-as-banks-modernize-cross-border-payments ; https://coindoo.com/jpmorgans-blockchain-numbers-what-public-data-shows/ ; https://reports.tiger-research.com/p/jpmorgan-kinexys-how-should-banks-use-eng |
| 5 | Artemis stablecoin payments volume report 2026 B2B P2P card-linked share of total | extended | https://reports.artemisanalytics.com/stablecoins/artemis-stablecoin-payments-from-the-ground-up-2025.pdf ; https://ambcrypto.com/crypto-card-payments-overtake-p2p-stablecoin-transfers-artemis-report/ ; https://www.kucoin.com/news/flash/mckinsey-and-artemis-report-only-1-of-35t-stablecoin-volume-is-real-payments |
| 6 | Canton Network daily repo volume Broadridge DLR monthly average 2026 | extended | https://pluang.com/en/news-feed/broadridge-proses-repo-ledger-terdistribusi-7-5-triliun-september ; https://www.kaiko.com/news/kaiko-brings-broadridges-7-5-trillion-dlr-onchain-repo-data-to-bloomberg-terminal ; https://cryptobriefing.com/broadridge-tokenized-repo-9-trillion-monthly/ ; https://cantonnews.org/broadridge-s-blockchain-repo-platform-processes-8-trillion-in-july-deepening-ties-to-canton-network ; https://rosa-roubini.com/wp-content/uploads/2026/05/Canton-RS-21May26.pdf (not opened) |
| 7 | tokenized private credit active loans RWA.xyz 2026 Figure Provenance | extended | https://eco.com/support/en/articles/15002235-rwa-tokens-2026-guide ; https://stablecoininsider.org/top-8-tokenized-private-credit-platforms-delivering-8-to-15-apy-in-may-2026/ ; https://cryptonews.net/news/finance/31143011/ ; https://blockworks.com/news/private-credit-tokenization-2-trillion-blackrock-maple |
| 8 | e-CNY cumulative transaction volume PBoC 2026 yuan | extended | https://www.atlanticcouncil.org/blogs/econographics/what-to-watch-as-china-prepares-its-digital-yuan-for-prime-time/ ; https://thepaypers.com/crypto-web3-and-cbdc/news/china-launches-dceps-and-e-cny-smart-contract-at-beijing-forum ; https://english.www.gov.cn/news/202512/29/content_WS69526d4ec6d00ca5f9a08511.html |
| 9 | McKinsey Artemis stablecoin payments 2025 $390 billion real payments of $35 trillion volume report | extended | https://www.mckinsey.com/featured-insights/charts/stablecoins-find-their-niche ; https://www.mckinsey.com/industries/financial-services/our-insights/stablecoins-in-payments-what-the-raw-transaction-numbers-miss ; https://www.bitget.com/amp/news/detail/12560605168188 |
| 10 | FedNow third quarter 2026 volume value participants Federal Reserve Financial Services statistics | extended | https://www.frbservices.org/resources/financial-services/fednow-service-resources/fednow-service-volume-value-statistics/ ; https://clearingpost.com/insights/fednow-at-three-volume-nearly-doubles-as-smaller-payments-drive-growth/ ; https://www.richmondfed.org/publications/research/economic_brief/2026/eb_26-28 |
| 11 | The Clearing House RTP network Q3 2026 volume daily record value transactions | extended | https://www.theclearinghouse.org/payment-systems/rtp ; https://clearingpost.com/insights/rtp-network-may-day-records-2026/ |
| 12 | Fedwire Funds Service 2025 annual volume value CHIPS 2025 NACHA ACH 2025 | extended | REFUSED: search budget exhausted |

## Fetches (WebFetch) and data pulls
| # | URL | Outcome |
|---|---|---|
| F1 | https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=1 | truncated by tool; replaced by curl pull |
| F2 | https://stablecoins.llama.fi/stablecoincharts/all | truncated; replaced by curl pull |
| F3 | https://app.rwa.xyz/treasuries | OK, 2026-11-04 snapshot |
| F4 | https://www.onebullex.com/news/articles/visa-stablecoin-revision-drops-dollar-volume-to-12-trillion-as-transaction-count-holds-steady | OK, 2026-09-27; aggregator, relays Stablecoin Insider |
| F5 | https://cryptobriefing.com/visa-record-stablecoin-volume-june/ | OK, 2026-07-06 |
| F6 | https://www.mckinsey.com/industries/financial-services/our-insights/stablecoins-in-payments-what-the-raw-transaction-numbers-miss | HTTP 503; used search summary only |
| F7 | https://visaonchainanalytics.com/ | loaded, no values visible (JS dashboard) |
| F8 | https://www.frbservices.org/.../fednow-service-volume-value-statistics/ | truncated, no table; Q3 figures from search snippet |
| F9 | https://www.theclearinghouse.org/payment-systems/rtp | OK |
| F10 | https://www.frbservices.org/resources/financial-services/wires/volume-value-statistics/index.html | 404 |
| F11 | https://www.theclearinghouse.org/payment-systems/chips | OK, undated |
| F12 | https://www.nacha.org/newsroom/ach-network-volume-and-value-statistics | 404 |
| F13 | https://www.coindesk.com/business/2026/06/29/j-p-morgan-broadens-blockchain-settlement-network-as-banks-modernize-cross-border-payments | OK |
| F14 | https://www.federalreserve.gov/paymentsystems/fedfunds_ann.htm | stale page (2020), redirects to frbservices |
| F15 | https://www.nacha.org/content/ach-network-volume-and-value-statistics | OK |
| F16 | https://clearingpost.com/insights/fednow-at-three-volume-nearly-doubles-as-smaller-payments-drive-growth/ | OK, 2026-08-18; internally inconsistent on Q1 value |
| F17 | https://www.ici.org/research/stats/mmf | OK, 2026-10-29 |
| F18 | https://www.frbservices.org/resources/financial-services/wires/volume-value-statistics | 404 |
| F19 | https://www.broadridge.com/press-release/2026/distributed-ledger-repo-september-2026 | 404 (guessed URL) |
| F20 | https://www.kaiko.com/news/kaiko-brings-broadridges-7-5-trillion-dlr-onchain-repo-data-to-bloomberg-terminal | OK, June 2026 figures, undated |
| D1 | curl https://stablecoins.llama.fi/stablecoincharts/all (also ?stablecoin=1, ?stablecoin=2, /Tron, /Ethereum) | JSON parsed locally with python -I |
| D2 | curl https://stablecoins.llama.fi/stablecoins?includePrices=true and /stablecoinchains | JSON parsed locally |

## Flagged sources
No fetched page contained instructions aimed at an agent. Flagged as aggregator or SEO-shaped: onebullex.com, kucoin.com/news flash, stablecoininsider.org, eco.com support articles, pluang.com. Used only as pointers, tagged Low.

---

## ws/search_log_ws1.md


Note: three further searches were refused after the shared per-turn web search limit was reached; no workaround was attempted.

## Searches (mode extended unless noted)

| # | Query | URLs used |
|---|---|---|
| 1 | stablecoin total supply USDT USDC October 2026 | coinmarketcap.com/academy/article/stablecoin-supply-falls-bitcoin-etf-outflows-1b; stablecoinbeat.com; stablecoin.com/market-cap; spark.money/tools/stablecoin-market-cap-tracker |
| 2 | RWA.xyz tokenized treasuries total value BUIDL AUM 2026 | secondary only (eco.com, coinpaprika.com); superseded by RWA.xyz fetch |
| 3 | Atlantic Council CBDC tracker 2026 | atlanticcouncil.org/cbdctracker |
| 4 | digital euro European Parliament vote ECB preparation phase 2026 | sofiaglobe.com/2026/07/09/european-parliament-votes-to-open-negotiations-on-the-digital-euro/ |
| 5 | Circle USDC circulation Q3 2026 earnings Arc mainnet | theblock.co (2026-11-04 Circle Q3); aol.com Circle Q3 transcript; benzinga transcript |
| 6 | Tether Q3 2026 attestation USDT USAT | cryptobriefing.com/tether-q3-2026-profit-reserve-buffer/; 247wallst.com; beincrypto.com; eco.com USAT; forbes.com 2026-05-27 |
| 7 | PYUSD RLUSD USDG market cap bank-issued stablecoin | metamask.com/price/paypal-usd; kucoin.com RLUSD news; spark.money; edgex news |
| 8 | GENIUS Act implementing rules final effective date OCC Treasury 2026 | occ.gov bulletin-2026-50; skadden.com; arnoldporter.com; wilmerhale.com |
| 9 | Kinexys JPMD deposit token volume; Citi Token Services; HSBC tokenised deposit | coindoo.com; the-businesstime.com; eco.com; tabinsights.com; theasianbanker.com; ledgerinsights.com |
| 10 | tokenized MMF expense ratio BUIDL BENJI 2026 (two result sets returned) | eco.com; altstreet.investments |
| 11 | Franklin BENJI AUM Fidelity FDIT Goldman BNY WisdomTree Ondo OUSG | pixelwebsolutions.com/tokenized-money-market-funds/; financefeeds.com |
| 12 | SEC DTCC tokenization no-action letter; Nasdaq tokenized securities | fintechanddigitalassets.com; coindesk.com/policy/2026/03/18; dechert.com |
| 13 | tokenized stocks market size xStocks Robinhood Ondo | castlelabs.io/research/tokenized-stocks; coinpaprika.com |
| 14 | Broadridge DLR daily repo volume 2026 Canton | broadridge.com press releases; sec.gov ARS |
| 15 | Project Agora BIS final report 2026 | bis.org/publ/othp110.pdf; ledgerinsights.com |
| 16 | mBridge 2026 Saudi exit | pymnts.com 2026 Saudi exit; fortune.com 2026-09-21 |
| 17 | Fnality sterling 2026; Partior 2026 | fnality.com news; tradeweb.com |
| 18 | Swift blockchain shared ledger 2026 | coindesk.com/business/2026/07/09; ledgerinsights.com; blockhead.co |
| 19 | Visa stablecoin settlement run rate; Mastercard BVNK Zerohash | kucoin.com Visa $25B; bvnk.com press; cnbc.com 2026-03-17; coindesk |
| 20 | Tempo mainnet 2026; Shopify USDC Stripe | coindesk.com/tech/2026/03/18; stripe.com/newsroom/news/shopify-stripe-stablecoin-payments |
| 21 | FedNow volume Q3 2026; RTP; Pix; UPI | paymentsjournal.com; frbservices.org; richmondfed.org/eb_26-28 |
| 22 | UPI October 2026; Pix 2026 | inc42.com UPI 25.47B |
| 23 | tokenization platform shut down 2026 | coindesk.com/business/2026/08/09 shakeout roundup |
| 24 | Securitize public listing 2026 tokenized AUM; SDX; HKEX | prnewswire.com Securitize Q2; kucoin.com Securitize |
| refused | ICI MMF expense ratio; ECB Pontes Appia; CLARITY and Anti-CBDC status | none |

## Fetches (16 of 20 budget)

| URL | Result |
|---|---|
| atlanticcouncil.org/cbdctracker/ | Used |
| app.rwa.xyz/treasuries | Used |
| app.rwa.xyz/ | Used |
| app.rwa.xyz/stocks | Used |
| app.rwa.xyz/private-credit | Used |
| broadridge.com/press-release/2026/broadridges-distributed-ledger-repo-processes-8-trillion-in-july | Used |
| frbservices.org FedNow statistics | Page did not render |
| occ.gov/news-issuances/bulletins/2026/bulletin-2026-50.html | Used |
| swift.com insights news MVP | HTTP 403 |
| prnewswire.com Securitize Q2 2026 | Used |
| bis.org/publ/othp110.pdf | Used (summary page) |
| ici.org/research/stats/mmf | Used (MMF assets only) |
| franklintempleton.com FOBXX page | Did not render |
| hkma.gov.hk press releases; stablecoin issuers page | No licensee names |
| investor.visa.com news | Did not render |

## Flags

No fetched page contained instructions aimed at the agent. SEO-shaped or low-quality sources used with [Low]: eco.com, stablecoininsider.org, KuCoin flash news, castlelabs.io, pixelwebsolutions.com, altstreet.investments. Interested sources: Circle, Tether CEO post, Broadridge, Securitize, Visa, Mastercard.

---

## ws/search_log_ws2.md

Shared WebSearch cap was exhausted after 15 searches (4 further calls refused). Fetches used: 20 of 20 budget (several returned 403, 404, 429).

## Searches run (all extended unless noted)
1. GENIUS Act implementing rules OCC FDIC Treasury Fed NCUA 2026
2. CLARITY Act Senate status October 2026
3. Stablecoin yield prohibition affiliates exchanges Senate compromise
4. SEC innovation exemption Project Crypto tokenization
5. Senate cloture vote CLARITY September 2026
6. Midterm results 2026 Senate control
7. Anti-CBDC Surveillance State Act status
8. Fed skinny master account proposal
9. Basel Committee cryptoasset standard review 2026
10. UCC Article 12 states enacted
11. Basel consultation press release (standard, bis.org only)
12. FDIC OCC tokenized deposits guidance
13. SEC generic listing standards, CFTC
14. Digital euro regulation EP vote
15. MiCA transitional period end
Refused (cap): BoE/FCA/DSS; HKMA licences; MAS and Japan; e-CNY.

## URLs fetched with useful content
- https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-50.html
- https://www.occ.gov/news-issuances/news-releases/2026/nr-occ-2026-92a.pdf (final rule text read via pdftotext)
- https://www.govinfo.gov/content/pkg/PLAW-119publ27/html/PLAW-119publ27.htm
- https://www.arnoldporter.com/en/perspectives/advisories/2026/10/implementing-the-genius-act-the-federal-reserve-proposes-a-comprehensive-rulemaking
- https://www.sidley.com/en/insights/newsupdates/2026/09/sec-issues-innovation-exemption-for-onchain-trading-of-tokenized-us-listed-stocks
- https://www.sec.gov/newsroom/press-releases/2026-90-sec-issues-innovation-exemption-facilitate-trading-tokenized-nms-stock-request-comment
- https://www.orrick.com/en/Insights/2026/10/The-CLARITY-Act-Stalls-in-the-Senate-Whats-Next-for-Digital-Asset-Regulation
- https://www.lw.com/en/us-crypto-policy-tracker/legislative-developments
- https://www.bis.org/media-releases/20251119-basel-committee-continues-prioritise-basel-iii-implementation-approves-final-principles-third
- https://www.bis.org/media-releases/20261001-basel-committee-meets-advance-supervisory-and-regulatory-initiatives-and-discuss-risks-and
- https://www.hkma.gov.hk/eng/key-functions/international-financial-centre/stablecoin-issuers/
## Failed fetches
congress.gov (403), uniformlaws.org (no data), paulhastings UCC (429) and tracker (429), circle IR (404), HKMA release and register (wrong page, 404).

---

## ws/search_log_ws3.md


Budget used: 28 searches (26 extended, 2 standard; within 40) and 13 fetches (within 20). A 29th search was refused by the harness (shared per-turn search limit). Items left unsearched are listed under Gaps in `ws/ws3.md`. Where a page was undated, `source_date` in CSVs is the retrieval date 2026-11-04.

## Searches

| # | Query | Key URLs used |
|---|---|---|
| 1 | stablecoin total supply market cap October 2026 DefiLlama | defillama.com/stablecoins/ethereum; stablecoininsider.org/stablecoin-statistics-in-2026 |
| 2 | RWA.xyz tokenized real-world assets total value distributed 2026 | onebullex.com RWA.xyz article; finextra.com 31625 |
| 3 | GENIUS Act implementing rules effective date OCC Treasury final rule 2026 | occ.gov bulletin-2026-50; skadden.com; mofo.com |
| 4 | CLARITY Act Senate market structure bill status October 2026 | dlapiper.com 2026/09; defirate.com/clarity-act-fact-sheet |
| 5 | stablecoin market forecast 2028 2030 2035 StanChart Citi JPM Bernstein | theblock.co 2026-10-14 StanChart |
| 6 | tokenized assets forecast 2030 BCG McKinsey Citi revised 2026 | citigroup.com/global/insights/tokenization-2030 |
| 7 | digital euro legislation EP vote 2026 ECB timeline | euronews 2026-06-23; coindesk 2026-06-23 |
| 8 | MiCA transitional period end July 2026; EU T+1 | trusty.report; elliptic.co |
| 9 | McKinsey 2030 $2T; BCG Ripple $18.9T; 21.co | ledgerinsights BCG Ripple; coindesk 2025-04-07 |
| 10 | Bernstein $4T 2035; JPMorgan $500B 2028 | finance.yahoo.com JPM; financialcontent Bernstein |
| 11 | Treasury TBAC stablecoin $2T 2028 | home.treasury.gov sb0680; bis.org/publ/work1270.pdf |
| 12 | SEC generic listing standards crypto ETF | cnbc.com 2025-09-30 |
| 13 | DTCC tokenization no-action letter 2026; Nasdaq tokenized | clearygottlieb.com; dtcc.com 2026 press release |
| 14 | Basel Committee cryptoasset standard review 2026 | bis.org 2026-02-25 release |
| 15 | BoE systemic stablecoin regime; FCA go-live | bankofengland.co.uk 2026-06; dentons.com 2026-07-16 |
| 16 | HKMA first stablecoin licences 2026 | coindesk 2026-03-24; leaprate.com |
| 17 | Kraken IPO 2026; Circle IPO | cnbc 2026-04-14; yahoo Kraken cancels |
| 18 | FOMC October 2026 decision | investinglive.com; admiralmarkets.com |
| 19 | Project Agora 2026; mBridge; Fed skinny account | bis.org/press/p260527 |
| 20 | SWIFT shared ledger; Canton; Fnality; Kinexys | eco.com 17 banks; coinburn.com |
| 21 | Europe T+1 11 October 2027 | mtrlegal.com; jpmorgan.com T+1 FAQ |
| 22 | SEC innovation exemption; Anti-CBDC Act 2026 | freewritings.law; congress.gov S.1124 |
| 23 | BUIDL AUM 2026; tokenized MMF totals | spark.money; defi-intel.com |
| 24 | Pix, UPI adoption statistics | clearingpost.com Pix H2 2025; ibef.org UPI 85.5% |
| 25 to 28 | M-Pesa adoption; EMV migration; enterprise blockchain failures; MMF history (four separate calls) | orfonline.org; gravitypayments.com; coindesk 2022-11-30 x2; awealthofcommonsense.com; cranedata.com 11503 |


## Fetches

| # | URL | Use |
|---|---|---|
| 1 | theblock.co StanChart 2026-10-14 | forecast, supply $309B, velocity |
| 2 | citigroup.com/global/insights/tokenization-2030 | Citi 5.5T base, 2.7 bear, 8.2 bull |
| 3 | occ.gov bulletin-2026-50 | OCC final rule date, effective 2027-01-18 |
| 4 | stablecoins.llama.fi/stablecoins | USDT $177.8B, USDC $71.3B (partial page) |
| 5 | app.rwa.xyz | Distributed $39.40B, Represented $395.97B |
| 6 | bis.org/press/p260527.htm | Agora, no testing dates |
| 7 | vasptracker.com GENIUS timeline | enactment, 2027-01-18, 2028-01-18, 2028-07-18 |
| 8 | dtcc.com 2026 press release | July limited production, October launch |
| 9 | dlapiper.com CLARITY failure | 2026-09-15 |
| 10 | proofoftalk.io digital euro | Council, EP, trilogue, ECB dates |
| 11 | freewritings.law innovation exemption | 2026-09-17, expires 2031-09-17 |
| 12 | bis.org Basel 2026-02-25 | review, no date |
| 13 | home.treasury.gov sb0680 | TBAC 2026-11-03 minutes |

---

## ws/search_log_ws4.md


18 searches completed (extended mode). 3 further searches refused by the shared web-search limit; no workaround attempted.

## Searches

| # | Query (abridged) | URLs used |
|---|---|---|
| 1 | Circle Q3 2026 results distribution costs | investingnews.com, theblock.co (Circle) |
| 2 | Tether Q3 2026 attestation | cryptobriefing.com |
| 3 | Coinbase Q3 2026 stablecoin revenue | SEC 10-Q coin-20260630; theblock.co |
| 4 | RWA.xyz tokenized assets by chain | app.rwa.xyz/networks |
| 5 | Ethereum fee revenue 2026 and burn | 21shares.com; tokenpost.com |
| 6 | Solana REV 2026 | app.blockworks.com/report/sol-value-accrual |
| 7 | Base sequencer revenue | vaasblock.com |
| 8 | Canton burn fee revenue | altcoinbuzz.io |
| 9 | Stablecoin deposit outflow estimates | whitehouse.gov CEA; theblock.co; congress.gov CRS |
| 10 | BIS stablecoin Treasury yields | bis.org work1270 |
| 11 | McKinsey cross-border revenue pool | mckinsey.com |
| 12 | Nilson US interchange 2025 | merchantspaymentscoalition.com |
| 13 | FOMC October 2026 | federalreserve.gov (fetched) |
| 14 | BUIDL, BENJI fees | financefeeds.com; eco.com |
| 15 | SAB 122 custody | natlawreview.com; xbrl.org |
| 16 | Global custody fees | State Street ARS FY2025; BNY annual report 2025 |
| 17 | Tokenized MMF AUM | financefeeds.com |
| 18 | Remittance and DTCC transfer agent fees | remitroutes.com; dtcc.com fee schedule |

## Fetches (19 of 20)

Circle Q3 release (investingnews.com); RWA.xyz networks; SEC Coinbase 10-Q 2026-06-30; 21shares Ethereum H1; Chainspect financials; Altcoin Buzz Canton; McKinsey GPR 2025 (HTTP 503, failed); White House CEA; BIS WP 1270; federalreserve.gov FOMC 2026-10-28; DefiLlama stablecoins; DefiLlama fees for Ethereum, Stellar, Base, Solana, XRPL, Avalanche, Arbitrum; The Block Circle Q3.

## Blocked queries

Stellar, XRPL, Avalanche, Polygon fee burn; staking ETF approvals; GENIUS Act implementing rules and CLARITY Act status.

## Source quality notes

Many search results were crypto-native or aggregator pages (KuCoin flash, blogs); they were used only where a primary or second source agreed, and are tagged [Low]. Some pages showed conflicting numbers (Circle EPS, Coinbase stablecoin revenue $307M vs $328M, Tether supply); the figure consistent with the filing was used.

---

## ws/search_log_ws5.md


Budget: 40 searches, 20 fetches. Used: 21 WebSearch (extended unless noted), 17 WebFetch, 1 CoinMarketCap quote call. Four further searches were refused by the harness (shared per-turn search budget exhausted); they are listed under "Blocked" and their topics are open gaps.

## Searches
| # | Query (short) | Key URLs used |
|---|---|---|
| 1 | Circle CRCL Q3 2026 price, cap, revenue | cnn.com/markets/stocks/CRCL; stocktitan.net CRCL Q3 release; fool.com transcript 2026-11-04 |
| 2 | Coinbase Q3 2026 results | sec.gov coin-20260930 10-Q; q326earningsdeck |
| 3 | Robinhood Q3 2026 results | stocktitan HOOD Q3; investing.com Q3 slides |
| 4 | Bitcoin price 2026-11-04 | fortune.com price-of-bitcoin-11-04-2026; analyticsinsight.net |
| 5 | Kraken IPO status | crowdfundinsider.com 2026/09; tradingview KRAKEN |
| 6 | GLXY BLSH FIGR GEMI prices | wallstreetzen GLXY; robinhood GEMI |
| 7 | Coinbase price after Q3 | ambcrypto.com/?p=645880 |
| 8 | Spot SOL and XRP ETF fees | cryptoetf.today XRP fee comparison; koinly SOL ETF |
| 9 | Stablecoin yield and CLARITY compromise | coindesk 2026-05-01; lw.com tracker |
| 10 | Tokenized MMF retail access | eco.com tokenized treasury KYC; financefeeds |
| 11 | CLARITY Act floor status | defirate.com; fintechweekly; cryptoticker |
| 12 | ETH staking ETFs | sec.gov Grayscale ETHE filings |
| 13 | Tokenization ETFs | amplifyetfs.com/tknq; globalx.ca TOKN |
| 14 | Spot BTC ETF fees and flows | spotedcrypto Oct 2026 flows; nerdwallet |
| 15 | T-bill yield and Fed | tradingeconomics; cnbc 2026-10-28; schwab FOMC |
| 16 | Securitize SECZ listing | investing.com 2026-07-01 |
| 17 | Stripe, Anchorage, Fireblocks, Chainalysis, Paxos valuations | axios 2026-02-24; bloomberg 2026-01-16; nasdaqprivatemarket Fireblocks |
| 18 | S&P 500 close | marketscreener (rejected, intraday and conflicting) |
| 19 | Ripple and Kraken secondary | benzinga 2026-09; forgeglobal Kraken |
| 20 | Crypto equity beta to BTC | nadcab.com, dailycoin (secondary) |
| 21 | Circle ARC presale, USDC, rate sensitivity | investing.com Circle Q3 slides; blockchainreporter; 247wallst 2026-11-04 |

## Fetches
| # | URL | Result |
|---|---|---|
| 1-2 | stockanalysis.com statistics COIN, CRCL | OK |
| 3-5 | stockanalysis compare pages (5 crypto equities; 6 payments and banks; 5 exchanges and managers) | OK, no EV or as-of dates |
| 6 | federalreserve.gov H.15 | OK, 2026-11-02 data |
| 7 | stockanalysis compare SECZ, BK, SPY, QQQ | OK, BK empty |
| 8 | lw.com US crypto policy tracker | OK (page current to Aug 2026) |
| 9 | coinbase.com/usdc | 403 |
| 10 | tokenomist.ai/unlocks | 403 |
| 11 | stockanalysis ETF compare (IBIT, ETHB, ETHA, GSOL, BSOL, BLOK) | OK, no dates |
| 12 | coindesk 2026-05-01 CLARITY yield text | OK |
| 13 | forgeglobal.com Kraken | OK |
| 14 | benzinga Ripple article | 403 |
| 15 | financefeeds tokenized treasury (mistyped URL) | 404 |
| 16-17 | stockanalysis statistics BK, HOOD | OK |

## Blocked searches (open gaps)
1. GENIUS Act final rules and effective-date detail, OCC charters.
2. Where US retail earns stablecoin yield today (Coinbase, Kraken, PayPal rates).
3. Apollo ACRED and Hamilton Lane minimums.
4. Crypto venture fund sizes and minimums.

---

## ws/search_log_ws6.md

Budget: 16 of 40 searches completed; further searches refused (shared session limit of web searches reached). 19 of 20 fetches used. 1 CoinMarketCap MCP quote call.

## Searches
| # | Query (abridged) | Mode | URLs used |
|---|---|---|---|
| 1 | crypto hack losses 2026 YTD | extended | yahoo finance crypto-hack-losses-hit-8; kucoin, incrypted, cryptoticker recap |
| 2 | Chainalysis 2025 theft | extended | chainalysis.com/blog/crypto-hacking-stolen-funds-2026; therecord.media |
| 3 | stablecoin depeg 2026 | extended | beincrypto.com/stablr-stablecoin-depeg-exploit; arxiv.org/abs/2606.07442 |
| 4 | FBI IC3 2025 crypto | extended | asisonline.org; foxbusiness; aarp |
| 5 | CLARITY yield ban status | extended | coindesk 2026-05-01; americanbanker; cnbc 2026-09-14 |
| 6 | Fed financial stability 2026 stablecoins | extended | federalreserve.gov FSR May 2026; FEDS notes |
| 7 | IMF GFSR Oct 2026 stablecoins | extended | imf.org WP 2026-10-02; policy paper 2026-10-09 |
| 8 | FSB stablecoin 2026 | extended | fsb.org 2026-10-12; coindesk 2026-10-12 |
| 9 | CLARITY cloture 49-50 | extended | fireblocks, orrick, defirate |
| 10 | BTC price Nov 2026 vs ATH | extended | admiralmarkets 2026-11-03; cryptobriefing |
| 11 | CRCL price Nov 2026 | extended | stockanalysis; tikr; heygotrade |
| 12 | COIN HOOD drawdown | extended | benzinga 2026-10-30; cryptobriefing; 247wallst |
| 13 | ETH SOL price | extended | coinmarketcap (stale); used MCP instead |
| 14 | CRCL ATH and BLOK | extended | tikr; valueaddvc; BLOK no result |
| 15 | Open USD launch | standard | fortune 2026-06-30; dailycoin; coinmarketcap academy |
| 16 | CRCL record high June 2025 | standard | coindesk mirror (irishnews.pages.dev) 2025-06-23 |
| 17 to 19 | BTC cycles; COIN HOOD history; BLOK | n/a | refused: search limit reached |

## Fetches
fortune Binance; chainalysis 2025 and 2024 posts; lw.com tracker; Fed FSR funding risks; FSB note; valueaddvc CRCL; stockanalysis CRCL and history; companiesmarketcap COIN and HOOD; govinfo FR 2026-21706 (PDF unreadable); fintechweekly; FEDS note 2026-04-08; NIST IR 8547 draft and final; ic3.gov PDF (unreadable); cryptoticker hack log; orrick CLARITY.

---

## ws/search_log_ws7.md


Budget note: 13 searches executed. A shared per-turn search limit was reached; 4 further searches were refused and not worked around. 19 fetches attempted (3 returned HTTP 403, 1 PDF unreadable). Search mode "extended" used for Δ12m items.

## Searches executed

| # | Query | Mode | URLs used |
|---|---|---|---|
| 1 | wash sale rule digital assets legislation 2026 status | extended | gordonlaw.com, chainwisecpa.com (secondary) |
| 2 | Form 1099-DA 2026 cost basis reporting requirement digital assets final regulations | extended | sovos.com, awaken.tax (secondary) |
| 3 | Rev. Proc. 2025-31 staking grantor trust exchange-traded products IRS | extended | ropesgray.com, rsmus.com, mcdermottlaw.com |
| 4 | de minimis exemption crypto tax bill 2026 stablecoin $200 Lummis Miller | extended | natlawreview.com, coindesk.com |
| 5 | irs.gov Rev. Proc. 2026-20 digital assets staking trusts safe harbor | extended | kpmg.com, rsmus.com, taxnews.ey.com |
| 6 | H.R. 10357 OR Digital Asset PARITY Act Ways and Means markup September 2026 | extended | waysandmeans.house.gov, bdo.com |
| 7 | Notice 2025-33 backup withholding digital asset brokers relief | extended | rsmus.com, kpmg.com |
| 8 | Rev. Proc. 2024-28 safe harbor allocation unused basis wallet-by-wallet | standard | thetaxadviser.com, rsmus.com |
| 9 | Rev. Rul. 2023-14 staking rewards dominion and control 2026 Jarrett | extended | thetaxadviser.com (2026-09) |
| 10 | Section 1202 QSBS OBBBA $15 million tiered holding period | standard | mondaq, perkinscoie.com, gibsondunn.com |
| 11 | California DFAL July 1 2026 license effective date | extended | mofo.com, adr.org, easternherald.com |
| 12 | California FTB nonconformity QSBS 1202 | extended | fbtgibbons.com, kugelmanlaw.com |
| 13 | California FTB money market fund exempt interest 50 percent | standard | california.public.law R&TC 17145, ota.ca.gov |

## Searches refused (shared budget exhausted), items left unresolved

| Planned query | Topic now [Unverified] |
|---|---|
| DOL 401k alternative assets crypto 2026 | 401k window status |
| Opportunity zones OBBBA 2027 designations | OZ rolling designations |
| California billionaire tax initiative 2026 | CA residency and wealth tax risk |
| (not attempted) tokenized MMF tax, PFIC tokenized funds, GENIUS Act tax | Character claims rest on statute and training |

## Fetches

| # | URL | Result |
|---|---|---|
| 1 | https://www.mcdermottlaw.com/insights/irs-refines-safe-harbor-for-exchange-traded-trusts-that-stake-digital-assets/ | OK, Rev. Proc. 2026-20 summary |
| 2 | https://waysandmeans.house.gov/2026/09/16/historic-digital-asset-tax-legislation-advances-to-keep-america-the-crypto-capital-of-the-world/ | OK |
| 3 | https://www.bdo.com/insights/tax/congress-working-to-reform-tax-treatment-of-digital-assets | OK (2026-01-22) |
| 4 | https://www.irs.gov/instructions/i1099da | OK (reviewed 2026-04-30) |
| 5 | https://www.law.cornell.edu/uscode/text/26/1202 | OK |
| 6 | https://www.thetaxadviser.com/issues/2026/sep/cryptocurrency-staking-rewards-are-income-in-year-received/ | OK |
| 7 | https://www.irs.gov/pub/irs-drop/rp-26-20.pdf | Unreadable binary, not used |
| 8 | https://kpmg.com/us/en/taxnewsflash/news/2026/10/rev-proc-2026-20-digital-asset-staking-safe-harbor.html | OK, limited |
| 9 | https://www.congress.gov/bill/119th-congress/house-bill/10357 | HTTP 403 |
| 10 | https://www.law.cornell.edu/uscode/text/26/1400Z-2 | OK |
| 11 | https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2026-including-amendments-from-the-one-big-beautiful-bill | OK (estate exclusion, std deduction) |
| 12 | https://www.law.cornell.edu/uscode/text/26/1091 | OK |
| 13 | https://www.law.cornell.edu/uscode/text/26/1256 | OK |
| 14 | https://www.law.cornell.edu/uscode/text/26/408 | OK (partial) |
| 15 | https://www.ftb.ca.gov/forms/2025/2025-1001-publication.pdf | HTTP 403 |
| 16 | https://www.irs.gov/individuals/international-taxpayers/frequently-asked-questions-on-digital-asset-transactions | OK (reviewed 2026-06-29) |
| 17 | https://www.irs.gov/irb/2025-45_IRB | OK (Rev. Proc. 2025-32 sec. 4.03) |
| 18 | https://www.ftb.ca.gov/file/personal/income-types/capital-gains-and-losses.html | HTTP 403 |
| 19 | https://cryptoforinnovation.org/2026-lookback-ccis-work-to-advance-a-workable-digital-asset-tax-framework/ | OK (advocacy source) |

---

## ws/search_log_ws8.md


Search budget: 24 searches executed, plus 4 refused (shared per-turn limit exhausted). Fetches: 14 attempted, 11 returned content, 3 returned HTTP 403.

| # | Query | Key URLs used |
|---|---|---|
| 1 | x402 Foundation Coinbase Cloudflare transaction volume 2026 | finance.yahoo.com x402 article; coindesk 2026-05-05; infoq |
| 2 | Visa Intelligent Commerce Trusted Agent Protocol 2026 live | usa.visa.com release 22856 |
| 3 | Mastercard Agent Pay 2026 live transactions Agentic Tokens | mastercard.com Santander release; LatAm release |
| 4 | Stripe ACP OpenAI Instant Checkout SPT | stripe.com/newsroom/news/stripe-openai-instant-checkout |
| 5 | Tempo mainnet MPP | theblock.co 394131 |
| 6 | Google AP2 UCP status | developers.googleblog.com UCP; efficientlyconnected I/O 2026 |
| 7 | ChatGPT Instant Checkout discontinued | cnbc.com 2026-03-20 |
| 8 | PayPal agentic commerce Perplexity | newsroom.paypal-corp.com 2025-10-28 |
| 9 | Skyfire KYAPay Nevermined | stellagent.ai; nevermined.ai |
| 10 | Cloudflare pay per crawl status | developers.cloudflare.com changelog; cloudflare.com press release |
| 11 | Agentic commerce forecast 2030 | stellagent.ai forecast summaries (secondary) |
| 12 | CFPB Regulation E AI agent | consumerbankers.com CBA white paper; techtimes Wells Fargo |
| 13 | PSD3 PSR agentic | nortonrosefulbright; dlapiper |
| 14 | Base USDC fee | spendnode.io; eco.com |
| 15 | Amazon Perplexity ruling | bloomberg; cnbc 2026-03-10; pymnts |
| 16 | Adyen Worldpay Amex agentic | digitaltransactions adyen |
| 17 | Visa Q4 FY26 earnings agentic | fool.com Visa transcript 2026-10-28 |
| 18 | Coinbase Q3 2026 earnings x402 | sec-api.io coinbase; sec.gov decks |
| 19 | x402 October 2026 volume | decrypt; tokenpost; blockchain.news |
| 20 | EU AI Act digital omnibus | gibsondunn; orrick; freshfields |
| 21 | Mastercard Q3 2026 earnings agent pay | finance.yahoo.com MA article |
| 22 | Stripe pricing stablecoin fee | stripe.com/pricing fetched |
| 23 | NET COIN price | marketbeat; tradersunion |
| 24 | FIDO AP2 KYA | fidoalliance.org; ppc.land |
| 25 | (planned but refused) FinCEN FATF AI agents AML; state law; Shopify/Amazon; Circle Arc | none |

Fetches: yahoo x402 article, cnbc 2026-03-20, theblock Tempo, coindesk 2026-05-05, Visa release, sec-api Mastercard (no agentic text), CBA PDF (binary, unreadable), techtimes Wells Fargo, fool.com Visa transcript, stripe.com/pricing. 403: businesswire FIDO, mastercard.com Santander, cloudflare.com press.

Note: search results contained no embedded instructions to follow.

---

## ws/search_log_ws9.md


Searches 1 to 30 ran; searches 31 to 33 were refused (shared per-turn budget exhausted) and were not worked around.

| # | Query (abridged) | Key URLs used |
|---|---|---|
| 1 | Drex BCB 2026 phase | ndmadvogados.com.br/artigo/o-que-e-o-drex/ |
| 2 | Brazil stablecoin regulation BCB 2026 | coindesk.com/policy/2026/05/02/... (fetched), thepaypers.com |
| 3 | UAE VARA stablecoin dirham CBUAE | neolegal.ae, alketbilaw.com |
| 4 | India digital rupee circulation 2026 | businessupturn.com (fetched) |
| 5 | South Korea won stablecoin law | law.asia, tech-insider.org |
| 6 | Nigeria eNaira SEC ISA 2025 | thecowriereport.com, babalakinandco.com |
| 7 | Argentina stablecoin adoption CNV | en.cryptonomist.ch (fetched), xcapit.com |
| 8 | Russia digital ruble 2026-09-01 | tass.com/economy/2180145 (fetched), paymentexpert.com |
| 9 | Switzerland FINMA stablecoin | sif.admin.ch (PDF unreadable), velaw.ch |
| 10 | Kazakhstan digital tenge, Alem fund | qazinform.com, financefeeds.com |
| 11 | Kenya VASP; Ghana; South Africa | techcabal.com, lawlab.africa |
| 12 | Australia digital asset legislation | gtlaw.com.au, coindesk.com |
| 13 | Turkey digital lira, Kazakhstan tenge | legal500.com, timesca.com |
| 14 | Cambodia Bakong | cambodiainvestmentreview.com |
| 15 | Thailand Indonesia Philippines | bakermckenzie.com, fystack.io |
| 16 | Saudi Bahrain Qatar | policy.4pillars.io/qatar, defi-intel.com |
| 17 | Mexico Colombia stablecoin | achivx.org/regulation/mexico, stablecoininsider.org |
| 18 | Canada Stablecoin Act | dlapiper.com, achivx.org/regulation/canada |
| 19 | India crypto tax 30% TDS | finance.yahoo.com, cleartax.in |
| 20 | A7A5 OFAC sanctions | elliptic.co, crystalintelligence.com |
| 21 | NU Q3 results price | marketbeat.com |
| 22 | MELI Q3 2026 | finviz.com |
| 23 | Kaspi KSPI 2026 | fbroker.kz |
| 24 | Dunamu Naver merger | theblock.co, cryptotimes.io |
| 25 | Chainalysis 2026 adoption index | chainalysis.com (fetched) |
| 26 | Argentina cepo dividends | bcaparaguay.com.py, buenosairesherald.com |
| 27 | Brazil election Oct 2026 | aljazeera.com (fetched), qz.com |
| 28 | Nigeria naira FPI | thewhistler.ng, blueprint.ng |
| 29 | OFAC Russia MOEX | debevoise.com PDF, ofac.treasury.gov |
| 30 | Korea stablecoin bill Oct 2026 | cointelegraph.com (fetched), cryptorank.io |

Fetches used (18): chainalysis index; coindesk Brazil; tass; achivx UAE; cryptonomist; aljazeera; businessupturn; sif.admin.ch (unreadable PDF); achivx CH; cointelegraph Korea; npci.org.in (no data); stockanalysis EWZ, INDA, EWY, NU, MELI, KSPI, ARGT (market data, 2026-11-04). Search-tool text in results was treated as data only; no instructions were found in any page.

---

## Lead gap-fill searches (Phase 1 to 3)

| # | Date | Query | URLs used |
|---|---|---|---|
| L1 | 2026-11-04 | 2026 midterm election results House Senate control November 4 2026 | cfr.org/articles/five-things-to-know-about-the-midterms; khaleejtimes.com/americas/us-midterm-elections-2026-voting-explainer (pre-election only) |
| L2 | 2026-11-04 | Binance hack October 2026 $6.3 billion (extended) | bloomberg.com/news/articles/2026-10-29/binance-founder-says-possible-hack-of-exchange-bitcoin-falls; cnbc.com/2026/10/29/circle-tether-freeze-funds-impacted-by-potential-binance-security-issue.html; washingtonpost.com/technology/2026/10/29/suspected-binance-hack-sets-off-scramble-lock-down-billions-crypto/; aljazeera.com/economy/2026/10/30/binance-says-2-54bn-in-crypto-funds-frozen-amid-potential-security-issue; npr.org/2026/10/31/nx-s1-6024426/binance-crypto-heist-cyber-criminals-north-korea |
| L3 | 2026-11-04 | rwa.xyz total tokenized real-world assets value November 2025 excluding stablecoins | news.bitcoin.com/rwa-market-nears-35b-after-10-58-monthly-gain-holders-top-489k; yellow.com/research/tokenized-rwas-31b-market-growth-real-race-starting |
| L4 | 2026-11-04 | Coinbase USDC rewards rate November 2026 | eco.com/support/en/articles/15182156-usdc-yield-in-2026-where-to-earn-interest-on-usdc; help.coinbase.com/en-au/coinbase/coinbase-staking/rewards/usd-coin-rewards-faq; dlnews.com/articles/web3/coinbase-ends-usdc-rewards-for-non-paying-customers/ |
| L5 | 2026-11-04 | midterm election results Democrats House Senate majority AP called (extended) | cbsnews.com/live-updates/senate-election-results-2026/; cbsnews.com/live-updates/house-election-results-2026/; nbcwashington.com/elections/election-day-after-2026-midterms-congress-results-live-updates/4177248/; forbes.com/sites/saradorn/2026/11/04/midterm-election-results-live-updates-democrats-sweep-house-and-senate-in-stunning-rout/ |
| L6 | 2026-11-04 | Franklin Templeton Benji Investments app retail investors FOBXX minimum 2026 | ycharts.com/mutual_funds/M:FOBXX; franklintempleton.com FOBXX product page; altstreet.investments/guides/superstate-vs-franklin-benji |
| API | 2026-11-04 | DefiLlama protocols API (RWA category check; not used, scope mismatch) | api.llama.fi/protocols |
