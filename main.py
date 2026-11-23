#!/usr/bin/env python3
"""One-Star Review of Something Essential — make.fun entry.

Writes a single deadpan one-star review (one line, 1-160 characters)
of an everyday essential to /output/entry.txt.
"""

import os
import sys

REVIEW = (
    "One star. Gravity never misses: it catches every phone I drop "
    "and every glass I knock over, but it has never once caught me."
)

MAX_CHARS = 160


def validate(line: str) -> None:
    """Guard the gate: 1-160 characters, a single line, not blank."""
    if not line or not line.strip():
        raise ValueError("review must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("review must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"review is {len(line)} characters, over the {MAX_CHARS} limit"
        )


def main() -> int:
    validate(REVIEW)
    os.makedirs("/output", exist_ok=True)
    # Write the review exactly, with no trailing newline, so the file
    # holds precisely the one line the judge reads.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)
    print(f"wrote /output/entry.txt ({len(REVIEW)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
