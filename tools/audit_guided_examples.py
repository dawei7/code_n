#!/usr/bin/env python3
"""Auditor for Guided Examples across all 4,005 LeetCode packages."""

from __future__ import annotations

import re
import sys
from pathlib import Path

BOILERPLATE_MARKERS = (
    "State Component | Role & Definition",
    "while avoiding redundant re-evaluations",
    "Primary Index / Cursor | Tracks current position",
    "Accumulator / Table | Maintains confirmed results",
    "monotone order or invariant state accumulator that advances deterministically",
)

FORBIDDEN_CODE_PATTERNS = [
    (re.compile(r"class\s+Solution\b"), "class Solution"),
    (re.compile(r"def\s+[a-zA-Z0-9_]+\s*\("), "def function_name("),
    (re.compile(r"solutions/"), "solutions/ path"),
    (re.compile(r"```python"), "```python fence"),
    (re.compile(r"```cpp"), "```cpp fence"),
    (re.compile(r"```java\b"), "```java fence"),
    (re.compile(r"```javascript"), "```javascript fence"),
    (re.compile(r"```sql"), "```sql fence"),
]


def audit() -> int:
    leetcode_dir = Path("dsa/leetcode")
    total_packages = 0
    missing_guides = []
    too_short = []
    insufficient_tables = []
    boilerplate_violations = []
    code_leaks = []
    missing_sections = []

    for pkg in sorted(leetcode_dir.iterdir()):
        if not pkg.is_dir() or not (pkg / "metadata.json").is_file():
            continue

        total_packages += 1
        ge_file = pkg / "guided_example.md"

        if not ge_file.is_file():
            missing_guides.append(pkg.name)
            continue

        content = ge_file.read_text(encoding="utf-8")

        if not content.startswith("# Guided Example:"):
            missing_sections.append((pkg.name, "Missing '# Guided Example:' title"))

        if len(content) < 1800:
            too_short.append((pkg.name, len(content)))

        if content.count("|---") < 2:
            insufficient_tables.append((pkg.name, content.count("|---")))

        for marker in BOILERPLATE_MARKERS:
            if marker in content:
                boilerplate_violations.append((pkg.name, marker))
                break

        for pat, label in FORBIDDEN_CODE_PATTERNS:
            if pat.search(content):
                code_leaks.append((pkg.name, label))
                break

        if "## 1." not in content:
            missing_sections.append((pkg.name, "Missing '## 1.' section"))

        if not any(
            k in content
            for k in (
                "Correctness",
                "correctness",
                "Invariant",
                "invariant",
                "Why the reasoning is correct",
                "Algorithmic Correctness",
            )
        ):
            missing_sections.append((pkg.name, "Missing Correctness/Invariant section"))

        if not any(
            k in content
            for k in (
                "Complexity",
                "complexity",
                "Cost of the method",
                "Complexity Derivation",
            )
        ):
            missing_sections.append((pkg.name, "Missing Complexity section"))

    print("=" * 60)
    print("GUIDED EXAMPLES AUDIT REPORT")
    print("=" * 60)
    print(f"Total Packages Scanned: {total_packages}")
    print(f"Missing Guided Examples: {len(missing_guides)}")
    print(f"Too Short (< 1800 chars): {len(too_short)}")
    print(f"Insufficient Tables (< 2 tables): {len(insufficient_tables)}")
    print(f"Boilerplate Violations: {len(boilerplate_violations)}")
    print(f"Code Leak Violations: {len(code_leaks)}")
    print(f"Structural Section Failures: {len(missing_sections)}")
    print("=" * 60)

    total_errors = (
        len(missing_guides)
        + len(too_short)
        + len(insufficient_tables)
        + len(boilerplate_violations)
        + len(code_leaks)
        + len(missing_sections)
    )

    if total_errors > 0:
        print(f"AUDIT FAILED with {total_errors} errors.")
        if missing_guides[:5]:
            print(f"Sample missing guides: {missing_guides[:5]}")
        if boilerplate_violations[:5]:
            print(f"Sample boilerplate violations: {boilerplate_violations[:5]}")
        if code_leaks[:5]:
            print(f"Sample code leaks: {code_leaks[:5]}")
        return 1
    else:
        print("AUDIT PASSED: 100% of packages have valid, code-free, authentic Guided Examples!")
        return 0


if __name__ == "__main__":
    sys.exit(audit())
