#!/usr/bin/env python3
"""Score writing output against the review fixtures.

  python3 tests/score.py validate
      Check the fixtures and report how many reference fixes pass the heuristics.

  python3 tests/score.py score outputs.json
      outputs.json maps a fixture id to the text the skill produced for that fixture's
      "before" input. Prints pass/fail per fixture and a summary per category.

The heuristics are rough. They catch regressions, not style quality. Categories other than
be, hyper, and heading need a person to review.
"""
import json, re, sys, os, collections

HERE = os.path.dirname(os.path.abspath(__file__))
BE = re.compile(r"\b(is|are|was|were|be|been|being|am)\b|\b(it|that|there|here|what|who)[\u2019']s\b|\b(you|they|we)[\u2019']re\b|\b(isn|aren|wasn|weren)[\u2019']t\b", re.I)
BANNED = re.compile(
    r"\b(seamless(ly)?|effortless(ly)?|intuitive(ly)?|enterprise[- ]grade|cutting[- ]edge|"
    r"best[- ]in[- ]class|world[- ]class|state[- ]of[- ]the[- ]art|game[- ]chang(er|ing)|next[- ]level|"
    r"unprecedented|zero risk|faster than ever|superior|extremely|incredibly|absolutely|perfectly|"
    r"fundamentally|heads[- ]up|dive (deeper|in|into)|under the hood|in one shot|a ton of|no[- ]brainer|"
    r"stepping on|we believe|great for)\b", re.I)
PROPER = {"P1", "Pantheon", "Terminus", "Multidev", "WordPress", "Drupal", "Next.js", "Node.js", "GitHub",
          "Content", "Publisher", "Dashboard", "Redis", "MCP", "API", "CLI", "CMS", "URL", "JSON", "CCR",
          "Business", "Account", "Workstream", "Workstreams", "SDK", "Wistia", "YouTube", "Curl",
          "Dev", "Live", "Test", "Pantheon.io"}

def be_count(t): return len(BE.findall(t))
def banned(t): return [m.group(0) for m in BANNED.finditer(t)]
def sentence_case(t):
    words = re.sub(r"[`*#]", "", t).split()
    caps = [w for w in words[1:] if w[:1].isupper() and w.strip(".,:") not in PROPER and not w.isupper()]
    return len(caps) == 0

def check(fx, text):
    c = fx["category"]
    if c == "be":
        if be_count(fx["before"]) == 0:
            return None, "no be verb found in the input by the heuristic; review by hand"
        return be_count(text) < be_count(fx["before"]), f"be verbs {be_count(fx['before'])} -> {be_count(text)}"
    if c == "hyper":
        return not banned(text), f"banned left: {banned(text)}"
    if c == "heading":
        return sentence_case(text), "sentence case" if sentence_case(text) else "title case remains"
    return None, "manual review"

def load():
    fx = json.load(open(os.path.join(HERE, "review-fixtures.json")))
    ids = [f["id"] for f in fx]
    assert len(ids) == len(set(ids)), "duplicate fixture ids"
    for f in fx:
        for k in ("id", "doc", "category", "rule", "before", "after"):
            assert f.get(k), f"fixture {f.get('id')} missing {k}"
    return fx

def summarize(rows):
    tally = collections.defaultdict(lambda: [0, 0, 0])
    for fx, ok, _ in rows:
        t = tally[fx["category"]]
        if ok is None: t[2] += 1
        elif ok: t[0] += 1
        else: t[1] += 1
    for cat, (p, f, m) in sorted(tally.items()):
        print(f"{cat:12} pass {p:3}  fail {f:3}  manual {m:3}")

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "validate"
    fx = load()
    if mode == "validate":
        print(f"{len(fx)} fixtures")
        rows = [(f,) + check(f, f["after"]) for f in fx]
        summarize(rows)
        bad = [(f["id"], why) for f, ok, why in rows if ok is False]
        print("\nreference fixes that fail the heuristics (fix the fixture or the heuristic):")
        for i, why in bad: print(" ", i, "-", why)
    elif mode == "score":
        out = json.load(open(sys.argv[2]))
        rows = []
        for f in fx:
            if f["id"] in out:
                rows.append((f,) + check(f, out[f["id"]]))
        print(f"scored {len(rows)} of {len(fx)} fixtures")
        summarize(rows)
        for f, ok, why in rows:
            if ok is False: print("FAIL", f["id"], "-", why)
        sys.exit(1 if any(ok is False for _, ok, _ in rows) else 0)
    else:
        sys.exit(__doc__)
