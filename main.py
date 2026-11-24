"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one funny single-line one-star review, written by a house cat
about its human, to ``entry.txt`` inside the output directory.

Fully deterministic: a fixed string, no time, no randomness, no network,
no file traversal. Standard library only.
"""

import os

# The entry: one line, 170 characters, inside the 1-200 gate.
ENTRY = (
    "One star. He refilled my bowl, then sat down to eat his own dinner "
    "first, like a waiter tasting the order. I have docked his "
    "chin-scratch privileges until further notice."
)


def main() -> None:
    # Gate self-check: the sealed scorer requires UTF-8 text of 1-200
    # characters, not only white space, on a single line.
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry is {len(ENTRY)} characters, gate needs 1-200")
    if "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be one non-blank line")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
