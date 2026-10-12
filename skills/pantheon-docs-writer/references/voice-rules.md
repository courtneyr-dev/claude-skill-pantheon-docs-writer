# Voice rules

> Use when drafting or editing prose. These rules come from the style guide's "Voice, Style, and Flow" section. They're ordered by how often writers broke them in a review of 25 docs (273 style findings), so fix the early ones first.
> Part of the `pantheon-docs-writer` skill. Return to `../SKILL.md` for the workflow.

The style guide says:

- Avoid be verbs.
- Avoid personal opinions, feelings, or anecdotes. Use an informal but succinct tone.
- Use inclusive language. Avoid colloquialisms and hyperbole.
- Assume only the knowledge the Before you begin section states.

## 1. Avoid be verbs (about 43% of review findings)

Be verbs: is, are, was, were, be, been, being, and phrases built on them ("can be used", "will be shown", "is able to").

**How to fix one:** name who or what acts, then use a verb that says what they do. If you can't name the actor, you may lack a fact. Ask for it (see `inputs-claims-and-sources.md`) instead of keeping a vague passive.

| Before | After |
|---|---|
| Pages are editable in the visual editor and their content is stored in the repository. | You edit pages in the visual editor, and the platform stores their content in the repository. |
| The route is defined by the location in the site structure and their slug. | The location in the site structure and the page slug define the route. |
| Locked blocks cannot be modified by editors without permission. | Editors cannot modify locked blocks without permission. |
| The token is only shown once. | The API shows the token only once. |
| Whether you are overseeing a single flagship site or a portfolio of sites... | Whether you oversee a single flagship site or a portfolio of sites... |
| A localized page can be a translation of a source page. | A localized page can translate a source page. |
| The Metadata section is collapsed by default so optional fields don't take space. | The Metadata section stays collapsed by default so optional fields don't take space. |
| A live environment is required for any production use. | Production use requires a live environment. |
| The default branch is main. | The repository uses `main` as its default branch. |
| You are able to filter the list. | You can filter the list. |
| Confirm that the block is available on the site. | Confirm that the site has the block. |
| At this time, the release is private. | Pantheon limits access during the private release. |
| Confirm that you are working in the intended workstream. | Confirm that you work in the intended workstream. |
| The field was left empty. | You left the field empty. |

**Rules for the rewrite:**
- Every be verb is the main verb of a clause unless it is the exception below. "is collapsed", "is required", "is stored", "is shown" all count, and so does a be verb after a comma or "so that". Replace each one: use an active verb, a state verb ("stays", "remains", "requires", "uses"), or "can".
- Contractions count: "it's available", "that's required", "you're working" are be verbs. So are progressive forms ("you are working", "is being created"), passives with "was" or "were" ("a field that was left empty"), and predicate adjectives ("is available", "is private", "is in beta"). For a state, name who or what limits or provides it ("the site has the block", "Pantheon limits access").
- Re-read your rewrite and search it for is, are, was, were, be, been, being, 's and 're before you answer. If one remains as the main verb, rewrite again.
- The only exception: a glossary-style definition of a term, where every alternative reads worse ("A workstream is a unit of work"). Keep it rare. Product intros, overviews, and feature descriptions aren't definitions: name the product as the actor ("P1 unites business tools and developer workflows in one platform", not "P1 is a platform that...").

**Don't over-correct:**
- Don't swap a be verb for a vague verb ("handles", "leverages", "provides"). Pick the verb that says what happens.
- A rewrite must not add a claim the source doesn't support. If the better verb implies a capability you haven't confirmed, keep your original wording and flag the claim.

## 2. No hyperbole, opinion, or colloquialism (about 17%)

Replace the phrase with a fact, a number, or a mechanism. If nothing remains after you cut it, delete the sentence.

**Marketing claims:** seamless(ly), effortless(ly), intuitive(ly), enterprise-grade, cutting-edge, best-in-class, world-class, state-of-the-art, game-changer, next-level, unprecedented, "zero risk", "faster than ever", "superior", "the best".

**Intensifiers:** extremely, incredibly, absolutely, perfectly, fundamentally.

**Opinion:** "we believe", "great for", "ideal for", "the best way". State the condition instead ("use this when you need X").

**Colloquialisms and idioms:** dive in or deeper, heads-up, under the hood, in one shot, a ton of, gotcha, no-brainer, "pretty simple", "stepping on toes", "juggling environments", "where your team lives".

| Before | After |
|---|---|
| Superior speed and control at scale | Speed and control at scale |
| ...build, manage, and scale websites faster than ever without losing control. | ...build, manage, and scale websites without losing control. |
| That's extremely helpful when you want to stage changes. | This lets you stage changes before they go live. |
| Heads-up: this changes what happens on unknown paths. | Note: this changes what happens on unknown paths. |
| ...not by juggling environments. | ...not by switching between environments. |
| Ready to dive deeper? Explore the guide to learn how to... | Next, learn how to... |
| Dive deeper into the component model. | Read the component model reference. |

A claim you delete may have been the only copy of a fact. Before you cut a number or a capability, check whether it belongs in the draft with a source.

## 3. Voice basics

- Second person, present tense, active voice. Say "you" and name the product ("P1 stores...", "Terminus returns...").
- Skip throat-clearing openers ("In this guide, we will cover...").
- One term per concept. Use the product's UI label.
- Short paragraphs. Put the outcome or key warning first.
- Spell out an acronym on first use unless every reader knows it.

## When you're asked to return only revised text

Output the revised text and nothing else: no self-check, no commentary, no earlier attempts. Do the checks below silently, and fix problems before you answer. Never print a draft and then a correction.

## Quick self-check before you deliver

1. Search the draft for is, are, was, were, be, been, being. Fix each that hides an actor.
2. Search for the words in section 2.
3. Read each heading for sentence case.
4. For each sentence that states product behavior, find its source or move it to open questions.
