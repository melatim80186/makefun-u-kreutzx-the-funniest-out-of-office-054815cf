#!/usr/bin/env python3
"""make.fun entry: u-kreutzx-the-funniest-out-of-office-054815cf.

Writes the one-line entry to /output/entry.txt.
Python 3, stdlib only, deterministic, no network.
"""

import os

ENTRY = "I'm out of the office until Monday. My inbox is unattended, unsupervised, and — judging by the 400 unread emails — unwell."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
