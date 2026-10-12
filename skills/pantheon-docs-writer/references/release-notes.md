# Release notes

> Use for anything in `src/source/releasenotes/`. Release notes have their own structure and frontmatter.
> Part of the `pantheon-docs-writer` skill. Return to `../SKILL.md` for the workflow.

## Step 10: Writing Release Notes

Release notes live in `src/source/releasenotes/` and follow a completely different structure from docs and guides.

### What belongs in a release note

**Include:**
- New features, releases, and enhancements
- Known issues and workarounds
- Required user action to avoid service disruption
- Visual and UI changes
- Future roadmap items that can be disclosed ahead of time

**Do not include:**
- Marketing or promotional content
- Organizational, financial, or branding updates that aren't technical
- Legal or compliance changes with no user-facing impact

### File naming

```
YYYY-MM-DD-short-slug.md
```

**The filename determines the URL.** `2026-06-15-terminus-4-4-0.md` becomes `/release-notes/2026/06/terminus-4-4-0`. Use the date the change goes live or is announced — not the date you're writing the file.

### Frontmatter

Release notes use a distinct schema. Do not use `contenttype`, `innav`, `audience`, or other regular doc frontmatter fields.

```yaml
---
title: "Short, specific title describing what changed"
published_date: "YYYY-MM-DD"
published_at: "YYYY-MM-DDTHH:MM:SSZ"
categories: [category-slug, category-slug]
description: "One sentence summary shown in listings and RSS."
---
```

| Field | Required | Notes |
|---|---|---|
| `title` | yes | Specific and descriptive. Use quotes if it contains special characters. |
| `published_date` | yes | ISO date: `"YYYY-MM-DD"` |
| `published_at` | yes | Full ISO timestamp — reflects the actual publish time; drives RSS ordering. Format: `"2026-06-15T14:00:00Z"` |
| `categories` | yes | One or more slugs from the list below |
| `description` | yes | One sentence shown in listing pages and RSS feeds |

### Categories

Choose from the slugs in `src/source/releasenotescategories/releaseNoteCategories.json`:

| Slug | When to use |
|---|---|
| `new-feature` | New capabilities or improvements |
| `action-required` | Customer must act to avoid disruption |
| `infrastructure` | Platform/infrastructure changes |
| `security` | Security fixes or updates |
| `wordpress` | WordPress-specific changes |
| `drupal` | Drupal-specific changes |
| `plugins` | Pantheon-maintained WordPress plugin updates |
| `modules` | Pantheon-maintained Drupal module updates |
| `tools-apis` | Terminus, APIs, CLI tools |
| `user-interface` | Dashboard/UI changes |
| `performance` | Performance improvements |
| `deprecated` | Features being phased out |
| `policy` | Policy changes |
| `billing` | Billing and finance |
| `account-management` | Account/permissions changes |
| `migration` | Migration-related updates |
| `documentation` | Significant doc additions or changes |
| `nextjs` | Next.js support changes |
| `content-publisher` | Content Publisher updates |
| `general` | Catch-all for changes that don't fit elsewhere |

Use multiple categories when appropriate: `[wordpress, action-required]`.

### Writing guidelines

#### 1. Headings use sentence case

Release notes use **sentence case** for all headings — capitalize only the first word and proper nouns. This is the same rule as regular docs.

- ✅ `## Explore new features in Pantheon's latest Drupal updates`
- ❌ `## Explore New Features in Pantheon's Latest Drupal Updates`

#### 2. Lead with what changed and why it matters

The opening paragraph should summarize the core change and its benefit to the user. Don't bury the point.

- ✅ "Turbo Boost is now available to elevate your site's speed with optimized server resources."
- ❌ "We've made a few changes in the latest release."

#### 3. Headings should capture the key message

Don't just name the thing — say what it does or why it matters.

- ✅ "Introducing Turbo Boost for enhanced site performance"
- ❌ "Turbo Boost is launched"

#### 4. Use bullets for lists of changes or benefits

Break substantial information into bullet points and short paragraphs. Don't pack multiple distinct benefits into a single run-on sentence.

#### 5. Link to docs for deeper context

End with or include a link to the relevant documentation:

- ✅ "Ready to learn more? See [Turbo Boost documentation](/turbo-boost)."
- ❌ "For more info, check out our documentation."

#### 6. Include visuals for UI changes

For UI changes and step-by-step instructions, include screenshots. Images go in `src/source/images/release-notes/`.

### Body structure patterns

**Simple announcement:**
```markdown
Brief description of what changed and why it matters.

[Learn more in the documentation](/path/to/doc).
```

**Action required:**
```markdown
Brief description of what changed.

## Action required

What the customer must do, by when, and what happens if they don't act.

[Upgrade instructions](/path/to/doc).
```

**Version release (Terminus, plugin, module):**
```markdown
[Product Name X.Y.Z](link-to-github-release) is now available. One sentence on what's new.

## Key improvements in this release

- **Feature name** — what it does ([#PR](link))
- **Fix name** — what it fixes ([#PR](link))

## How to upgrade

Steps or link to upgrade documentation.
```

### Release note style rules

- Present tense: "Terminus 4.3.0 is now available" — not "has been released"
- Lead with customer benefit, not internal implementation details
- Titles should be specific: "PHP 7.2, 7.3, and 8.0 are now End of Sale" — not "PHP version update"
- Always use `action-required` category when customers must do something to avoid disruption
- The body is standard Markdown — no MDX components
