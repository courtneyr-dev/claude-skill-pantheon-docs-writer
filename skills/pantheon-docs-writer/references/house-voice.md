# House voice: what real Pantheon pages sound like

> Use before you draft any page, and again when a draft reads flat or machine-made. This file calibrates tone; `voice-rules.md` holds the pass/fail rules.
> Part of the `pantheon-docs-writer` skill. Return to `../SKILL.md`.
> Observed 2026-10-12 in `pantheon-systems/documentation` (main @ 9b15056): `guides/mcp/`, `guides/multidev/`, `guides/git/06-resolve-merge-conflicts.md`. Quotes are short and show the pattern; re-read the source pages before you rely on them.

## What the pages do

| Pattern | Example from the docs |
|---|---|
| State the real condition in the first sentence, not a topic label. | "It's read-only by default; anything that changes something requires your explicit approval in your AI client before it runs." (`guides/mcp/01-introduction.md`) |
| Give the number or the limit. | "Each site has a limit of 10 Multidev environments." Branch names "no more than 11 characters". |
| Say what the reader will see or wait for. | "It will take a few minutes to create the environment... You can continue working on the Dashboard while it's being created." |
| Name the cause and the fix for a known failure. | "If you receive an error message that the clone was aborted, clear caches on the source environment and retry the procedure." |
| Say what to do and why in the same breath. | "We recommend that you use the Pantheon platform instead" of deleting branches locally, "but this may have unintended consequences". |
| End a procedure by telling the reader how to check it worked, with something they can type. | "Verify the installation by asking either of these questions: Are you connected to Pantheon MCP?" |
| Admit limits plainly, in a table. | "Not applicable to Next.js sites... It fails with a generic 'operation failed' message. For these sites, code is deployed by pushing to the external repository." (`guides/mcp/03-known-limitations.md`) |
| Use the product's labels in bold and the path in one clause. | "Go to the Site Dashboard, then click the **Multidev** tab." |
| Use contractions and "you". | "doesn't", "can't", "You can create a new fork..." |

## What made a draft read as machine-written

A P1 how-to draft on 2026-10-12 had these problems. Check yours for them.

- **A catalog of prompts with no consequence.** Five prompts in a row, none says what happens or why you'd pick one. Real pages tell the reader what to expect after each step, or admit they don't know yet in the open questions.
- **Parallel scaffolding.** Every section opened "Type:" followed by a quote. Vary the rhythm: some steps need a sentence of context, some need a warning, some need nothing.
- **A topic-label opening.** "Merge a workstream to move its changes to the live site." restates the title. Open with the reader's situation or the stake ("Mark's page is finished, and it's sitting in a workstream where only you can see it").
- **Repeated reassurance.** "You don't need tool names" said twice adds nothing after the first time.
- **Everything the tool can do, listed.** A how-to follows the path the reader needs. Put the rest in one sentence and a link.
- **No decision.** When the reader faces a real choice (merge directly or ask for a review), say what each choice costs and who it suits, using only sourced facts.

## Limits of this file

- It describes tone, not facts. It never licenses a claim about the product. A draft that gets more specific by inventing an outcome, a time, or a limit has failed.
- Older pages carry marketing-style lines ("you can't have too many cooks in a Multidev kitchen"). Don't copy those. The style guide's ban on idiom and hyperbole still applies.
- Where a source gap blocks the specific detail that would make a page interesting, say so in Open questions. Don't fill it with color.
