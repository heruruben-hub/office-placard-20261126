#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes a single museum placard — one line, at most 180 characters — for an
ordinary office object treated as an ancient artifact, to /output/entry.txt.
"""

import os

ENTRY = (
    # One line, 131 characters: catalogue date, material, donor, and a
    # small deadpan tragedy — the call was never made.
    "Votive sticky note, c. 900 BCE. Papyrus and optimism. "
    "'Call back re: grain.' The call was never made. "
    "Bequest of an unknown intern."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 180, f"entry is {len(ENTRY)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
