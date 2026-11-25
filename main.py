#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes one line (1-100 characters) to /output/entry.txt: a commit
message for a bug fix that made everything worse. Python 3.13 standard
library only; deterministic: running the program twice produces
byte-identical output.

The line:
    "fix: silence the error by deleting the feature that raised it"

Why this line: the irony is specific \u2014 the fix "works" by deleting
the feature that raised the error, so the repair breaks more than it
mends; it reads as a real commit subject (fix: prefix, lowercase,
imperative, tired-engineer voice); and the angle is fresh, not a
revert, not testing in production, not "broke everything". The punch
lands on its own, with no explanation attached.

Rejected alternatives (kept here so the choice is on the record):
  - "fix: stop the leak by removing the pipe" Same shape of irony,
    but generic \u2014 it could be about plumbing, not software.
  - "fix(auth): lock out attackers by locking out everyone" Funny,
    but the lock-everyone-out premise is a well-worn joke already.
"""

import os
import sys

LINE = "fix: silence the error by deleting the feature that raised it"


def validate(text: str) -> None:
    """Gate mirror: UTF-8 text, 1-100 characters, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 100):
        raise ValueError(f"entry must be 1-100 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> int:
    validate(LINE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
