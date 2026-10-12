# Repo workflow and terminology

> Use for branch, commit, and PR conventions, and for Pantheon's canonical product terms.
> Part of the `pantheon-docs-writer` skill. Return to `../SKILL.md` for the workflow.

## Step 13: Contribution and PR Workflow

When creating a new doc or editing an existing one:

1. **Branch naming**: `{issue-number}-{short-description}` (e.g., `10234-add-redis-guide`)
2. **Commit format**: follow the conventional commits pattern (`docs: add Redis configuration guide`)
3. **PR description**: explain what changed and why
4. **Redirect label**: add the **Redirect** label to any PR that touches `src/middleware.ts`

## Quick Reference: Terminology

Use Pantheon's canonical terms:
- **Site Dashboard** — the per-site admin page
- **My Dashboard** — a user's personal workspace
- **Professional Workspace** — (formerly Organization) workspace for a team/org
- **Supporting Workspace** — (formerly Supporting Organization) a workspace added to a site's team
- **Multidev** — Pantheon's feature-branch environments
- **Terminus** — Pantheon's CLI (always capitalized)
