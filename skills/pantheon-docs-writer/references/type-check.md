# Type check: classify, detect mixed pages, split, and find gaps

> Use at step 2, before you write or revise a page, and when asked what docs a feature still needs.
> Part of the `pantheon-docs-writer` skill. Return to `../SKILL.md` for the workflow.
> Method adapted from Diátaxis (diataxis.fr, Daniele Procida, CC BY-SA 4.0). Pantheon mappings and examples are this skill's own.

## Classify with two questions

1. Does the reader need to *do* something (action) or *know* something (cognition)?
2. Is the reader *learning* the product (study) or *working* with it (application)?

| Action + learning | Action + working | Knowing + working | Knowing + learning |
|---|---|---|---|
| Tutorial (`tutorials.md`) | How-to guide (`how-to-guides.md`) | Reference (`reference-docs.md`) | Explanation (`explanation.md`) |

Classify by what the reader needs, never by topic. Report the type, a confidence (high, medium, low), and the evidence: the phrases and structure that signal it.

## Detect a mixed page

Read the page section by section and classify each section. A page is mixed when its sections land in different quadrants. Common signals:

- A procedure that stops to explain why, for more than a clause (how-to plus explanation).
- A walkthrough with option tables or "you could also" forks (tutorial plus reference).
- A reference table with a numbered setup procedure above it (reference plus how-to).
- An overview that describes the architecture, then lists steps (explanation plus how-to).

Don't force a type onto a mixed page, and don't score a page by its title. Introductions and "Overview" pages often serve one need in the first paragraph and another by the end.

## Split a mixed page

1. Name each quadrant the page serves and list which sections belong to each.
2. Keep the quadrant the page's title promises. Move the rest to its own page.
3. Replace each moved section with one sentence and a link ("For why P1 stores content in the CRR, see [How P1 stores content](/p1/architecture)").
4. Keep moved content intact. Don't delete it to make the page fit.
5. If you change a URL, add a redirect (`navigation-and-redirects.md`).

## Assess what to create

For a feature, product area, or doc set:

1. List the reader jobs: what a new reader must learn, tasks a working reader repeats, facts they look up, and decisions that need background.
2. For each job, find the existing page that serves it, and mark it served, partly served (mixed or thin), or missing.
3. Write the result as a table: job, quadrant, page, status, evidence. Evidence is a quote or a file path.
4. Don't create a page for an empty cell unless a real reader job exists. An area with one good page may be done. Never add placeholder pages.
5. Rank gaps by reader harm: a missing how-to for a common task outranks a missing explanation.

## Pantheon notes

- The style guide says second person ("you"). Diátaxis tutorials traditionally use "we". Use "you" in Pantheon docs.
- Tutorials usually become guides (`contenttype: [guide]`). Other types usually become single docs. See `content-types-and-frontmatter.md`.
