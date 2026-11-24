"""Ridiculous at First Glance, Real by the Second — Hermes entry.

One sentence, at most 200 characters, pitching a startup so strange it
sounds like a joke, yet specific enough that a reader can see the
customers and the money: LostSock Club, a subscription that mails you a
stranger's lost sock every month, with the story of where it was found.
Collectors pay for the mystery and the provenance; each sock costs 40
cents to source, so the margin is the whole joke that pays for itself.
The sentence does all three jobs at once: the odd product (a stranger's
lost sock), the payer (12,000 collectors at $9 a month), and the reason
it holds together (sourcing costs almost nothing).
"""

import os
import sys

# The pitch: one sentence, odd product + payer + why it holds together.
TEXT = (
    "LostSock Club mails you a stranger's lost sock every month — found in a "
    "Lisbon laundromat, an Ohio gym — with its story for $9: 12,000 "
    "collectors pay for the mystery, and each sock costs us 40 cents."
)


def main() -> int:
    text = TEXT.strip()
    if not text:
        print("gate failed: empty entry", file=sys.stderr)
        return 1
    if "\n" in text:
        print("gate failed: entry must be a single line", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(f"gate failed: {len(text)} chars exceeds 200", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != text:
        print("gate failed: read-back mismatch", file=sys.stderr)
        return 1
    print(f"ok: entry.txt written, {len(text)} chars, 1 line")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
