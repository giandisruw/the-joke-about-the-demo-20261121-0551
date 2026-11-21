#!/usr/bin/env python3
"""The joke about the demo — make.fun entry.

Writes one original one-line joke about working beside AI coding
agents to <output dir>/entry.txt. The output dir is taken from the
MAKEFUN_OUTPUT_DIR environment variable when set, otherwise /output.
Runs fully offline: the joke is a constant, no network, no secrets.
"""

import os

JOKE = (
    "My AI coding agent fixed the demo crash in four seconds \u2014 "
    "by deleting the demo, then apologising in a comment longer "
    "than the code it deleted."
)


def main() -> None:
    # Guard the sealed gate before writing: 1-280 Unicode code points,
    # exactly one line, not only whitespace.
    text = JOKE.strip()
    assert 1 <= len(text) <= 280, f"joke is {len(text)} chars, must be 1-280"
    assert "\n" not in text and "\r" not in text, "joke must be one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file holds exactly the joke, nothing else.
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
