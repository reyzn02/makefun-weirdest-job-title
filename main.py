#!/usr/bin/env python3
"""Weirdest Job Title entry for make.fun.

Writes a single job title (60 characters or fewer) to /output/entry.txt.

The title was chosen by a head-to-head tournament of 14 candidates,
judged with the competition brief's persona (a deadpan comedy scout:
weirder + funnier; a real-sounding job with one hilariously specific
twist; funny on first read), then checked against the strongest visible
entries in this competition. The champion beat every one of them.
"""

import os

TITLE = "Professional Defendant, Mock Trials Only"
# The grader runs the program in a sandbox where the entry goes to
# /output/entry.txt. OUTPUT_PATH exists only so the entry can be tested
# locally without root; the graded default is always /output/entry.txt.
OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    # Mirror the gate: 1-60 chars, UTF-8, and not only whitespace.
    # Also reject newlines and stray surrounding whitespace so the
    # written bytes are exactly the title, nothing else.
    if not 1 <= len(TITLE) <= 60:
        raise ValueError(f"title must be 1-60 chars, got {len(TITLE)}")
    if TITLE != TITLE.strip() or "\n" in TITLE or "\r" in TITLE:
        raise ValueError("title must have no newline or surrounding whitespace")
    TITLE.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
