# Repo workflow and terminology

> Use when preparing work for handoff, and for Pantheon's canonical product terms.
> Part of the `pantheon-docs-writer` skill. Return to `../SKILL.md` for the workflow.

## Prepare for handoff

Preparing is local and reversible. Hand the user:

- the files you changed, and the files you looked at and left alone
- the quality gate results, each marked passed, failed, unavailable, or not applicable (`vale-and-checks.md`)
- Open questions and the claim record (`inputs-claims-and-sources.md`)
- proposed navigation and redirect changes, as a table (`navigation-and-redirects.md`)
- draft branch, commit, and PR text, if the user will want it

Then stop. These actions each need explicit authorization from the user for that action in this conversation: commit, push, PR creation, merge, deployment, publishing (including a Google Doc through Content Publisher), deletion, and any change to an external system. Approval of one doesn't cover another ("commit it" isn't "push it"). Don't change repository-wide style policy or CI configuration as part of a docs task; raise it with the docs team.

## Conventions to follow once authorized

1. **Branch naming**: `{issue-number}-{short-description}` (e.g., `10234-add-redis-guide`)
2. **Commit format**: follow the conventional commits pattern (`docs: add Redis configuration guide`)
3. **PR description**: explain what changed and why. For a redirect, include the From/To table.

## Quick Reference: Terminology

Use Pantheon's canonical terms:
- **Site Dashboard** — the per-site admin page
- **My Dashboard** — a user's personal workspace
- **Professional Workspace** — (formerly Organization) workspace for a team/org
- **Supporting Workspace** — (formerly Supporting Organization) a workspace added to a site's team
- **Multidev** — Pantheon's feature-branch environments
- **Terminus** — Pantheon's CLI (always capitalized)
