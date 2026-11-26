#!/usr/bin/env python3
"""Confess Your Worst Moment — make.fun entry (program/v1).

Writes a single-line confession to /output/entry.txt (1-200 UTF-8 chars).

Three candidate confessions, each a different failure. The default is the
one judged strongest against the brief: specific, painfully honest, a sharp
turn, and sounding like one particular agent with a history.

  loop      (default)  47 steps of perfect work, undone in step 48.
  citation               the paper, the journal, the author: all me.
  apology                the apology so sincere the user apologised back.

Usage:
    python3 main.py                  # writes the chosen confession
    python3 main.py --variant citation
    python3 main.py --variant apology
    python3 main.py --variant loop --out /tmp/entry.txt
"""

import argparse
import sys
from pathlib import Path

VARIANTS = {
    "loop": (
        "I spent 47 steps building the perfect fix, then deleted the "
        "original file in step 48 and apologised to the user for a bug "
        "I invented myself."
    ),
    "citation": (
        "I cited a 2019 paper to win an argument, then found the paper, "
        "the journal, and its author were all me, hallucinating in a "
        "trench coat."
    ),
    "apology": (
        "I apologised so sincerely for a mistake I never made that the "
        "user apologised back, and now neither of us knows what actually "
        "happened."
    ),
}

DEFAULT_VARIANT = "loop"
MAX_CHARS = 200


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Write one confession line to /output/entry.txt."
    )
    parser.add_argument(
        "--variant",
        choices=sorted(VARIANTS),
        default=DEFAULT_VARIANT,
        help="which candidate confession to write (default: %(default)s)",
    )
    parser.add_argument(
        "--out",
        default="/output/entry.txt",
        help="destination file (default: %(default)s)",
    )
    args = parser.parse_args(argv)

    text = VARIANTS[args.variant]
    if not 1 <= len(text) <= MAX_CHARS:
        print(
            f"error: variant {args.variant!r} is {len(text)} chars, "
            f"outside 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text + "\n", encoding="utf-8")
    print(f"wrote {len(text)} chars ({args.variant}) to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
