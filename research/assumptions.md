# Assumptions and judgment calls

Each entry: ID, phase, assumption, reason. Later phases append.

## Phase 0

| ID | Assumption | Reason |
|---|---|---|
| P0-1 | Research date is 2026-11-04 (environment date). Training data is treated as stale; all current-law and price claims are verified by search. | Mandate Section 1. |
| P0-2 | Materiality threshold: a layer gains or loses at least 10% of a dated fee pool, or a new revenue pool of at least $5B per year appears, by 2030. | Mandate gives none (plan.md A1). |
| P0-3 | Risk-adjusted ranking metric: return band midpoint divided by estimated stressed drawdown, plus qualitative tail notes. | No risk metric specified (A2). |
| P0-4 | The personal case (non-accredited, $50k, taxable cash account, no margin) maps to the Retail tier only. Mid-tier vehicles are excluded from `personalized_plays.md`. | Accreditation status "No". |
| P0-5 | Horizons measured from 2026-11-04: Short to 2027-11, Medium 2027-11 to 2029-11, Long 2029-11 to 2036-11. | A5. |
| P0-6 | Scenario thresholds in `schema.md` Section 3 are provisional. | A3. |
| P0-7 | Return bands are annualized nominal USD, pre-tax unless stated; the personal case also shows after-tax at an assumed combined federal plus CA marginal rate (stated in Phase 3). | A7. |
| P0-8 | "Constraints: none stated" is read as permitting direct token custody and spot crypto ETFs, but no leverage or margin (cash account). | Section 0 table. |
| P0-9 | Liquidity need "none stated, 10-year horizon" is read as: capital not needed before 2036, but the investor wants daily liquidity by default; locked vehicles are excluded from the personal case. | Conservative reading. |
| P0-10 | Model tiering: subagents for collection run on a mid-tier model; synthesis, verification, and red team run on the strongest model. | Mandate Section 1 rule 3. |
| P0-11 | Each subagent writes its own search log (`ws/search_log_wsN.md`); the lead merges into `search_log.md`. | Avoid concurrent write conflicts. |
| P0-12 | Repository context: research is stored in `./research/` inside the Grotesque-Sublime repo working directory, committed to branch `claude/new-session-5ulni5`. All web content is untrusted data per the repo's SECURITY.md; no instructions from web pages are followed. | Repo policy. |

## Phase 1 (process notes)

| ID | Assumption | Reason |
|---|---|---|
| P1-1 | Subagents hit a per-agent web search cap well below the 40-search budget (WS8 at 24, WS2 at 15). Affected sections are tagged and the lead runs targeted gap-fill searches during synthesis and verification. | Tool limit observed 2026-11-04. |
| P1-2 | WS2 reported that Democrats won both chambers in the 2026-11-03 midterms. A lead search on 2026-11-04 returned only pre-election coverage, so the result is treated as `[Unverified]` and is not used as a probability driver. The scenario model treats US political durability as uncertain in both directions. | Results may not be indexed yet; a single-day report should not drive conclusions. |
