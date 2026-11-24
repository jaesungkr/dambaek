"""Build a Claude custom-skill ZIP from the checkout."""
import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]


def build(output: Path) -> None:
    members = [ROOT / "SKILL.md", *sorted((ROOT / "references").glob("*.md"))]
    with ZipFile(output, "x", compression=ZIP_DEFLATED) as archive:
        for member in members:
            archive.write(member, (Path("dambaek") / member.relative_to(ROOT)).as_posix())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="Path to a new ZIP file")
    build(parser.parse_args().output)
