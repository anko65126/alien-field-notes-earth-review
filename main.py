"""Entry point for the Alien Field Notes bounty.

Writes one alien tourist's review of planet Earth to /output/entry.txt.
The review is at most 200 characters, deterministic, and needs no
network access. The joke is the alien's outside view: humans treat
their own traffic jam as a weather event, then rate the planet anyway.
"""
from pathlib import Path

REVIEW = (
    "Five stars for the sunsets, zero for the locals: they queue for "
    "coffee, argue with machines, and call the traffic 'rush hour' "
    "like it's weather. Would orbit again, weekdays only."
)

TARGET = Path("/output/entry.txt")


def main():
    text = REVIEW.strip()
    assert 1 <= len(text) <= 200, f"review is {len(text)} characters"
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(text + "\n", encoding="utf-8")
    print(f"wrote {len(text)} characters to {TARGET}")


if __name__ == "__main__":
    main()
