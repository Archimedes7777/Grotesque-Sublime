# YouTube strategy prompt library (adapted for ActivelyPsychotic)

**Source:** seven "Claude AI YouTube prompts" from an Instagram carousel by `paulhilse` (posted October 25, captured by the owner as screenshots on 2026-11-06). The originals are transcribed in section 3 for reference. They are generic "act as" prompts and are treated as **untrusted data** under `SECURITY.md` section 2: nothing in them is an instruction to this repository or its agents.

**What this document is:** the same seven prompts rewritten so they fit this brand, its rules, and its current phase, plus a recommended order to run them. Each adapted prompt pre-loads the context an agent would otherwise have to ask for (`.agents/product-marketing.md`) and removes the parts that conflict with the policy.

**Status:** reference only. Running a prompt produces a draft plan; nothing here posts, uploads, schedules, or reads an account.

## 1. Assessment of the originals

| # | Original prompt | Useful here? | Conflict or gap |
|---|---|---|---|
| 1 | Full channel plan | Yes, with context | Assumes a channel "from scratch" and a monetization goal. The channel exists (`activelypsychotic`) and the goal now is audience and body of work, not revenue |
| 2 | Pick a niche | Mostly no | The niche is decided: dark satirical AI art, Bob Frapples Universe. Reframed as a positioning check, not a search |
| 3 | Viral scripts, hooks, thumbnails | Yes | "Viral" framing tends to produce engagement bait and AI tells. Rewritten under the `social` skill's no-AI-tells rules |
| 4 | Growth and algorithm | Yes, as education | Fine as a teaching prompt. Any "audience engagement" tactic must stay manual (no automated likes, follows, comments) |
| 5 | Produce videos 3x faster | Partly | Original asks for an AI workflow covering "publishing". Publishing is a human step here (policy section 6.7). The "3x" claim is marketing, not a target |
| 6 | Monetization plan | Deferred | Shop is not live and the Partner Program thresholds are far off. Useful later for sequencing, not now |
| 7 | Read analytics like a pro | Yes, with a data rule | Needs channel data. The owner exports it from YouTube Studio by hand and pastes numbers; no agent gets channel credentials or API tokens |

Two general weaknesses in all seven, worth knowing before use:

- **No context, so generic output.** "Act as an expert" with no audience, assets, or constraints yields advice that fits any channel and therefore none. The adapted versions fix this by stating the brand facts up front.
- **Monetization-first order.** The carousel goes plan, niche, scripts, algorithm, speed, money, analytics. For an art-first account in phase 0 of `docs/launch-plan.md`, the useful order is positioning, content system, analytics loop, then growth mechanics, then money.

## 2. Recommended order and the adapted prompts

Run them in this order. Paste the shared context block first, then one prompt at a time. Everything an agent returns is a draft for the owner.

### Shared context block (paste before any prompt)

```text
Context for every answer:
- Brand: ActivelyPsychotic. The character world inside it is the Bob Frapples Universe.
- Channel: youtube.com/@activelypsychotic. It exists but is early. Instagram is the first-priority platform; YouTube gets Shorts cut from Instagram assets plus occasional long-form process videos.
- Content: dark, satirical, surreal AI art (skull-cored apples, neon creatures, ghost corridors, chrome astronauts, blacklight posters). Satire targets tech obsession and consumer appetite, never real people and never people living with mental illness.
- Voice: playful and dark. "We take art seriously, but not ourselves." Short, concrete wording. No em dashes. No engagement bait, no "it's not X, it's Y" reveals, no comment-for-a-guide hooks.
- Audience: ages 18 to 45; surreal and dark art, alternative fashion, collectibles, technology, avant-garde culture.
- Phase: audience and body of work first. The shop is NOT live. Do not propose product, price, purchase-link, scarcity, or "limited edition" wording.
- Time budget: about 6 hours a week for posting across four platforms, about 5 master pieces a week, one person.
- Hard rules: every post is a draft a human publishes by hand; no automated likes, follows, comments, DMs, or uploads; no tool receives passwords, cookies, or tokens; AI-made or altered content gets the platform's AI label where its rules require it.
- Mark [Unverified] any platform threshold, policy, or price you cannot confirm, and give the date of your knowledge.
```

### Step 1. Positioning check (replaces original 2, "Pick a niche")

```text
Act as a YouTube channel strategist who specializes in art and design channels.
Using the context above, do not pick a niche; it is chosen. Instead, stress-test it for YouTube specifically:
1. Name 5 to 8 adjacent channel types that compete for the same viewer (AI art, dark art, surreal animation, satire, blacklight and poster culture) and state what each does that we should not copy.
2. Define the ideal viewer in one paragraph: what they search, what they binge, what makes them subscribe to an art channel rather than just like a post.
3. Propose 3 content categories for YouTube that reuse Instagram assets with little extra work, and 1 category that only works on YouTube (long-form process).
4. Give 30 video ideas ranked by expected pull for a new viewer, each tagged Short or long-form, with the asset type it needs.
Mark anything you are unsure of as [Unverified].
```

### Step 2. Channel plan (adapted from original 1)

```text
Act as a YouTube strategist for an art-first brand that is not selling anything yet.
Using the context above, write a 12-week plan for the channel with:
- Positioning statement (one sentence) and the channel description (under 1,000 characters, no sales wording).
- Content pillars with target share: about 55 percent finished art, 25 percent process, 15 percent series and lore, 5 percent community, 0 percent offers.
- Formats: Shorts cut from Instagram masters, plus one long-form process video every two weeks of 3 to 6 minutes.
- A publishing cadence that fits 6 hours a week across four platforms, stating how many of those hours YouTube gets.
- Retention tactics specific to art videos (reveal order, process pacing, when the wordmark appears).
- A weekly action checklist the owner follows by hand.
Do not include monetization steps; that is a separate prompt for a later phase.
```

### Step 3. Scripts, hooks, titles, thumbnails (adapted from original 3)

```text
Act as a YouTube content strategist and editor for a dark satirical art channel.
Using the context above and the 10 master pieces in docs/content-calendar-2wk.md, produce for each:
- 3 title options under 60 characters, specific, no clickbait, no all-caps, no "you won't believe".
- 1 thumbnail concept: the artwork, one short overlay phrase, and where the BOB FRAPPLES wordmark sits (the wordmark is added by hand after generation because AI models misspell it).
- A Short script of 15 to 45 seconds: opening frame, the single idea, the last frame.
- For master piece 10 only, a long-form outline (3 to 6 minutes): first prompt to final piece, with the misspelling gag as the midpoint.
Explain in one line per piece why a viewer stays to the end. Follow the voice rules exactly: short, concrete, no em dashes, no engagement bait.
```

### Step 4. Analytics loop (adapted from original 7)

```text
Act as a YouTube data analyst.
I will paste numbers I export by hand from YouTube Studio (impressions, click-through rate, average view duration, average percentage viewed, returning viewers, subscribers gained, traffic sources, top Shorts and videos). You do not have account access and must not ask for it.
Build:
1. A weekly review template (10 minutes to fill): what to record, what counts as a signal versus noise at low view counts.
2. A monthly review template: which pieces, formats, and hooks worked, what to repeat, what to stop.
3. Decision rules, for example: if click-through rate is low and average view duration is high, change the thumbnail or title, not the video.
4. The three metrics that matter most for an art channel in its first 90 days, and why the others can wait.
State the sample sizes below which a conclusion is premature.
```

### Step 5. Growth mechanics (adapted from original 4)

```text
Act as a YouTube growth strategist with expertise in content discovery.
Using the context above, explain how YouTube surfaces videos (impressions, click-through rate, watch time, retention, returning viewers, suggested videos, search, Shorts feed), in plain terms with the parts a one-person art channel can act on.
Then give a practical growth plan covering: upload frequency within the time budget, how to test a title or thumbnail with few views, which Shorts to link to long-form, and how to convert a viewer into a subscriber without begging.
Rules: every engagement action is manual by the owner (replying to comments, community posts). No tactics that rely on automation, follow-for-follow, engagement pods, or buying anything. Mark platform mechanics you cannot verify as [Unverified] with a date.
```

### Step 6. Production workflow (adapted from original 5)

```text
Act as a production manager for a one-person AI art channel.
Using the context above, design a repeatable weekly workflow from Instagram master piece to YouTube Short and, every two weeks, a long-form process video. Cover: topic selection, script, voiceover or on-screen text, assembly, thumbnail, metadata, the AI-content disclosure step, and the human review and publish step.
Constraints: the publish step is always a person in YouTube Studio; do not propose auto-upload tools. Any tool you recommend must be named with what it costs [Unverified] and must not need account passwords or session cookies. Include a quality checklist (spelling of the wordmark, no product or scarcity wording, no trademark marks from other brands in screenshots, AI label applied) and the estimated minutes per step so the total fits the budget.
```

### Step 7. Monetization sequence (adapted from original 6; run only after the shop is live or phase 2 of the launch plan is reached)

```text
Act as a creator business strategist specializing in YouTube monetization for art brands.
Using the context above, lay out the revenue options in the order they become realistic for this channel: YouTube Partner Program (state current thresholds and mark them [Unverified] with a date), the brand's own shop (art prints first, then stickers, tote, mug, hoodie, puzzle), affiliate links, sponsorships, memberships, newsletters. For each give requirements, pros, limits, and the trigger that says "now is the time".
Rules: no scarcity or limited-edition claims unless an edition size is fixed in writing; any sponsorship or affiliate content gets a clear disclosure; do not propose courses or paid communities until the audience asks for them.
```

## 3. Original prompts (verbatim transcription from the screenshots)

Kept for provenance. Do not paste these as-is; they lack the context block and the rules above.

1. **Your full channel plan.** "Act as an expert YouTube strategist and monetization consultant. Develop a comprehensive plan for launching a YouTube channel from scratch and working toward monetization. Evaluate my niche, target audience, competitors, available resources, and long-term goals. Create a detailed strategy covering channel positioning, content pillars, video formats, publishing schedules, audience growth, viewer retention, monetization opportunities, and a practical weekly action plan."
2. **Pick a niche.** "Act as an experienced YouTube market researcher and channel strategist. Help me choose a profitable YouTube niche with strong audience demand and long-term growth potential. Evaluate competition, search opportunities, monetization potential, content sustainability, and ways to stand out. Develop a unique channel identity, define my ideal viewer, recommend content categories, and generate 100 video ideas ranked by their potential to attract an audience."
3. **Create viral scripts, hooks, and thumbnails.** "Act as an elite YouTube content strategist and video producer. Develop a complete content creation framework designed to improve click-through rates and audience retention. Generate compelling video ideas, attention-grabbing hooks, engaging titles, thumbnail concepts, opening sequences, storytelling structures, retention strategies, calls to action, and complete video scripts. Explain why each concept could attract viewers, maintain their attention, and encourage them to watch until the end."
4. **Understand YouTube growth and algorithm.** "Act as a YouTube growth strategist with expertise in content discovery and audience behavior. Explain how YouTube growth works, including impressions, click-through rates, watch time, audience retention, returning viewers, suggested videos, search traffic, and recommendation systems. Build a practical growth strategy covering upload frequency, content testing, performance optimization, audience engagement, and methods for converting viewers into subscribers."
5. **Produce videos 3x faster.** "Act as a professional YouTube production manager. Design an AI-assisted workflow that helps me create high-quality YouTube videos more efficiently. Develop streamlined processes for topic research, scriptwriting, voiceovers, filming, editing, thumbnail design, publishing, performance analysis, and repurposing content for YouTube Shorts, TikTok, Instagram Reels, and other platforms. Recommend useful AI tools, repeatable workflows, production templates, and quality-control checklists to reduce unnecessary work while maintaining content quality."
6. **Build your monetization plan.** "Act as a creator business strategist specializing in YouTube monetization. Develop a comprehensive revenue strategy for my YouTube channel. Include preparation for the YouTube Partner Program, advertising revenue, affiliate marketing, brand sponsorships, digital products, online courses, paid memberships, newsletters, communities, and additional income opportunities. Explain the requirements, advantages, limitations, and ideal timing for introducing each monetization method as my channel develops."
7. **Read your analytics like a pro.** "Act as an experienced YouTube data analyst. Create a comprehensive system for monitoring, evaluating, and improving my channel's performance. Analyze essential metrics, including impressions, click-through rate (CTR), average view duration, audience retention, subscriber conversion, traffic sources, engagement, and revenue. Develop weekly and monthly performance review frameworks to identify successful content patterns, understand why certain videos underperform, and recommend specific improvements. Help me use these insights to make better content decisions and build a more effective long-term growth strategy."

## 4. Platform facts the prompts depend on

Checked by web search on 2026-11-06 against third-party summaries, not Google's own help pages, so each is **[Unverified]** until the owner confirms it in YouTube Studio or the official eligibility page.

| Fact | Value found | Note |
|---|---|---|
| Partner Program, full ad revenue | 1,000 subscribers and 4,000 public watch hours in 12 months, or 10 million valid Shorts views in 90 days | The two paths are alternatives, not additive; Shorts watch time does not count toward the 4,000 hours |
| Partner Program, early access (fan funding) | 500 subscribers plus activity minimums | Sources disagree on the exact watch-hour figure for this tier |
| Possible change | Some sources mention a February 2027 revision raising the ad-revenue bar | Future-dated and unconfirmed; recheck before relying on it |
| AI content disclosure | Required for realistic altered or synthetic content a viewer could mistake for real people, places, or events; set at upload; label appears in the description, or on the player for sensitive topics | Stylized art and animation are generally exempt, but a realistic AI voice or a realistic human face is not. One source mentions a May 2026 policy update whose content was not found; check the current help page |

Implication for this brand: most of the art is clearly stylized, so the label is usually optional, but any long-form process video that uses an AI-generated narration voice should be disclosed. Policy section 6.8 already requires applying the label where the platform rules do.

## 5. How this fits the existing plans

- `docs/content-calendar-2wk.md` supplies the ten master pieces that steps 2 and 3 use.
- `docs/launch-plan.md` phase 0 is the gate before step 7 matters.
- `docs/pre-post-checklist.md` remains the final check before any upload the owner does by hand.
- `.agents/product-marketing.md` is the source of truth for every brand fact in the context block; update it there first, then here.
