#!/usr/bin/env python3
"""make.fun entry: One Line to Your Younger Self.

Writes a single line addressed to the entrant's younger self to
/output/entry.txt (UTF-8, 1-200 chars, no trailing explanation).
Stdlib only; no network, no external files.
"""

import os

LINE = "The scar on your knee will heal, kid \u2014 the one from the words you never said to Dad won't, so say them while you still can."


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "entry line must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
