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
