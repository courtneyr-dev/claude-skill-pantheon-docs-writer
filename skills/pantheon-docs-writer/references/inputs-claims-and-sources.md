# Inputs, claims, and sources

> Use before you draft a new page and whenever a page states what a product does. The review of 25 docs produced 143 comment findings (questions for a person, not fixes). Many were product behavior stated without a source; the rest covered unsettled terms and where the reader starts. This step prevents them.
> Part of the `pantheon-docs-writer` skill. Return to `../SKILL.md` for the workflow.

## Inputs to get before you write

Ask for any you don't have. Don't fill a gap with plausible text.

1. **Reader and goal:** who reads the page and what they can do afterward.
2. **Starting point:** the exact place the reader begins (which dashboard, which tab, which tool). Open every procedure there ("Where's the User?").
3. **Prerequisites:** what the reader needs or already knows. They go in "Before you begin". Assume nothing beyond that section.
4. **Sources:** where each product claim comes from: a spec, a person, or the product itself.
5. **Product terms:** the exact names in the UI, and any term the team hasn't settled.
6. **Content type:** the Diátaxis quadrant (see `../SKILL.md`).

## What counts as a claim

Any sentence that states what a product does, or doesn't do:

- capabilities and limits ("supports up to...", "only once")
- defaults, versions, and availability ("available by default", "requires Node 24")
- behavior and side effects ("redirects all URLs under it")
- ownership and permissions ("administrators can...")
- numbers, times, and comparisons

## Mark each claim

| Marker | Meaning |
|---|---|
| `observed` | You saw it in the product, a screenshot, or the source. |
| `reproduced` | You ran it and got the result. |
| `reported` | A named person or doc said so; you haven't checked. |
| `inferred` | You reasoned to it from other facts. |
| `unverified` | No source yet. |

Only `observed`, `reproduced`, and a named `reported` source belong in the draft as stated fact. Everything else goes to open questions, with the sentence it blocks.

## Output format

Deliver three things:

1. **The draft.**
2. **Open questions:** each question, who can answer (product team, MCP owner, SDK owner, support), and the sentence it blocks.
3. **Self-check:** how many be verbs and banned words you fixed, and any claim left unsourced.

## Rules that keep rewrites honest

- A rewrite must not add a capability the source doesn't state. In the review, three rewrites would have invented claims ("meaningful services", "speed and governance"). The right fix was to leave the sentence for the author and ask.
- Don't turn "may" into "does", or "can" into "will".
- When you cut a hyperbolic phrase, keep any fact it carried.
- When two sources disagree (for example, two version numbers), don't pick one. Put the conflict in open questions.
- A screenshot shows how something looks. It doesn't prove how it behaves.
