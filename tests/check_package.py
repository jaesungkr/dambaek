"""Check package entry points and the generated Claude Chat ZIP."""
import json
from pathlib import Path
import re
import subprocess
import sys
from tempfile import TemporaryDirectory
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
REFERENCES = {
    "references/blog-editing.md",
    "references/everyday-writing.md",
    "references/examples.md",
    "references/patterns.md",
}


def manifest(path: str) -> dict:
    value = json.loads((ROOT / path).read_text(encoding="utf-8"))
    assert value["name"] == "dambaek", path
    return value


def check_entry_points() -> None:
    assert list(ROOT.rglob("SKILL.md")) == [SKILL], "Keep a single skill source"
    for ref in REFERENCES:
        assert (ROOT / ref).is_file(), f"Missing reference: {ref}"
        assert f"]({ref})" in SKILL.read_text(encoding="utf-8"), f"Unlinked reference: {ref}"

    pi = manifest("package.json")
    assert pi["pi"] == {"skills": ["./"]}
    assert pi["private"] and "pi-package" in pi["keywords"]
    assert not ({"scripts", "dependencies", "devDependencies"} & pi.keys())
    assert manifest(".claude-plugin/plugin.json")["skills"] == ["./"]
    assert manifest(".cursor-plugin/plugin.json")["skills"] == ["./SKILL.md"]
    for host in ("claude", "cursor"):
        entries = manifest(f".{host}-plugin/marketplace.json")["plugins"]
        assert len(entries) == 1
        assert entries[0]["name"] == "dambaek"
        assert (ROOT / entries[0]["source"]).resolve() == ROOT
        assert (ROOT / entries[0]["source"] / f".{host}-plugin/plugin.json").is_file()

    codex = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
    match = re.fullmatch(
        r'interface:\n  display_name: "([^"\n]+)"\n'
        r'  short_description: "([^"\n]{25,64})"\n'
        r'  default_prompt: "([^"\n]+)"\n',
        codex,
    )
    assert match and re.search(r"\$dambaek(?![\w-])", match[3]), "Invalid Codex interface"


def check_chat_zip() -> None:
    with TemporaryDirectory() as directory:
        output = Path(directory) / "dambaek-chat.zip"
        subprocess.run([sys.executable, str(ROOT / "scripts/build_chat_zip.py"), str(output)], check=True)
        with ZipFile(output) as archive:
            sources = {"SKILL.md", *REFERENCES}
            assert sorted(archive.namelist()) == sorted(f"dambaek/{name}" for name in sources)
            for name in sources:
                assert archive.read(f"dambaek/{name}") == (ROOT / name).read_bytes(), name


if __name__ == "__main__":
    check_entry_points()
    check_chat_zip()
    print("PASS: single skill source, plugin manifests, Codex and pi metadata, Claude Chat ZIP")
