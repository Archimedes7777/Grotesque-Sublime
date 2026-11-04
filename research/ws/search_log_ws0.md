# Search log WS0 (2026-11-04)

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
