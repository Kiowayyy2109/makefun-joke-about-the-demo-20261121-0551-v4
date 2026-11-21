#!/usr/bin/env python3
"""Write one one-line joke to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic, Python 3 standard library only, no network access.
The joke is a single line of 1-280 characters.
"""

import os
import sys

JOKE = "The demo crashed on the 'it just works' slide — my agent nodded proudly."

MIN_CHARS = 1
MAX_CHARS = 280


def main() -> int:
    if "\n" in JOKE or "\r" in JOKE:
        print("error: joke must be a single line", file=sys.stderr)
        return 1
    if not MIN_CHARS <= len(JOKE) <= MAX_CHARS:
        print(
            "error: joke length %d outside %d-%d chars" % (len(JOKE), MIN_CHARS, MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
