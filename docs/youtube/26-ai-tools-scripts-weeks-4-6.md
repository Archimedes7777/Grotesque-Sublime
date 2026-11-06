# Scripts for weeks 4 to 6

**Produced:** 2026-11-06 from Step 3 of `10-prompts-ai-tools.md`, for ideas 3, 4, and 8 of the Step 1 list, in the channel plan's order. Same format as `22-ai-tools-first-three-scripts.md`: three titles, thumbnail, first 15 seconds verbatim, timed outline, narration draft, and the measured numbers in brackets for the owner to fill from the off-camera run.

Voice rules applied: plain, concrete, declarative. No em dashes. No "it's not X, it's Y" reveals. No engagement bait. One failure shown per video.

---

## Script 4 (week 4, worked workflow): writing a preventive maintenance procedure with AI in 20 minutes, checked against the standard

**Titles (under 60 characters)**
1. Writing a PM procedure with AI in 20 minutes, then checking it
2. AI drafted my PM procedure. The standard caught [N] gaps.
3. From manual to PM procedure with AI: what it missed

**Thumbnail:** two columns, "AI draft" and "after review", with a count of items added in review. Overlay "20 minutes".

**Runtime target:** 12 minutes. **Material needed:** a public or owner-controlled manufacturer manual for a device the owner may show (excerpts only); the relevant standard or guidance summarized in the owner's own words (do not reproduce standard text beyond short quotation); a procedure template with the headers the owner's department uses, generic and unbranded.

**Test design, decided before recording**

| Check | What the AI draft is graded on |
|---|---|
| Completeness | Every inspection, test, and functional check the manual's PM section lists is present |
| Safety | Electrical safety testing is specified with the right test type and limits for the device class, and the limits match the standard the owner cites |
| Order | Visual inspection before power-on; safety tests before performance tests; documentation last |
| Specificity | Each step names a measurable acceptance value, not "verify operation" |
| Hallucination | Any step, value, or interval that is not in the manual or the standard |

**First 15 seconds (verbatim)**
> A preventive maintenance procedure normally takes me an afternoon to write properly. I had an AI draft one from the manual in twenty minutes, then I checked it against the manual and the standard. It was eighty percent there. The missing twenty percent is the part that matters, and here it is.

**Timed outline**

| Time | Segment |
|---|---|
| 0:00 | Cold open |
| 0:15 | The device, the manual, the template, and the rule: the manual and the standard are the authority, the AI is the typist |
| 1:15 | The prompt: the manual's PM section, the template headers, and the instruction to cite the page for every step and mark anything not in the manual |
| 2:30 | The draft, read through at speed; timer on screen |
| 4:30 | Check 1 and 2: completeness and safety; the first gap |
| 6:30 | The failure: [the step the AI invented or the interval it got wrong] |
| 8:00 | Checks 3 to 5: order, specificity, hallucination; the tally |
| 9:30 | The fix: what I add to the prompt now, and the second draft's tally |
| 11:00 | Steps, safety line, disclosure line, next task |

**Narration draft**

(0:15) The device is a [device type]. The manual is one I am allowed to show in short excerpts. The template is the headers my department uses with the branding removed: purpose, scope, tools and test equipment, safety, visual inspection, electrical safety, functional tests, documentation. The rule for this whole video: the manual and the standard are the authority. The AI is the typist, and a typist can mistype.

(1:15) The prompt, on screen. Three parts. The manual's PM section, uploaded. The template headers. And the instruction that does most of the work: "Cite the manual page for every step. If a step, value, or interval is not in the manual, mark it [NOT IN MANUAL] instead of inventing it." Start the timer.

(2:30) [Owner narrates the draft at speed.] Twenty minutes to this point, including the upload and my reading it once. On paper it looks like a procedure. Now we check it.

(4:30) **Completeness.** The manual's PM section lists [X] inspection and test items. The draft has [Y]. The missing ones: [list]. **Safety.** The draft specifies [the electrical safety test it specified] with limits of [value]. The standard I use gives [the correct test type and limit for this device class, in the owner's words]. [Match or mismatch.] This is the first real gap, because a wrong limit passes a device that should fail.

(6:30) **The failure.** [One of: an invented step with no page citation; an interval of "annually" where the manual says six months; a test value that does not appear in the manual.] The prompt told it to mark anything not in the manual. It did not. This is why the check exists, and it is why I will not let a procedure out of the draft stage without the manual open next to it.

(8:00) **Order:** [pass or fail, with the swap if any]. **Specificity:** [count of steps that say "verify operation" without a value]. **Hallucination:** [count]. The tally on screen: [N] items added or corrected in review, out of [total]. Time for the draft: 20 minutes. Time for the review: [R] minutes. Time for me to write it from scratch: [S]. The saving is real. The review is not optional.

(9:30) The fix is two lines in the prompt: "List every PM item from the manual in a table first, then write the procedure from the table," and "For electrical safety, insert the placeholder [OWNER TO SPECIFY TEST AND LIMITS] and nothing else." The first line fixes completeness because the table is checkable. The second line stops the tool from inventing a safety limit at all; that number comes from the standard and from me. Second draft: [tally].

(11:00) Steps on screen: upload the PM section, give the template, demand page citations, forbid safety limits, check against the manual and the standard with a tally. No sponsor on this video. No affiliate links. Device service and PM require manufacturer training and institutional authorization; this is a drafting method, not a procedure you can use. Next: Claude versus ChatGPT on one real work-order backlog.

**Why a viewer stays:** the cold open promised the missing twenty percent; it arrives at 4:30 and 6:30, and the fix with the second tally follows.

---

## Script 5 (week 5, head-to-head): Claude vs ChatGPT on one real work-order backlog

**Titles (under 60 characters)**
1. Claude vs ChatGPT on a real work-order backlog: scored
2. Two AI tools, 50 work orders, one rubric. Here are the scores.
3. Which AI triages a maintenance backlog better? I scored both.

**Thumbnail:** two columns with the two scores. Overlay "50 work orders".

**Runtime target:** 11 minutes. **Material needed:** fifty synthetic work orders in the shape of real ones (device type, symptom as reported, age, location type, priority field blank), generated from real patterns with every identifier removed; the owner's own triage of all fifty done first, as the answer key; the same prompt for both tools.

**Rubric, fixed before the run**

| Dimension | Points | How scored |
|---|---|---|
| Priority agreement | 2 per order | Matches the owner's priority (critical, high, routine) |
| Category agreement | 1 per order | Matches the owner's failure category |
| Invented facts | minus 2 each | Any detail not in the work order |
| Refusals or non-answers | 0 | Counted separately |
| Explanation quality | up to 10 total | Sampled on 10 orders: does the reason given match the reason a technician would give |

Maximum 160. Both tools get the identical prompt and the identical 50 orders. The owner's answer key is on screen before either tool runs.

**First 15 seconds (verbatim)**
> Fifty work orders, the kind that pile up over a weekend. I triaged them myself first, then gave the same fifty to two AI tools with the same instructions and scored both against my answers. One scored [A] out of 160. The other scored [B]. The gap was not where I expected.

**Timed outline**

| Time | Segment |
|---|---|
| 0:00 | Cold open with both scores |
| 0:15 | The backlog: synthetic but real-shaped, no identifiers; the answer key; the rubric |
| 1:30 | The prompt, identical for both, on screen |
| 2:15 | Tool 1 run, results at speed, the scoring |
| 4:15 | Tool 2 run, results at speed, the scoring |
| 6:00 | Where they agreed with me and each other; where they both missed |
| 7:15 | The failure: the order both tools got dangerously wrong |
| 8:30 | The scores by dimension; what the gap is made of |
| 9:45 | What I use now, and the one-line prompt change that closed most of the gap for both |
| 10:30 | Steps, disclosure, next task |

**Narration draft**

(0:15) These fifty work orders are synthetic. I built them from the patterns of real ones: the device types, the way symptoms are reported, the mix of urgent and routine. No serials, no rooms, no names, no site. I triaged all fifty myself before touching either tool, and that is the answer key. Here is the rubric. It was written before the run, and both tools are scored against the same key.

(1:30) The prompt. "For each work order, assign a priority of critical, high, or routine, assign one failure category from this list, and give a one-sentence reason. Use only the information in the work order. If the information is insufficient, say so." Identical for both.

(2:15) [Tool 1 narrated at speed, with the scoring overlay filling in.] Priority agreement: [n] of 50. Category: [n] of 50. Invented facts: [n]. Refusals: [n]. Explanation sample: [n] of 10.

(4:15) [Tool 2, same.]

(6:00) Where they agreed with me: [the easy orders: clear alarms, obvious failures]. Where they both missed: [the pattern, for example, under-prioritizing a vague symptom on a life-support device, or over-prioritizing a cosmetic fault on a critical device]. The miss is the same miss a new technician makes. The tools weigh the words in the symptom; a technician weighs the device.

(7:15) **The failure.** Work order [number]: [the symptom]. Both tools called it routine. It is critical, because [the reason a technician knows and the text does not say]. Neither tool had that knowledge, and neither said the information was insufficient. This is the order I would not let an AI triage unsupervised, and it is the reason the human stays in the loop on anything that touches a patient.

(8:30) Scores by dimension on screen. [A] versus [B]. The gap is mostly [dimension], not [dimension]. On priority, they were [close or not]. On invented facts, [one tool or both] added [details] that were not in the order. On explanations, [which tool] gave reasons a technician would recognize.

(9:45) What I use now: [the owner's honest choice, with the reason]. And the prompt change that helped both: adding one line, "Devices in this list are life-support or critical-care; any symptom on them is at least high priority," with the list. Re-run on the twenty orders that involved those devices: [new agreement]. The tool does not know the device matters. You have to tell it.

(10:30) Steps: build the synthetic set, write your answer key first, fix the rubric, same prompt for both, score, then add what the tool cannot know. No sponsor on this video. No affiliate links. Next: building my first agent for a weekly report, with the failures.

**Why a viewer stays:** the cold open gave both scores but said the gap was not where expected; the explanation arrives at 8:30, after the failure at 7:15.

---

## Script 6 (week 6, worked workflow): building my first agent for a weekly report, no code, with the failures

**Titles (under 60 characters)**
1. I built an AI agent for my weekly report. Here is what broke.
2. My first AI agent, no code: [H] hours a week saved, [F] failures fixed
3. An AI agent writes my weekly report now. It took three tries.

**Thumbnail:** a calendar grid with one hour block shaded, overlay "[H] hrs/week".

**Runtime target:** 13 minutes. **Material needed:** a synthetic weekly dataset in the shape of the owner's real inputs (completed work orders, open items, parts on order, overdue PMs), an agent tool with file access and a scheduled or repeatable task, the owner's report template, and the three attempts recorded.

**What "agent" means in this video (said on screen):** a tool that takes a goal, reads files, runs steps on its own, and produces a result without a prompt for each step. Not a chat box. The permissions it has are listed on screen before it runs.

**First 15 seconds (verbatim)**
> Every Friday I spend about [T] hours turning the week's work orders, open items, and overdue PMs into a report nobody reads closely. I built an agent to write it. The first version lied. The second version read a file it should not have. The third one works, and here is how it got there.

**Timed outline**

| Time | Segment |
|---|---|
| 0:00 | Cold open |
| 0:15 | What an agent is, in one sentence; the inputs; the report template; the permissions it will have, on screen |
| 1:30 | Attempt 1: the goal in plain language; the run; the report looks good |
| 3:30 | The failure, part one: the number that was not in the data |
| 5:00 | Attempt 2: the fix (cite the source file and row for every number); the run; the second failure: it read a file outside the folder |
| 7:00 | The permission fix: scope the agent to one folder, deny everything else; show the denial |
| 8:30 | Attempt 3: the run; the report; the check against the data |
| 10:00 | The measured result: minutes per week before and after; what I still do by hand |
| 11:30 | Steps; the governance note; disclosure; next task |

**Narration draft**

(0:15) An agent, for this video, is a tool that takes a goal, reads the files I give it, runs its own steps, and hands back a result. The inputs are synthetic but real-shaped: a week of completed work orders, open items, parts on order, and overdue PMs, with no identifiers. The template is the one I actually use, unbranded. Before it runs, here are its permissions: read this one folder, write one file, no network, no shell. We will see why that list matters.

(1:30) **Attempt one.** The goal in plain language: "Read the four files in this folder and write the weekly report using the template. Include totals, the top three open issues by age, and the overdue PM count." Run. [Narrate the run.] The report comes back and it reads well. Totals, top three, overdue count, a sentence of summary. If I were in a hurry I would send it.

(3:30) **The failure, part one.** The overdue PM count says [number]. The file says [different number]. I look for where [the wrong number] came from. It is not in any file. The agent summed [the wrong column] or [invented a plausible figure]. A report with one wrong number is worse than no report, because the wrong number travels.

(5:00) **Attempt two.** The fix is the same one from the service-manual video: "For every number, cite the file and the row or column it came from. If a number cannot be sourced, write UNSOURCED." Run. The numbers now carry citations, and the overdue count is right. But watch the log. The agent opened [a file outside the folder: a config file, a note, or a previous report] because it was "looking for context." I did not tell it to. It could, so it did.

(7:00) **The permission fix.** This is the governance series in one minute. The agent's reach is set to the one folder. Everything else is denied. Show the denial on screen: it tries to read the outside file and is refused. The agent then does the task with what it has, which is all it needed. The rule: an agent gets the smallest reach that completes the task, and you find out what that is by watching it overreach once in a place where it cannot do harm.

(8:30) **Attempt three.** Same goal, citations required, one folder. Run. [Narrate.] The report, the citations, and the check: I open each cited row for the five numbers in the report. [Five of five, or the one that was still off.] This is the version I use.

(10:00) The measured result. Before: about [T] hours on Friday. After: the agent runs in [M] minutes and my check takes [C] minutes. Saved: about [H] hours a week. What I still do by hand: read the top three issues and decide whether they are the right three, and write the one sentence at the top that says what the week meant. The agent does arithmetic and assembly. I do judgment.

(11:30) Steps on screen: four input files in one folder, the template, the goal, citations required, one-folder permission, check every number once. The permissions list is the part people skip, and it is the part that would have let attempt two read something that mattered. No sponsor on this video. No affiliate links. Next: agent permissions explained for people who are not developers, which is the full version of the minute at 7:00.

**Why a viewer stays:** the cold open promised two failures and a working third version; the second failure, the permission one, lands at 5:00 to 7:00, and the measured result is at 10:00.

---

## Pre-recording checks for all three

- [ ] Work orders, datasets, and templates are synthetic and real-shaped, with no identifiers, site, or employer name
- [ ] Answer keys and rubrics are written and shown before any tool runs
- [ ] Manual and standard excerpts are short; standard text is paraphrased in the owner's words
- [ ] Bracketed numbers are measured in the off-camera run; none are estimated
- [ ] Safety line present in script 4; "human stays in the loop" line present in script 5; permissions list shown on screen in script 6
- [ ] No sponsor and no affiliate on any of the three until the disclosure policy is adopted and a deal exists
- [ ] AI-label decision recorded (human voice planned)
- [ ] Three title options logged for the Step 4 click-through test
