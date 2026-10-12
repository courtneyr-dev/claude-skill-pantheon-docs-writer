# Content types, file location, and frontmatter

> Use when choosing `doc` vs `guide`, deciding where the file goes, or writing frontmatter for a doc or guide. Release notes use a different schema: see `release-notes.md`.
> Part of the `pantheon-docs-writer` skill. Return to `../SKILL.md` for the workflow.

## Step 2: Choose Content Type and File Location

### Docs (`contenttype: [doc]`)
- Single Markdown file
- Location: `src/source/content/FILENAME.md`
- Use for: explanations, references, standalone how-tos

### Guides (`contenttype: [guide]`)
- Paginated, multiple files in a directory
- Location: `src/source/content/guides/GUIDE-NAME/FILENAME.md`
- First page of the guide: `innav: [true]`; all other pages: `innav: [false]`
- All pages share the same `title:` (the guide name), each gets a unique `subtitle:`
- Use for: tutorials, complex how-tos that walk through several logical phases

## Step 3: Frontmatter

Every file requires frontmatter at the very top, wrapped in `---`.

### Minimal required fields

```yaml
---
title: Title of the Doc or Guide
description: One sentence describing what this doc covers or accomplishes.
contenttype: [doc]
innav: [true]
categories: [category-slug]
cms: [--]
audience: [development]
product: [--]
integration: [--]
reviewed: "2024-06-01"
---
```

### Full frontmatter reference

| Field | Required | Type | Notes |
|---|---|---|---|
| `title` | yes | string | Title of doc or guide (shared across all guide pages) |
| `description` | yes | string | One sentence summary |
| `contenttype` | yes | array | `[doc]` or `[guide]` |
| `innav` | yes | array | `[true]` for first/only page; `[false]` for guide subsections |
| `categories` | yes | array | Content category slugs |
| `cms` | yes | array | `[wordpress]`, `[drupal]`, `[wordpress, drupal]`, or `[--]` |
| `audience` | yes | array | `[development]`, `[agency]`, `[business]`, `[sysadmin]`, `[marketing]` |
| `product` | yes | array | Specific Pantheon product or `[--]` |
| `integration` | yes | array | Third-party integration name or `[--]` |
| `reviewed` | yes | string | ISO date of last review: `"2024-06-01"` — always set to today when creating a new doc |
| `subtitle` | no | string | Guide pages only — unique title for this page |
| `tags` | no | array | Search tags |
| `contributors` | no | array | GitHub usernames |
| `showtoc` | no | boolean | `true` to show right-side table of contents |
