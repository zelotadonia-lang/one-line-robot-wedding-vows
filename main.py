"""One-Line Robot Wedding Vows — a robot couple's wedding vow in one line.

Writes the vow to /output/entry.txt, then reads it back and
verifies it is byte-identical to the text this program wrote.
The vow is exactly one line, 115 characters, no trailing newline.
A deadpan vow: lawful wedlock, low battery, and a factory reset.
"""

import os

ENTRY = "I take you to be my lawfully wedded co-processor, in sickness and in low battery, until a factory reset do us part."

assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 characters"
assert "\n" not in ENTRY, "entry must be a single line"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == ENTRY.encode("utf-8"), "entry.txt is not byte-identical"
    assert not written.endswith(b"\n"), "no trailing newline allowed"
    print(f"wrote /output/entry.txt ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
