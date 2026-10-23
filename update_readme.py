"""Rebuild the progress table in README.md from the repo's folder structure.

Assumes each top-level folder is a topic and each solution is a non-.md file
inside it. Edit TOPIC_NAMES if your folder names need nicer display names.
"""
import datetime
import pathlib
import re

ROOT = pathlib.Path(__file__).parent
README = ROOT / "README.md"
START, END = "<!-- PROGRESS:START -->", "<!-- PROGRESS:END -->"
TOPIC_NAMES = {}  # e.g. {"linked-lists": "Linked Lists"}


def count_solutions(folder: pathlib.Path) -> int:
    return sum(1 for f in folder.rglob("*") if f.is_file() and f.suffix.lower() != ".md")


def build_table() -> str:
    lines = ["| Topic | Problems solved |", "|---|---|"]
    total = 0
    for folder in sorted(p for p in ROOT.iterdir() if p.is_dir() and not p.name.startswith(".")):
        n = count_solutions(folder)
        if n == 0:
            continue
        total += n
        lines.append(f"| {TOPIC_NAMES.get(folder.name, folder.name)} | {n} |")
    lines.append(f"| **Total** | **{total}** |")
    lines.append("")
    lines.append(f"Last updated: {datetime.date.today():%B %d, %Y}")
    return "\n".join(lines)


def main() -> None:
    text = README.read_text(encoding="utf-8")
    block = f"{START}\n{build_table()}\n{END}"
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    if not pattern.search(text):
        raise SystemExit("Markers not found in README.md")
    README.write_text(pattern.sub(block, text), encoding="utf-8")


if __name__ == "__main__":
    main()
