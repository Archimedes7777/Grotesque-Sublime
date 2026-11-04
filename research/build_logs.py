"""Build search_log.md (merged), sources.md (all cited URLs with bias notes), return_methods.md."""
import glob, re
from collections import OrderedDict
from urllib.parse import urlparse
import pandas as pd

# search_log.md
parts = ["# Search log (merged)\n", "Merged from `ws/search_log_ws*.md` by the lead. Lead gap-fill searches are listed at the end.\n"]
for f in sorted(glob.glob("ws/search_log_ws*.md")):
    parts.append(f"\n---\n\n## {f}\n\n" + re.sub(r"^# .*\n", "", open(f).read(), count=1))
parts.append("""
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
""")
open("search_log.md", "w").write("".join(parts))

# sources.md
urls = OrderedDict()
def add(u, date, where):
    u = str(u).strip().rstrip(").,;]")
    if not u.startswith("http"): return
    rec = urls.setdefault(u, {"dates": set(), "where": set()})
    if date and str(date) != "nan" and str(date) != "NA": rec["dates"].add(str(date))
    rec["where"].add(where)
for f in glob.glob("*.csv") + glob.glob("data/*.csv"):
    try: d = pd.read_csv(f)
    except Exception: continue
    for col in [c for c in d.columns if "url" in c.lower()]:
        dc = "source_date" if "source_date" in d.columns else None
        for _, r in d.iterrows():
            for u in re.split(r"[;\s|]+", str(r[col])):
                add(u, r[dc] if dc else "", f)
for f in glob.glob("ws/ws*.md"):
    for u in re.findall(r"https?://[^\s)\]>|,\"'`]+", open(f).read()):
        add(u, "", f)

INTEREST = {
    "circle.com": "Issuer of USDC [Interested source]", "tether.to": "Issuer of USDT [Interested source]",
    "coinbase.com": "Exchange, USDC distributor, Base operator [Interested source]", "visa.com": "Card network reporting own volumes [Interested source]",
    "broadridge.com": "Operator of DLR, self-reported volumes [Interested source]", "rwa.xyz": "Tokenization data vendor with industry clients [Interested source]",
    "chainalysis.com": "Blockchain analytics vendor [Interested source]", "forgeglobal.com": "Secondary marketplace [Interested source]",
    "franklintempleton.com": "Issuer of BENJI [Interested source]", "blackrock.com": "Issuer of BUIDL, IBIT [Interested source]",
    "ripple.com": "Ripple [Interested source]", "chain.link": "Chainlink [Interested source]", "securitize.io": "Tokenization platform [Interested source]",
    "ondo.finance": "Tokenization issuer [Interested source]", "mckinsey.com": "Consultancy selling implementation [Interested source]",
    "bcg.com": "Consultancy selling implementation [Interested source]", "sc.com": "Bank with digital asset business [Interested source]",
    "citigroup.com": "Bank with tokenization business [Interested source]", "jpmorgan.com": "Bank operating Kinexys [Interested source]",
    "fireblocks.com": "Custody vendor [Interested source]", "stobox.io": "Tokenization vendor [Interested source]", "eco.com": "Crypto app content marketing [SEO-shaped]",
    "kucoin.com": "Exchange news aggregator [Interested source]", "mexc.com": "Exchange news aggregator [Interested source]",
    "onebullex.com": "Exchange content [Interested source, SEO-shaped]", "stablecoininsider.org": "Crypto media [Low]",
    "valueaddvc.com": "VC blog [Interested source]", "defillama.com": "Open data aggregator", "llama.fi": "Open data aggregator (DefiLlama API)",
    "federalreserve.gov": "Central bank (primary)", "bis.org": "BIS (primary)", "sec.gov": "Regulator or filings (primary)",
    "occ.gov": "Regulator (primary)", "govinfo.gov": "Statute (primary)", "congress.gov": "Legislature (primary)", "irs.gov": "Tax authority (primary)",
    "treasury.gov": "US Treasury (primary)", "fdic.gov": "Regulator (primary)", "ici.org": "Industry association (fund data)",
    "cornell.edu": "Statute text mirror", "atlanticcouncil.org": "Think tank", "theclearinghouse.org": "Bank-owned operator of RTP and CHIPS [Interested source]",
    "nacha.org": "ACH rule-maker", "stockanalysis.com": "Market data aggregator", "coindesk.com": "Crypto-native media (product facts only)",
    "theblock.co": "Crypto-native media (product facts only)", "decrypt.co": "Crypto-native media (product facts only)",
    "cnbc.com": "Major financial press", "bloomberg.com": "Major financial press", "reuters.com": "Major financial press",
    "ft.com": "Major financial press", "wsj.com": "Major financial press", "cbsnews.com": "Major press", "aljazeera.com": "Major press",
    "fortune.com": "Major press", "washingtonpost.com": "Major press", "npr.org": "Major press",
}
def note(u):
    host = urlparse(u).netloc.lower()
    for k, v in INTEREST.items():
        if host == k or host.endswith("." + k): return v
    if any(x in host for x in ("lawfirm", "law", "llp", "dlapiper", "orrick", "sidley", "lw.com", "mofo", "mwe.com", "kpmg", "alston")): return "Law or accounting firm alert (secondary legal)"
    return "Secondary; no specific interest identified"
lines = ["# Sources\n", "Every URL cited in workstream files and CSVs, deduplicated. Dates are source dates recorded by agents (blank where the agent cited inline only). Bias notes by publisher domain; see schema.md tags.\n",
         f"Total unique URLs: {len(urls)}\n", "| # | URL | Source dates | Interest or bias note | Cited in |", "|---|---|---|---|---|"]
for i, (u, r) in enumerate(sorted(urls.items(), key=lambda kv: urlparse(kv[0]).netloc), 1):
    lines.append(f"| {i} | {u} | {'; '.join(sorted(r['dates']))[:60]} | {note(u)} | {'; '.join(sorted(r['where']))} |")
open("sources.md", "w").write("\n".join(lines) + "\n")

# return_methods.md (v2 method, changelog C1)
p = pd.read_csv("plays.csv")
out = ["# Return methods and arithmetic per play\n",
       "Each row gives the workstream's stated method and arithmetic (verbatim from `return_method_detail`), then the lead's v2 central estimate.\n",
       "Lead formula (v2): read the band as roughly the 10th to 90th percentile of annual returns. sigma = (high - low) / 2.563; central = midpoint - sigma^2 / 2 (compounding drag). Excess = central - 4.21% (3M T-bill constant maturity, H.15, 2026-11-02). Plays are ranked within tier on excess; stress drawdown is shown separately (assumptions.md P6-1 to P6-3).\n",
       "Retired v1 method: scenario-weighting of band low, mid and high by Bear, Base and Bull probabilities. Both red teams showed it maps adoption states onto assets whose returns do not depend on adoption (changelog C1).\n",
       "Caution: bands are workstream judgment, not calibrated distributions.\n"]
for _, r in p.iterrows():
    m = re.findall(r"-?\d+(?:\.\d+)?", str(r["return_band_annual_pct"]))
    if len(m) >= 2:
        lo, hi = float(m[0]), float(m[1]); mid = (lo + hi) / 2; sig = (hi - lo) / 2.563
        arith = (f"mid = ({lo:g} + {hi:g}) / 2 = {mid:g}; sigma = {hi - lo:g} / 2.563 = {sig:.1f}%; "
                 f"central = {mid:g} - {sig:.1f}^2 / 200 = {r['geo_central_pct']:.2f}%; excess {r['excess_vs_tbill_pct']:.2f} pts; "
                 f"stress {r['stress_drawdown_pct']:g}%; tier rank {r['rank_in_tier'] if r['rank_in_tier'] == r['rank_in_tier'] else 'NA'}")
    else:
        arith = "No band asserted by workstream; not scored."
    out.append(f"\n## {r['play_id']} {r['vehicle']} ({r['ticker_or_route']}), {r['tier']}, {r['horizon']}\n")
    out.append(f"- Band: {r['return_band_annual_pct']} percent per year. Method: {r['return_method']}.")
    out.append(f"- Workstream arithmetic ({r['source_ws']}): {r['return_method_detail']}")
    out.append(f"- Lead central estimate: {arith}")
open("return_methods.md", "w").write("\n".join(out) + "\n")
print(len(urls), "urls")
