"""Validate local package structure; not a Korean quality evaluator."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
assert skill.startswith("---\n"), "Missing frontmatter"
frontmatter = skill.split("---", 2)[1]
assert re.search(r"^name: dambaek$", frontmatter, re.M), "Wrong skill name"
assert re.search(r"^description: .+", frontmatter, re.M), "Missing description"
cases = json.loads((ROOT / "tests/cases.json").read_text(encoding="utf-8"))
assert len(cases) >= 16, "Missing cases"
assert len({case["id"] for case in cases}) == len(cases), "Duplicate case ID"
for case in cases:
    assert all(isinstance(case[key], str) and case[key].strip() for key in ("id", "request", "input"))
    assert case["invariants"] and all(isinstance(item, str) and item.strip() for item in case["invariants"])
    if "improvement_checks" in case:
        assert case["improvement_checks"] and all(isinstance(item, str) and item.strip() for item in case["improvement_checks"])
for path in ROOT.rglob("*.md"):
    text = path.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        if target.startswith(("https://", "http://", "mailto:", "#")):
            continue
        assert (path.parent / target.split("#", 1)[0]).exists(), f"Broken link: {path}: {target}"
print(f"PASS: skill metadata, {len(cases)} fixtures, local Markdown links")
