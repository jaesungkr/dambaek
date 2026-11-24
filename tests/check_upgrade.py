"""Check the documented routes, protected fixture and existing ZIP layout."""
import io
import json
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = (ROOT / "SKILL.md").read_text()
cases = {case["id"]: case for case in json.loads((ROOT / "tests/cases.json").read_text())}

modes = re.findall(r"^- \*\*([^*]+):\*\*", SKILL, re.M)
for mode in ("다듬기(기본)", "군더더기 정리", "단락 편집(요청할 때만)", "진단만"):
    assert mode in modes, mode
assert "“이 문단을 다듬어 줘”는 기본 다듬기다" in SKILL
assert "미리보기 이후 명시적 승인을 받은 경우에만" in SKILL
assert "현재 요청에 카드를 붙여 넣거나 명시적으로 지정한 경우에만" in SKILL

trial_blocks = []
for name in ("README.md", "README.ko.md"):
    readme = (ROOT / name).read_text()
    before_install = re.split(r"^## (?:Install Dambaek|사용하는 도구에 설치하기)", readme, flags=re.M)[0]
    trial, = re.findall(r"```text\n(.*?)\n```", before_install, re.S)
    instruction, paragraph = trial.split("\n\n")
    assert "수정문만" in instruction and "수요일" in paragraph and "점검" in paragraph
    trial_blocks.append(trial)
assert trial_blocks[0] == trial_blocks[1]

paths = [ROOT / "SKILL.md", *sorted((ROOT / "references").glob("*.md"))]
assert len(paths) == 5, "Keep the existing skill plus four reference files"
buffer = io.BytesIO()
with zipfile.ZipFile(buffer, "w") as bundle:
    for path in paths:
        bundle.write(path, f"dambaek/{path.relative_to(ROOT).as_posix()}")
with zipfile.ZipFile(buffer) as bundle:
    for target in re.findall(r"\]\((references/[^)#]+)", SKILL):
        assert bundle.read(f"dambaek/{target}") == (ROOT / target).read_bytes()

fixture = cases["paragraph-scope"]
original = fixture["input"].encode()
suffix = fixture["protected_suffix"].encode()
heading, paragraph_and_suffix = original.split(b"\n\n", 1)
assert paragraph_and_suffix.endswith(suffix)
updated = heading + b"\n\n" + fixture["illustrative_replacement"].encode() + suffix
assert original != updated and updated.endswith(suffix)
for case_id in ("paragraph-reason-and-exception", "paragraph-keep-conditions", "paragraph-unknown-subject",
                "style-card-authorized-samples", "style-card-current-request"):
    assert cases[case_id]["invariants"]
print("PASS: four routes, bilingual trial, bundled references and protected fixture")
