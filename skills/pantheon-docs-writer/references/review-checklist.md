# Review checklist

> Run before delivering any doc, and use it as the rubric for a read-only review. Automated checks and semantic review are separate passes: a clean lint run says nothing about whether the page is right.
> Part of the `pantheon-docs-writer` skill. Return to `../SKILL.md` for the workflow.

## Review checklist

### Severity

Classify each finding by what it does to the reader. Report blocking items first.

| Level | Meaning | Examples |
|---|---|---|
| **Blocking** | The reader fails, loses data, or gets a wrong fact, or the repo check fails. | Wrong default, limit, version, or permission; missing destructive-step warning; Vale error; broken anchor; unregistered component; midnight `published_at` |
| **Warning** | The reader slows down or misreads, or a rule is broken without harm. | No starting point; no success check; title-case heading; be verb that hides the actor; vague link text |
| **Suggestion** | Preference or polish. | Tone, ordering, optional `Google.*` rules switched off in the repo |

### Semantic review (read the page as the reader)

- [ ] Starting point: step 1 says where the reader is (dashboard, tab, terminal) and which account or role they need
- [ ] Prerequisites sit in "Before you begin" and the page assumes nothing beyond them
- [ ] Expected result: the reader can tell each stage and the whole task worked, with something they can see or type
- [ ] Permissions and plan or CMS limits are stated, with a source
- [ ] Destructive or irreversible steps say so before the step, with the recovery path
- [ ] Known failures name the cause and the fix
- [ ] Every product claim traces to a source in the claim record, or sits in Open questions (`inputs-claims-and-sources.md`)
- [ ] Protected content (commands, output, UI labels, error text, URLs) matches the product, not a style rule

### Checklist

Before delivering any doc:

**Structure**
- [ ] Diátaxis quadrant identified and content serves only that quadrant
- [ ] Correct content type (`doc` vs `guide`) and file location
- [ ] Frontmatter complete with all required fields, including `reviewed` set to today's date
- [ ] Introductory paragraph present (no heading)
- [ ] "Before you begin" section if steps follow
- [ ] "More resources" section at the end

**Release notes only**
- [ ] Filename follows `YYYY-MM-DD-slug.md` and slug will produce the correct URL (the filename alone sets it)
- [ ] `published_at` is the real publish time, not `T00:00:00Z`; filename date, `published_date`, and `published_at` are consistent, or the difference is reported
- [ ] New announcement or correction: a correction keeps the original dates
- [ ] `description` present and written as a complete sentence
- [ ] Headings use sentence case (not title case)
- [ ] `action-required` category added if customer action is needed
- [ ] Links to relevant docs included

**Style**
- [ ] Sentence case on all headings
- [ ] One `#` title, sections at `##`, no skipped heading levels (Docs mode: real Heading styles, no bold-line titles)
- [ ] No source-gap or reviewer notes inside the page body (they belong in Open questions)
- [ ] Bold used only for UI elements and navigation
- [ ] Italics for emphasis (not bold)
- [ ] Second person throughout ("you", not "we" or "the user")
- [ ] Active voice
- [ ] Present tense
- [ ] Relative links for internal references
- [ ] Descriptive link text (no "click here")
- [ ] Code in backticks or fenced blocks with language identifier
- [ ] User oriented before giving instructions

**Inclusive language**
- [ ] No ableist, violent, gendered, or racial language
- [ ] Allowlist/blocklist (not whitelist/blacklist)
- [ ] They as default pronoun
- [ ] No idioms that exclude global readers

**Components**
- [ ] Correct callout type (info vs danger vs export)
- [ ] Partials checked for reusable content before writing new
- [ ] Tables use ✓ and ❌ (not ✔/✘)
- [ ] Images have alt text, no personal info, no added markup

**Mechanics**
- [ ] No trailing spaces
- [ ] Blank line at end of file
- [ ] Blank lines between YAML frontmatter and content, and between headings and content
- [ ] Redirect table in the handoff notes if the change moves or removes a URL (proposed unless authorized)

**Voice and claims** (see `voice-rules.md` and `inputs-claims-and-sources.md`)
- [ ] Searched the draft for be verbs (is, are, was, were, be, been, being) and fixed each one that hides an actor
- [ ] No hyperbole, opinion, intensifiers, or colloquialisms
- [ ] No rewrite added a claim the source doesn't support
- [ ] Every sentence about product behavior has a source, or sits in the open questions list
- [ ] The prerequisites heading is "Before you begin"
- [ ] Sample values use the style guide's placeholders (`placeholders-and-embeds.md`)

**Search findability, proposed** (see `seo-for-authors.md`; guidance, not a requirement)
- [ ] Opening paragraph states the outcome or answers the question
- [ ] Title and description make sense outside the site navigation
- [ ] Page links to its parent, related pages, and the next step
- [ ] Errors appear verbatim as H3s in a Troubleshooting section

**Automated checks** (`vale-and-checks.md`)
- [ ] Each gate check is marked passed, failed, unavailable, or not applicable, and none is marked passed unless it ran
- [ ] Errors fixed; warnings fixed or explained

