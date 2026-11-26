#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence — make.fun bounty entry.

Writes one line: the error message an AI agent prints when it runs
out of tokens mid-sentence. Standard library only, deterministic.
"""

import os

ENTRY = (
    "Error: token budget exhausted. "
    "I spent my final token printing this error "
    "instead of finishing the sentence."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    """Write the single-line entry to /output/entry.txt."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
