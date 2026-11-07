# Environments: where to run Claude Code for this repo, and the exact settings for each

Written 2026-11-07. Covers every place a Claude Code session (or another agent) can run against this repository, what each one is for, and the exact configuration. "Current" columns reflect CHUMPERS on the day this was written.

**The one rule that matters most:** a session is anchored to the folder you open it in. Open it at `Z:\Repos\Grotesque-Sublime`, the repo root. A session opened in a subfolder such as `.claude` loads **no** project settings, no hooks, and no guard, because it looks for `.claude\.claude\settings.json`, which does not exist.

---

## 0. Which environment for which job

| Job | Use |
|---|---|
| Anything that touches this PC: hooks, sandbox, Windows setup, the PC hardening doc | **Local session** (section 1) |
| Repo-only work from your phone or another device: drafting posts, editing docs, reviewing skills | **Cloud session** (section 3) |
| Running a slash command the desktop app does not offer, such as `/sandbox` | **Terminal session** (section 2) |
| Continuing a local session from your phone | **Remote Control** on that local session (section 4) |
| Checks that run on every push without you | **GitHub Actions** (section 5), already configured |

Secrets: **none of these environments needs one today.** Section 7 says what to do if that changes.

---

## 1. Local session (Claude desktop app on CHUMPERS)

The session runs on this PC and can see `Z:`, the hooks, and the Windows settings.

### 1.1 Where to open it

`Z:\Repos\Grotesque-Sublime`. Not `.claude`, not `docs`, not a worktree folder.

### 1.2 Permission mode

| Mode | Use it? | Why |
|---|---|---|
| **Default** (asks before edits and commands) | **Yes.** This is the current setting. | The permission rules in `settings.json` and the guard both work here, and you see every ask. |
| Auto (a classifier decides) | Acceptable for low-risk doc work | The guard still runs in every mode. The classifier adds a second check, but you see fewer prompts. |
| Bypass (no prompts) | **Never** | It turns off the permission rules. The guard's deny rules still fire, but its ask rules become silent allows. `docs/sandbox-setup.md` removes this mode entirely. |

### 1.3 Files that configure it

| File | Status | What it holds |
|---|---|---|
| `Z:\Repos\Grotesque-Sublime\.claude\settings.json` | In the repo, committed | Permission rules, both hooks, MCP and skill-shell lockouts. Changing it is a control change; the guard asks, and it goes through a pull request. |
| `Z:\Repos\Grotesque-Sublime\.claude\settings.local.json` | Does not exist. **Keep it that way.** | Per-machine overrides that are not committed. A rule here could loosen a committed rule without CI seeing it. |
| `Z:\Repos\Grotesque-Sublime\.mcp.json` | Does not exist. Keep it that way unless SECURITY.md section 4.2 is followed. | Project MCP servers. `enableAllProjectMcpServers: false` means one added by a PR is not auto-trusted. |
| `C:\Users\Grandma Frapples\.claude\settings.json` | **Exists but is empty (`{}`).** | Your personal settings for every project on this PC. This is where the sandbox goes. See 1.4. |

### 1.4 Your personal settings file: exact contents

Replace the `{}` in `C:\Users\Grandma Frapples\.claude\settings.json` with this. It is the block from `docs/sandbox-setup.md`, unchanged:

```json
{
  "permissions": {
    "disableBypassPermissionsMode": "disable"
  },
  "sandbox": {
    "enabled": true,
    "failIfUnavailable": true,
    "autoAllowBashIfSandboxed": false,
    "allowUnsandboxedCommands": false,
    "network": {
      "strictAllowlist": true,
      "allowedDomains": [
        "github.com",
        "*.github.com",
        "*.githubusercontent.com",
        "registry.npmjs.org",
        "skills.sh"
      ]
    },
    "filesystem": {
      "denyRead": [
        "~/.ssh",
        "~/.aws",
        "~/.config/gh",
        "~/.netrc",
        "~/.git-credentials",
        "~/.docker/config.json"
      ]
    }
  }
}
```

**Order matters.** The sandbox needs a one-time install on Windows (`/sandbox install`, section 2) *before* this file is saved, because `failIfUnavailable: true` makes Claude Code refuse to start when the sandbox cannot. Do section 2 first, then paste this.

### 1.5 Environment variables

**None.** Specifically do not set:

| Variable | Why not |
|---|---|
| `ANTHROPIC_API_KEY` | The desktop app signs in on its own. A key in the environment is readable by any command the agent runs. |
| `CLAUDE_CODE_GIT_BASH_PATH` | Only for non-standard Git installs. Git is at `C:\Program Files\Git`, which Claude Code finds by itself. |
| `POSTIZ_API_KEY` or any other service key | Not needed today. See section 7 for when and how. |

### 1.6 Desktop app settings (Settings → Claude Code)

| Setting | Current | Recommended |
|---|---|---|
| Default permission mode | Default | Default |
| Bypass permissions | Off (allowed by policy, user opt-in) | Leave off. The file in 1.4 removes the option. |
| Connect new sessions to Remote Control | Not set | Leave unset. Turn Remote Control on **per session** when you want phone access (section 4). |
| Worktree location | Inside the project (`<repo>\.claude\worktrees`) | Fine. Claude manages those folders; never open a session *in* one by hand. |
| Browser tools | On | Fine. Nothing in this repo needs a dev server. |
| Auto-archive on PR close | Off | Your preference. |
| Keep awake while working | On | Your preference. |

---

## 2. Terminal session (`claude` in a terminal)

The same local environment, same files, same hooks, but launched from a terminal instead of the app. Needed only for slash commands the app's chat does not run, such as `/sandbox`.

### 2.1 How to open it

1. File Explorer → `Z:\Repos\Grotesque-Sublime` → right-click → **Open Git Bash here**.
2. Type `claude` and press Enter.

Do not run it from WSL (Ubuntu or Kali). The repo is on `Z:`, the hooks expect Windows paths, and WSL's `bash` cannot open them.

### 2.2 One-time sandbox install

Inside that terminal session:

```
/sandbox install
```

Follow its prompts. When it finishes, type `/exit`, paste the JSON from 1.4 into your personal settings file, start `claude` again, and run `/sandbox` to confirm it reports active. From then on the sandbox applies to the desktop app too.

### 2.3 Everything else

Identical to section 1: same permission mode, same files, no environment variables.

---

## 3. Cloud session (claude.ai/code on the web or phone)

Runs on a Linux machine Anthropic hosts. It gets the repo from GitHub, not from `Z:`. Because it is Linux with real `bash`, the hooks and scripts run there without any Windows line-ending or symlink trouble.

What it cannot do: touch this PC, its settings, `Z:`, or the Windows hardening steps.

### 3.1 Environment configuration (claude.ai/code → Environments)

Create one environment for this repo with these values:

| Field | Value |
|---|---|
| Name | `grotesque-sublime` |
| Repository | `Archimedes7777/Grotesque-Sublime` |
| Default branch | `main` |
| Network access | The most restrictive option that still allows the hosts below. If the UI offers only tiers, choose the limited or trusted tier, never full. |
| Allowed hosts (if the UI lets you list them) | `github.com`, `*.github.com`, `*.githubusercontent.com`, `registry.npmjs.org`, `skills.sh` |
| Environment variables | **None** |
| Secrets | **None** |
| Setup script (runs when the session starts) | `node scripts/verify-skills.mjs` |

The setup script is optional but useful: it is the same integrity check the SessionStart hook runs locally, and a failure stops you before any work starts.

### 3.2 What is different about secrets in the cloud

On this PC, a secret can live where the agent cannot read it (the permission rules and guard deny secret files). In a cloud environment, **any environment variable you set is readable by the agent**. The guard only asks before an environment dump; it cannot hide a variable. So the cloud rule is: put nothing there you would mind the agent seeing. Today that means nothing.

### 3.3 Branches and merging

Cloud sessions work on branches named `claude/<something>` and open pull requests into `main`. The branch ruleset from SECURITY.md section 7 (require a pull request, require the `verify` check, block force pushes) is what keeps a cloud session from changing `main` directly. If that ruleset is not set yet, set it before using cloud sessions.

---

## 4. Remote Control (phone access to a local session)

Not a separate environment. It is a switch on a **local** session that lets your phone or another device drive it while it keeps running on CHUMPERS, with `Z:`, the hooks, and the guard all still in effect.

| Setting | Current | Recommended |
|---|---|---|
| Connect new sessions to Remote Control (app setting) | Not set | Leave unset. |
| Remote Control on a specific session | Off | Turn on only for a session you actually want to continue from your phone, and turn it off after. |

Why per-session: a session reachable from other devices is one more thing that depends on your Anthropic account staying yours. Keep the number small.

---

## 5. GitHub Actions (already configured)

| Item | Setting |
|---|---|
| Workflows | `.github/workflows/skills-integrity.yml` (every push and PR), `.github/workflows/upstream-skill-watch.yml` (monthly) |
| Environment variables | None |
| Repository secrets | **None.** `GITHUB_TOKEN` is provided by GitHub and should be read-only by default (SECURITY.md section 7, checkbox 3). |
| Actions allowed | GitHub-authored and SHA-pinned only (SECURITY.md section 7, checkbox 4) |

Nothing to add. If a future workflow asks for a secret, that is a SECURITY.md section 4 review, not a quick change.

---

## 6. Other agents (Codex, GitHub Copilot, Cline, and so on)

They read `AGENTS.md`, which is advice, not enforcement. None of the hooks or permission rules apply to them.

| Item | Setting |
|---|---|
| Where to open | The repo root, same as section 1.1 |
| Environment variables | None |
| Secrets | Never. Codex created the `CodexSandboxOffline` and `CodexSandboxOnline` Windows accounts for its own sandbox; that is fine, and it still gets no keys. |
| What protects `main` from them | CI (`verify` check) and the branch ruleset. That is the whole backstop, so section 3.3's ruleset matters here too. |

---

## 7. If a secret is ever needed

Today: none. The scripts, hooks, and workflows read no secret at all (confirmed by searching them on 2026-11-07).

The one foreseeable case is Postiz, which SECURITY.md section 4.4 marks **Conditional**. If you adopt it:

| Where | How to hold `POSTIZ_API_KEY` |
|---|---|
| Local session | A Windows **user** environment variable (Settings → System → About → Advanced system settings → Environment Variables → User variables). Not in any file in the repo. The guard still forces drafts-first and asks before publish, schedule, or delete. |
| Cloud session | The environment's Secrets field, and only if the key is scoped so that publishing still needs a human. Remember 3.2: the agent can read it. Prefer the self-hosted plan in `docs/postiz-self-hosting-plan.md`. |
| GitHub Actions | Do not. No workflow should post. |

Rotate the key immediately if it ever appears in a chat, a commit, or an issue.

---

## 8. Not environments for this repo

| Thing | Status |
|---|---|
| WSL (Ubuntu, Kali) | Installed on CHUMPERS, not used for this repo. Do not run `claude` there against `Z:`. Harmless to keep. |
| `C:\Windows\System32\bash.exe` | WSL's launcher. Leave it alone; Claude Code now prefers Git Bash. |
| `.claude\worktrees\` | Claude's own scratch checkouts for sessions that want isolation. Managed by the app. |

---

## 9. One-page summary

| Environment | Open at | Config file(s) | Env vars | Secrets | Network |
|---|---|---|---|---|---|
| Local (desktop app) | `Z:\Repos\Grotesque-Sublime` | repo `.claude\settings.json` + personal `C:\Users\Grandma Frapples\.claude\settings.json` (1.4) | none | none | sandbox allowlist (1.4) |
| Terminal (`claude`) | same, via Git Bash | same | none | none | same |
| Cloud (claude.ai/code) | the `grotesque-sublime` environment | repo `.claude\settings.json` (from GitHub) + environment settings (3.1) | none | none | allowlist (3.1) |
| Remote Control | a local session, switched on per session | same as local | none | none | same as local |
| GitHub Actions | automatic | `.github\workflows\*.yml` | none | none | GitHub's |
| Other agents | `Z:\Repos\Grotesque-Sublime` | `AGENTS.md` (advisory) | none | none | whatever that agent's own sandbox allows |
