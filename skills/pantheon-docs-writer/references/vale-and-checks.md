# Vale and automated checks

> Use before you deliver a doc or when a Vale comment appears on a PR. The facts below come from `.vale.ini` and `.github/workflows/vale.yml` in `pantheon-systems/documentation` on `main` (checked 2026-10-12). Re-check them when the config changes.
> Part of the `pantheon-docs-writer` skill. Return to `../SKILL.md` for the workflow.

## What runs

- A Vale job runs on every PR that touches `src/source/content/**/*.md`, `src/source/releasenotes/*.md`, `.vale.ini`, or `.vale/**`. It lints only the docs files the PR adds, changes, or renames. Vale is pinned to a version in the workflow.
- Config: `.vale.ini` at the repo root. `MinAlertLevel = warning`, `Vocab = Pantheon`, `BasedOnStyles = Pantheon, Google`. The Google package is pinned to a release.
- Only Pantheon rules report errors: `Pantheon.Inclusive` and `Pantheon.TermsStrict`. `Pantheon.Headings` and `Pantheon.Terms` report warnings. The Google rules that stay on report at warning.
- Many Google rules are off (for example `Google.Will`, `Google.We`, `Google.FirstPerson`, `Google.Colons`, `Google.WordList`). Some of them are off only for a report-only trial that started 2026-10-06. Read `.vale.ini` before you assume a rule applies.

## Run it locally

```bash
vale sync          # once, to download the Google package into .vale/styles
vale path/to/doc.md
```

Run it on the file you changed before you open a PR. Fix errors first, then warnings.

## What Vale can't see

Passing Vale doesn't mean the doc follows the style guide. In a review of 25 docs, the most common findings had no working check:

- be verbs (`Google.Passive` exists but sits at `suggestion`, below the warning threshold, and fires thousands of times on the repo)
- hyperbole, opinion, and most colloquialisms
- bold used for emphasis (should be italics)
- where the reader starts, and the "Before you begin" structure
- unsourced product claims
- inline code for file names and fields

Use `voice-rules.md`, `inputs-claims-and-sources.md`, and `review-checklist.md` for those.

## Known quirks

- `Pantheon.Headings` matches its exception list as prefixes, so "Dev" also exempts "Developers" and "Devices". It can miss real title case that way, and it can flag a product name it doesn't know. Judge heading case yourself using the style guide's sentence-case rule.
- Don't rewrite a product name or an exact error message to satisfy Vale. Raise a false positive with the docs team.
- A `Pantheon.TermsStrict` or `Pantheon.Inclusive` error means a wrong spelling of a product name (for example `Wordpress`, `NextJS`) or a non-inclusive term. Fix those first. The workflow reports alerts as PR review comments and, for the first four weeks from its first merged run, sets `fail_on_error: false`, so alerts don't block a merge yet.

## Proposed additions

A proposal for four report-only checks (hyperbole, colloquial phrases, "Prerequisites" headings, and a narrow be-verb list) is open at `pantheon-systems/documentation#10354`. Until the docs team adopts them, treat those patterns as guidance from `voice-rules.md`, not as enforced rules.
