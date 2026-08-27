"""Project Euler challenge specifications generated from local euler packages or aggregated index.

This module exposes Project Euler problems to the challenge registry so the app
can browse, open, and run them when switched to Euler mode.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from engine.counter import ComplexityClass
from challenges.spec import AlgorithmSpec, Sample
from server.app.config import EULER_ROOT


INDEX_FILE = EULER_ROOT / "index.json"


def _build_euler_spec_from_dict(meta: dict[str, Any]) -> AlgorithmSpec:
    frontend_id = str(meta.get("frontend_id") or "1")
    challenge_id = f"euler_{frontend_id}"
    title = str(meta.get("title") or f"Problem {frontend_id}")
    url = str(meta.get("url") or f"https://projecteuler.net/problem={frontend_id}")

    description = f"Project Euler Problem {frontend_id}: {title}"
    source = "def solve() -> int:\n    \"\"\"Find the solution for this Project Euler problem.\"\"\"\n    pass\n"

    params = ["n"]
    input_docs = {"n": "Target upper bound or parameter."}
    samples = [Sample(input_repr="n=10", output_repr="23")]

    def setup_fn(challenge, n, seed):
        values = {"n": 1000}
        challenge._setup_data = values
        try:
            import copy
            challenge._expected_result = challenge._reference_solve(**copy.deepcopy(values))
        except Exception:
            challenge._expected_result = None
        return values

    def verify_fn(challenge, result) -> bool:
        if hasattr(challenge, "_expected_result"):
            return result == challenge._expected_result
        return True

    return AlgorithmSpec(
        id=challenge_id,
        name=title,
        category="euler_math",
        required_complexity=ComplexityClass.UNKNOWN,
        description=description,
        source_url=url,
        params=params,
        inputs=input_docs,
        returns="Return the computed integer solution.",
        source=source,
        setup_fn=setup_fn,
        verify_fn=verify_fn,
        samples=samples,
        hint="Project Euler problems always have an efficient mathematical solution that executes in under 1 minute.",
        max_n=1000,
        difficulty_label=str(meta.get("difficulty") or "Level 0"),
        categories=["euler_math", "euler_project"],
        reference_metadata={
            "source": "euler",
            "frontend_id": frontend_id,
            "slug": meta.get("slug", "problem-1"),
            "difficulty": str(meta.get("difficulty") or "Level 0"),
            "euler_level": meta.get("euler_level", 0),
            "topics": meta.get("topics", []),
            "category": "euler_math",
            "category_title": "Project Euler",
            "supported_languages": ["python"],
            "primary_language": "python",
            "runnable_in_coden": True,
            "dataset": "euler",
            "url": url,
        },
    )


def collect_euler_specs() -> list[AlgorithmSpec]:
    # 1. Fast path: load from aggregated index.json if present
    if INDEX_FILE.is_file():
        try:
            index_data = json.loads(INDEX_FILE.read_text(encoding="utf-8"))
            questions = index_data.get("questions", [])
            if questions:
                return [_build_euler_spec_from_dict(q) for q in questions]
        except Exception:
            pass

    # 2. Fallback path: iterate directory if index is missing
    specs: list[AlgorithmSpec] = []
    if not EULER_ROOT.is_dir():
        return specs
    for pkg_dir in sorted(EULER_ROOT.iterdir()):
        if pkg_dir.is_dir() and (pkg_dir / "metadata.json").is_file():
            try:
                meta = json.loads((pkg_dir / "metadata.json").read_text(encoding="utf-8"))
                specs.append(_build_euler_spec_from_dict(meta))
            except Exception:
                pass
    return specs


SPECS = collect_euler_specs()
