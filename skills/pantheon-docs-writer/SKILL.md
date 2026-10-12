---
name: pantheon-docs-writer
description: "Write, edit, or review Pantheon documentation. Applies Pantheon style guide, inclusive language guidelines, Diátaxis structure, and Google Developer Style Guide. Use when creating new docs, editing existing ones, reviewing PRs for style, or deciding how to structure content."
---

# Pantheon Docs Writer

## When to Use

- Writing a new doc or guide from scratch
- Editing an existing doc for style, clarity, or accuracy
- Reviewing a PR for style guide compliance
- Deciding whether content belongs in a doc vs a guide
- Choosing the right Diátaxis content type for a topic
- Structuring a "Before You Begin" section or "More Resources" list
- Selecting the right MDX component (callout, tab, accordion, etc.)
- Writing or editing release notes
- Adding a new page to the site navigation
- Creating a redirect for a moved or removed URL

## Inputs to Gather (if not provided)

1. **Topic** — what does this doc cover?
2. **Audience** — who is the reader? (development, agency, sysadmin, business, marketing)
3. **CMS scope** — does it apply to WordPress, Drupal, both, or neither?
4. **Doc or guide?** — single-page reference vs multi-page walkthrough
5. **New content or edit?** — creating from scratch or revising existing

---

---

## Step 1: Classify with Diátaxis

Before writing a single word, classify the content. All Pantheon docs fall into one of four quadrants:

| Quadrant | Orientation | User goal | Pantheon form |
|---|---|---|---|
| **Tutorial** | Learning | "Let me try this" | Paginated guide with numbered steps |
| **How-to guide** | Task | "How do I accomplish X?" | Guide or doc with clear steps |
| **Explanation** | Understanding | "Why does this work this way?" | Doc, conceptual, no step-by-step |
| **Reference** | Information | "What are the exact values/options?" | Doc, table/list-heavy, dry and complete |

**Rule:** A single document should serve one quadrant. Don't mix a tutorial with a reference. If you're covering both concepts and steps, split them.

**Pantheon mapping:**
- Tutorials → multipage guides (`contenttype: [guide]`) in `src/source/content/guides/`
- How-to guides → single docs or guides depending on length/complexity
- Explanations → single docs (`contenttype: [doc]`) in `src/source/content/`
- Reference → single docs in `src/source/content/`

---

## Workflow

Work through these in order. Load a reference file only when its step applies; don't read them all up front.

| # | Step | What you do | Load |
|---|---|---|---|
| 1 | Classify | Pick the Diátaxis quadrant (above). | none |
| 2 | Content type and location | `doc` or `guide`; where the file goes; frontmatter. Release notes use a different schema. | `references/content-types-and-frontmatter.md`, `references/release-notes.md` |
| 3 | Structure | Intro, Before you begin, sections, Troubleshooting, More resources. | `references/document-structure.md` |
| 4 | Write | Voice, headings, emphasis, code, links, lists, tables, images, where the user is. | `references/writing-style.md` |
| 5 | Components | Callouts, accordions, tabs, partials, popovers, variables. | `references/components-and-variables.md` |
| 6 | Inclusive language | Apply on every page. | `references/inclusive-language.md` |
| 7 | Check | Run the checklist before delivering. | `references/review-checklist.md` |
| 8 | Ship | Navigation, redirects, branch, commit, PR. | `references/navigation-and-redirects.md`, `references/repo-workflow-and-terminology.md` |

## Rules that apply to every page

These are the short form. The detail and examples are in the reference files.

- Sentence case for all headings. The frontmatter `title` renders as the H1; start the body at `##` and don't skip levels.
- Second person, active voice, present tense. Avoid be verbs where you can.
- Bold for UI elements and navigation only. Italics for emphasis.
- Inline code for file names, paths, variables, commands, and output. Fenced blocks always name the language.
- Relative links for internal pages, with descriptive link text.
- Tell the reader where to be before the first instruction ("Where's the User?").
- "Before you begin" holds prerequisites and variable definitions. "More resources" is the last section.
- Inclusive language: allowlist/blocklist, `main`, `primary`/`replica`, "they" as the default pronoun.
- Check `src/source/content/partials/` for reusable content before writing new.

## Quick reference

The canonical sources are the Pantheon style guide (`src/source/content/style-guide.md`) and the doc template. This skill restates them for working use; if they disagree, the style guide wins and this skill needs a fix.
