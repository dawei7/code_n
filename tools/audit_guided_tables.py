#!/usr/bin/env python3
"""Audit Guided Example tables for a consistent cell count.

`tools/audit_guided_examples.py` counts tables by their delimiter row, so a
table whose rows disagree on width still satisfies the "at least two tables"
rule while rendering with shifted columns in the app. This tool reports those
tables.

A table is a contiguous run of pipe-leading lines outside a fenced code block.
Within one run the first line is the header, the second must be the delimiter
row, and every later line is expected to have the same number of cells as the
header. A pipe escaped as ``\\|`` is literal cell content, not a boundary, and is
never counted.

Usage:
    python tools/audit_guided_tables.py                     # whole corpus
    python tools/audit_guided_tables.py 0014 0272 0418      # package filters
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

LEETCODE_DIR = Path(__file__).resolve().parent.parent / "dsa" / "leetcode"
DELIMITER_ROW = re.compile(r"^\s*\|?\s*:?-{1,}:?\s*(?:\|\s*:?-{1,}:?\s*)*\|?\s*$")
CELL_SPLIT = re.compile(r"(?<!\\)\|")


def count_cells(line: str) -> int:
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|") and not stripped.endswith("\\|"):
        stripped = stripped[:-1]
    return len(CELL_SPLIT.split(stripped))


def table_problems(text: str) -> list[str]:
    """Return one message per table whose rows disagree with its header."""
    problems: list[str] = []
    run: list[tuple[int, str]] = []
    inside_fence = False

    def flush() -> None:
        if len(run) < 2 or not DELIMITER_ROW.match(run[1][1]):
            return
        width = count_cells(run[0][1])
        for line_number, raw in run[2:]:
            actual = count_cells(raw)
            if actual != width:
                problems.append(
                    f"line {line_number}: header declares {width} cells, row has {actual}"
                )
                return

    for line_number, line in enumerate(text.splitlines(), start=1):
        if line.strip().startswith("```"):
            inside_fence = not inside_fence
            if run:
                flush()
                run = []
            continue
        if not inside_fence and line.strip().startswith("|"):
            run.append((line_number, line))
            continue
        if run:
            flush()
            run = []

    flush()
    return problems


def iter_packages(filters: list[str]):
    for package in sorted(LEETCODE_DIR.iterdir()):
        if not package.is_dir():
            continue
        if filters and not any(f in package.name for f in filters):
            continue
        guide = package / "guided_example.md"
        if guide.is_file():
            yield package.name, guide


def main() -> int:
    args = sys.argv[1:]
    names_only = "--names" in args
    filters = [a for a in args if a != "--names"]
    failing = 0
    scanned = 0
    if not names_only:
        print("GUIDED EXAMPLE TABLE AUDIT REPORT")
    for name, guide in iter_packages(filters):
        scanned += 1
        problems = table_problems(guide.read_text(encoding="utf-8"))
        if not problems:
            continue
        failing += 1
        if names_only:
            print(name)
            continue
        print(f"  {name}")
        for problem in problems:
            print(f"    {problem}")
    if names_only:
        return 1 if failing else 0
    print(f"Total Packages Scanned: {scanned}")
    print(f"Tables with an inconsistent cell count: {failing}")
    if failing:
        print(
            "Repair guidance: literal pipes inside a cell must be escaped as \\| "
            "(or written with \\lvert and \\rvert); every row of a table must have "
            "the same number of cells as its header."
        )
        return 1
    print("TABLE AUDIT PASSED: every Guided Example table has a consistent cell count!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())