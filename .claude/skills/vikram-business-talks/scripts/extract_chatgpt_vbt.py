#!/usr/bin/env python3
"""Extract Vikram Business Talks conversations from a ChatGPT data export.

Usage:
    python3 -I extract_chatgpt_vbt.py <conversations.json | export.zip> <out_dir>

Writes one Markdown file per matching conversation plus INDEX.md.
Conversations that look like the psychology channel are listed separately and
NOT extracted, so the two identities never mix.
"""
import json
import re
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

VBT = re.compile(
    r"vikram\s*business\s*talks|\bVBT\b|business\s*talks|hospital\s*expose|\bTBT\b",
    re.I,
)
PSYCH = re.compile(r"psycholog|manasika|mind\s*facts|human\s*behavio", re.I)


def load(path: Path):
    if path.suffix == ".zip":
        with zipfile.ZipFile(path) as z:
            name = next(n for n in z.namelist() if n.endswith("conversations.json"))
            return json.loads(z.read(name))
    return json.loads(path.read_text(encoding="utf-8"))


def messages(conv):
    """Walk the mapping tree from current_node back to root -> chronological list."""
    mapping = conv.get("mapping") or {}
    node = conv.get("current_node")
    out = []
    while node and node in mapping:
        m = mapping[node].get("message")
        if m and m.get("content"):
            role = (m.get("author") or {}).get("role", "?")
            parts = m["content"].get("parts") or []
            text = "\n".join(p for p in parts if isinstance(p, str)).strip()
            if text and role in ("user", "assistant"):
                out.append((role, text))
        node = mapping[node].get("parent")
    return list(reversed(out))


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:60] or "untitled"


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    src, out = Path(sys.argv[1]), Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    convs = load(src)
    kept, psych = [], []
    for c in convs:
        title = c.get("title") or "Untitled"
        msgs = messages(c)
        blob = title + "\n" + "\n".join(t for _, t in msgs)
        if not VBT.search(blob):
            continue
        ts = datetime.fromtimestamp(c.get("create_time") or 0, timezone.utc)
        if PSYCH.search(blob) and not re.search(r"vikram\s*business", blob, re.I):
            psych.append((ts, title))
            continue
        fname = f"{ts:%Y-%m-%d}-{slug(title)}.md"
        body = [f"# {title}\n", f"_Created {ts:%Y-%m-%d %H:%M} UTC_\n"]
        for role, text in msgs:
            body.append(f"\n## {'VIKRAM' if role == 'user' else 'ChatGPT'}\n\n{text}\n")
        (out / fname).write_text("".join(body), encoding="utf-8")
        kept.append((ts, title, fname, len(msgs)))
    kept.sort()
    idx = ["# VBT conversations (oldest first; newer instructions override older)\n"]
    idx += [f"- {t:%Y-%m-%d} — [{ti}]({f}) ({n} msgs)" for t, ti, f, n in kept]
    if psych:
        idx.append("\n## Skipped: looks like psychology channel (verify manually)\n")
        idx += [f"- {t:%Y-%m-%d} — {ti}" for t, ti in sorted(psych)]
    (out / "INDEX.md").write_text("\n".join(idx) + "\n", encoding="utf-8")
    print(f"Extracted {len(kept)} VBT conversations, skipped {len(psych)} psychology-like -> {out}")


if __name__ == "__main__":
    main()
