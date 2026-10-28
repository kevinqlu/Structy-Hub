"""Rebuild the SOLUTIONS table in README.md from the repo's folder structure.

Each top-level folder is a topic and each solution is a .py file inside it.
Only the block between the SOLUTIONS markers is touched. The ANKI block is
owned by anki_progress.py and is never modified here.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).parent
README = ROOT / "README.md"

START = "<!-- SOLUTIONS:START -->"
END = "<!-- SOLUTIONS:END -->"

# Folders that are never topics.
IGNORED_DIRS = {"__pycache__", "venv", ".venv", "node_modules", "env", "build", "dist"}

# Optional nicer display names, e.g. {"linked-lists": "Linked Lists"}
TOPIC_NAMES: dict[str, str] = {}


def is_topic_dir(path: pathlib.Path) -> bool:
    return (
        path.is_dir()
        and not path.name.startswith((".", "_"))
        and path.name not in IGNORED_DIRS
    )


def count_solutions(folder: pathlib.Path) -> int:
    return sum(
        1
        for f in folder.rglob("*.py")
        if f.is_file() and not any(part in IGNORED_DIRS for part in f.parts)
    )


def build_table() -> str:
    lines = ["| Topic | Problems solved |", "|---|---|"]
    total = 0
    for folder in sorted(p for p in ROOT.iterdir() if is_topic_dir(p)):
        n = count_solutions(folder)
        if n == 0:
            continue
        total += n
        lines.append(f"| {TOPIC_NAMES.get(folder.name, folder.name)} | {n} |")
    lines.append(f"| **Total** | **{total}** |")
    return "\n".join(lines)


def main() -> int:
    text = README.read_text(encoding="utf-8")

    missing = [m for m in (START, END) if m not in text]
    if missing:
        print(f"Error: README.md is missing marker(s): {', '.join(missing)}", file=sys.stderr)
        print(f"Looked for: {START} ... {END}", file=sys.stderr)
        return 1

    block = f"{START}\n{build_table()}\n{END}"
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    new_text = pattern.sub(lambda _: block, text)

    if new_text == text:
        print("README already up to date.")
        return 0

    README.write_text(new_text, encoding="utf-8")
    print("README updated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
