# Search findability for authors (proposed)

> **Status: proposed, not an official Pantheon standard.** This restates the author-facing part of a draft "Docs SEO Playbook" (v1.0, prepared 2026-10-12, not yet adopted). Items marked **Style guide** already come from the Pantheon style guide. Items marked **Proposed** don't. Use the proposed ones as guidance, and don't present them as required.
> Part of the `pantheon-docs-writer` skill. Return to `../SKILL.md` for the workflow.

Authors own these. Canonicals, sitemaps, `robots`, redirect implementation, structured data, and CI checks belong to engineers; they're out of scope here.

## Before you draft

- **Proposed:** name the reader's task as a verb: install, configure, migrate, troubleshoot, compare, understand, or look up. If an existing page already serves that task, update it instead of writing a competing page.
- **Proposed:** match the page type to the task (Diátaxis): "what is X" is an explanation, "how do I" is a how-to, an exact error is a troubleshooting section, a lookup is reference.
- **Proposed:** note the product, version, and platform the page covers.

## Title, description, and headings

- **Style guide:** the frontmatter `title` renders as the page title (the H1). Don't repeat it in the body. Start the body at `##` and don't skip heading levels.
- **Proposed:** write a descriptive, unique title that makes sense in a browser tab or search result. Put the most important term first when it reads naturally. Don't stuff keywords.
- **Style guide:** `description` is required frontmatter: one sentence saying what the doc covers or accomplishes.
- **Proposed:** make the description useful on its own, outside the navigation. Don't reuse one description across pages.
- **Proposed:** make headings describe what follows. Avoid "Introduction" and "More information".

## Body

- **Proposed:** answer the reader's question or state the outcome in the opening paragraph.
- **Proposed:** use the words readers use: product names, UI labels, and exact error text.
- **Style guide:** document an error message verbatim as an H3 inside a Troubleshooting section, so people find it by searching the error.
- **Style guide:** use descriptive link text and relative links for internal pages.
- **Current practice:** give every image descriptive alt text (the style guide's image examples all include it).
- **Proposed:** link each page to its parent or guide, to related pages, and to the next step. Don't leave a page unlinked from anything.

## When a URL changes

- **Style guide:** moving, renaming, or deleting a page needs a redirect, and the PR gets the Redirect label. See `navigation-and-redirects.md`.
- **Proposed:** don't change a URL just to add a keyword.

## Keep it current

- **Style guide:** set `reviewed` to the date you reviewed the doc.
- **Proposed:** retire, merge, or update pages that no longer match the product.

## What this section isn't

It's not a promise of ranking. Clear, accurate, task-focused pages help readers and search engines. A page that satisfies a keyword tool but misstates the product fails the reader.
