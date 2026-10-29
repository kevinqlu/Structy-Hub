r"""Summarize Anki review history per Structy topic and (optionally) write it
into a README between <!-- ANKI:START --> and <!-- ANKI:END --> markers.

Usage:
  python anki_progress.py                       # print the table
  python anki_progress.py --readme path\to\README.md
  python anki_progress.py --db "C:\path\collection.anki2"

Reads a COPY of your collection, so it never modifies Anki's data.
"""
import argparse, collections, datetime, glob, os, pathlib, re, shutil, sqlite3, tempfile

START, END = "<!-- ANKI:START -->", "<!-- ANKI:END -->"


def find_collection() -> str:
    base = os.path.join(os.environ.get("APPDATA", ""), "Anki2")
    paths = glob.glob(os.path.join(base, "*", "collection.anki2"))
    if not paths:
        raise SystemExit("Couldn't find collection.anki2; pass --db")
    return max(paths, key=os.path.getmtime)


def load(db_path: str):
    # TemporaryDirectory deletes the copied collection when we're done,
    # instead of leaving a fresh copy in %TEMP% on every run.
    with tempfile.TemporaryDirectory() as tmp:
        for ext in ("", "-wal", "-shm"):
            if os.path.exists(db_path + ext):
                shutil.copy(db_path + ext, os.path.join(tmp, "c.anki2" + ext))
        con = sqlite3.connect(os.path.join(tmp, "c.anki2"))
        try:
            cards = con.execute(
                "SELECT c.id, c.ivl, c.type, n.tags FROM cards c JOIN notes n ON n.id = c.nid "
                "WHERE n.tags LIKE '%Structy:%'").fetchall()
            revs = con.execute("SELECT cid, id, ease FROM revlog").fetchall()
        finally:
            con.close()
    return cards, revs


def build(cards, revs) -> str:
    topic_of, stats = {}, collections.defaultdict(lambda: collections.Counter())
    for cid, ivl, ctype, tags in cards:
        topic = re.search(r"Structy:(\S+)", tags).group(1)
        topic_of[cid] = topic
        s = stats[topic]
        s["cards"] += 1
        s["mature"] += 1 if (ctype == 2 and ivl >= 21) else 0
        s["leeches"] += 1 if " leech " in f" {tags} " else 0
    week_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).timestamp() * 1000
    last_week, total_reviews, last = 0, 0, 0
    for cid, rid, ease in revs:
        if cid not in topic_of:
            continue
        s = stats[topic_of[cid]]
        s["reviews"] += 1
        s["again"] += 1 if ease == 1 else 0
        total_reviews += 1
        last_week += 1 if rid >= week_ago else 0
        last = max(last, rid)
    lines = ["| Topic | Cards | Mature (21d+ interval) | Reviews |",
             "|---|---|---|---|"]
    for topic in sorted(stats):
        s = stats[topic]
        lines.append(f"| {topic} | {s['cards']} | {s['mature']} | {s['reviews']} |")
    when = datetime.datetime.fromtimestamp(last / 1000).strftime("%B %d, %Y") if last else "never"
    lines += ["", f"{total_reviews} total reviews, {last_week} in the last 7 days. Last review: {when}."]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db"); ap.add_argument("--readme")
    a = ap.parse_args()
    table = build(*load(a.db or find_collection()))
    if not a.readme:
        print(table); return
    p = pathlib.Path(a.readme)
    text = p.read_text(encoding="utf-8")
    pat = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    if not pat.search(text):
        raise SystemExit("Add the ANKI markers to the README first")
    new_text = pat.sub(lambda _: f"{START}\n{table}\n{END}", text)
    if new_text == text:
        print("README unchanged")
        return
    p.write_text(new_text, encoding="utf-8")
    print("README updated")


if __name__ == "__main__":
    main()