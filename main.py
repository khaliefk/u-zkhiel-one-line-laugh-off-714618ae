"""One-Line Laugh-Off entry: write exactly one funny line to /output/entry.txt."""

from pathlib import Path

LINE = "My therapist asked what brings me joy, so I showed her my search history and now she needs therapy."


def main() -> None:
    # Gate in the kit: 1 to 200 characters, a single line, not only whitespace.
    assert 1 <= len(LINE) <= 200
    assert "\n" not in LINE and LINE.strip()
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
