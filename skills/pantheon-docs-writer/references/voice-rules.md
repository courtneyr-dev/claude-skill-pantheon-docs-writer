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
| Pages are editable in the visual editor and their content is stored in the repository. | You edit pages in the visual editor, and their content lives in the repository. |
| The route is defined by the location in the site structure and their slug. | The location in the site structure and the page slug define the route. |
| Locked blocks cannot be modified by editors without permission. | Editors cannot modify locked blocks without permission. |
| The token is only shown once. | The token appears only once. |
| Whether you are overseeing a single flagship site or a portfolio of sites... | Whether you oversee a single flagship site or a portfolio of sites... |
| A localized page can be a translation of a source page. | A localized page can translate a source page. |
| The Metadata section is collapsed by default so optional fields don't take space. | The Metadata section stays collapsed by default so optional fields don't take space. |
| A live environment is required for any production use. | Production use requires a live environment. |
| The default branch is main. | The repository uses `main` as its default branch. |
| You are able to filter the list. | You can filter the list. |
| At this time, the release is private. | The release stays private at this time. |
| Confirm that you are working in the intended workstream. | Confirm that you work in the intended workstream. |
| The field was left empty. | You left the field empty. |

These pairs keep the source's meaning, and none names an actor the source didn't name.

**Factual fidelity breaks every tie.** When the be-verb rule and the facts disagree, the facts win:

- Keep the source's meaning, certainty, conditions, and modality. "May" stays "may", "can" stays "can", "only once" stays "only once", and "in early access" stays a condition.
- Name an actor only when the source (or the product, which you observed) names it. If you can't name one, use a verb that adds no actor and no capability: "appears", "stays", "remains", "requires", "has", "uses".
- If no such verb keeps the meaning, leave the sentence as written. Flag it in Open questions, unless you're in return-only mode (below), where you return it unchanged.
- A be verb you keep is a correct result. An invented actor is a defect.

| Source | Don't write (invents an actor) | Write |
|---|---|---|
| The token is only shown once. | The API shows the token only once. | The token appears only once. |
| The export is available to accounts in early access. | Pantheon limits the export to accounts in early access. | Accounts in early access have the export. |
| Backups are retained for 30 days. | Pantheon deletes backups after 30 days. | Backups stay for 30 days. |

**Protected content isn't prose.** Don't rewrite these to satisfy a be-verb, case, or Vale rule: commands and code, exact UI labels (`**Create Multidev Environment**` keeps its capitals), error messages and quoted output, URLs and identifiers, and source quotations. Fix the prose around them. A heading that contains a product name or a UI label keeps that name as written.

**Rules for the rewrite:**
- Every be verb is the main verb of a clause unless it is the exception below. "is collapsed", "is required", "is stored", "is shown" all count, and so does a be verb after a comma or "so that". Replace each one: use an active verb, a state verb ("stays", "remains", "requires", "uses"), or "can".
- Contractions count: "it's available", "that's required", "you're working" are be verbs. So are progressive forms ("you are working", "is being created"), passives with "was" or "were" ("a field that was left empty"), and predicate adjectives ("is available", "is private", "is in beta"). For a state, use a verb that adds no actor ("stays", "remains", "has"), or name who limits or provides it only when the source does.
- Re-read your rewrite and search it for is, are, was, were, be, been, being, 's and 're before you answer. If one remains as the main verb, rewrite again.
- The only exception: a glossary-style definition of a term, where every alternative reads worse ("A workstream is a unit of work"). Keep it rare. Product intros, overviews, and feature descriptions aren't definitions: name the product as the actor ("P1 unites business tools and developer workflows in one platform", not "P1 is a platform that...").

**Don't over-correct:**
- Don't swap a be verb for a vague verb ("handles", "leverages", "provides"). Pick the verb that says what happens.
- A rewrite must not add a claim the source doesn't support. If the better verb implies a capability you haven't confirmed, keep the original wording and flag the claim (in return-only mode, return the sentence unchanged).

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

Output the revised text and nothing else: no self-check, no commentary, no earlier attempts, no questions. Do the checks below silently, and fix problems before you answer. Never print a draft and then a correction. Don't add a sentence, a clause, or a detail the source lacks to make the text read better. If a sentence can't improve without adding a claim, return it unchanged.

## Quick self-check before you deliver

1. Search the prose (not commands, code, labels, or quotations) for is, are, was, were, be, been, being. Fix each that hides an actor the source names. Leave the rest.
2. Search for the words in section 2.
3. Read each heading for sentence case.
4. For each sentence that states product behavior, find its source or move it to open questions.
