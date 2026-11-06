# Governance series: "Safe AI at Work", a 10-video arc

**Purpose:** the Governed AI pillar from `21-ai-tools-step2-channel-plan.md`, expanded into a sequenced series with a lead magnet. The source material is this repository: `SECURITY.md`, `CLAUDE.md`, the command guard, the session-start integrity check, `scripts/verify-skills.mjs`, and the docs on account hardening, sandbox setup, and incident response. Every episode records something the owner has already built and runs, which is the series' credibility and its inauthentic-content defense.

**Audience:** professionals inside institutions with rules, who use AI tools without a security background. The series never teaches an attack. It teaches habits, decisions, and checks.

## 1. Sequence

Episodes are numbered for the series playlist and mapped to the channel plan's week where one is scheduled. Idea numbers refer to the Step 1 list.

| Ep | Title (working) | Idea | Week | The one habit it leaves behind | Repository source |
|---|---|---|---|---|---|
| 1 | What I never paste into an AI tool at work, and the test I use | #1 | 1 | The five-item "can this leave the building" test | `SECURITY.md` sections 2 and 5; `.gitignore` secret rules |
| 2 | How to vet an AI tool or skill before you install it | #5 | 3 | The ten-minute admission check: read it all, execute nothing, look for installers and credential asks | `SECURITY.md` section 4.1 and 4.2; the superpowers-clone rejection in 4.4 |
| 3 | AI agent permissions explained for people who are not developers | #7 | 7 | Deny, ask, allow: a permission map on one page | `.claude/settings.json` rules; `CLAUDE.md` non-negotiables |
| 4 | Six AI "skills" I rejected and why | #11 | 13 | Red flags by example: name-squatting, pipe-to-shell, third-party logins, engagement bots | `SECURITY.md` section 4.4 register |
| 5 | How I keep AI from touching secrets: the setup | #24 | 15 | Secrets live in environment variables the agent cannot read; show the read being denied | `SECURITY.md` section 5; the command guard's secret-file block |
| 6 | The AI wrote a confident wrong answer. Here is how I caught it. | #9 | 17 | The three-step check: source, reproduce, cross-tool | Workflow videos' failure segments |
| 7 | Agent sandboxing for normal people: what it is and when you need it | #21 | 19 | A decision rule: if it can run commands, it runs in a box | `docs/sandbox-setup.md` |
| 8 | What an AI incident looks like at work and the five steps I follow | #17 | 21 | Stop, contain, rotate, report, review | `docs/incident-response.md` |
| 9 | Locking down the accounts behind your AI tools | new | 23 | Passkeys first, SMS never, quarterly app review | `docs/account-hardening-checklist.md`; `SECURITY.md` section 6 |
| 10 | Verifying what you installed is still what you reviewed | new | 25 | Hash it once, check it every session; the integrity check explained without code | `scripts/verify-skills.mjs`; the session-start hook; the upstream drift watch |

Episodes 1, 2, 3, 5, and 8 are the spine. If the budget forces cuts, the other five become Shorts or viewer-problem videos.

## 2. Shape of a governance episode (8 to 12 minutes)

| Time | Segment |
|---|---|
| 0:00 to 0:20 | The risk in one plain sentence, and the one habit the viewer will have by the end |
| 0:20 to 1:00 | A real example from the owner's own vetting or incident log, anonymized |
| 1:00 to 6:00 | The habit, shown being done on screen, at the speed a non-developer can follow |
| 6:00 to 8:00 | "How to check you did it right": the verification step |
| 8:00 to end | The one-page summary on screen; the lead magnet link; no sponsor, no affiliate, ever |

Titles are calm and declarative. Thumbnails show the checklist item or the denied action, never a hooded figure or a red warning triangle.

## 3. Lead magnet: the "Safe AI at Work" one-page checklist

A single Markdown and PDF page, linked from every governance episode and from the channel description. Draft content, to be refined after episode 1 is recorded:

**Before you paste**
- [ ] Would this be a problem if it appeared in a public search result? If yes, do not paste it.
- [ ] Does it contain a name, an identifier, a patient or customer, a password, a key, or an internal hostname? Remove it first.
- [ ] Does my employer's policy allow this tool for this data? If unsure, ask before, not after.

**Before you install**
- [ ] Read every file. Execute nothing. Look for installers that download and run, requests for logins or cookies, and automation of likes, follows, or messages.
- [ ] Who maintains it? A named person with a public history, or a name that copies a popular project?
- [ ] Record what you reviewed (the version or commit) so you can tell if it changes later.

**While it runs**
- [ ] Does the tool have only the permissions the task needs? Can it read secrets? Can it run commands? Can it send anything out?
- [ ] If it can run commands, is it in a sandbox?
- [ ] Verify the output: find the source, reproduce one result, check a second tool.

**When something goes wrong**
- [ ] Stop the tool. Contain what it touched. Rotate any secret it could have seen. Report it. Review what to change.

**Every quarter**
- [ ] Review connected apps on every account. Confirm recovery methods. Re-check that installed tools still match what you reviewed.

## 4. Series rules

- No sponsor segment and no affiliate link in any governance episode (policy in `24-ai-tools-disclosure-policy.md`, section 1.6).
- No offensive technique, ever. Where an attack must be named to explain a defense, it is described in one sentence and never demonstrated.
- Every claim about a platform's behavior is dated on screen.
- Every episode ends with the checklist item it added, so the lead magnet grows in step with the series.

## 5. How the series pays

It will not carry ads as well as the workflow videos (security content monetizes fewer views than tutorials), and it carries no sponsors by rule. Its return is indirect: it is the reason a department head subscribes, the reason a vendor approaches, the basis for the paid "Safe AI at Work" workshop in Step 7, and the thing no tool-of-the-week channel can copy.
