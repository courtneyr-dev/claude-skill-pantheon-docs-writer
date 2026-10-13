# Explanation

> Use when the reader needs to understand why: concepts, architecture, trade-offs, design decisions.
> Part of the `pantheon-docs-writer` skill. Return to `../SKILL.md`. Adapted from Diátaxis (diataxis.fr, CC BY-SA 4.0).

Explanation gives context that makes the rest of the docs make sense. Readers study it away from the keyboard.

## Rules

- Name the topic in the title and open with the question it answers ("Why P1 separates content from rendering").
- Give the context: history, the problem, the constraint, the alternatives, the trade-off.
- Connect concepts to each other and to the pages that apply them.
- Make claims you can source. A design reason needs a person or a document behind it. Mark the rest as an open question.
- Use a diagram when relationships matter. Add alt text.
- State boundaries: when this approach doesn't fit.
- Link to the how-to and reference pages instead of repeating them.

## Don't

Step-by-step procedures, exhaustive option lists, or opinion presented as fact. Don't use hyperbole to sell the design; state what it does and what it costs.

## Skeleton

```markdown
---
title: Concept title
description: One sentence stating the question this page answers.
contenttype: [doc]
innav: [true]
categories: [category-slug]
cms: [--]
audience: [development]
product: [--]
integration: [--]
reviewed: "YYYY-MM-DD"
---

One paragraph: the question and why it matters.

## The problem

## How it works

## Trade-offs and alternatives

## More resources
```

## Check before you deliver

- Does a numbered procedure appear? Move it to a how-to.
- Does every design claim have a source?
- Can a reader say why, not only what, after reading it?
