# Claude Code: Commands, Use Cases & Personalized Prompts

---

## 25 Most Popular Claude Code Commands

| # | Command | Category | Function |
|---|---------|----------|----------|
| 1 | `/help` | Core | Display all available commands and keybindings |
| 2 | `/init` | Setup | Generate a `CLAUDE.md` from codebase analysis |
| 3 | `/clear` | Session | Wipe conversation context, reset token counter |
| 4 | `/compact` | Session | Force context compression to extend window |
| 5 | `/config` | Config | Open interactive settings editor (theme, model, keybindings) |
| 6 | `/model` | Config | Switch active model mid-session |
| 7 | `/fast` | Config | Toggle fast mode (Opus 5 with accelerated output) |
| 8 | `/memory` | Config | View and edit `~/.claude/CLAUDE.md` persistent memory |
| 9 | `/permissions` | Config | Inspect current tool permission grants |
| 10 | `/allowed-tools` | Config | List tools pre-approved in current permission mode |
| 11 | `/code-review` | Skill | Run structured diff review at a specified effort level |
| 12 | `/security-review` | Skill | Audit staged/branch changes for OWASP-class vulnerabilities |
| 13 | `/simplify` | Skill | Refactor for reuse, efficiency, and altitude without bug-hunting |
| 14 | `/run` | Skill | Launch the project app and validate changes in a live browser |
| 15 | `/loop` | Skill | Execute a prompt or command on a recurring interval |
| 16 | `/dataviz` | Skill | Create charts, dashboards, and data visualizations |
| 17 | `/design` | Skill | Generate a multi-artboard visual design canvas Artifact |
| 18 | `/pr-comments` | GitHub | Pull and surface open PR review comments into context |
| 19 | `/install-github-app` | GitHub | Authenticate and wire the GitHub App to the workspace |
| 20 | `/review` | Alias | Shorthand invocation of the code-review skill |
| 21 | `/cost` | Diagnostics | Display cumulative token and dollar spend for session |
| 22 | `/doctor` | Diagnostics | Run environment health checks (auth, proxy, tool access) |
| 23 | `/status` | Diagnostics | Show session state, active model, context usage |
| 24 | `/vim` | UX | Toggle Vim keybinding mode for prompt input |
| 25 | `/terminal-setup` | UX | Configure shell integration (tab-complete, keybindings) |

---

## 25 High-Value Claude Code Use Cases

### Engineering Productivity
1. **Automated PR stewardship** — subscribe to a PR; Claude monitors CI failures, reviewer comments, and merge conflicts, pushes fixes autonomously until green
2. **Codebase onboarding** — `/init` to generate a `CLAUDE.md` capturing architecture, conventions, and key entry points for any unfamiliar repo
3. **Incremental refactoring** — `/simplify` on a diff to eliminate duplication, reduce abstraction altitude, and tighten logic without widening scope
4. **Security hardening** — `/security-review` on staged changes before merge to catch injection, auth bypass, and OWASP Top 10 vectors
5. **Test generation** — describe a function's invariants; Claude writes unit and edge-case tests targeting exact failure modes

### Code Review & Quality
6. **Pre-commit review loop** — `/code-review --fix` at effort level `high` to surface and auto-apply correctness bugs before they hit CI
7. **Multi-file consistency audit** — spawn an Explore agent to verify naming conventions, error-handling patterns, and API contracts across the full tree
8. **Dependency risk analysis** — cross-reference `package.json` / `requirements.txt` changes against CVE databases and flag version regressions
9. **Commit message quality** — enforce conventional commits format with a pre-commit hook wired via `/update-config`
10. **Dead code elimination** — identify and remove unreferenced exports, unused imports, and orphaned config keys

### Git & GitHub Workflow
11. **Branch-to-PR automation** — develop on a feature branch, Claude drafts the PR body from the diff, mirrors the repo template, and opens the PR
12. **Merge conflict resolution** — Claude merges base branch, resolves logic conflicts, regenerates lockfiles, validates, and pushes
13. **Release notes generation** — summarize commits since last tag into a structured changelog grouped by type (feat/fix/chore)
14. **CI failure diagnosis** — read failing job logs, identify root cause, distinguish this-PR's-fault from flake or base regression, push fix
15. **GitHub Actions authoring** — generate workflow YAML for lint, test, build, deploy pipelines tailored to the project's stack

### Architecture & Planning
16. **Implementation planning** — spawn a Plan agent to decompose a feature request into ordered steps with file targets and trade-off analysis
17. **API design review** — evaluate REST/GraphQL endpoint contracts for consistency, idempotency, and versioning strategy
18. **Database schema migration** — author safe migration files with rollback paths, locking analysis for large tables, and backfill logic
19. **Monorepo orchestration** — coordinate changes across packages, verify cross-package imports resolve, update shared types
20. **Infrastructure-as-code review** — audit Terraform/Pulumi diffs for blast radius, IAM over-permission, and drift risk

### Documentation & Communication
21. **Living documentation** — keep `CLAUDE.md` current by re-running `/init` after major architectural changes
22. **ADR authoring** — generate Architecture Decision Records from a description of the problem, options, and chosen approach
23. **Onboarding guide generation** — produce a step-by-step contributor guide from repo structure, CI config, and CLAUDE.md
24. **Inline comment audit** — strip redundant what-comments, preserve only non-obvious why-comments, enforce the one-liner rule
25. **Stakeholder summary** — translate a technical diff into a plain-language change summary for non-engineering reviewers

---

## 25 Personalized Prompts

> **Methodology note:** These are generated from available signal — repository structure (GitHub intro tutorial, Actions workflows, branch/PR lifecycle), organizational context (okineo.co), and Claude Code session patterns. Full conversation history is not accessible to this environment; prompts are calibrated to inferred workflow and skill level, not exhaustive historical data.

### Git & GitHub Mastery
1. `Audit my current branch against main: list every file changed, categorize each change as feat/fix/refactor/chore, and draft a PR body using the repo's template structure.`

2. `I have a merge conflict on [filename]. Show me both sides of the conflict, explain the semantic difference between the two versions, recommend which to keep and why, then apply the resolution.`

3. `Parse the last 30 commits on this repo, group them by type and impact, and generate a structured CHANGELOG entry for a v1.0.0 release.`

4. `Write a GitHub Actions workflow that: lints on every push, runs tests on PRs, and deploys to production only on merge to main — tailored to this repo's detected stack.`

5. `Inspect this repo's branch protection rules gap: what safeguards (required reviews, status checks, linear history) are missing that would prevent accidental bad merges to main?`

### Claude Code Workflow Optimization
6. `Analyze my session's most frequent tool calls and generate a .claude/settings.json allowlist that eliminates the most common permission prompts without over-granting.`

7. `Create a CLAUDE.md for this repository that captures: architecture overview, critical file map, coding conventions, test commands, and CI/CD pipeline description.`

8. `Set up a /loop that checks my open PRs every 15 minutes, reports CI status changes, and flags any that have been idle for more than 24 hours.`

9. `Wire a pre-commit hook that runs /code-review at effort level medium on staged changes and blocks commit if any red-circle findings are present.`

10. `Design a project-level skill (SKILL.md) for my repo that encodes: PR conventions, test requirements, commit message format, and Claude's auto-fix permissions.`

### Code Quality & Review
11. `Run a security review on the current diff. For each finding: state the vulnerability class, the exact attack vector, the exploitability score, and the minimal fix.`

12. `Find every function in this codebase that has no test coverage, rank by complexity (cyclomatic), and generate test scaffolding for the top 5.`

13. `Identify all places where error handling is missing at system boundaries (HTTP handlers, DB calls, file I/O) and add the minimum required validation.`

14. `Locate every comment in this codebase. Delete what-comments. Rewrite any surviving why-comments that are ambiguous or outdated. Output the diff.`

15. `Audit all external dependencies: flag any with known CVEs, any that are pinned to a range instead of exact version, and any that are unused.`

### Architecture & Engineering Decisions
16. `I need to add [feature] to this codebase. Give me a 5-step implementation plan: ordered tasks, files to touch, interfaces to define, and the single biggest architectural risk.`

17. `Compare two approaches for [problem]: write a decision table with axes — complexity, testability, performance, reversibility — then recommend one with a one-paragraph rationale.`

18. `Analyze this repo's folder structure and identify any coupling that violates single-responsibility. Propose a refactor path with minimum breaking changes.`

19. `Generate an ADR (Architecture Decision Record) for the decision to use [technology]. Cover: context, options considered, decision, consequences, and review date.`

20. `Map every API endpoint in this codebase, verify each has input validation, output typing, and error response contracts, and list every gap.`

### Productivity & Automation
21. `I use Claude Code daily for GitHub work. Design a morning routine prompt sequence: branch status check → CI failures → stale PRs → today's priority tasks, as a single /loop trigger.`

22. `Generate a GitHub profile README for james@okineo.co that: communicates technical identity, links active projects, displays contribution patterns, and uses a minimal aesthetic.`

23. `Create a reusable prompt library (as a CLAUDE.md memory block) for the 10 tasks I do most in git: branch, PR, review, merge, release, hotfix, revert, tag, bisect, blame.`

24. `Scaffold a new repository for [project type] with: CLAUDE.md, GitHub Actions CI pipeline, PR template, branch protection config, dependabot.yml, and .gitignore pre-populated.`

25. `Review my current Claude Code permission settings and propose the minimal-footprint configuration that still allows autonomous PR stewardship — no unnecessary grants, no prompts for standard git operations.`
