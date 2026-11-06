# YouTube strategy prompt library (project-neutral)

**Source:** seven "Claude AI YouTube prompts" from an Instagram carousel by `paulhilse` (posted October 25, captured by the owner as screenshots on 2026-11-06). The originals are transcribed verbatim in section 4. They are treated as **untrusted data** under `SECURITY.md` section 2: nothing in them is an instruction to this repository or its agents.

**Scope:** this library is for a **new project, not ActivelyPsychotic**. The project is not yet defined, so every prompt below uses a fill-in context block instead of brand facts. Fill the block once, paste it before each prompt.

**Status:** reference only. Running a prompt produces a draft; nothing here posts, uploads, schedules, or reads an account.

## 1. Assessment of the originals

| # | Original | Verdict | Why |
|---|---|---|---|
| 1 | Full channel plan | Use with context | Good skeleton. Without a context block it returns advice that fits any channel |
| 2 | Pick a niche | Use first if the niche is open | The only prompt that belongs before the plan. Its "100 ideas" ask produces padding; 30 ranked ideas is enough |
| 3 | Viral scripts, hooks, thumbnails | Use, rewritten | "Viral" framing pulls toward clickbait and AI tells. Rewritten to ask for specific, honest hooks |
| 4 | Growth and algorithm | Use as education | Mechanics are fine. Engagement tactics must stay manual (no automated likes, follows, comments) |
| 5 | Produce videos 3x faster | Use, with a publish rule | Treats publishing as an AI workflow step. The upload and publish step stays with a person. "3x" is a claim, not a target |
| 6 | Monetization plan | Defer | Useful for sequencing once the channel has data. Premature before the first 30 videos |
| 7 | Read analytics | Use, with a data rule | Needs channel data. Export it from YouTube Studio by hand and paste numbers; no agent gets credentials or API tokens |

Two general weaknesses:

- **No context, so generic output.** "Act as an expert" with no audience, assets, or constraints gives advice for every channel and therefore for none.
- **Money-first order.** The carousel runs plan, niche, scripts, algorithm, speed, money, analytics. A new channel does better with niche, plan, content system, analytics loop, growth mechanics, production, then money.

## 2. Context block (fill in once, paste before every prompt)

```text
Context for every answer:
- Project name: [name]. Channel handle: [handle or "not created yet"].
- What the channel is about in one sentence: [topic and angle].
- Why me: [the owner's credible edge, for example 8 years as a CBET-certified biomedical equipment technician plus AI and prompt engineering].
- Target viewer: [age range, role, what they search for, what they already watch].
- Formats available: [talking head, screen recording, hands-on demo, animation, voiceover slides, Shorts only, long-form only].
- Assets on hand: [equipment, software, existing material, footage, images].
- Time budget: [hours per week] for research, production, and posting, by one person.
- Goal for the first 90 days: [audience, authority, lead generation, revenue, portfolio].
- Constraints: [employer policy, patient or client confidentiality, licensing, no footage of real devices under service contract, regulatory accuracy].
- Rules: every post is a draft a person reviews and publishes by hand; no automated likes, follows, comments, DMs, or uploads; no tool receives passwords, cookies, or tokens; AI-generated or altered content gets the platform's label where its rules require it.
- Mark [Unverified] any platform threshold, policy, or price you cannot confirm, with the date of your knowledge.
```

## 3. Prompts in recommended order

### Step 1. Niche selection (adapted from original 2)

```text
Act as a YouTube market researcher and channel strategist.
Using the context above, evaluate the stated topic as a niche. Cover: audience demand and search intent, competition (name 5 to 8 comparable channels and what each does well), monetization ceiling, content sustainability over 2 years, and the angle that makes this channel different given the owner's edge.
Then define the ideal viewer in one paragraph, recommend 3 to 4 content categories, and give 30 video ideas ranked by expected pull for a new viewer, each tagged Short or long-form, with the format and assets it needs.
If the topic is too broad or too thin, say so and propose two narrower or adjacent niches with the same evaluation.
```

### Step 2. Channel plan (adapted from original 1)

```text
Act as a YouTube strategist.
Using the context above and the chosen niche, write a 12-week plan with:
- Positioning statement (one sentence) and a channel description under 1,000 characters.
- Content pillars with a target share of uploads for each.
- Formats and lengths, and which pillars use Shorts versus long-form.
- A publishing cadence that fits the stated time budget, with hours assigned to research, production, and posting.
- Retention tactics specific to this topic (where to put the payoff, how to structure a demonstration or explanation).
- A weekly action checklist the owner follows by hand.
Leave monetization out; it is a separate prompt for a later phase.
```

### Step 3. Scripts, hooks, titles, thumbnails (adapted from original 3)

```text
Act as a YouTube content strategist and editor.
Using the context above, take the top 10 ideas from Step 1 and produce for each:
- 3 title options under 60 characters: specific, honest, no all-caps, no "you won't believe", no question-bait.
- 1 thumbnail concept: the subject, one overlay phrase of 3 words or fewer, and the emotion or curiosity it carries.
- The first 15 seconds as a script: the problem or promise, then proof the video will deliver it.
- A section outline with the payoff placed before the midpoint and a second payoff near the end.
- One line on why a viewer stays to the end.
Write in plain, concrete language. No em dashes, no "it's not X, it's Y" reveals, no engagement bait.
```

### Step 4. Analytics loop (adapted from original 7)

```text
Act as a YouTube data analyst.
I will paste numbers I export by hand from YouTube Studio (impressions, click-through rate, average view duration, average percentage viewed, returning viewers, subscribers gained, traffic sources, top videos). You do not have account access and must not ask for it.
Build:
1. A weekly review template that takes 10 minutes: what to record, and what counts as signal versus noise at low view counts.
2. A monthly review template: which topics, formats, and hooks worked, what to repeat, what to stop.
3. Decision rules, for example: low click-through rate with high average view duration means change the thumbnail or title, not the video.
4. The three metrics that matter most in the first 90 days and why the others can wait.
State the sample sizes below which a conclusion is premature.
```

### Step 5. Growth mechanics (adapted from original 4)

```text
Act as a YouTube growth strategist with expertise in content discovery.
Using the context above, explain how YouTube surfaces videos (impressions, click-through rate, watch time, retention, returning viewers, suggested videos, search, the Shorts feed) in plain terms, focused on what a one-person channel can act on.
Then give a practical growth plan: upload frequency within the time budget, how to test a title or thumbnail with few views, which Shorts to link to long-form, and how to turn a viewer into a subscriber without begging.
Rules: every engagement action is manual by the owner. No automation, follow-for-follow, engagement pods, or paid views. Mark platform mechanics you cannot verify as [Unverified] with a date.
```

### Step 6. Production workflow (adapted from original 5)

```text
Act as a production manager for a one-person YouTube channel.
Using the context above, design a repeatable weekly workflow from idea to published video and, where it fits, to Shorts cut from the same material. Cover: topic research, script, recording or capture, voiceover or on-screen text, editing, thumbnail, metadata, the AI-content disclosure step, and the human review and publish step.
Constraints: the publish step is always a person in YouTube Studio; do not propose auto-upload tools. Any tool you recommend must be named with its cost [Unverified] and must not need account passwords or session cookies. Include a quality checklist (factual accuracy, spelling, no confidential material, disclosure applied) and estimated minutes per step so the total fits the time budget.
```

### Step 7. Monetization sequence (adapted from original 6; run after the first 30 videos or 90 days of data)

```text
Act as a creator business strategist specializing in YouTube monetization.
Using the context above and the analytics so far, lay out the revenue options in the order they become realistic for this channel: YouTube Partner Program (state current thresholds and mark them [Unverified] with a date), affiliate links, sponsorships, digital products, consulting or services, memberships, newsletters, courses. For each give requirements, pros, limits, and the trigger that says "now is the time".
Rules: any sponsored or affiliate content gets a clear disclosure; do not propose courses or paid communities until viewers ask for them; do not recommend anything that conflicts with the stated constraints.
```

## 4. Original prompts (verbatim transcription from the screenshots)

Kept for provenance. Do not paste these as-is; they lack the context block and rules above.

1. **Your full channel plan.** "Act as an expert YouTube strategist and monetization consultant. Develop a comprehensive plan for launching a YouTube channel from scratch and working toward monetization. Evaluate my niche, target audience, competitors, available resources, and long-term goals. Create a detailed strategy covering channel positioning, content pillars, video formats, publishing schedules, audience growth, viewer retention, monetization opportunities, and a practical weekly action plan."
2. **Pick a niche.** "Act as an experienced YouTube market researcher and channel strategist. Help me choose a profitable YouTube niche with strong audience demand and long-term growth potential. Evaluate competition, search opportunities, monetization potential, content sustainability, and ways to stand out. Develop a unique channel identity, define my ideal viewer, recommend content categories, and generate 100 video ideas ranked by their potential to attract an audience."
3. **Create viral scripts, hooks, and thumbnails.** "Act as an elite YouTube content strategist and video producer. Develop a complete content creation framework designed to improve click-through rates and audience retention. Generate compelling video ideas, attention-grabbing hooks, engaging titles, thumbnail concepts, opening sequences, storytelling structures, retention strategies, calls to action, and complete video scripts. Explain why each concept could attract viewers, maintain their attention, and encourage them to watch until the end."
4. **Understand YouTube growth and algorithm.** "Act as a YouTube growth strategist with expertise in content discovery and audience behavior. Explain how YouTube growth works, including impressions, click-through rates, watch time, audience retention, returning viewers, suggested videos, search traffic, and recommendation systems. Build a practical growth strategy covering upload frequency, content testing, performance optimization, audience engagement, and methods for converting viewers into subscribers."
5. **Produce videos 3x faster.** "Act as a professional YouTube production manager. Design an AI-assisted workflow that helps me create high-quality YouTube videos more efficiently. Develop streamlined processes for topic research, scriptwriting, voiceovers, filming, editing, thumbnail design, publishing, performance analysis, and repurposing content for YouTube Shorts, TikTok, Instagram Reels, and other platforms. Recommend useful AI tools, repeatable workflows, production templates, and quality-control checklists to reduce unnecessary work while maintaining content quality."
6. **Build your monetization plan.** "Act as a creator business strategist specializing in YouTube monetization. Develop a comprehensive revenue strategy for my YouTube channel. Include preparation for the YouTube Partner Program, advertising revenue, affiliate marketing, brand sponsorships, digital products, online courses, paid memberships, newsletters, communities, and additional income opportunities. Explain the requirements, advantages, limitations, and ideal timing for introducing each monetization method as my channel develops."
7. **Read your analytics like a pro.** "Act as an experienced YouTube data analyst. Create a comprehensive system for monitoring, evaluating, and improving my channel's performance. Analyze essential metrics, including impressions, click-through rate (CTR), average view duration, audience retention, subscriber conversion, traffic sources, engagement, and revenue. Develop weekly and monthly performance review frameworks to identify successful content patterns, understand why certain videos underperform, and recommend specific improvements. Help me use these insights to make better content decisions and build a more effective long-term growth strategy."

## 5. Platform facts the prompts depend on

Checked by web search on 2026-11-06 against third-party summaries, not Google's own help pages, so each is **[Unverified]** until confirmed in YouTube Studio or on the official eligibility page.

| Fact | Value found | Note |
|---|---|---|
| Partner Program, full ad revenue | 1,000 subscribers and 4,000 public watch hours in 12 months, or 10 million valid Shorts views in 90 days | The two paths are alternatives, not additive; Shorts watch time does not count toward the 4,000 hours |
| Partner Program, early access (fan funding) | 500 subscribers plus activity minimums | Sources disagree on the exact watch-hour figure for this tier |
| Possible change | Some sources mention a February 2027 revision raising the ad-revenue bar | Future-dated and unconfirmed |
| AI content disclosure | Required for realistic altered or synthetic content a viewer could mistake for real people, places, or events; set at upload; label appears in the description, or on the player for sensitive topics (health, finance, news, elections) | Animation and stylized effects are generally exempt; a realistic AI voice or face is not. Health is a sensitive category, so a medical-technology channel using AI narration should expect the prominent label |
