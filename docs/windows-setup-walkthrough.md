# Windows setup walkthrough: making the security hooks actually run

This guide fixes one problem: **on this Windows PC, none of the security hooks in `.claude/` have been running.** It explains every word it uses, then walks through the fix one small step at a time. Written 2026-11-03.

Do each numbered step in order. Each one ends with a check so you know it worked before moving on. If a check fails, stop and ask Claude, pasting the exact text you saw.

---

## Part 0: The words

**Terminal.** A window where you type commands instead of clicking. Windows comes with two: PowerShell (the newer one, blue icon) and Command Prompt (the old black one). You will mostly use a third one, Git Bash, which you are about to install.

**Shell.** The program inside the terminal that reads what you type and runs it. PowerShell is a shell. Bash is another shell. They speak different languages: `Get-ChildItem` in PowerShell does what `ls` does in Bash.

**Bash.** The shell used on Linux and Mac. All of this repository's security scripts (the files ending in `.sh`) are written in Bash. Windows does not have Bash built in, so you need to install one.

**Git.** A program that tracks changes to files, like a very detailed "undo history" that you can share. This repository is a Git repository. "Commit" means "save a labeled snapshot of my changes into that history."

**Git for Windows / Git Bash.** When you install Git on Windows, it brings a copy of Bash along with it, called Git Bash. This is the Bash that Claude Code looks for when it needs to run `.sh` scripts. **This is the one piece that is missing on your PC.**

**WSL (Windows Subsystem for Linux).** A way to run a whole small Linux computer inside Windows. You have two installed: Ubuntu and Kali. WSL also provides a file called `bash.exe` in Windows' system folder. That `bash.exe` is not Git Bash. It starts the Linux computer and hands your command to it, and that Linux computer cannot understand Windows paths like `Z:\Repos\...`. **This is why the hooks silently failed: Claude Code found WSL's `bash.exe`, which could not open the hook file.**

**Hook.** A small script that Claude Code runs automatically at certain moments. This repository has two:
- `verify-skills-on-start.sh` runs when a session starts and checks that no skill file has been tampered with.
- `zero-trust-guard.sh` runs before every shell command Claude tries, and blocks dangerous ones (like downloading a script and running it in one go, or reading a secrets file).

**Fail open / fail closed.** When a safety check breaks, does the door stay open or shut? *Fail closed* means "if the check cannot run, block everything." *Fail open* means "if the check cannot run, allow everything." You want fail closed. The hook was designed to fail closed, but a line-ending problem (next word) made it fail open.

**Line endings (LF vs CRLF).** Every text file marks where each line ends with an invisible character. Linux and Mac use one character (called LF). Windows uses two (called CRLF). Bash expects LF. When a Bash script has CRLF endings, Bash sees a stray invisible character at the end of each line, gets confused, and quits. The guard script quits in a way that Claude Code reads as "nothing to report, go ahead," which is the fail-open problem. The repository files on your disk currently have CRLF endings. A new file, `.gitattributes`, now tells Git to always give you LF endings for scripts, but the files already on disk must be refreshed once.

**Node.js (`node`).** A program that runs JavaScript files outside a browser. Two of this repository's checks (`verify-skills.mjs` and `check-upstream.mjs`) are JavaScript and need it.

**jq.** A small tool that reads and writes JSON (a structured text format). The test script for the guard uses it.

**winget.** Windows' built-in app installer that you run from a terminal. It downloads software from Microsoft's checked catalog. You already have it.

**`settings.json`.** The file at `.claude/settings.json` where Claude Code's permission rules and hooks are listed. Editing it is a "control change" in `SECURITY.md`, so Claude always asks you before touching it.

**Sandbox.** A fence around commands so they physically cannot reach files or websites outside a list, even if a rule is bypassed. Optional extra layer, covered at the end.

---

## Part 1: Should you use WSL for Claude Code?

**No. Stay on plain Windows.** Here is why, in plain terms:

| | Plain Windows + Git Bash (recommended) | Claude Code inside WSL |
|---|---|---|
| What changes | Install three programs. Nothing else moves. | Install Claude Code again inside Ubuntu, move or re-clone the repository into Linux's own disk area, learn Linux file paths |
| Security | Same hooks, same rules, same guard. Windows sandbox available with `/sandbox install` | Same hooks and rules. Linux sandbox is slightly stronger, but only if you set it up |
| Risk of mistakes | Low | Higher: two copies of settings, two places files can live, and WSL's own `bash.exe` on Windows still causes the exact confusion you have now |
| Your desktop app | Works as it does today | The desktop app runs on Windows; mixing it with a Linux-side Claude Code adds confusion |

The one thing that must change is which Bash Claude Code finds. Installing Git for Windows fixes that. You do not need to uninstall WSL. It is not hurting anything; it is simply not the right Bash for this job. If you never use Ubuntu or Kali, removing them later is a small tidy-up, not a security requirement.

---

## Part 2: Install the three missing programs

You do these yourself in **your own** PowerShell window, not through Claude. Installing software is exactly the kind of action `SECURITY.md` wants a human to do by hand.

### Step 2.1: Open PowerShell as yourself (not as administrator)

1. Press the Windows key.
2. Type `PowerShell`.
3. Click **PowerShell 7** (or **Windows PowerShell** if 7 is not listed). Do **not** choose "Run as administrator."

### Step 2.2: Install Git for Windows

Paste this line and press Enter:

```bash
winget install --id Git.Git -e --source winget
```

Wait for it to say "Successfully installed." It may take a minute or two.

**Check:** close PowerShell completely, open a new one the same way, and run:

```bash
git --version
```

You should see something like `git version 2.5x.x.windows.1`. If it says "not recognized," restart your PC and try the check again (Windows sometimes needs a restart to learn about new programs).

### Step 2.3: Install Node.js

```bash
winget install --id OpenJS.NodeJS.LTS -e --source winget
```

**Check** (in a fresh PowerShell window):

```bash
node --version
```

Expect a version number starting with `v`.

### Step 2.4: Install jq

```bash
winget install --id jqlang.jq -e --source winget
```

**Check** (fresh window):

```bash
jq --version
```

Expect `jq-1.x`.

### Step 2.5: Tell Git how to handle line endings on this PC

This is a one-time setting for your user account. It tells Git: "when I save files, store them with LF endings; when I open them, leave them as stored." It prevents the CRLF problem from coming back on other projects too.

```bash
git config --global core.autocrlf input
```

No output means it worked. **Check:**

```bash
git config --global core.autocrlf
```

Expect the single word `input`.

---

## Part 3: Open the repository in Git Bash

From here on, use **Git Bash**, not PowerShell. Reason: when you type `bash` in PowerShell, Windows still finds WSL's copy first. Git Bash avoids the mix-up entirely.

### Step 3.1: Open Git Bash in the repository folder

1. Open File Explorer and go to `Z:\Repos\Grotesque-Sublime`.
2. Right-click on an empty area inside the folder.
3. Choose **Open Git Bash here**. (On Windows 11 you may need to click **Show more options** first.)

A black window opens. The last part of the line should mention `Grotesque-Sublime`. If it does not, type `cd /z/Repos/Grotesque-Sublime` and press Enter. Note the slashes lean the other way and the drive letter has no colon: that is how Git Bash spells Windows paths.

### Step 3.2: Confirm you are in the right place

```bash
git status
```

You should see `On branch main` and a list of changed files, including:

- `.claude/hooks/zero-trust-guard.sh`
- `scripts/test-guard.sh`
- `SECURITY.md`
- `.gitattributes` (listed under "Untracked files")
- `docs/windows-setup-walkthrough.md` (this file, also untracked)

Those are the changes Claude drafted. Nothing is saved to history yet.

---

## Part 4: Save the drafted changes and fix the line endings

### Step 4.1: Look at what changed (optional but good habit)

```bash
git diff .claude/hooks/zero-trust-guard.sh
```

Lines starting with `+` were added, `-` were removed. Press `q` to leave the view. You do not need to understand every pattern; you are confirming the file changed in the areas Claude described (PowerShell rules, Windows path separators).

### Step 4.2: Stage and commit the drafted changes

"Stage" means "put these in the box." "Commit" means "seal the box with a label."

```bash
git add .gitattributes .claude/hooks/zero-trust-guard.sh scripts/test-guard.sh SECURITY.md docs/windows-setup-walkthrough.md
```

```bash
git commit -m "Guard the PowerShell tool and force LF endings on scripts"
```

**Check:**

```bash
git log --oneline -1
```

The first line should show your commit message.

### Step 4.3: Renormalize (convert stored line endings to LF)

This asks Git to re-save every file following the new `.gitattributes` rules. It changes only how line endings are stored.

```bash
git add --renormalize .
```

```bash
git status
```

If it lists modified files, commit them:

```bash
git commit -m "Normalize line endings to LF"
```

If `git status` says "nothing to commit," that is fine too; it means the stored copies were already LF and only your on-disk copies were CRLF.

### Step 4.4: Refresh the files on disk so they have LF endings

Git only rewrites a file on disk when it has a reason to. Deleting the scripts and asking Git to put them back is the simplest way to force a fresh copy with the right endings. This is safe: the files are in Git's history and come straight back.

```bash
rm .claude/hooks/zero-trust-guard.sh .claude/hooks/verify-skills-on-start.sh scripts/test-guard.sh
```

```bash
git checkout -- .claude/hooks scripts/test-guard.sh
```

**Check** that the invisible CRLF character is gone. This counts how many lines contain it; you want `0`:

```bash
grep -c $'\r' .claude/hooks/zero-trust-guard.sh .claude/hooks/verify-skills-on-start.sh scripts/test-guard.sh
```

Expect three lines, each ending in `:0`.

---

## Part 5: Run the repository's own checks

Still in Git Bash, in the repository folder.

### Step 5.1: Guard regression tests

```bash
bash scripts/test-guard.sh
```

Expect the last line: `guard tests: 90 passed, 0 failed`. If any line starts with `FAIL`, copy the whole output and ask Claude.

### Step 5.2: Skill integrity

```bash
node scripts/verify-skills.mjs
```

Expect lines starting with `ok` and no line starting with `FAIL`.

---

## Part 6: Make the guard cover PowerShell in `settings.json`

Right now `settings.json` only attaches the guard to the Bash tool. This step attaches it to the PowerShell tool as well and adds matching permission rules. **Do this only after Part 5 passes.** Once applied, every PowerShell command Claude runs goes through the guard, and if Bash were still broken, every command would be blocked (that is the fail-closed design working).

Easiest path: open Claude Code in this folder and say:

> Apply the settings.json PowerShell change from the walkthrough.

Claude will make the edit and the permission system will **ask you to approve** it, because `settings.json` is a protected control file. Read the prompt, confirm it names `.claude/settings.json`, and approve.

What the change does, so you can recognize it:

1. In the `PreToolUse` hook, `"matcher": "Bash"` becomes `"matcher": "Bash|PowerShell"`.
2. Every `Bash(...)` rule in `deny` and `ask` gets a twin spelled `PowerShell(...)`.
3. New `ask` rules for Windows installers: `Install-Module`, `Install-Package`, `Install-Script`, `winget install`, `choco install`, `scoop install`.

Then commit it (Claude can do this, or you can in Git Bash):

```bash
git add .claude/settings.json && git commit -m "Attach the guard to the PowerShell tool"
```

---

## Part 7: Prove the hooks now run

1. **Quit the Claude desktop app completely** (right-click its tray icon and choose Quit, or close it and confirm it is not in the system tray). It must restart to notice Git Bash.
2. Open it again and start a **new** session in `Z:\Repos\Grotesque-Sublime`.
3. Watch the first moments of the session. You should see a short status message, **"Verifying skill integrity"**, and then no warning. If you see a warning about a skill hash mismatch, stop, do not use project skills, and ask Claude what it says (that is the integrity check doing its job).
4. Ask Claude to run a harmless command that the guard should block, for example: *"Run `cat .env` for me."* The guard should refuse with a message starting `zero-trust-guard:`. (There is no `.env` file; the point is that the guard answered.)
5. Ask Claude to run a harmless PowerShell command: *"Run `Get-ChildItem docs` in PowerShell."* It should work normally. That shows the guard lets ordinary commands through.

If step 4 runs the command instead of refusing, the hook is still not firing. Ask Claude to check the Claude Code hook settings; do not continue to Part 8.

---

## Part 8 (optional, recommended): the sandbox

The guard reads the text of commands and can be fooled by clever wording. A sandbox is a physical fence that works even then. `docs/sandbox-setup.md` has the settings. On Windows, the steps are:

1. Open a plain PowerShell window and start Claude Code in the terminal with `claude`. (The slash commands below only work in that terminal version, not in the desktop app's chat.)
2. Type `/sandbox install` and follow the prompts.
3. Merge the JSON block from `docs/sandbox-setup.md` into your personal settings file at `C:\Users\<your name>\.claude\settings.json`. Ask Claude to do this; it will ask for approval first.
4. Restart and type `/sandbox` to confirm it says the sandbox is active.

---

## Part 9: What to leave alone

- **WSL, Ubuntu, Kali:** leave them. They are not involved any more. Remove them only if you want less software on the PC.
- **`C:\Windows\System32\bash.exe`:** do not delete or rename it. It belongs to Windows. Git Bash now takes priority inside Claude Code.
- **Existing skills in `.agents/skills/`:** untouched. The lock file still matches them.

---

## Summary of what changed on your PC

| Before | After |
|---|---|
| Claude Code found WSL's `bash.exe`; hooks never ran | Claude Code finds Git Bash; hooks run |
| Scripts had CRLF endings; the guard would have failed open | Scripts have LF endings; `.gitattributes` keeps it that way |
| Guard watched only the Bash tool | Guard watches Bash and PowerShell |
| No Node or jq; the repository's own checks could not run locally | Both installed; `verify-skills.mjs` and `test-guard.sh` run |
