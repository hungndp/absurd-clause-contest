"""The Absurd Clause Contest — entrypoint.

Writes exactly one absurd terms-of-service clause, at most 200
characters, to /output/entry.txt. The file holds the line alone,
with no trailing newline, so its byte count is the line's
character count.
"""

import os

# The line, built last-word-first: the landing is "goat" — a service
# outage compensated not with credits or a refund, but with a live
# animal, delivered on the same deadpan schedule as any refund.
# One mechanism (outage compensation), one incident, twist word last,
# stop at the landing.
SETUP = (
    "Section 12.4: in the event of a service outage, the provider "
    "shall compensate each affected user, within thirty (30) "
    "business days, with "
)
PUNCH = "one (1) live goat."

MAX_CHARS = 200


def build_line() -> str:
    """Assemble the clause from its deadpan setup and its punch."""
    return SETUP + PUNCH


def check_line(line: str) -> None:
    """Enforce the competition gate: one sentence, 1-200 characters."""
    if not line.strip():
        raise SystemExit("line is empty or only whitespace")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            f"line is {len(line)} chars, must be 1-{MAX_CHARS}"
        )
    # One sentence: ends with a period and holds no sentence break.
    # (The section number "12.4" carries a period of its own, so a
    # raw period count would misfire.)
    if not line.endswith(".") or ". " in line:
        raise SystemExit("line must be exactly one sentence")


def output_path() -> str:
    """Resolve where the entry text goes; honour $OUTPUT_DIR in tests."""
    return os.path.join(os.environ.get("OUTPUT_DIR", "/output"), "entry.txt")


def write_entry(line: str) -> str:
    """Write the line alone, with no trailing newline, and return it."""
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    return path


def main() -> None:
    line = build_line()
    check_line(line)
    path = write_entry(line)
    print(f"wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
