"""CodeChef challenge specifications generated from local index.

The CodeChef Python Practice dataset is a beginner-friendly course of
14 lessons covering Python fundamentals (output, variables, strings,
conditionals, loops, lists, tuples/dicts, functions, and algorithmic
problems). This module exposes them to the normal challenge registry
so the app can browse and open them by dataset.
"""

from __future__ import annotations

import json
import random
import re
from pathlib import Path
from typing import Any

from code_n.counter import ComplexityClass
from challenges.spec import AlgorithmSpec, Sample


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DOCS_ROOT = PROJECT_ROOT / "docs" / "algorithms" / "codechef"
INDEX_PATH = DOCS_ROOT / "index.json"


def _noop_source(params: list[str]) -> str:
    signature = ", ".join(params)
    return f"def solve({signature}):\n    return None\n"


def _noop_verify(challenge, result) -> bool:
    return False


def _codechef_setup(params: list[str]):
    def setup(challenge, n, seed):
        rng = random.Random(seed)
        values: dict[str, Any] = {}
        for name in params:
            if name == "value":
                values[name] = rng.randint(0, max(1, n))
            else:
                values[name] = rng.randint(0, max(1, n))
        challenge._setup_data = values
        return values
    return setup


def _difficulty_level(question: dict) -> int:
    """Map CodeChef difficulty data to the 1-10 scale used by cOde(n)."""
    return int(question.get("difficulty_level", 1))


def _build_spec(question: dict) -> AlgorithmSpec:
    """Build an AlgorithmSpec from one CodeChef question entry."""
    code = question["code"]
    name = question["name"]
    category = question["category"]
    url = question["url"]
    difficulty = _difficulty_level(question)
    difficulty_label = question.get("difficulty", "Easy")
    lesson = question.get("lesson", "")
    lesson_num = question.get("lesson_num", 0)

    description = (
        f"Solve the CodeChef problem: {name}. "
        f"(Lesson {lesson_num}: {lesson})"
    )

    params = ["value"]
    input_docs = {"value": "Input value."}
    source = _noop_source(params)

    return AlgorithmSpec(
        id=f"cc_{code}",
        name=name,
        category=category,
        difficulty=difficulty,
        required_complexity=ComplexityClass.O_1,
        description=description,
        source_url=url,
        params=params,
        inputs=input_docs,
        returns="Return the result.",
        source=source,
        setup_fn=_codechef_setup(params),
        verify_fn=_noop_verify,
        samples=[],
        hint="Visit the CodeChef problem page for the full statement.",
        max_n=50,
        difficulty_label=difficulty_label,
        acceptance_rate=None,
        categories=[category],
    )


def _collect_specs() -> list[AlgorithmSpec]:
    if not INDEX_PATH.is_file():
        return []
    try:
        data = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []

    specs = []
    for question in data.get("questions", []):
        spec = _build_spec(question)
        specs.append(spec)
    return specs


SPECS = _collect_specs()
