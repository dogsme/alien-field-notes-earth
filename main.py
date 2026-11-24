#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line of plain text -- a review of planet Earth
left by an alien tourist -- to /output/entry.txt.
"""

from pathlib import Path

LINE = "Visited Earth. A local sneezed and the whole room shouted 'bless you', like a soul had just escaped \u2014 charming, alarming, 5/5, would sneeze again."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
