# How-to guides

> Use when a reader who knows the basics needs to complete a specific task.
> Part of the `pantheon-docs-writer` skill. Return to `../SKILL.md`. Adapted from Diátaxis (diataxis.fr, CC BY-SA 4.0).

A how-to guide gets a competent reader from a stated starting point to a stated goal.

## Rules

- Title it for the outcome ("Connect an AI assistant to P1"), not the feature ("MCP").
- State the starting point in the first step: which dashboard, tab, or tool ("In the P1 dashboard, open the site's **Users** tab").
- Put prerequisites in "Before you begin" and define repeated variables there.
- Write steps as imperatives. One action per step.
- Assume skill, not setup. Don't teach concepts; link to an explanation.
- Cover the real task, including the branch a working reader hits ("If the site uses Drupal, ...") only when it's common. Otherwise write a second guide.
- Add Troubleshooting for known failure modes, with error text verbatim as the heading.
- Show a verification step so the reader knows the task worked. Say where the reader opens the result (a public URL, a dashboard, a terminal), and list the exact values to check.
- Write each step so it works without a screenshot. A screenshot supports a step; it doesn't carry one. A capture that needs a live change (merge, publish, delete) needs the user's go-ahead before you take it.

## Don't

Teach from zero (tutorial), list every option (reference), or argue why (explanation).

## Skeleton

```markdown
---
title: Outcome-focused title
description: One sentence stating what the reader accomplishes.
contenttype: [doc]
innav: [true]
categories: [category-slug]
cms: [--]
audience: [development]
product: [--]
integration: [--]
reviewed: "YYYY-MM-DD"
---

One paragraph: the task and when to do it.

## Before you begin

- Prerequisites.

## Do the first stage

1. Where to be, then the action.

## Verify the result

## Troubleshooting

### Verbatim error message

## More resources
```

## Check before you deliver

- Does step 1 say where the reader starts?
- Does a paragraph teach a concept? Move it out and link.
- Can the reader tell the task worked?
