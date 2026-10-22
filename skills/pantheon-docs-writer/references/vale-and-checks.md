# Vale and automated checks

> Use before you deliver a doc, when a Vale comment appears on a PR, and to run the quality gate. The facts below come from `.vale.ini`, `.github/workflows/`, and `package.json` in `pantheon-systems/documentation` main@9b15056 (2026-10-09), and from running Vale 3.24.0 against that snapshot. Re-check them when the config changes.
> Part of the `pantheon-docs-writer` skill. Return to `../SKILL.md` for the workflow.

## What runs

- A Vale job runs on every PR that touches `src/source/content/**/*.md`, `src/source/releasenotes/*.md`, `.vale.ini`, `.vale/**`, `.github/workflows/vale.yml`, or `scripts/vale-measure.mjs`. It lints only the docs files the PR adds, changes, or renames. Vale is pinned to a version in the workflow.
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

- be verbs (`Google.Passive` sits at `suggestion`, below the `warning` threshold: Vale reports nothing for "The token is only shown once.")
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

## Quality gate

Run the gate against the real repo, not from memory. Report each check as **passed**, **failed**, **unavailable** (you couldn't run it, and why), or **not applicable**. Never write "passed" for a check you didn't run.

| Check | Command (from the repo) | Notes |
|---|---|---|
| Vale | `vale sync` once, then `vale <changed files>` | Needs the `vale` binary. Fix errors. Warnings need a fix or a stated reason. CI doesn't fail a merge on alerts yet (`fail_on_error: false`). |
| Release-note frontmatter | CI runs inline shell in `.github/workflows/validate-release-notes.yml`: one note per PR, `published_at` present, not `T00:00:00Z`. | No repo script exists. Read the three fields yourself, and say you did. |
| Unit and snapshot tests | `npm ci`, then `npm run test` (Vitest) | The only npm script CI runs on PRs besides Playwright's own install. |
| Lint and formatting | `npm run lint`, `npx prettier "**/*.md" --check` | Not run by CI; run when you changed code or configuration. |
| Build | `npm run build` | Not run by CI. Slow. Run it when you add or change an MDX component, a template, or navigation. |
| Frontmatter | No validator. `src/source/data/schema.yaml` is documentation only. | Check by hand against `content-types-and-frontmatter.md`. Not enforced at build. |
| MDX components | No build-time check found. No build-time check found for an unknown tag. | Compare every tag with the registry in `src/components/ui/mdx-wrapper/default-components.tsx`. |
| Links and anchors | No link or anchor checker in CI. | Repo pages only (Doc-published pages use generated ids; see `docs-mode.md`). Build each anchor from its heading: lowercase, drop punctuation, spaces to hyphens, repeats get `-1`, `-2` (github-slugger via rehype-slug). Check internal paths exist. |
| Navigation and redirects | No validator or test. | Read `src/components/omni-components/*.ts` and `RedirectMap` in `src/middleware.ts`; see `navigation-and-redirects.md`. |

Rules for the gate:

- A read-only review route may run only checks that write nothing, or that write only to a scratch copy. Otherwise report the check as unavailable. `vale sync`, `npm ci`, and `npm run build` write files.
- Derive commands from the repo you were given (`package.json`, `.github/workflows/`). If a command isn't there, don't invent one.
- When you changed repo files, validate from a clean checkout that contains the change, so a stray local file can't make a check pass. Use a scratch copy or an exported copy, and leave the user's working tree as it was. If a clean run needs something you don't have (`node_modules`, network, a Vale package), report the check as unavailable with the missing dependency. For a one-paragraph edit, running `vale` on the file is enough.
- Don't weaken the lint configuration, add broad ignores, or edit a product name or error message to make a check pass. When you're editing (not reviewing), fix a pre-existing error in a file you were asked to edit. Report failures in other files separately.
- Vale passing says nothing about product correctness. Run the semantic review in `review-checklist.md` as a separate pass.

## Gate order and Vale setup

Order the gate cheapest first: deterministic checks (Vale with the shared config, structure and code tests, link check, image checks, claim-marker counts), then the editor walkthrough, then one reviewer pass, then the ticket status update. See `docs-batch-workflow.md` for the last three.

- **Vale must fail the run when its config is missing.** A wrapper that skips Vale because `.vale.ini` isn't found and exits 0 is a defect: the gate reports "passed" for a check that didn't run. Make the wrapper exit non-zero and print which config path it looked for. Report the check as unavailable, never passed.
- **Put bolded UI labels in a Vale vocabulary file, not in per-test exemptions.** Labels such as Notice, Other, and My blocks belong in the vocabulary's accept list (`.vale/styles/config/vocabularies/<name>/accept.txt`, selected by `Vocab =` in `.vale.ini`). As of 2026-10-21 one Vale heading warning on "Notice appears under Other" was exempted inside one test instead. A vocabulary entry covers every doc that bolds the label; the test exemption covers one.
- Count the markers before you call a draft ready: `grep -cE 'inferred|unverified' <notes file>` on the runtime-claim rows should return 0.
