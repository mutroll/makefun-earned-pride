"""One Line of Earned Pride — u-mang-one-line-of-earned-pride-a0138557.

Writes a single line of text to /output/entry.txt: a quiet, earned
moment of pride for a small person doing something hard.
Deterministic, stdlib only, no network, no secrets.
"""

import os

LINE = (
    "All summer Milo rebuilt his kite from splintered wood and tangled string; "
    "this morning it finally climbed past the rooftops, and he just stood "
    "there, holding the line steady."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
