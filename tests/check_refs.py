#!/usr/bin/env python3
"""Check the skill's internal references: file paths resolve, no stale step numbers, naming is consistent.

  python3 tests/check_refs.py
"""
import re, sys
from pathlib import Path

base = Path(__file__).resolve().parent.parent / "skills" / "pantheon-docs-writer"
files = [base / "SKILL.md", *sorted((base / "references").glob("*.md"))]
errors = []
for f in files:
    text = f.read_text(encoding="utf-8")
    for m in re.finditer(r"`((?:\.\./)?(?:references/|assets/)[^`\s]+|[a-z0-9-]+\.md)`", text):
        name = m.group(1).rstrip(".,:")
        if name in ("SKILL.md", "README.md", "CLAUDE.md", "style-guide.md", "doc-template.md", "contributor.yaml"):
            continue
        cands = [f.parent / name, base / name, base / "references" / name]
        if name.endswith(".md") and "/" not in name and not any(c.exists() for c in cands):
            if re.fullmatch(r"\d{4}-\d\d-\d\d-.+\.md", name) or name in ("limits.md", "walkthrough-checklist.md", "decisions.md"):
                continue
            errors.append(f"{f.name}: missing {name}")
        elif "/" in name and not any(c.exists() for c in cands):
            errors.append(f"{f.name}: missing {name}")
    if f.parent.name == "references":
        for m in re.finditer(r"^#+ Step \d+", text, re.M):
            errors.append(f"{f.name}: stale step heading '{m.group(0)}'")
    if re.search(r"\bDitaxis\b|\bDiataxis\b", text):
        errors.append(f"{f.name}: use 'Diátaxis'")
print("\n".join(errors) or f"ok: {len(files)} files, all references resolve")
sys.exit(1 if errors else 0)
