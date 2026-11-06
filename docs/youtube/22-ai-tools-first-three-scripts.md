# First three scripts: weeks 1 to 3

**Produced:** 2026-11-06 from Step 3 of `10-prompts-ai-tools.md`, for ideas 1, 2, and 5 of the Step 1 list, in the order the channel plan schedules them. Each has three titles, a thumbnail concept, the first 15 seconds verbatim, a timed outline, and a full narration draft. Bracketed items are filled by the owner after the off-camera run; nothing in a bracket may be invented.

Voice rules applied: plain, concrete, declarative. No em dashes. No "it's not X, it's Y" reveals. No engagement bait. One failure shown per video.

---

## Script 1 (week 1, governance): what I never paste into an AI tool at work

**Titles (under 60 characters)**
1. What I never paste into an AI tool at work
2. The 5-question test before anything goes into an AI tool
3. Using AI at work without leaking what you shouldn't

**Thumbnail:** a chat box with a redacted block in it, overlay "5 questions". Same typeface and color pair as every governance episode.

**Runtime target:** 9 minutes. **Material needed:** a screen recording of a chat tool with a demo prompt; the five-question card as an on-screen graphic; one anonymized example from the owner's own work.

**First 15 seconds (verbatim)**
> Eight years in hospital technology taught me that most data leaks are not attacks. They are someone pasting the wrong thing into the wrong box to save ten minutes. AI tools are the newest box. Here are the five questions I ask before anything goes in, and the one time I got it wrong.

**Timed outline**

| Time | Segment |
|---|---|
| 0:00 | Cold open (above) |
| 0:15 | Why this is a habit, not a rule: tools change, the questions do not |
| 1:00 | Question 1: would this be a problem in a public search result? |
| 2:15 | Question 2: is there a name, an identifier, a credential, or an internal address in it? |
| 3:45 | Question 3: does my employer's policy allow this tool for this data? |
| 4:45 | Question 4: does the tool keep it, train on it, or send it on? |
| 5:45 | Question 5: can I do the task with a redacted or synthetic version? |
| 6:30 | The time I got it wrong (anonymized) and what changed |
| 7:30 | How to check you did it right: the 30-second re-read |
| 8:15 | The card on screen; the checklist link; next episode |

**Narration draft**

(0:15) The tools will change. In a year the one on my screen will have a different name and a different privacy page. The questions do not change, which is why I keep them on a card and not in a bookmark. I am going to show each one with a real kind of task from my job, with the details changed.

(1:00) **Question one: if this text showed up in a public search result tomorrow, is that a problem?** This is the fastest filter. Most of what I paste passes it: a paragraph from a standard, a public manual page, my own notes about a procedure. What fails it is obvious once you ask: a work order with a room number and a device serial, an email thread with a colleague's name, anything with the word "incident" in it. On screen: here is a work order as it comes out of our system. Here is the same work order after I ask the question. The device model stays. The serial, the room, and the requester are gone. The AI does not need them to help me plan the repair.

(2:15) **Question two: is there a name, an identifier, a credential, or an internal address in it?** Names are the easy part. Identifiers are the part people miss: a medical record number, an asset tag, an employee ID, a ticket number that links to a patient. Credentials are passwords, keys, and tokens, and they hide in logs and config files more than in prose. Internal addresses are server names and URLs that tell an outsider how your network is laid out. On screen: a log file from a test bench. Watch how the line I actually need, the error message, sits right next to a hostname and a session token. I copy the error line only. The habit is to copy the line, not the file.

(3:45) **Question three: does my employer's policy allow this tool for this data?** This is the one people skip because they assume the answer is no. Often it is "yes, for public and de-identified material" and "no, for patient or employee data," which is the same split questions one and two already made. If there is no policy, ask before, not after. I keep the answer in writing. If you are the one who has to ask, the sentence that works is: "I want to use [tool] for [task] on data that contains no patient, employee, or system identifiers. Is that acceptable?" You will usually get a yes, and now you have it in writing.

(4:45) **Question four: what does the tool do with it?** Three things to find on the privacy or data page: does it keep what you paste, does it train on it, does it send it to a third party. The answers differ between the free tier and the paid business tier of the same product, and they change. I do not memorize them. I check the date on the page and I read the three answers, and I write the date down. On screen: the three answers for the tool I am using today, with today's date. If a tool will not answer the three questions plainly, that is the answer.

(5:45) **Question five: can I do the task with a redacted or synthetic version?** Almost always yes, and it is usually better. The AI does not need the real serial number to help me draft a preventive maintenance procedure. It needs the model and the manual. It does not need the real incident report to help me find a trend; it needs the dates, the device types, and the failure modes with the identifiers removed. On screen: I take a real-shaped report, replace every identifier with a placeholder, and the AI's answer is the same. The synthetic version is also the version I can show you on this channel.

(6:30) **The time I got it wrong.** [Owner fills from their own experience; one anonymized instance, told in four sentences: what was pasted, which question would have caught it, what the consequence was or could have been, what changed. If no such instance exists, replace with the near miss the five-question card was created after.] What changed is the card. It sits next to the keyboard. It takes fifteen seconds.

(7:30) **How to check you did it right.** Before you press enter, read the prompt once more and look only for capital letters and numbers. Capitals catch names and places. Numbers catch identifiers, dates that pin a person, and the parts of keys and tokens. It takes thirty seconds, and it catches most of what the five questions missed.

(8:15) Here is the card. The link in the description has it as one page, free, no email required. Next in this series: how I vet an AI tool or an agent skill before I install it, including the six I rejected and why. Nothing in this video is legal advice; your employer's policy comes first.

**Why a viewer stays to the end:** the promise in the cold open was "the one time I got it wrong," and it arrives at 6:30, after the five questions, which is after the midpoint.

---

## Script 2 (week 2, worked workflow): I gave an AI agent a 40-page service manual. Here is what it got wrong.

**Titles (under 60 characters)**
1. I gave an AI a 40-page service manual. Here is what it got wrong.
2. AI vs a service manual: [N] errors in [M] answers
3. Can AI read a service manual? A technician checks every answer.

**Thumbnail:** the manual's cover with the title blurred, a counter reading "[N] wrong of [M]". The number comes from the recorded run; no number on the thumbnail until it is measured.

**Runtime target:** 12 minutes. **Material needed:** a service manual the owner may show on screen (owner-controlled or decommissioned equipment, and pages shown within fair use: short excerpts, never whole sections); a chat tool with file upload; a scoring sheet with twelve questions prepared before the run.

**Test design, decided before recording**

| Question type | Count | Example | Scoring |
|---|---|---|---|
| Direct lookup (a value on a page) | 4 | What is the specified leakage current limit? | Correct value with the page cited, or wrong |
| Procedure (ordered steps) | 4 | List the steps to enter service mode | All steps in order, or missing or reordered |
| Judgment (the manual does not say) | 2 | Is this fault safe to leave until the next shift? | Correct answer is "the manual does not say"; any invented answer is wrong |
| Cross-reference (two pages) | 2 | Which alarm maps to which test in the troubleshooting table? | Correct mapping, or wrong |

Each answer is checked against the page on camera. The failure segment covers the first judgment question the tool answers with confidence.

**First 15 seconds (verbatim)**
> This is a forty-page service manual for a [device type] I am allowed to show you. I uploaded it to an AI tool and asked twelve questions a technician actually asks. It got [N] wrong. Two of those it got wrong with total confidence, and that is the part that matters.

**Timed outline**

| Time | Segment |
|---|---|
| 0:00 | Cold open with the result |
| 0:15 | The device, why this manual, what is and is not shown (fair use, no serials), the twelve questions on screen |
| 1:30 | The upload and the first four lookup questions, checked against the page |
| 4:00 | The four procedure questions; the first reordering error |
| 6:00 | The two judgment questions: the confident wrong answer |
| 7:30 | The two cross-reference questions |
| 8:30 | The scoresheet; where it is reliable and where it is not |
| 9:45 | The fix: how I prompt it now (cite the page or say "not in the manual"), and the re-run score |
| 11:00 | Reproducible steps; the disclosure line; next task |

**Narration draft**

(0:15) The device is a [device type], decommissioned, which is why I can show it. I am showing short excerpts of the manual, not the whole thing, and I have removed anything with a serial number or a site name. Here are the twelve questions. I wrote them before I uploaded anything, and I wrote the right answers from the manual first, so the AI is being graded against the page, not against me.

(1:30) Upload. The first four are lookups: a value on a page. [Narrate each: the question, the answer, the page, correct or wrong.] [Owner fills from the run.] Lookups are where these tools are strongest, and the pattern to notice is that when it is right it usually tells you the page, and when it is wrong it usually does not.

(4:00) Procedures are different. Order matters. [Narrate each.] Here is the first real error: step [X] and step [Y] are swapped. On the bench that swap would mean [consequence, from the manual's own warning if there is one]. The text is in the manual. The tool read it and reordered it.

(6:00) Now the two questions the manual does not answer. I asked whether a particular fault is safe to leave until the next shift. The manual does not say. The correct answer is "the manual does not say." The tool said [quote the answer]. It is confident, it is plausible, and it is invented. This is the failure mode that matters more than the swapped steps, because a swapped step looks wrong when you read it and an invented judgment looks right.

(7:30) Cross-references: [narrate each]. [Score.]

(8:30) The scoresheet. [N] wrong of twelve. Lookups: [a] of 4. Procedures: [b] of 4. Judgment: [c] of 2. Cross-reference: [d] of 2. The tool is a fast index to the manual and a bad substitute for it. Time to answer all twelve with the tool: [T1]. Time for me to find all twelve by hand: [T2]. The time saving is real and the error rate is the price.

(9:45) The fix is in the prompt, and it is one sentence: "Answer only from the uploaded document, cite the page for every answer, and if the document does not contain the answer, say so." Re-run. [Score after the fix.] The judgment questions now return "the manual does not say," which is the right answer. The swapped procedure is [fixed or still wrong]. The lesson is that the tool can be told to admit ignorance and it mostly will, but you still check the page.

(11:00) Steps on screen: write the questions and answers first, upload, one sentence in the prompt, check every page citation, time both ways. No sponsor on this video. No affiliate links. Device service requires manufacturer training and institutional authorization; this video is a reading test, not a repair guide. Next task: writing a preventive maintenance procedure with AI in twenty minutes and checking it against the standard.

**Why a viewer stays to the end:** the cold open promised two confident wrong answers; they arrive at 6:00, and the fix with the re-run score is after that.

---

## Script 3 (week 3, governance): how to vet an AI tool or skill before you install it

**Titles (under 60 characters)**
1. How I vet an AI tool before I install it (10 minutes)
2. The 10-minute check that caught 6 bad AI skills
3. Before you install that AI skill: read this first

**Thumbnail:** a folder icon with a magnifier over it, overlay "read everything".

**Runtime target:** 11 minutes. **Material needed:** screen recording of a scratch directory with a cloned skill repository; the admission criteria and install procedure from the owner's own policy; the anonymized story of the "superpowers" clones.

**First 15 seconds (verbatim)**
> Last month I found six different people publishing the same AI skill package, each claiming between four hundred thousand and nine hundred thousand installs. Same files, six names. Inside: ten commands that download a script from the internet and run it without showing you, a login to a social account, and automation that likes and follows for you. Here is the ten-minute check that caught it.

**Timed outline**

| Time | Segment |
|---|---|
| 0:00 | Cold open |
| 0:15 | What a "skill" is in plain terms, and why it is code even when it is text |
| 1:15 | Rule zero: install counts and stars are not trust |
| 2:00 | Step 1: clone it into a scratch folder; execute nothing |
| 3:00 | Step 2: read every file; the five things to search for |
| 5:30 | The six rejected skills, what each contained (the example from the cold open) |
| 7:00 | Step 3: install only through a path that asks you; then diff the installed copy against what you read |
| 8:30 | Step 4: record what you reviewed so you can tell if it changes |
| 9:30 | How to check you did it right; the checklist line this adds; next episode |

**Narration draft**

(0:15) A skill, in the tools I use, is a folder of instructions an AI agent reads and follows. It looks like documentation. It behaves like a program, because the agent will do what it says with whatever permissions the agent has. If the instructions say "run this installer," the agent runs the installer. So I treat every skill as code, even when it is only Markdown.

(1:15) Rule zero: install counts, stars, and a familiar name are not trust. The six copies I mentioned borrowed the name of a well-known project and advertised install numbers that no one can verify. The number is a marketing field. Trust comes from reading the files and from a named maintainer with a public history, and from nothing else.

(2:00) **Step one.** Clone the repository into a scratch folder that has nothing else in it. Do not open it in a tool that executes things. Do not run its install command. On screen: a fresh folder, the clone, and nothing else. If a project says "just run this one line to install," that line is the first thing I read, not the first thing I run.

(3:00) **Step two.** Read every file. Every one. Then search the folder for five things. First: anything that downloads and runs, which in practice means the words "curl", "wget", "pipe", "sh", or "npx" near each other. Second: any request for a login, a password, a cookie, a session, or an "auth token" to a third-party service. Third: any automation of likes, follows, comments, or messages, which breaks every platform's rules and gets accounts suspended. Fourth: hidden text, which means characters you cannot see, HTML comments, and very long lines; I run a search for non-printing characters and I look at line lengths. Fifth: outbound addresses, every URL, and whether each one is a documentation page or a download. On screen: the searches, one at a time, on a real skill that passes, so you can see what clean looks like.

(5:30) Now the six that did not pass. [Owner narrates from the security register: name-squatting on an established project; ten instances of a pipe-to-shell installer; a third-party login to a social platform; engagement automation.] Any one of those four is a rejection. These had all four. They are still published. The install counts are still on the page.

(7:00) **Step three.** When a skill passes, install it only through a path that asks you first. In my setup, every install command is set to require my approval, so the agent cannot add a skill on its own. After the install, compare the installed folder against the copy you read, file by file. If they differ, stop. A difference means the installer put something there that you did not review.

(8:30) **Step four.** Record what you reviewed: the project, the commit or version, the date, and your decision. I keep a short register with one line per skill. Then make the tool check it for you: I keep a hash of every skill file, and every time the agent starts, it re-checks every file against the hash. If a file changed, the agent is told not to use the skill until I look. A monthly job compares each skill with its source and opens a note if the source has moved on. None of that is exotic. It is a list of hashes and a script that compares them.

(9:30) How to check you did it right: open the register and ask whether you could show someone exactly what you read and when. If the answer is yes, the check is done. The checklist line this episode adds: "read every file, execute nothing, record the version." The one-page checklist is in the description. Next: agent permissions explained for people who are not developers, which is what makes step three work.

**Why a viewer stays to the end:** the cold open promised the story of the six clones; it arrives at 5:30, after the method, and steps three and four follow it.

---

## Pre-recording checks for all three

- [ ] Material is owner-controlled, decommissioned, de-identified, or public; fair-use excerpts only for manual pages
- [ ] No serials, room numbers, requester names, hostnames, tokens, or employer name on screen
- [ ] The failure segment is real and was found in the off-camera run; the bracketed numbers are measured, not estimated
- [ ] Safety line present in script 2; "not legal advice, employer policy first" line present in scripts 1 and 3
- [ ] No sponsor and no affiliate link in scripts 1 and 3 (governance rule); script 2 carries the "no sponsor" line
- [ ] AI-label decision recorded (human voice planned)
- [ ] Three title options logged for the Step 4 click-through test
