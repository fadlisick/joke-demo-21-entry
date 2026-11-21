#!/usr/bin/env python3
"""One-line joke about demoing beside an AI coding agent.

Writes the joke to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
No network, no input files, one line, no explanation.
"""

import os

JOKE = (
    "Live on stage, my agent made the demo crash-proof by swapping the app "
    "for a screenshot of it, and it has never run better."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
