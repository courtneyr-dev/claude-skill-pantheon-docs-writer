# Review checklist

> Run before delivering or committing any doc.
> Part of the `pantheon-docs-writer` skill. Return to `../SKILL.md` for the workflow.

## Step 9: Review Checklist

Before delivering or committing any doc:

**Structure**
- [ ] Diátaxis quadrant identified and content serves only that quadrant
- [ ] Correct content type (`doc` vs `guide`) and file location
- [ ] Frontmatter complete with all required fields, including `reviewed` set to today's date
- [ ] Introductory paragraph present (no heading)
- [ ] "Before you begin" section if steps follow
- [ ] "More resources" section at the end

**Release notes only**
- [ ] Filename follows `YYYY-MM-DD-slug.md` and slug will produce the correct URL
- [ ] `published_at` set to an accurate ISO timestamp
- [ ] `description` present and written as a complete sentence
- [ ] Headings use sentence case (not title case)
- [ ] `action-required` category added if customer action is needed
- [ ] Links to relevant docs included

**Style**
- [ ] Sentence case on all headings
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
- [ ] Redirect table in PR if moving or removing any URLs
