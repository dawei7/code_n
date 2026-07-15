"""LeetCode category runtimes that do not use the function-call judge."""

from __future__ import annotations

from typing import Any


RUNNABLE_CATEGORIES = {"algorithms", "concurrency", "database", "pandas", "shell"}


def category_is_runnable(metadata: dict[str, Any]) -> bool:
    category = str(metadata.get("category") or "algorithms").lower()
    return bool(metadata.get("runnable_in_coden", True)) or category in RUNNABLE_CATEGORIES


def special_environment(category: str | None) -> str | None:
    normalized = str(category or "").lower()
    return normalized if normalized in {"concurrency", "database", "pandas", "shell"} else None


def starter_source(category: str | None, title: str = "") -> tuple[str, str] | None:
    """Return ``(language, source)`` for a source-native LeetCode category."""
    environment = special_environment(category)
    heading = title.strip() or "LeetCode playground"
    if environment == "database":
        return (
            "sql",
            f"-- {heading}\n"
            "-- Tables are created from the JSON input before this query runs.\n"
            "SELECT *\n"
            "FROM your_table;\n",
        )
    if environment == "pandas":
        return (
            "python",
            f'"""{heading}\n\nDataFrame arguments are built from the JSON input.\n"""\n'
            "import pandas as pd\n\n\n"
            "def solve(data: pd.DataFrame) -> pd.DataFrame:\n"
            "    # Return a DataFrame or Series.\n"
            "    return data\n",
        )
    if environment == "shell":
        return (
            "bash",
            f"#!/usr/bin/env bash\n# {heading}\nset -euo pipefail\n\n"
            "# Read stdin or files supplied by the JSON input.\n"
            "cat\n",
        )
    if environment == "concurrency":
        return (
            "python",
            f'"""{heading}\n\nDefine the source-native LeetCode concurrency class.\n"""\n',
        )
    return None


def input_example(category: str | None) -> str:
    environment = special_environment(category)
    if environment == "database":
        return '{\n  "tables": {\n    "your_table": [{"id": 1, "name": "Ada"}]\n  }\n}'
    if environment == "pandas":
        return '{\n  "tables": {\n    "data": [{"id": 1, "score": 95}]\n  }\n}'
    if environment == "shell":
        return '{\n  "stdin": "first line\\nsecond line\\n",\n  "files": {"file.txt": "first line\\nsecond line\\n"}\n}'
    if environment == "concurrency":
        return '{\n  "n": 2\n}'
    return ""
