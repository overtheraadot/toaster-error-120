#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun entry (account A / overtheraa).

Writes one line, at most 120 characters: the error message a kitchen
toaster shows its owner when something goes wrong. Deterministic, no
network, no model calls.
"""

import os

ENTRY = "ERROR: TOASTING CANCELLED. THE BREAD LOOKED AT ME, AND I COULD NOT DO IT."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
