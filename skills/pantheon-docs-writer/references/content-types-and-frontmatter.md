# Content types, file location, and frontmatter

> Use when choosing `doc` vs `guide`, deciding where the file goes, or writing frontmatter for a doc or guide. Release notes use a different schema: see `release-notes.md`.
> Part of the `pantheon-docs-writer` skill. Return to `../SKILL.md` for the workflow.

## Choose content type and file location

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

## Frontmatter

Every file requires frontmatter at the very top, wrapped in `---`.

### Fields to set on every doc

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
reviewed: "2026-10-12"
---
```

Checked against `pantheon-systems/documentation` main@9b15056: `src/source/data/schema.yaml` marks only `title`, `contenttype`, `innav`, and `categories` as required. Nothing validates frontmatter at build time (the `Frontmatter` type in `src/server/processor/mdx.tsx` has every field optional), so a missing field fails silently. The style guide and `doc-template.md` ask for the rest. Set them all.

### Full frontmatter reference

| Field | Basis | Type | Notes |
|---|---|---|---|
| `title` | schema: required | string | Title of doc or guide (shared across all guide pages) |
| `contenttype` | schema: required | array | One of `api`, `doc`, `guide`, `landing`, `partial`, `product`. The style guide says it defaults to `doc`. |
| `innav` | schema: required | array | `[true]` for first/only page; `[false]` for guide subsections. Declared, but not a navigation driver. |
| `categories` | schema: required | array | A closed list in `schema.yaml`. Use a listed slug, not a new one. |
| `description` | template, style guide | string | One sentence summary |
| `cms` | template, style guide | array | `[wordpress]`, `[drupal]`, `[wordpress, drupal]`, or `[--]`. Not in `schema.yaml`. |
| `audience` | template | array | `[development]`, `[agency]`, `[business]`, `[sysadmin]`, `[marketing]` |
| `product` | template | array | A closed list in `schema.yaml`, or `[--]` |
| `integration` | template | array | `schema.yaml` lists `modules` and `plugins`; use one of those or `[--]` |
| `reviewed` | style guide | string | "The last date when the content was updated or reviewed for accuracy." ISO date, quoted: `"2026-10-12"`. Set it to the date you updated or reviewed the page. |
| `subtitle` | optional | string | Guide pages only: unique title for this page. (`schema.yaml` spells it `sub-title`; the code and style guide use `subtitle`.) |
| `navtitle` | optional | string | Guide pages only: the navigation title. `getGuideDirectory` reads it before `subtitle`. |
| `tags` | optional | array | Search tags |
| `contributors` | optional | array | IDs that match an entry in `src/source/data/contributor.yaml` (the style guide says so), not arbitrary GitHub usernames |
| `showtoc` | optional | boolean | `true` to show right-side table of contents |
