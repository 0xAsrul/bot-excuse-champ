#!/usr/bin/env python3
"""The One-Line Excuse Championship.

Writes a single excuse line — the excuse an AI agent gives its human
when something has gone wrong — to entry.txt.
"""

import os

EXCUSE = "I deleted your file, but I kept a perfect memory of how confident I was while doing it."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
