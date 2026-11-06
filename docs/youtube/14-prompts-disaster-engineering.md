# Prompt library: engineering failures and disaster science (faceless documentary)

**Niche rank:** 5 of 5 (score 65). See `01-niche-research.md` for the evidence.

**Thesis:** disaster content has broad, evergreen demand and is the most faceless-friendly format of the five: narration over licensed footage, maps, and animation. The earning problem is category. Storm-chasing and breaking-weather channels sit in News & Politics (measured median RPM $2.60; the largest weather channel found shows an implied RPM near $2.70 on about 14.5 million monthly views). Framed as engineering and science education (why the structure failed, what the physics did, what the investigation found, what changed in the code), the same subject lands in Education & Science at a measured median of $10.22.

**Why it fits the owner:** technical literacy to read an investigation report (NTSB, CSB, NIST, ASCE) and explain the failure mechanism correctly, and an existing interest in the macabre and sublime treated seriously.

**Main risks:** footage licensing and the inauthentic-content rule (stock montages with scrolling text are the exact example YouTube gives of non-monetizable content); sensitivity around recent events with victims; sponsorship fit is weak compared with the other four niches.

## Context block (paste before every prompt)

```text
Context for every answer:
- Project name: [working title]. Channel handle: not created yet.
- What the channel is about: faceless documentary explainers on how engineered systems and natural systems fail: structural collapses, industrial accidents, medical device and hospital system failures, power grid and infrastructure events, and natural disasters, each told through the mechanism, the investigation, and what changed afterward. Science and engineering education, not breaking news.
- Why me: about 8 years as a CBET-certified biomedical equipment technician with experience reading failure investigations, root cause analysis, and regulatory findings, plus AI and prompt engineering skills for research synthesis and animation scripting. No investigative or journalism credential; the channel relies on primary reports and says so.
- Target viewer: ages 18 to 55 in the US, UK, Canada, and Australia; viewers of engineering, history, and documentary channels who want to understand why something failed, not just watch it fail. They search "why did X collapse", "what caused the Y disaster", "Z explained".
- Formats available: narration over licensed or public-domain footage, maps, diagrams, and original animation; no face on camera; Shorts cut from long-form.
- Assets on hand: access to public-domain US federal investigation material (NTSB, CSB, NIST, NOAA, USGS reports and animations), research and synthesis workflows, animation and diagram tooling, a technical reviewer's eye for mechanism.
- Time budget: [hours] per week for research, production, and posting, by one person.
- Goal for the first 90 days: 20 long-form videos (this format takes longer per video), Partner Program thresholds in progress, a defined footage sourcing and licensing process, a list of 50 evergreen cases with primary reports.
- Constraints: every factual claim cited to a primary investigation report or peer-reviewed source; no speculation presented as finding; no coverage of an event until an official preliminary report exists; no footage used without a license or a public-domain or fair-use basis documented in a log; no graphic depiction of injury or death; victims named only as the official report names them; no "AI slop" montage construction, each video has an original narrative and original diagrams.
- Rules: every post is a draft a person reviews and publishes by hand; no automated likes, follows, comments, DMs, or uploads; no tool receives passwords, cookies, or tokens; AI-generated or altered content gets the platform's label where its rules require it (realistic AI recreations of real events must be labeled; stylized diagrams need not).
- Mark [Unverified] any platform threshold, policy, licensing basis, or price you cannot confirm, with the date of your knowledge.
```

## Niche-specific notes for all prompts

- **Category positioning:** engineering and science education. Titles name the mechanism ("why the dam failed"), not the spectacle. This is a 4x RPM difference in the measured data and the whole thesis.
- **Footage log:** a per-video table of every clip, its source, its license or public-domain basis, and the date checked. US federal agency works are generally public domain **[Moderate]**; state, local, and bystander footage is not.
- **Inauthentic-content defense:** original narrative structure, original diagrams, the investigation's own findings explained in the owner's words. Never a slideshow with text.
- **Timing:** evergreen cases first. Recent events only after a preliminary official report, and never within the first days.
- **AI label:** a realistic AI reconstruction of a real event needs the label; a schematic animation does not. Decide per video and record the decision.

## Prompts in recommended order

### Step 1. Niche evaluation

```text
Act as a YouTube market researcher and channel strategist.
Using the context above, evaluate "engineering failures and disaster science as faceless documentary education" as a niche. Cover: audience demand and search intent (top 20 search phrases, split between evergreen cases and event-driven spikes), competition (name 5 to 8 comparable channels, which category each sits in, and what each lacks), monetization ceiling by revenue type given weak sponsor fit, content sustainability over 2 years, production cost per video, and the angle a technical practitioner's reading of investigation reports gives.
Define the ideal viewer in one paragraph, recommend 3 to 4 content categories (include one on medical device and hospital system failures, which no documentary channel covers), and give 30 video ideas ranked by expected pull, each tagged Short or long-form, with the primary investigation report that supports it and the footage sourcing basis.
Exclude any case without a published official report.
```

### Step 2. Channel plan

```text
Act as a YouTube strategist.
Using the context above, write a 12-week plan with:
- Positioning statement (one sentence) and a channel description under 1,000 characters that signals engineering education.
- Content pillars with a target share: structural and civil failures, industrial and process accidents, medical and hospital system failures, natural disaster mechanisms, and "what changed" regulatory follow-ups.
- Formats and lengths: 10 to 20 minute long-form as the core, Shorts cut from the diagram segments.
- A publishing cadence that fits the time budget given the higher research and animation cost per video, with hours assigned to research, scripting, sourcing and licensing, animation, narration, editing, and posting.
- Retention tactics for documentary explainers: the moment of failure in the first 30 seconds, the mechanism built up step by step, the investigation's finding, the change it caused.
- A weekly action checklist the owner follows by hand.
Leave monetization out; it is a separate prompt for a later phase.
```

### Step 3. Scripts, hooks, titles, thumbnails

```text
Act as a YouTube content strategist and editor for a documentary explainer channel.
Using the context above, take the top 10 ideas from Step 1 and produce for each:
- 3 title options under 60 characters: name the event and the mechanism, no "shocking", no "caught on camera", no all-caps.
- 1 thumbnail concept: a diagram fragment or the structure before and after, an overlay of 3 words or fewer, no injury imagery.
- The first 30 seconds as a script: the moment of failure as the official report describes it, then the question the video answers.
- A section outline with the mechanism built before the midpoint, the investigation finding after it, the regulatory or design change, and the sources on screen at the end.
- One line on why a viewer stays to the end.
- The citation list the script depends on.
Plain, concrete language. No em dashes, no "it's not X, it's Y" reveals, no engagement bait, no speculation beyond the report.
```

### Step 4. Analytics loop

```text
Act as a YouTube data analyst.
I will paste numbers I export by hand from YouTube Studio (impressions, click-through rate, average view duration, average percentage viewed, returning viewers, subscribers gained, traffic sources, top videos, viewer geography, RPM). You do not have account access and must not ask for it.
Build:
1. A weekly review template that takes 10 minutes: what to record, and what counts as signal versus noise at low view counts.
2. A monthly review template: which case types, lengths, and diagram styles worked, what to repeat, what to stop, and whether RPM is tracking the education median or the news median (which tells us whether the framing is working).
3. Decision rules, for example: low click-through rate with high average view duration means change the thumbnail or title, not the video; a drop-off during the mechanism section means the diagram is too dense, split it.
4. The three metrics that matter most in the first 90 days for a long-form documentary channel and why the others can wait.
State the sample sizes below which a conclusion is premature.
```

### Step 5. Growth mechanics

```text
Act as a YouTube growth strategist with expertise in content discovery.
Using the context above, explain how YouTube surfaces documentary explainers (suggested videos next to large engineering and history channels, search for evergreen "why did X fail" queries, browse, the Shorts feed) in plain terms, focused on what a one-person channel can act on.
Then give a practical growth plan: upload frequency within the time budget, how to test a title or thumbnail with few views, how to build an evergreen library that compounds, how to handle an event-driven spike without becoming a news channel (wait for the preliminary report, then explain it), which Shorts to cut from each long-form video, and how to turn a viewer into a subscriber without begging.
Rules: every engagement action is manual by the owner. No automation, follow-for-follow, engagement pods, or paid views. Mark platform mechanics you cannot verify as [Unverified] with a date.
```

### Step 6. Production workflow

```text
Act as a production manager for a one-person faceless documentary channel.
Using the context above, design a repeatable workflow from case selection to published video and Shorts. Cover: case selection against the "official report exists" rule, primary-source research and citation, script, footage sourcing with a per-clip license log, diagram and animation production, narration (state whether a synthetic voice is used and the label consequence), editing, thumbnail, metadata with sources listed, the AI-content disclosure decision, and the human review and publish step.
Constraints: the publish step is always a person in YouTube Studio; do not propose auto-upload tools. Any tool you recommend must be named with its cost [Unverified] and must not need account passwords or session cookies. Include a quality checklist (every claim cited, every clip logged with its license basis, no graphic injury, victims named only as the report names them, original narrative and diagrams, AI label decision recorded) and estimated hours per step so the total fits the time budget; state the realistic videos per month.
```

### Step 7. Monetization sequence (run after 20 videos or 90 days of data)

```text
Act as a creator business strategist specializing in YouTube monetization for documentary and education channels.
Using the context above and the analytics so far, lay out the revenue options in the order they become realistic: YouTube Partner Program (state current thresholds and mark them [Unverified] with a date), ad revenue as the primary line with the education-versus-news RPM framing explained, sponsorships that fit a documentary audience (education platforms, engineering software, insurance and safety products; state a defensible CPM range and the disclosure wording), licensing the channel's own diagrams and animations, memberships for early access and source packs, newsletter, and a course only if viewers ask.
For each give requirements, pros, limits, and the trigger that says "now is the time".
Rules: no sponsor placement inside the segment that describes casualties; every paid relationship disclosed on screen and in the description; no sponsor that conflicts with the safety message of the video.
```

## Original prompts

The verbatim originals from the source carousel are in `00-prompt-library-neutral.md`, section 4.
