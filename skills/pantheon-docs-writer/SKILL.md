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
- Checking whether a page mixes types, or finding which docs a feature still needs
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

## Classify with Diátaxis

Before writing a single word, classify the content. All Pantheon docs fall into one of four quadrants:

| Quadrant | Orientation | User goal | Pantheon form |
|---|---|---|---|
| **Tutorial** | Learning | "Let me try this" | Paginated guide with numbered steps |
| **How-to guide** | Task | "How do I accomplish X?" | Guide or doc with clear steps |
| **Explanation** | Understanding | "Why does this work this way?" | Doc, conceptual, no step-by-step |
| **Reference** | Information | "What are the exact values/options?" | Doc, table/list-heavy, dry and complete |

**Rule:** A single document should serve one quadrant. Don't mix a tutorial with a reference. If you're covering both concepts and steps, split them.

**What each type does and doesn't do** (full rules and skeletons in the file named in the last column):

| Type | Does | Doesn't | File |
|---|---|---|---|
| Tutorial | Opens with what the reader builds. One path, a visible result at every step, expected output, one-clause explanations. | Offer options, teach theory, assume knowledge. | `references/tutorials.md` |
| How-to guide | Titles by outcome, starts at a named place, gives imperative steps, ends with a check. | Teach from zero, list every option, argue why. | `references/how-to-guides.md` |
| Reference | Mirrors the product, uses one pattern per entry, states exact names, defaults, limits. | Instruct, explain, or opine. | `references/reference-docs.md` |
| Explanation | Answers why, gives context and trade-offs, links to the pages that apply it. | Give procedures or exhaustive option lists. | `references/explanation.md` |

If a request or page spans more than one type, or you're asked what a feature still needs, load `references/type-check.md`: it covers mixed-page detection, splitting, and gap assessment.

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
| 1 | Inputs and claims | Get the reader, goal, starting point, prerequisites, and a source for each product claim. Mark what you can't source as an open question. | `references/inputs-claims-and-sources.md` |
| 2 | Classify | Pick the Diátaxis quadrant (section above). Report type, confidence, and evidence. Load the type's file for its rules and skeleton. | `references/type-check.md`, plus the type's file |
| 3 | Content type and location | `doc` or `guide`; where the file goes; frontmatter. Release notes use a different schema. In a Google Doc published through Content Publisher, use Docs mode instead. | `references/content-types-and-frontmatter.md`, `references/release-notes.md`, `references/docs-mode.md` |
| 4 | Structure | Intro, Before you begin, sections, Troubleshooting, More resources. | `references/document-structure.md` |
| 5 | Write | Voice (be verbs, hyperbole), headings, emphasis, code, links, lists, tables, images, where the user is. | `references/voice-rules.md`, `references/writing-style.md` |
| 6 | Components and embeds | Callouts, accordions, tabs, partials, popovers, variables, videos, icons, placeholders, review dates. | `references/components-and-variables.md`, `references/placeholders-and-embeds.md` |
| 7 | Inclusive language | Apply on every page. | `references/inclusive-language.md` |
| 8 | Findability (proposed) | Search intent, title, description, links. Guidance, not an adopted standard. | `references/seo-for-authors.md` |
| 9 | Check | Run `vale`, then the checklist. Vale can't see most voice and claim problems. | `references/vale-and-checks.md`, `references/review-checklist.md` |
| 10 | Ship | Navigation, redirects, branch, commit, PR. | `references/navigation-and-redirects.md`, `references/repo-workflow-and-terminology.md` |

## Rules that apply to every page

These are the short form. The detail and examples are in the reference files.

- Sentence case for all headings. The frontmatter `title` renders as the H1; start the body at `##` and don't skip levels.
- In a Google Doc (Docs mode), the page title is the one `#` Heading 1, not a bold line or a "Title:" label. Sections start at `##`. Never skip a level.
- The page body holds only reader content. Source gaps, "none stated in the source", reviewer notes, and "I assumed" remarks go in Open questions after the draft, never in a heading, table cell, or paragraph of the page.
- Second person, active voice, present tense. Replace every be verb that is a clause's main verb: name who acts and use a verb that says what they do. Contractions (`it's`, `you're`), progressives ("you are working" becomes "you work"), passives ("a field that was left empty" becomes "a field you left empty"), and predicate adjectives ("is available", "is private") all count. For a state, say who provides or limits it ("the site has the block"). Keep "is" only in a glossary-style definition; product intros and overviews name the product as the actor. Before you answer, search your rewrite for is, are, was, were, be, been, being, `'s`, `'re`. Details and examples: `references/voice-rules.md`.
- No hyperbole, opinion, intensifiers, or colloquialisms. Replace them with a fact, a number, or a mechanism, or cut them.
- Don't state product behavior you can't source. Put it in open questions. Never let a rewrite add a claim the source doesn't support.
- Bold for UI elements and navigation only. Italics for emphasis.
- Inline code for file names, paths, variables, commands, and output. Fenced blocks always name the language.
- Relative links for internal pages, with descriptive link text.
- Tell the reader where to be before the first instruction ("Where's the User?").
- "Before you begin" holds prerequisites and variable definitions. "More resources" is the last section.
- Inclusive language: allowlist/blocklist, `main`, `primary`/`replica`, "they" as the default pronoun.
- Check `src/source/content/partials/` for reusable content before writing new.

## Output

When you draft or revise a page, deliver:

1. The draft.
2. Open questions: each question, who can answer, and the sentence it blocks.
3. A self-check: be verbs and banned words you fixed, and any claim left unsourced. Skip it when the request is to return only revised text (see `references/voice-rules.md`).

## Quick reference

The canonical sources are the Pantheon style guide (`src/source/content/style-guide.md`) and the doc template. This skill restates them for working use; if they disagree, the style guide wins and this skill needs a fix.
