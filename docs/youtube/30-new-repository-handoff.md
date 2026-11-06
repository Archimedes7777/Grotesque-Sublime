# New repository handoff: governed-ai-workflows

**Status:** the new repository is built and verified locally as an archive; it is not yet on GitHub. This session's GitHub access is scoped to `Archimedes7777/Grotesque-Sublime` only, and creating repositories is outside that scope by design, so the owner creates the empty repository and pushes the archive. Nothing in this folder has been deleted from `Grotesque-Sublime`; delete `docs/youtube/` here only after the new repository's CI is green.

**Name:** `governed-ai-workflows` is a placeholder. Rename at creation if the channel has a name.

## 1. What the archive contains

| Path | Origin | Changes made |
|---|---|---|
| `SECURITY.md` | copied | Section 2 adds YouTube comments and sponsor email as untrusted input; section 4.4 register emptied; section 6 rewritten for a channel and Google account; related-guide links point to `docs/security/` |
| `CLAUDE.md`, `AGENTS.md` | copied | Social-media rule replaced by the YouTube drafts-only rule; "never invent a measured result" added; project context section added |
| `README.md` | new | Describes the layout; notes that no license is included |
| `.claude/settings.json`, `.claude/hooks/*` | copied verbatim | None. The guard's Postiz lines are inert without that plugin |
| `scripts/*` | copied verbatim | None |
| `.github/workflows/*` | copied verbatim | None; action SHAs unchanged |
| `.gitignore` | copied verbatim | None |
| `skills-lock.json` | new | Empty register (`"skills": {}`) |
| `.agents/skills/` | new | Empty; no skills are installed in the new project |
| `docs/youtube/*` | copied | All planning, scripts, policies, templates, and the checklist |
| `docs/security/*` | copied | Account hardening, incident response, sandbox setup; written for the earlier project, platform steps apply |

Not copied: `LICENSE` (the owner chooses one), `.agents/product-marketing.md` and the four installed skills (brand-specific), `docs/*` outside the security and YouTube sets.

## 2. Verification run inside the archive on 2026-11-06

```text
node scripts/verify-skills.mjs        All skill integrity checks passed.
bash scripts/test-guard.sh            guard tests: 50 passed, 0 failed
node scripts/check-upstream.mjs --self-test   self-test passed
```

## 3. Steps for the owner

1. On GitHub, create an empty private repository named `governed-ai-workflows` (or the channel name). Do not initialize it with a README or license.
2. Download `governed-ai-workflows.tar.gz` from this session, extract it in a scratch folder, and read `SECURITY.md` and `CLAUDE.md` once; the archive is a product of an AI session and the same review rule applies to it.
3. In the extracted folder:

```bash
git init -b main
git add .
git commit -m "Initial import: zero-trust controls and channel planning"
git remote add origin git@github.com:<owner>/governed-ai-workflows.git
git push -u origin main
```

4. In the repository settings, complete `SECURITY.md` section 7: secret scanning and push protection, a `main` ruleset requiring a pull request and the `verify` check, read-only default `GITHUB_TOKEN`, pinned actions only.
5. Open the folder in Claude Code once and confirm the SessionStart integrity check reports a pass.
6. Add a `LICENSE` if the repository will be public.
7. Only then: open a pull request in `Grotesque-Sublime` that deletes `docs/youtube/` and the YouTube link line from its README, so the brand repository holds brand work only.

## 4. Files produced in this session that live in both places

- `docs/youtube/28-analytics-templates.xlsx`: Step 4 weekly and monthly review workbook with decision-rule flags and a title-test sheet.
- `docs/youtube/29-safe-ai-at-work-checklist.pdf` and `.html`: the governance series lead magnet, one page, rendered from the HTML source.
- `docs/youtube/26-ai-tools-scripts-weeks-4-6.md` and `27-ai-tools-rate-card-and-outreach.md`.
