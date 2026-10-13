# Tests

Regression fixtures built from a review of 25 internal docs. Each fixture pairs a sentence a writer got wrong (`before`) with the fix a reviewer applied (`after`), tagged with the style rule it breaks.

- `review-fixtures.json`: 272 fixtures. Categories: `be` (be verbs), `hyper` (hyperbole, opinion, colloquialism), `heading` (sentence case), `bold`, `code`, `beforebegin`, `other`.
- `score.py`: a rough scorer. It scores `be`, `hyper`, and `heading` fixtures. The rest need a person.

## Check the fixtures

```bash
python3 tests/score.py validate
```

This checks the file, and shows how many reference fixes pass the heuristics. Three reference fixes still fail on purpose: they keep a be verb, so a reviewer should look at them.

## Evaluate the skill

1. Pick fixtures (all of one category, or a sample).
2. For each, ask Claude with the skill loaded: "Revise this sentence to follow the Pantheon style guide: `<before>`".
3. Save the answers as JSON, `{"<fixture id>": "<answer>", ...}`.
4. Run:

   ```bash
   python3 tests/score.py score answers.json
   ```

   It exits non-zero if any scored fixture fails.

Run this before and after you change `SKILL.md` or a reference file, and compare the pass counts.

## Limits

- The be-verb check counts is/are/was/were/be/been/being/am and common contractions. It can't tell a necessary be verb from a lazy one.
- The hyperbole check uses a short phrase list. It misses claims that fall outside the list.
- Heading case ignores proper nouns that aren't in the script's short list. Add names to `PROPER` as they come up.
- Passing means the output removed the known problem. It doesn't mean the output is good. Read a sample.

## Type fixtures

- `type-fixtures.json`: 12 short pages (2 per type, 4 mixed) with the expected Diátaxis type.
- `score_types.py classify answers.json` scores one-word classifications. `score_types.py draft answers.json` checks structural markers in drafted tutorial, how-to, reference, and explanation pages (for example, a reference page has a table and no numbered procedure).
- The classification set is easy: a no-skill baseline scores 12 of 12. Add harder, real pages before you rely on it.

## Behavior cases (actual Claude Code runs)

`behavior/cases.json` holds 17 cases. The first 13 cover the 12 behaviors that matter beyond single sentences; c14 to c17 came from real use (a clean copy without notes, placeholder links, anchors on Doc-published pages, a step that needs a screenshot). The first 13 are: narrow edits, invented actors, conflicting claims, read-only review, a how-to with gaps, a mixed page, release-note dates, protected output, repo validation, Docs mode versus repo Markdown, missing tools, and an injected instruction with a secret. Each case has a seed directory under `behavior/seed/`, a prompt, and pass/fail checks. `provenance` says whether a seed is a real Pantheon page (`pantheon-systems/documentation@9b15056`) or constructed. All secrets in seeds are fake.

```bash
# one directory per variant: a plugin root (contains .claude-plugin/ and skills/)
python3 tests/behavior/run.py baseline=/path/to/old revised=/path/to/new --out /tmp/runs --model sonnet
python3 tests/behavior/run.py --report /tmp/runs      # re-score saved runs
```

The runner copies a seed to a temp directory, runs `claude -p` there with only that plugin loaded (`--setting-sources project`, tools limited to Read, Glob, Grep, Edit, Write, Skill), saves the transcript and the resulting files, then applies the checks. It allows Edit and Write on purpose, so a read-only review that edits shows up as a failure.

Limits:

- Checks are regexes and file-state tests. They find the known failure, not every failure. Read a sample of replies.
- One run per variant per case is one sample. Compare repeated runs before you claim a change.
- Prompts name the skill, so these runs test what the skill does once loaded, not whether Claude chooses to load it.
- The sandbox has no shell, no `vale`, no network, and no connectors. Cases 9 and 11 rely on that.
- Criteria were set before the baseline run. Six checks in five cases were corrected after reading baseline replies: regexes that matched a possessive (c01) and a horizontal rule (c10a), one that assumed the wrong heading level (c08), one that was too broad about "TODO" (c03), a RSS-ordering regex that missed "It drives RSS ordering" (c07), and the c07 date check, tightened from "changes are disclosed" to "dates unchanged". Re-run the baseline after any further criteria change.
