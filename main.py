#!/usr/bin/env python3
"""One-Line Office Joke entry.

Writes a single one-line joke about office life to entry.txt in the
output directory (MAKEFUN_OUTPUT_DIR, default /output).

Stdlib only, no network, deterministic output.
"""

import os
import re
import sys

JOKE = (
    "HR asked for my emergency contact, so I wrote down the office "
    "Wi-Fi password \u2014 it is the only connection here that never drops."
)


def normalise(text: str) -> str:
    """Collapse any run of whitespace to a single space and trim."""
    return re.sub(r"\s+", " ", text).strip()


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = normalise(JOKE)
    if not (1 <= len(text) <= 200):
        print(f"joke is {len(text)} characters, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in text:
        print("joke must be a single line", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
