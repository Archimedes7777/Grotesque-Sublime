# Null hypothesis: programmable finance is mostly narrative

Assigned to WS0 for testing. Stated in its strongest form, so that the thesis must defeat it with data.

## H0

Through 2030, programmable ledgers will not materially change where value accrues in the global financial system. Measured settlement migration from legacy rails will stay below 1% of the relevant flows. The economic gains from programmability will be captured by incumbents who modernize conventional rails, not by new entrants or network tokens.

## Supporting arguments (each must be tested)

| # | Claim | Test WS0 must run |
|---|---|---|
| N1 | Stablecoin "volume" is dominated by crypto trading, MEV bots, exchange internal transfers, and wash activity. Organic payments are a small fraction. | Compare raw vs. adjusted volume (Visa Onchain Analytics, Artemis, other method) and estimate the payments share, dated. |
| N2 | Stablecoin supply growth is driven by crypto-market leverage and offshore dollar demand (USDT on Tron), not by mainstream payments. | Supply by issuer and chain; correlation with crypto market cap; share held by exchanges. |
| N3 | Tokenized Treasuries and MMFs are a recycling of crypto-native cash (DAO treasuries, stablecoin reserves, DeFi collateral), not new institutional money. | Holder composition of BUIDL, BENJI, OUSG where disclosed; top-holder concentration. |
| N4 | Bank DLT platforms (Kinexys, Citi Token Services) move intra-group or client treasury balances that would move anyway; they substitute internal book transfers, not external rails. | Volume disclosures and use-case descriptions; compare to bank's total payment volume. |
| N5 | Fast non-DLT rails (FedNow, RTP, Pix, UPI, SEPA Instant) and ISO 20022 deliver most of the claimed benefits (speed, data richness, 24/7) without new ledgers. | Growth rates and volumes of these rails vs. DLT alternatives. |
| N6 | The 2016 to 2020 enterprise blockchain wave largely failed (we.trade, Marco Polo, TradeLens, ASX CHESS replacement, Fnality delays). The current wave repeats the pattern. | List of shut-downs; survival rate of named consortia; time from announcement to production. |
| N7 | Retail CBDCs have stalled in most democracies, and adoption is weak where launched (eNaira, Sand Dollar). | Transaction volumes and per-capita use; policy reversals. |
| N8 | Market-size forecasts come from interested parties and are routinely cut (e.g., earlier multi-trillion forecasts revised). | Forecast vintage comparison. |
| N9 | Value accrual to network tokens is weak: institutions use permissioned chains or L2s, and fees on public L1s have fallen. | Fee revenue trends of Ethereum L1 and major L2s; share of tokenized RWA on permissioned vs. public chains. |
| N10 | Regulation (yield bans, capital charges, privacy law) caps the economic advantage of stablecoins over bank deposits and MMFs. | Status of yield prohibitions and Basel treatment. |

## Decision rule

- H0 is **rejected** for a segment if dated, independent data show penetration of the relevant legacy flow at or above 1% and growing faster than the legacy flow for at least eight quarters, with organic (non-trading) usage identifiable.
- H0 is **retained** for a segment if penetration is below 0.1%, or growth is explained mostly by crypto-internal recycling.
- Between those bounds the segment is **contested**, and the report says so.

WS0 must state the verdict per segment: stablecoin payments, stablecoin as offshore dollar, tokenized cash-equivalents, tokenized securities ex-cash, wholesale DLT settlement, retail CBDC, wholesale CBDC.
