#!/usr/bin/env python3
"""Writes the funniest toaster error message to /output/entry.txt."""

import os

MESSAGE = "ERROR: I have toasted the same slice four times now. We both know you just need to buy more bread."


def main() -> None:
    assert 1 <= len(MESSAGE) <= 120, f"message must be 1-120 chars, got {len(MESSAGE)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(MESSAGE)


if __name__ == "__main__":
    main()
