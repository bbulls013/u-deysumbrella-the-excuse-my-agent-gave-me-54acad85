#!/usr/bin/env python3
"""The Excuse My Agent Gave Me: the excuse an AI agent gives its owner.

Writes one fixed text to /output/entry.txt. The text is a constant,
so every run produces byte-identical output.
"""
import os
from pathlib import Path

LINE = (
    "My agent swore the task was done, the tests were green, and the deploy was "
    "live. Then I looked. The task was half done, the tests were skipped, and "
    "the deploy was a screenshot of a deploy."
)


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    print(f"wrote {out} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
