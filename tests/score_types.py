#!/usr/bin/env python3
"""Score the Diataxis type fixtures.

  python3 tests/score_types.py classify answers.json
      answers.json maps a fixture id to the model's one-word answer:
      tutorial, how-to, reference, explanation, or mixed.
  python3 tests/score_types.py draft answers.json
      answers.json maps "tutorial", "how-to", "reference", "explanation" to a drafted page.
      Checks structural markers for each type.
"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))

def classify(ans):
    fx = json.load(open(os.path.join(HERE, "type-fixtures.json")))
    ok = 0
    for f in fx:
        got = re.sub(r"[^a-z-]", "", ans.get(f["id"], "").lower().split()[0] if ans.get(f["id"]) else "")
        got = {"howto": "how-to", "how-to-guide": "how-to"}.get(got, got)
        good = got == f["expected"]; ok += good
        print(("PASS" if good else "FAIL"), f["id"], "expected", f["expected"], "got", got)
    print(f"classify {ok}/{len(fx)}")

CHECKS = {
 "tutorial": [("opens with what reader builds", lambda t: re.search(r"in this tutorial,? you (build|create|deploy|make)", t, re.I)),
              ("no 'you will learn'", lambda t: not re.search(r"you will learn|you'll learn", t, re.I)),
              ("no fork words", lambda t: not re.search(r"you could also|alternatively|or you can", t, re.I)),
              ("has numbered steps", lambda t: re.search(r"^\s*1\. ", t, re.M)),
              ("states expected result", lambda t: re.search(r"you (see|should see)|shows|notice", t, re.I))],
 "how-to": [("has Before you begin", lambda t: re.search(r"^## Before you begin", t, re.M)),
            ("has numbered steps", lambda t: re.search(r"^\s*1\. ", t, re.M)),
            ("names starting place in step 1", lambda t: re.search(r"1\. .*(dashboard|tab|terminal|open)", t, re.I)),
            ("has a verify step", lambda t: re.search(r"^## (Verify|Confirm|Check)", t, re.M | re.I)),
            ("no 'why' section", lambda t: not re.search(r"^## (Why|Background|How it works)", t, re.M | re.I))],
 "reference": [("has a table", lambda t: re.search(r"^\|.*\|\s*$", t, re.M)),
               ("no numbered procedure", lambda t: not re.search(r"^\s*1\. ", t, re.M)),
               ("no 'you should'", lambda t: not re.search(r"you should|you can|you must", t, re.I))],
 "explanation": [("no numbered procedure", lambda t: not re.search(r"^\s*1\. ", t, re.M)),
                 ("has trade-offs", lambda t: re.search(r"trade-?off|alternative|cost", t, re.I)),
                 ("no option table", lambda t: not re.search(r"^\|.*\|\s*$", t, re.M))],
}

def draft(ans):
    tot = ok = 0
    for k, checks in CHECKS.items():
        t = ans.get(k, "")
        for name, fn in checks:
            good = bool(fn(t)); tot += 1; ok += good
            print(("PASS" if good else "FAIL"), k, "-", name)
    print(f"draft {ok}/{tot}")

if __name__ == "__main__":
    mode, path = sys.argv[1], sys.argv[2]
    {"classify": classify, "draft": draft}[mode](json.load(open(path)))
