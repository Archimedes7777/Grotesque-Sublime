# Grotesque-Sublime

Working repository for the Bob Frapples Universe and the ActivelyPsychotic accounts: brand context, content planning, AI agent skills, and the security controls around them.

Nothing in this repository posts to a social account or holds a password. Agents draft; a person reviews and publishes.

## What is here

| Path | Purpose |
|---|---|
| `SECURITY.md` | The zero-trust policy: how skills are vetted, what agents may never do, account protection |
| `CLAUDE.md`, `AGENTS.md` | Short operating rules for Claude Code and other AI agents |
| `.agents/product-marketing.md` | Brand context the social, image, and video skills read first |
| `.agents/skills/` | Installed agent skills (hash-locked in `skills-lock.json`) |
| `.claude/` | Claude Code settings, the command guard, and the session-start integrity check |
| `docs/` | Content calendar, drafts, account hardening checklist, incident runbook, Postiz plan, trademark plan, GitHub and sandbox setup guides |
| `scripts/` | Skill integrity check, upstream drift check, guard regression tests |
| `.github/workflows/` | CI gate (`Skills integrity`) and the monthly upstream watch |

## Start here

1. Read `SECURITY.md`. It applies to people and to every AI agent.
2. Open this folder in Claude Code. It loads `CLAUDE.md` and the security hooks automatically.
3. Brand questions go in `.agents/product-marketing.md`. Posting plans go in `docs/`.

## Checks you can run

```bash
node scripts/verify-skills.mjs          # every skill matches skills-lock.json
bash scripts/test-guard.sh              # command guard regression tests
node scripts/check-upstream.mjs         # compare locked skills with upstream (needs network)
```

The same integrity checks run in CI on every pull request and every push to `main`.

## Reporting a security problem

Use GitHub private vulnerability reporting (Security tab). Do not open a public issue for a security problem.

## License

See `LICENSE`.
