# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## What this repo is

A Claude Code skill packaged as an installable plugin for writing, editing, and reviewing Pantheon documentation. This is **not** a documentation site — it is a skill definition repo. The skill instructs Claude how to write docs that conform to Pantheon's style guide, inclusive language guidelines, Diátaxis content structure, and platform conventions.

## Files

- **`skills/pantheon-docs-writer/SKILL.md`** — The skill definition. This is what Claude reads and executes when `/jazzsequence-skills:pantheon-docs-writer` is invoked. Kept short: it holds the intro, the Diátaxis step, the workflow table, and the rules that apply to every page. Written as imperative instructions for Claude to follow.
- **`skills/pantheon-docs-writer/references/*.md`** — Detail loaded on demand from the workflow table in `SKILL.md`: inputs and claims, content types and frontmatter, document structure, voice rules, writing style, components and variables, placeholders and embeds, inclusive language, search findability (proposed), Vale and automated checks, Docs mode (Google Docs and Content Publisher), the review checklist, release notes, navigation and redirects, and repo workflow and terminology.
- **`tests/`** — `review-fixtures.json` (272 before/after sentences from a review of 25 docs) and `score.py`, a rough scorer. `tests/type-fixtures.json` and `score_types.py` check Diátaxis classification and per-type drafting structure. Rules that must apply to short edits belong in `SKILL.md`, because the model doesn't open `references/` for one-sentence tasks. See `tests/README.md`. Run `python3 tests/score.py validate` after you edit the fixtures or the scorer, and use `score` mode to compare skill output before and after a change.
- **`.claude-plugin/marketplace.json`** — Marketplace manifest. Registers this repo as a Claude Code plugin source.
- **`.claude-plugin/plugin.json`** — Plugin manifest. Name, version, author.
- **`install.sh`** — Installer script. Registers the marketplace and installs the plugin via the Claude CLI.

## Maintaining this skill

When editing `skills/pantheon-docs-writer/SKILL.md`:

- Keep instructions imperative — written for Claude to execute, not for a human to read
- Put detail in `references/`, not `SKILL.md`. When you add a reference file, add it to the workflow table in `SKILL.md` and to the Files list here.
- `references/seo-for-authors.md` is proposed guidance, not an adopted Pantheon standard. Keep each item labeled **Style guide**, **Current practice**, or **Proposed**, and don't promote a proposed item without the docs team's agreement.
- Verify Vale facts in `references/vale-and-checks.md` against `.vale.ini` and `.github/workflows/vale.yml` on `main` whenever you change them.
- Verify every file path the skill names against `main` in `pantheon-systems/documentation` (for example, partials live in `src/source/content/partials/`, not `src/source/partials/`)
- Verify style rules and component names against the live Pantheon docs repo (`pantheon-systems/documentation`) before updating
- The docs site uses Next.js and MDX, not Gatsby — do not reference Gatsby
- Navigation is driven by `src/components/omni-components/` TypeScript files, not frontmatter or YAML config
- Redirects are managed in `src/middleware.ts` in the `RedirectMap` object
- Release notes live in `src/source/releasenotes/` with their own frontmatter schema separate from regular docs
- The `innav` frontmatter field is declared in the type system but not actively consumed — do not present it as a navigation driver

When editing `README.md`:
- Installation is via `install.sh` — update that script if the plugin registration mechanism changes, then update the README to match

## Versioning

**Always bump the version in both `.claude-plugin/marketplace.json` and `.claude-plugin/plugin.json` when making changes to the skill.** The plugin system compares version numbers to determine if an update is available.

Use semantic versioning:
- `patch` (e.g. `1.0.0` → `1.0.1`) — wording corrections, minor additions, fixing stale information
- `minor` (e.g. `1.0.0` → `1.1.0`) — new skill sections, new content type guidance
- `major` (e.g. `1.0.0` → `2.0.0`) — breaking changes to the skill's structure or approach

After bumping the version and pushing:
```bash
claude plugin tag
git push origin refs/tags/jazzsequence-skills--v<version>
```
