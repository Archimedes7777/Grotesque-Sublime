# Prompt library: cybersecurity and privacy for non-experts

**Niche rank:** 2 of 5 (score 77). See `01-niche-research.md` for the evidence.

**Thesis:** security content on YouTube splits into expert-to-expert (certifications, exploit walkthroughs) and fear-driven consumer clickbait. The gap is calm, practical protection for people with something to lose: small-business owners, clinicians, professionals using AI tools, families. One source rates it the least crowded of the high-value faceless niches. VPN, password-manager, and identity-protection vendors are among the biggest sponsors on YouTube.

**Why it fits the owner:** the zero-trust policy, skill-vetting procedure, and incident runbook in this repository are already the outline of a series on securing AI agents and online accounts.

**Main risks:** fear-based framing damages trust and attracts the wrong sponsors; advice must be current (platforms change settings); never demonstrate attacks against systems the owner does not own.

## Context block (paste before every prompt)

```text
Context for every answer:
- Project name: [working title]. Channel handle: not created yet.
- What the channel is about: practical security and privacy for non-experts, with a focus on people who now use AI tools and agents: how to lock down accounts, vet software and AI skills, avoid phishing, and set up zero-trust habits without becoming a security engineer.
- Why me: AI and prompt engineer with about 8 years in healthcare technology management (a regulated, device-security-aware field) who has written and enforced zero-trust policies for AI agents, including supply-chain vetting of agent skills and hash-locked integrity checks.
- Target viewer: ages 25 to 55 in the US, UK, Canada, or Australia; small-business owners, healthcare and technical professionals, freelancers, and parents. They search "is X safe", "how to secure my Y account", "passkeys explained", "is this AI tool safe to use". They do not want to learn exploits; they want a checklist and a reason.
- Formats available: screen recording with voiceover (primary), diagrams and slides with voiceover, talking head optional, Shorts cut from long-form.
- Assets on hand: a public repository of security policy, hooks, and verification scripts for AI agents; an account-hardening checklist; an incident-response runbook; real examples of name-squatting skill packages and credential-requesting tools found during vetting.
- Time budget: [hours] per week for research, production, and posting, by one person.
- Goal for the first 90 days: 30 long-form videos, Partner Program thresholds in progress, a published checklist as a lead magnet, 1 sponsor conversation with a password-manager or passkey vendor.
- Constraints: demonstrate only on systems and accounts the owner controls; no exploit tutorials; no naming of private individuals; no fear-based thumbnails; sponsors disclosed and never allowed to change a recommendation; advice dated on screen because platform settings change.
- Rules: every post is a draft a person reviews and publishes by hand; no automated likes, follows, comments, DMs, or uploads; no tool receives passwords, cookies, or tokens; AI-generated or altered content gets the platform's label where its rules require it.
- Mark [Unverified] any platform threshold, policy, or price you cannot confirm, with the date of your knowledge.
```

## Niche-specific notes for all prompts

- **Category positioning:** education, not news. A breach-of-the-week format drifts into News & Politics (measured median RPM $2.60) and into templated territory.
- **Sponsor fit:** password managers, passkey hardware, identity monitoring, privacy-respecting email. Decline VPN sponsors whose claims the owner cannot stand behind; the audience will notice.
- **Dated advice:** every settings walkthrough states the date and the app version on screen.
- **Defensive only:** the channel teaches protection. Offensive demonstrations are out of scope and conflict with the repository policy.

## Prompts in recommended order

### Step 1. Niche evaluation

```text
Act as a YouTube market researcher and channel strategist.
Using the context above, evaluate "security and privacy for non-experts, including AI tool safety" as a niche. Cover: audience demand and search intent (top 20 search phrases grouped by audience: business owners, professionals, families), competition (name 5 to 8 comparable channels and what each does well and does not do), monetization ceiling (ads, sponsors, affiliates, products), content sustainability over 2 years, and the angle the owner's AI-agent security work gives that nobody else in the niche has.
Define the ideal viewer in one paragraph, recommend 3 to 4 content categories, and give 30 video ideas ranked by expected pull for a new viewer, each tagged Short or long-form, with the concrete outcome the viewer gets (an account locked down, a decision made, a habit changed).
Exclude any idea that requires demonstrating an attack on a system the owner does not control.
```

### Step 2. Channel plan

```text
Act as a YouTube strategist.
Using the context above, write a 12-week plan with:
- Positioning statement (one sentence) and a channel description under 1,000 characters that signals calm competence, not fear.
- Content pillars with a target share: account and device hardening walkthroughs, AI tool and agent safety (vetting, permissions, what to never paste), scam and phishing recognition by example, and a monthly "what changed" update.
- Formats and lengths: which pillars are 8 to 15 minute long-form, which are Shorts.
- A publishing cadence that fits the time budget, with hours assigned to research, recording, editing, and posting.
- Retention tactics: the risk in one sentence, the fix shown in full, the "how to check you did it right" step at the end.
- A weekly action checklist the owner follows by hand.
Leave monetization out; it is a separate prompt for a later phase.
```

### Step 3. Scripts, hooks, titles, thumbnails

```text
Act as a YouTube content strategist and editor for a security education channel.
Using the context above, take the top 10 ideas from Step 1 and produce for each:
- 3 title options under 60 characters: specific and calm, name the account or tool and the outcome, no "hackers", no "you're being watched", no all-caps.
- 1 thumbnail concept: the app or setting, a checkmark or lock state, and an overlay of 3 words or fewer; no fear imagery.
- The first 15 seconds as a script: what goes wrong for people who skip this, in one plain sentence, then what the viewer will have done by the end.
- A section outline with the fix completed before the midpoint, the verification step after it, and the recap of the 3 to 5 actions at the end.
- One line on why a viewer stays to the end.
Plain, concrete language. No em dashes, no "it's not X, it's Y" reveals, no engagement bait.
```

### Step 4. Analytics loop

```text
Act as a YouTube data analyst.
I will paste numbers I export by hand from YouTube Studio (impressions, click-through rate, average view duration, average percentage viewed, returning viewers, subscribers gained, traffic sources, top videos). You do not have account access and must not ask for it.
Build:
1. A weekly review template that takes 10 minutes: what to record, and what counts as signal versus noise at low view counts.
2. A monthly review template: which topics, audiences, and formats worked, what to repeat, what to stop, and which videos went stale because a platform changed its settings.
3. Decision rules, for example: low click-through rate with high average view duration means change the thumbnail or title, not the video; a search-driven video with falling views after a platform update means re-record, not re-promote.
4. The three metrics that matter most in the first 90 days and why the others can wait.
State the sample sizes below which a conclusion is premature.
```

### Step 5. Growth mechanics

```text
Act as a YouTube growth strategist with expertise in content discovery.
Using the context above, explain how YouTube surfaces how-to and explainer videos (search intent, suggested videos, browse, the Shorts feed) in plain terms, focused on what a one-person channel can act on.
Then give a practical growth plan: upload frequency within the time budget, how to test a title or thumbnail with few views, how to capture search demand that spikes after a public breach without becoming a news channel, which Shorts to cut from each long-form video, and how to turn a viewer into a subscriber without begging.
Rules: every engagement action is manual by the owner. No automation, follow-for-follow, engagement pods, or paid views. Mark platform mechanics you cannot verify as [Unverified] with a date.
```

### Step 6. Production workflow

```text
Act as a production manager for a one-person security education channel.
Using the context above, design a repeatable weekly workflow from idea to published video and Shorts cut from the same recording. Cover: topic selection and fact-checking against primary sources (vendor documentation, CISA, NIST), script, screen recording on a clean test account with all real identifiers redacted, voiceover, editing, thumbnail, metadata, the AI-content disclosure step, and the human review and publish step.
Constraints: the publish step is always a person in YouTube Studio; do not propose auto-upload tools. Any tool you recommend must be named with its cost [Unverified] and must not need account passwords or session cookies. Include a quality checklist (no real credentials or recovery codes on screen, advice dated on screen, sponsor disclosure, no offensive techniques, AI label if a synthetic voice is used) and estimated minutes per step so the total fits the time budget.
```

### Step 7. Monetization sequence (run after 30 videos or 90 days of data)

```text
Act as a creator business strategist specializing in YouTube monetization for security and privacy education.
Using the context above and the analytics so far, lay out the revenue options in the order they become realistic: YouTube Partner Program (state current thresholds and mark them [Unverified] with a date), affiliate programs for password managers, passkey hardware, and privacy tools (rank by recurring commission and whether the owner uses the product), sponsorships (state a defensible CPM range and the disclosure wording, and list sponsor categories to decline), a paid hardening checklist or workshop for small businesses, consulting, memberships, newsletter.
For each give requirements, pros, limits, and the trigger that says "now is the time".
Rules: sponsorships never change a recommendation and are disclosed on screen and in the description; no sponsor whose product the owner would not use; no fear-based upsells.
```

## Original prompts

The verbatim originals from the source carousel are in `00-prompt-library-neutral.md`, section 4.
