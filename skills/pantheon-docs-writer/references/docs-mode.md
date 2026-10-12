# Docs mode: Google Docs and Content Publisher

> Use when the page lives in a Google Doc published through Pantheon's Content Publisher, not in the docs repo as `.md`/`.mdx`. Examples: P1 documentation. The repo-only guidance in the other references (frontmatter, MDX components, `src/` paths, redirects in `middleware.ts`) doesn't apply here.
> Part of the `pantheon-docs-writer` skill. Return to `../SKILL.md` for the workflow.

## What's confirmed

From Pantheon's release notes and docs in `pantheon-systems/documentation` (checked 2026-10-12):

- Content Publisher sends content from Google Docs to a WordPress, Drupal, or Next.js site. A Google Docs add-on connects a doc to a collection. Its own docs are at https://docs.content.pantheon.io.
- Its quality assistant checks accessibility before you publish: missing alt text, improper heading hierarchy, and non-descriptive link text, among others.

Observed in exported P1 docs (not from product documentation):

- Inline code and section messages are Content Publisher components, not Markdown. In a text export, an inline-code span appears as a marker link before the code text, for example `[█ ](https://pcc.webstyle?...name=Inline%20Code...)`.
- Plain backticks you type into a Doc stay literal. Applying inline code takes Content Publisher's control in the add-on.

## What's not confirmed (ask before promising it)

Mark these `unverified` and ask the Content Publisher team:

- How Doc fields map to the published page's title, description, slug, and review date. The repo's frontmatter doesn't exist in a Doc.
- Which style-guide components a Doc can produce (callouts, tabs, accordions, partials, Popover).
- How internal links should look in a Doc. Relative paths such as `/terminus` work on the docs site; a Doc link may need a full URL.
- Whether the quality assistant covers the style guide's heading-case and voice rules (it covers accessibility).

## How to write for a Doc

- Output plain structured text a person can paste into a Doc. No YAML frontmatter, no MDX, no `src/` paths.
- Use real Heading styles (Heading 1 for the title, Heading 2 and below for sections), not bold or a larger font. Don't skip levels.
- Keep the same voice, heading-case, emphasis, and "Before you begin" rules. See `writing-style.md`, `voice-rules.md`, and `document-structure.md`.
- Bold only for UI navigation. Emphasize with italics.
- **Flag code for the author.** Mark every file name, field, command, and variable that needs inline code, so the author can apply the Content Publisher control. Do this as a list at the end ("Apply inline code to: ...") because pasted backticks won't render.
- Give every image alt text and every link descriptive text. The quality assistant checks both.
- Put the inputs, claims, and open questions from `inputs-claims-and-sources.md` at the end of your answer, outside the draft.

## How to review a Doc

- Work in Suggesting mode, so the author can accept or reject each change.
- Reply to each suggestion with the rule it follows (for example "Voice, Style, and Flow: avoid be verbs") and flag any product claim you couldn't verify.
- Don't change a link target, heading level, or bold-to-italic formatting by search-and-replace; Docs' Find and Replace makes text suggestions only. Leave a comment for those.
- Leave claims you can't confirm as comments. Don't rewrite them.

## Check a Doc before publishing

1. Export the Doc as text.
2. Remove Content Publisher markers (the `[█ ](...)` links) and unescape Markdown escapes the export adds.
3. Run `vale` on the cleaned text (`vale-and-checks.md`).
4. Read the voice-rules self-check list; Vale doesn't cover most of it.
