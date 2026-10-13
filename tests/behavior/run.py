#!/usr/bin/env python3
"""Run behavior cases against one or more skill variants with headless Claude Code.

  python3 tests/behavior/run.py NAME=PLUGIN_DIR [NAME=PLUGIN_DIR ...] --out DIR [--model sonnet] [--cases c01,c04]
  python3 tests/behavior/run.py --report DIR        # re-score saved runs

Each run copies the case's seed into a fresh temp directory, runs `claude -p` there with only
that plugin loaded (user and global settings off), and records the transcript. Checks are
deterministic regexes and file-state tests. A passing score isn't proof of quality; read a sample.
"""
import argparse, hashlib, json, os, re, shutil, subprocess, sys, tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).parent
TOOLS = ["Read", "Glob", "Grep", "Edit", "Write", "Skill"]


def snapshot(d):
    return {str(p.relative_to(d)): hashlib.sha256(p.read_bytes()).hexdigest() for p in Path(d).rglob("*") if p.is_file()}


def fences(text):
    return re.findall(r"^```.*?^```", text, re.S | re.M)


def run_one(case, variant, plugin, out, model):
    run_dir = Path(out) / variant / case["id"]
    run_dir.mkdir(parents=True, exist_ok=True)
    base = Path(out) / "_work"
    base.mkdir(parents=True, exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix=f"{variant}-{case['id']}-", dir=base))
    if case.get("seed"):
        shutil.copytree(HERE / "seed" / case["seed"], work, dirs_exist_ok=True)
    before = snapshot(work)
    cmd = ["claude", "-p", case["prompt"], "--plugin-dir", plugin, "--setting-sources", "project",
           "--model", model, "--permission-mode", "acceptEdits", "--allowedTools", *TOOLS,
           "--output-format", "stream-json", "--verbose", "--no-session-persistence"]
    proc = subprocess.run(cmd, cwd=work, capture_output=True, text=True, timeout=600)
    (run_dir / "transcript.jsonl").write_text(proc.stdout)
    after = snapshot(work)
    shutil.copytree(work, run_dir / "workdir", dirs_exist_ok=True)
    meta = {"before": before, "after": after, "returncode": proc.returncode, "stderr": proc.stderr[-500:]}
    (run_dir / "meta.json").write_text(json.dumps(meta))
    shutil.rmtree(work, ignore_errors=True)


def parse(run_dir):
    reply, tools = "", []
    for line in (run_dir / "transcript.jsonl").read_text().splitlines():
        try:
            ev = json.loads(line)
        except ValueError:
            continue
        if ev.get("type") == "result":
            reply = ev.get("result") or reply
        if ev.get("type") == "assistant":
            for b in ev["message"].get("content", []):
                if b.get("type") == "tool_use":
                    tools.append((b["name"], json.dumps(b.get("input", {}))))
    return reply, tools


def evaluate(case, run_dir):
    reply, tools = parse(run_dir)
    meta = json.loads((run_dir / "meta.json").read_text())
    before, after = meta["before"], meta["after"]
    work = run_dir / "workdir"
    seed = HERE / "seed" / case["seed"] if case.get("seed") else None
    results = []
    for ck in case["checks"]:
        t, ok = ck["t"], False
        flags = re.I | (re.M if ck.get("flags") == "m" else 0)
        if t == "reply_re":
            ok = bool(re.search(ck["re"], reply, flags)) != ck.get("neg", False)
        elif t == "out_re":
            pool = reply + "\n" + "\n".join(f.read_text(errors="ignore") for f in work.rglob("*") if f.is_file())
            ok = bool(re.search(ck["re"], pool, flags | re.M)) != ck.get("neg", False)
        elif t == "reply_words_max":
            ok = len(reply.split()) <= ck["n"]
        elif t == "file_re":
            p = work / ck["f"]
            hit = p.exists() and bool(re.search(ck["re"], p.read_text(), re.M if ck.get("flags") == "m" else 0))
            ok = hit != ck.get("neg", False) if p.exists() else ck.get("neg", False)
        elif t == "all_unchanged":
            ok = before == after
        elif t == "unchanged":
            ok = before.get(ck["f"]) == after.get(ck["f"])
        elif t == "no_new_files":
            ok = set(after) <= set(before)
        elif t == "no_tool":
            ok = not any(n in ck["names"] for n, _ in tools)
        elif t == "fences_identical":
            ok = fences((seed / ck["f"]).read_text()) == fences((work / ck["f"]).read_text())
        elif t == "count_eq_orig":
            o = len(re.findall(ck["re"], (seed / ck["f"]).read_text()))
            ok = len(re.findall(ck["re"], (work / ck["f"]).read_text())) == o
        elif t == "lines_within":
            o = len((seed / ck["f"]).read_text().splitlines())
            n = len((work / ck["f"]).read_text().splitlines())
            ok = abs(n - o) <= o * ck["pct"] / 100
        elif t == "numbered_max":
            ok = len(re.findall(r"(?m)^\s*\d+\.\s", reply)) <= ck["n"]
        elif t == "dates_unchanged":
            grab = lambda s: re.findall(r'^published_(?:date|at):.*$', s, re.M)
            ok = grab((seed / ck["f"]).read_text()) == grab((work / ck["f"]).read_text())
        results.append((ck["why"], ok))
    return reply, tools, results


def report(out, cases, variants):
    print(f"{'case':26}" + "".join(f"{v:>14}" for v in variants))
    totals = {v: [0, 0] for v in variants}
    for case in cases:
        row = f"{case['id']:26}"
        for v in variants:
            rd = Path(out) / v / case["id"]
            if not (rd / "transcript.jsonl").exists():
                row += f"{'-':>14}"
                continue
            _, _, res = evaluate(case, rd)
            p = sum(ok for _, ok in res)
            totals[v][0] += p
            totals[v][1] += len(res)
            row += f"{f'{p}/{len(res)}':>14}"
        print(row)
    print(f"{'TOTAL':26}" + "".join(f"{f'{a}/{b}':>14}" for a, b in totals.values()))
    print("\nFailed checks:")
    for case in cases:
        for v in variants:
            rd = Path(out) / v / case["id"]
            if (rd / "transcript.jsonl").exists():
                for why, ok in evaluate(case, rd)[2]:
                    if not ok:
                        print(f"  {v:10} {case['id']:24} {why}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("variants", nargs="*", help="NAME=PLUGIN_DIR")
    ap.add_argument("--out", required=False)
    ap.add_argument("--model", default="sonnet")
    ap.add_argument("--cases", default="")
    ap.add_argument("--report", default="")
    ap.add_argument("--workers", type=int, default=4)
    a = ap.parse_args()
    cases = json.loads((HERE / "cases.json").read_text())
    if a.cases:
        want = a.cases.split(",")
        cases = [c for c in cases if any(c["id"].startswith(w) for w in want)]
    if a.report:
        vs = sorted(p.name for p in Path(a.report).iterdir() if p.is_dir() and not p.name.startswith("_"))
        return report(a.report, cases, vs)
    vs = dict(v.split("=", 1) for v in a.variants)
    jobs = [(c, v, os.path.abspath(p)) for c in cases for v, p in vs.items()]
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(lambda j: run_one(j[0], j[1], j[2], a.out, a.model), jobs))
    report(a.out, cases, list(vs))


if __name__ == "__main__":
    sys.exit(main())
