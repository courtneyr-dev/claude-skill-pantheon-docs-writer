# Tutorials

> Use when the reader is new and needs to learn by completing one meaningful project.
> Part of the `pantheon-docs-writer` skill. Return to `../SKILL.md`. Adapted from Diátaxis (diataxis.fr, CC BY-SA 4.0).

A tutorial leads a newcomer through one build and guarantees they finish it. The author carries the responsibility for success.

## Rules

- Open with what the reader builds or deploys ("In this tutorial, you deploy a Next.js site on P1"). Don't open with "you will learn".
- One path. No options, forks, or "you could also".
- Every step produces a visible result. Show the exact expected output.
- Say what to expect and what to notice ("The dashboard shows a new site named Anita Agency").
- Add a recovery line for the likeliest wrong turn ("If you see a 401, sign in again").
- Explain in one clause at most, and link to an explanation page for more.
- Use specific names and values (Anita Agency, Anita Drupal), not generic ones.
- Make steps re-runnable. Avoid steps that block a second attempt.
- End by naming what the reader built, then link onward.

## Don't

Reference tables, optional branches, background theory, assumed knowledge beyond "Before you begin".

## Skeleton

```markdown
---
title: Tutorial name
subtitle: Page name
description: One sentence naming what the reader builds.
contenttype: [guide]
innav: [true]
categories: [category-slug]
cms: [--]
audience: [development]
product: [--]
integration: [--]
reviewed: "YYYY-MM-DD"
---

One paragraph: what the reader builds, and how long it takes.

## Before you begin

- Items the reader must have, nothing more.

## Create the project

1. Where to be, then the action.
2. Expected result.

## What you built

Name the result and link to next steps.

## More resources
```

## Check before you deliver

- Does any step lack an expected result? Add one.
- Is there a fork? Remove it, or move it to a how-to.
- Does any explanation run past a clause? Move it to an explanation page.
- Did the steps run? If not, mark them unverified in open questions.
