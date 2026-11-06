# Competitor audit: AI tools and agent channels

**Captured:** 2026-11-06 from each channel's public YouTube page with a headless browser (About tab for totals; Videos tab for the 12 most recent long-form uploads). Shorts are not shown on the Videos tab, so cadence below is long-form only. Counts are the rounded figures YouTube displays.

## 1. Totals

| Channel | Handle | Subscribers | Videos | Total views | Joined | Views per video (lifetime average) |
|---|---|---|---|---|---|---|
| freeCodeCamp.org | @freecodecamp | 12M | 2,341 | 1,032,282,012 | Dec 2014 | 441,000 |
| Nate Herk, AI Automation | @nateherk | 1.11M | 586 | 66,092,850 | Nov 2013 | 113,000 |
| Matt Wolfe | @mreflow | 1.03M | 831 | 85,379,663 | Apr 2009 | 103,000 |
| Matthew Berman | @matthew_berman | 643K | 1,215 | 97,029,481 | Jan 2008 | 80,000 |
| Nick Saraev | @nicksaraev | 598K | 362 | 28,421,706 | Mar 2020 | 79,000 |
| The AI Advantage | @aiadvantage | 493K | 833 | 35,410,421 | Dec 2012 | 43,000 |
| Cole Medin | @ColeMedin | 231K | 334 | 13,612,203 | Aug 2012 | 41,000 |
| IndyDevDan | @indydevdan | 154K | 221 | 6,100,534 | Dec 2020 | 28,000 |

## 2. Recent cadence, length, and performance (last 12 long-form uploads)

| Channel | Uploads per week | Length range | Views on recent uploads | Recent views as share of subscribers | Dominant format |
|---|---|---|---|---|---|
| Nick Saraev | about 6 | 5 to 28 min | 34K to 801K | 6 to 134 percent | Opinion, news reaction, courses, income framing |
| Matthew Berman | about 5 | 10 to 45 min | 74K to 500K | 12 to 78 percent | Model and release news, interviews |
| The AI Advantage | 3 to 4 | 3 to 20 min | 8.5K to 179K | 2 to 36 percent | Short practical tips, update roundups |
| freeCodeCamp | about 3 | 10 min to 10 hours | 79K to 635K | 1 to 5 percent | Full courses, including an "MCP Security Fundamentals" course at 108K views |
| Nate Herk | 2 to 3 | 9 to 45 min | 52K to 577K | 5 to 52 percent | Claude systems, tool rankings, business framing |
| Matt Wolfe | 2 to 3 | 18 to 38 min | 59K to 277K | 6 to 27 percent | Weekly AI news, tool roundups |
| Cole Medin | about 2 | 12 to 21 min | 10K to 36K | 4 to 16 percent | Agentic engineering practice, "software factory" management |
| IndyDevDan | about 1 | 18 to 39 min | 27K to 209K | 18 to 136 percent | Agentic engineering principles, benchmarks, devlogs |

## 3. What the data says

1. **The field has split into news and practice.** Berman, Wolfe, Saraev, and (partly) Herk run a news-reaction cadence of 3 to 6 uploads a week. Medin and IndyDevDan upload once or twice a week with 15 to 40 minute practice videos. The practice channels are smaller but have the loyal audience: IndyDevDan's recent uploads often exceed his subscriber count in views; Medin's run 4 to 16 percent.
2. **Nobody addresses a profession.** Every recent title across all eight is about a tool, a model, a release, a business, or engineering practice. Not one is about a job outside software or agency work. The closest is Herk's "Every Claude 2.0 Concept Explained for Normal People" (176K views), which shows the demand for translation into non-developer language.
3. **Governance has an audience and almost no supply.** freeCodeCamp's "MCP Security Fundamentals Course" drew 108K views; Medin's "Anthropic's New Study: You're Not Controlling AI as Much as You Think" drew 15K. Those are the only two security-adjacent uploads among 96 recent videos, and both are developer-framed.
4. **Length norms for the practice lane:** 12 to 21 minutes (Medin), 18 to 39 minutes (IndyDevDan). An 8 to 15 minute workflow video sits at the short end of what the practice audience accepts and above the 8-minute mid-roll threshold.
5. **Realistic early performance.** Views per upload for a practice channel at 150K to 250K subscribers are 10K to 60K. A new channel should expect hundreds to low thousands per upload for the first 20 videos, with search-driven titles compounding.
6. **Title patterns to avoid, because they are taken:** "I Tried 100+ X", "Every X Ranked", "X Just Got Insane", "They did it...". The practice lane's titles are declarative and specific ("Run Your AI Software Factory Like a Real Engineering Org"). That is the register for this channel.

## 4. Positioning map

| | Developer and engineer audience | Agency and business audience | General office worker | Regulated and technical professions |
|---|---|---|---|---|
| News and releases | Berman | Saraev, Wolfe | Wolfe, AI Advantage | nobody |
| Practice and workflows | Medin, IndyDevDan, freeCodeCamp | Herk, Saraev | AI Advantage | **open** |
| Governance and security | freeCodeCamp (one course) | nobody | nobody | **open** |

The two open cells are the position stated in `20-ai-tools-step1-niche-evaluation.md`.

## 5. Method and limits

- Totals from the About tab; cadence from visible upload ages on the Videos tab, which YouTube rounds ("2w ago", "1mo ago"). Treat uploads per week as plus or minus one.
- Shorts, members-only videos, and live streams are not included.
- The "views as share of subscribers" column is a rough loyalty signal, not a retention metric.
- Re-run the capture quarterly; the two scripts used are in this session's scratch directory and can be re-created from the description above (Playwright, read `ytInitialData` for About, read the Videos grid text for recent uploads).
