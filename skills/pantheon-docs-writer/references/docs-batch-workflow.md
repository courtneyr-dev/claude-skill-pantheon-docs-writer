# Tutorial batch workflow: walkthrough, test bed, panel, tickets

> Use when you draft, verify, and hand off tutorials or how-tos that describe a running product (an editor, a CLI, or a dashboard), for one doc or many. The rules come from a tutorial run on 2026-10-21: three pilot P1 docs, a three-lens review panel, 43 passing tests, and an editor walkthrough that still found a wrong sentence.
> Part of the `pantheon-docs-writer` skill. Return to `../SKILL.md` for the workflow. Claim markers are in `inputs-claims-and-sources.md`; the gate is in `vale-and-checks.md`; Docs mode rules are in `docs-mode.md`.

## Walkthrough first

A claim about runtime or editor behavior that you read from source or docs stays `inferred` until someone runs it in the real editor. Run the editor walkthrough before the reviewer panel.

Evidence from the run:

- The draft said "a new tab starts on Live". A three-lens panel and 43 passing tests let it through. The tests assert strings in SDK source, so they can't see runtime behavior.
- The walkthrough had 12 checks. 10 passed (one of them, a reload keeping the workstream, wasn't conclusive), 1 failed and 1 wasn't run. Check 8 failed: a new tab opened on `Bureau site build`, not on Live. The project's `.env` sets `NEXT_PUBLIC_CSS_BRANCH_ID` to that workstream, but nobody removed the variable to confirm it's the cause.
- The same walkthrough settled an open question (a block that no category lists appears under **Other**) and showed the category label displays in capitals.
- Across the three pilot docs, 29 `it.todo` editor steps (9, 6, and 14) were unrun. Each was its doc's top risk.

"Ready for human review" requires no `inferred` or `unverified` marker on a runtime claim. Put the walkthrough results in the notes file, then update the draft's claim markers from them. When a result differs from the draft, rewrite the sentence to match the result and move the evidence to the notes.

## Generate the walkthrough checklist

For each tutorial, write `walkthrough-checklist.md` from two inputs: the claim table, and the `it.todo` list in the test file. One `it.todo` or one runtime claim becomes one numbered check. Don't add checks the draft doesn't need.

Use this structure.

```markdown
# Walkthrough checklist: <doc title> (<ticket>)

Run this on <the test bed, see below>. Don't publish anything. Where a result differs from "Expect", change the draft and tell the author.

## A. Set up

- [ ] <one command or action per line, with the output to expect>

## B. Checks

| # | Check | Expect | Draft sentence it tests | If different |
|---|---|---|---|---|
| 1 | <what to do and look at> | <exact result> | "<the sentence, quoted>" | <what to change> |

## C. Record your results

For each check, write pass, or what you saw. The author updates the draft's claim markers and marks the `it.todo` entries done.
```

Rules for the table:

- **Check** names the action and where to look. **Expect** states a result you can compare, not "works".
- **If different** says what to change: rewrite the step, delete the sentence (when the only source is code), or send the console error to the author.
- Add one row for anything the draft leaves vague ("reload the editor"): record how long the editor takes, or which command you actually ran.
- Setup lists every file you edit, so cleanup can undo it. End the checklist with a cleanup section when the setup creates a branch, a test page, or a config change.

## Use a fresh scaffold as the test bed

Verify and screenshot a tutorial on a fresh scaffold of the starter (`pnpm create @pantheon-systems/p1-starter-kit`), not on a customized sandbox.

Evidence from the run:

- The sandbox was a themed fan-site build: a custom heading font, custom colors, the site name in metadata, and its own skip-link styles. Copying it for screenshots needed the theme stripped across four production rebuilds.
- The tutorial's claims about "your starter site" never ran on a pristine scaffold.

For final screenshots:

- Capture from a production build. A dev server adds an overlay badge.
- Use a browser profile without extensions. In the run, an extension changed `<html>` and triggered a dev-only hydration warning.
- Use a site whose name is safe to publish.

## Plan screenshots from the first draft

Keep the capture list in the notes file from the first draft, not after the text is final. Each row gives the state to capture, the step it supports, the viewport, and who signs in.

- Use a smaller viewport, about 1100x700 at 2x, so the UI stays legible at the docs column width.
- Annotate with the Annotation kit (see `brand-and-assets.md`).
- The kit-stamp check must pass before capture. The `screenshots-to-docs` skill describes it.
- A capture that needs a live change (merge, publish, delete) needs the user's go-ahead first.

## Review packet and panel

Give each reviewer a packet, not the whole repo:

1. The draft.
2. The claim table.
3. The numbered decision list (see `inputs-claims-and-sources.md`, "Decisions file").
4. The diff since the last pass.

Run one parallel pass. Roster:

| Lens | Reviews for |
|---|---|
| Docs-site owner | Placement, titles, nav, image hosting, the site's conventions |
| Engineer or SDK owner | Product behavior, names, defaults, code |
| Support | Where a reader gets stuck, error messages, missing prerequisites |
| UI strings | Labels and messages shown in the product. Run the `pantheon-product-design:ux-writing` skill. |

Add an accessibility lens or a security lens only when the doc touches either.

Cost control:

- Mechanical stages (Vale, tests, links, image checks) run as scripts, not models.
- Reviewers run on a mid-tier model at low effort.
- The strongest model only fixes blocking findings.

Stop rule: end after two consecutive passes with 0 blocking findings. Cap same-lens passes at 3. Route each remaining open question to a named role, not another pass.

Evidence: the PCC-4133 doc took five passes that returned 2, 1, 0, 0, and 0 blocking findings and 5, 10, 8, 4, and 4 warnings. The three-doc pilot used about 2.5M subagent tokens, 467 tool uses, and 51 minutes.

### Build the docs-site-owner lens from real review comments

The docs-site owner's review is the one you can't replace, so distill it from the owner's own words.

1. Collect the owner's review comments from past docs PRs and Doc threads (`gh api repos/<repo>/pulls/<n>/comments`, or the Doc's comment export). Keep the comment text, the sentence it hit, and whether it blocked.
2. Group the blocking comments by pattern (title wording, nav placement, image path, link form). Count each group.
3. Write the lens as an agent file. It lists each pattern with one verbatim example, states the rule the owner applied, and says what the lens can't judge. Mark every finding the lens makes `inferred`.
4. Quote the owner. Don't paraphrase a ruling into a rule the owner never stated.

After each real review by the owner, log which blocking comments the lens missed. Keep one row per comment: doc, comment, pattern, whether the lens caught it. The measure is misses per doc. A miss adds a pattern to the lens. A pattern with no hit across three docs comes out.

## Gate order

Run the cheapest check first and stop at the first failure you can fix:

1. Deterministic checks: Vale with the shared config, structure and code tests, link check, image checks, claim-marker counts.
2. Editor walkthrough.
3. One panel pass.
4. Status update on the ticket.

Details for step 1 are in `vale-and-checks.md`, "Gate order and Vale setup".

## Ticket status

Keep one status record per doc. Fields: stage, tests passing and `todo`, Vale errors, open questions, and who is needed.

Post one templated Jira comment per milestone: draft ready, checks green, walkthrough done, review requested, changes after review. Each comment copies the status record and adds the milestone's one new fact (the checklist result, the reviewer's name, the diff link).

Use the Atlassian MCP or the REST API. Don't drive the Jira UI with automation: in the run, UI typing triggered Jira keyboard shortcuts and about 20 stray assignee changes.

The docs lead creates tickets under the agreed parent epic. Don't create a ticket, change an assignee, or transition a status without the user's go-ahead.
