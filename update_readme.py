"""Rebuild the SOLUTIONS table in README.md.

Counts come from two places:
  - "In repo": .py solution files inside each top-level topic folder.
  - "Before repo": the BASELINE dict below, for problems solved on Structy
    before this repo existed (not in git history).

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

IGNORED_DIRS = {"__pycache__", "venv", ".venv", "node_modules", "env", "build", "dist"}

# Optional display names, keyed by folder name, e.g. {"Binary-Tree-I": "BinaryTree"}
TOPIC_NAMES: dict[str, str] = {
    "Beginner-Recursion": "Recursion",
    "Big-O-Notation": "BigO",
    "Binary-Tree-I": "BinaryTree",
    "Linked-List-I": "LinkedList",
}

# Problems solved before this repo existed, keyed by the SAME name used in the
# table (folder name, or its TOPIC_NAMES display name). Fill in from Structy.
# If you later backfill real files for a topic, lower or delete its entry so
# nothing is counted twice.
BASELINE: dict[str, int] = {
    # Coding problems per Structy module (laptop-icon items) minus the files
    # already in the repo. Update when you add real files for a topic.
    "Introduction": 4,   # 5 coding - 1 in repo
    "BigO": 1,           # 2 coding - 1 in repo
    "Hashing": 8,        # 8 coding - 0 in repo
    "Recursion": 5,      # 6 coding - 1 in repo
    "LinkedList": 8,     # 11 coding - 3 in repo
    "BinaryTree": 9,     # 14 coding - 5 in repo
}


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
    in_repo: dict[str, int] = {}
    for folder in sorted(p for p in ROOT.iterdir() if is_topic_dir(p)):
        n = count_solutions(folder)
        if n:
            in_repo[TOPIC_NAMES.get(folder.name, folder.name)] = n

    topics = sorted(set(in_repo) | {k for k, v in BASELINE.items() if v})

    lines = ["| Topic | In repo | Before repo | Total |", "|---|---|---|---|"]
    sum_repo = sum_base = 0
    for t in topics:
        r, b = in_repo.get(t, 0), BASELINE.get(t, 0)
        sum_repo += r
        sum_base += b
        lines.append(f"| {t} | {r} | {b} | {r + b} |")
    lines.append(f"| **Total** | **{sum_repo}** | **{sum_base}** | **{sum_repo + sum_base}** |")
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
