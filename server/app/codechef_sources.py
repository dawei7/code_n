"""Select CodeChef-owned source candidates for internal baselines.

The visible Reference page must stay source-faithful to the official problem
statement/editorial and must not show solution code.  These helpers are for the
separate internal AST baseline pipeline: prefer CodeChef-provided Python when
available, otherwise expose the best official/editorial source so it can be
translated and submitted for validation.
"""

from __future__ import annotations

import re
from typing import Any


PYTHON_TOKENS = ("PYTH", "PYTHON", "PYPY")
PREFERRED_LABELS = (
    "editorialist",
    "setter",
    "tester",
    "official",
)


def is_python_language(language: str) -> bool:
    """Return whether a CodeChef language label means Python 3/PyPy."""
    upper = language.upper()
    return any(token in upper for token in PYTHON_TOKENS)


def _label_score(label: str) -> tuple[int, str]:
    lower = label.lower()
    for index, token in enumerate(PREFERRED_LABELS):
        if token in lower:
            return index, lower
    return len(PREFERRED_LABELS), lower


def _language_from_label(label: str, source: str) -> str:
    label_upper = label.upper()
    if "PYTHON" in label_upper or "PYTH" in label_upper:
        return "PYTH 3"
    if "C++" in label_upper or "#include" in source or "using namespace std" in source:
        return "C++"
    if "JAVA" in label_upper or "public class" in source:
        return "JAVA"
    if "C#" in label_upper:
        return "C#"
    if "JAVASCRIPT" in label_upper or "NODE" in label_upper:
        return "NODEJS"
    return "Text"


def extract_editorial_blocks(editorial: str) -> list[dict[str, str]]:
    """Return source blocks embedded in a normalized CodeChef editorial."""
    blocks: list[dict[str, str]] = []
    pattern = re.compile(r"(?P<label>[^\n`]{0,120}?)\n?``(?P<source>[\s\S]*?)``")
    for match in pattern.finditer(editorial):
        source = match.group("source").strip()
        if source.startswith("`"):
            source = source[1:].strip()
        if not source or "\n" not in source or len(source) < 40:
            continue
        label = match.group("label").strip()
        label = re.split(r"\n+", label)[-1].strip("* :#") or "Editorial code"
        blocks.append(
            {
                "label": label,
                "language": _language_from_label(label, source),
                "source": source.rstrip() + "\n",
            }
        )
    return sorted(blocks, key=lambda row: _label_score(row["label"]))


def codechef_source_candidates(problem: dict[str, Any]) -> list[dict[str, str]]:
    """Return official-solution rows followed by editorial code blocks."""
    candidates: list[dict[str, str]] = []
    for solution in list(problem.get("official_solutions") or []):
        if isinstance(solution, dict) and solution.get("source"):
            candidates.append(
                {
                    "label": "Official solution",
                    "language": str(solution.get("language") or "Text"),
                    "source": str(solution["source"]).rstrip() + "\n",
                }
            )
    candidates.extend(extract_editorial_blocks(str(problem.get("editorial") or "")))
    return candidates


def best_codechef_source(problem: dict[str, Any], *, prefer_python: bool = True) -> dict[str, str] | None:
    """Return the best CodeChef-owned source candidate for a problem."""
    candidates = codechef_source_candidates(problem)
    if prefer_python:
        python = [row for row in candidates if is_python_language(row.get("language", ""))]
        if python:
            return python[0]
    return candidates[0] if candidates else None
