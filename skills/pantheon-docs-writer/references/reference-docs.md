# Reference docs

> Use when readers look up exact facts: commands, fields, options, limits, tool names, API shapes.
> Part of the `pantheon-docs-writer` skill. Return to `../SKILL.md`. Adapted from Diátaxis (diataxis.fr, CC BY-SA 4.0).

Reference describes the product and nothing else. Readers scan it; they don't read it top to bottom.

## Rules

- Mirror the product's own structure (the same order as the UI, the CLI, or the schema).
- Use one pattern per entry, so the reader finds the same fact in the same place.
- Be complete and neutral. Record defaults, limits, types, allowed values, and error codes.
- Use tables and lists. Use the exact names from the UI, API, or code, in inline code where they're typed values.
- State facts. No instruction, opinion, or explanation. A short example per entry is fine.
- Every fact needs a source: the schema, the code, or the product. Mark an unsourced fact as an open question.
- Link out for tasks and background; don't embed them.

## Don't

Numbered procedures, narrative, "you should", and marketing description.

## Skeleton

```markdown
---
title: Thing reference
description: One sentence naming what this page lists.
contenttype: [doc]
innav: [true]
categories: [category-slug]
cms: [--]
audience: [development]
product: [--]
integration: [--]
reviewed: "YYYY-MM-DD"
---

One sentence: what this page covers and its scope.

## Entry name

One-line description.

| Field | Type | Default | Description |
|---|---|---|---|
| `name` | string | none | What it controls. |

## More resources
```

## Check before you deliver

- Does any entry give instructions? Move them to a how-to.
- Does every entry follow the same pattern?
- Do the names match the product exactly?
