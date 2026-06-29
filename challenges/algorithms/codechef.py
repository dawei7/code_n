"""CodeChef challenge specifications generated from local index.

The CodeChef Python Practice dataset is a beginner-friendly course of
14 lessons covering Python fundamentals (output, variables, strings,
conditionals, loops, lists, tuples/dicts, functions, and algorithmic
problems). This module exposes them to the normal challenge registry
so the app can browse and open them by dataset.
"""

from __future__ import annotations

import json
import io
import re
import sys
from typing import Any

from code_n.counter import ComplexityClass
from challenges.spec import AlgorithmSpec, Sample
from server.app.config import DOCS_ROOT as CONFIGURED_DOCS_ROOT
from server.app.codechef_sources import best_codechef_source, is_python_language


DOCS_ROOT = CONFIGURED_DOCS_ROOT / "algorithms" / "codechef"
INDEX_PATH = DOCS_ROOT / "index.json"
DETAILS_PATH = DOCS_ROOT / "problem_details.json"
TRANSLATIONS_PATH = DOCS_ROOT / "translated_solutions.json"
CAREER_GROUP_PREFIXES = (
    "codechef_become_5_star",
)


def _noop_source(params: list[str]) -> str:
    signature = ", ".join(params)
    return f"def solve({signature}):\n    return None\n"


def _noop_verify(challenge, result) -> bool:
    return False


def _normalize_stdin(value: str) -> str:
    lines = [line.rstrip() for line in str(value or "").replace("\r\n", "\n").replace("\r", "\n").splitlines()]
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines) + ("\n" if lines else "")


def _sample_stdin(samples: list[Sample]) -> str:
    for sample in samples:
        stdin = _normalize_stdin(sample.input_repr)
        if stdin.strip():
            return stdin
    return "1\n"


def _repeat_sample_cases(stdin: str, n: int) -> str:
    """Scale simple CodeChef sample input while preserving its testcase shape.

    Most CodeChef tasks use ``T`` followed by fixed-line testcase blocks.  When
    that shape is obvious from the sample, repeat whole testcase blocks up to a
    small n-sized target.  For variable/ambiguous samples, keep the official
    sample as-is; valid-but-small beats clever-but-broken here.
    """
    lines = [line for line in _normalize_stdin(stdin).splitlines() if line.strip()]
    if len(lines) < 2:
        return _normalize_stdin(stdin)
    try:
        sample_t = int(lines[0].strip())
    except ValueError:
        return _normalize_stdin(stdin)
    if sample_t <= 0:
        return _normalize_stdin(stdin)

    payload = lines[1:]
    if len(payload) % sample_t != 0:
        return _normalize_stdin(stdin)
    block_size = len(payload) // sample_t
    if block_size <= 0:
        return _normalize_stdin(stdin)

    blocks = [
        payload[index:index + block_size]
        for index in range(0, len(payload), block_size)
    ]
    target_t = max(1, min(int(n or sample_t), 50))
    repeated = [blocks[index % len(blocks)] for index in range(target_t)]
    output_lines = [str(target_t)]
    for block in repeated:
        output_lines.extend(block)
    return "\n".join(output_lines) + "\n"


def _run_stdin_program(source: str, input_data: str) -> str:
    old_stdin, old_stdout = sys.stdin, sys.stdout
    namespace: dict[str, Any] = {"__name__": "codechef_reference"}
    capture = io.StringIO()
    try:
        exec(source, namespace)  # noqa: S102 - trusted local optimal baseline
        solve = namespace.get("solve")
        if not callable(solve):
            return ""

        stdin_bytes = io.BytesIO(input_data.encode("utf-8"))
        sys.stdin = io.TextIOWrapper(stdin_bytes, encoding="utf-8")
        sys.stdout = capture
        solve()
    finally:
        sys.stdin = old_stdin
        sys.stdout = old_stdout
    return capture.getvalue().strip()


def _codechef_setup(samples: list[Sample]):
    def setup(challenge, n, seed):
        del seed
        input_data = _repeat_sample_cases(_sample_stdin(samples), n)
        challenge._setup_data = {"input_data": input_data}
        challenge._expected_output = None
        try:
            from server.app.codechef_community import load_cached_source
            reference_source = load_cached_source(challenge.info.id)
            if reference_source:
                challenge._expected_output = _run_stdin_program(reference_source, input_data)
        except (Exception, SystemExit):
            challenge._expected_output = None
        return challenge._setup_data
    return setup


def _codechef_verify(challenge, result) -> bool:
    expected = getattr(challenge, "_expected_output", None)
    if expected is None:
        return False
    if isinstance(result, (list, tuple)):
        actual = "\n".join(str(item) for item in result)
    else:
        actual = str(result)
    return actual.strip() == str(expected).strip()


def _difficulty_level(question: dict) -> int:
    """Map CodeChef difficulty data to the 1-10 scale used by cOde(n)."""
    return int(question.get("difficulty_level", 1))


def _build_spec(question: dict, detail: dict[str, Any] | None = None) -> AlgorithmSpec:
    """Build an AlgorithmSpec from one CodeChef question entry."""
    code = question["code"]
    name = question["name"]
    category = question["category"]
    url = question["url"]
    difficulty = _difficulty_level(question)
    difficulty_rating = int(question.get("difficulty_rating", -1) or -1)
    difficulty_label = str(difficulty_rating) if difficulty_rating > 0 else "Unknown"
    lesson = question.get("lesson", "")
    lesson_num = question.get("lesson_num", 0)

    detail = detail or {}
    description = str(detail.get("statement") or (
        f"Solve the CodeChef problem: {name}. "
        f"(Lesson {lesson_num}: {lesson})"
    ))

    params = ["input_data"]
    input_docs = {
        "input_data": (
            "A complete CodeChef stdin string generated from the official "
            "sample shape and capped to at most 50 repeated test cases."
        )
    }
    source = _noop_source(params)
    codechef_solution = best_codechef_source(detail, prefer_python=True)
    preferred_solution = (
        codechef_solution
        if codechef_solution and is_python_language(codechef_solution.get("language", ""))
        else _TRANSLATIONS.get(code, {})
    )
    samples = [
        Sample(str(sample.get("input") or ""), str(sample.get("output") or ""))
        for sample in list(detail.get("samples") or [])[:3]
    ]

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
        returns=str(detail.get("output_format") or "Return the exact stdout as a string."),
        source=source,
        setup_fn=_codechef_setup(samples),
        verify_fn=_codechef_verify,
        samples=samples,
        hint="Use the constraints to choose the intended time complexity.",
        max_n=50,
        difficulty_label=difficulty_label,
        acceptance_rate=None,
        categories=list(question.get("categories") or [category]),
        reference_source=str(preferred_solution.get("source") or ""),
        reference_language=str(preferred_solution.get("language") or ""),
        reference_metadata=detail,
    )


def _load_index() -> dict[str, Any]:
    if not INDEX_PATH.is_file():
        return {}
    try:
        return json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def _build_career_paths(questions: list[dict[str, Any]]) -> list[list[str]]:
    """Build strict CodeChef career paths.

    The Become 5 star track is intentionally a single rating ladder: unlocks
    always move from lower official CodeChef rating to higher rating, with the
    problem code as a stable tie-breaker. Other CodeChef tracks remain practice
    material and are not gated by this career path list.
    """
    paths: list[list[str]] = []
    for prefix in CAREER_GROUP_PREFIXES:
        seen: set[str] = set()
        path: list[str] = []
        members = [
            question for question in questions
            if any(
                str(category).startswith(prefix)
                for category in question.get("categories", [question.get("category", "")])
            )
        ]
        members.sort(key=lambda item: (
            int(item.get("difficulty_rating", -1)) if int(item.get("difficulty_rating", -1) or -1) > 0 else 10**9,
            str(item.get("code", "")),
        ))
        for question in members:
            challenge_id = f"cc_{question['code']}"
            if challenge_id not in seen:
                seen.add(challenge_id)
                path.append(challenge_id)
        if path:
            paths.append(path)
    return paths


_INDEX = _load_index()
try:
    _DETAILS = json.loads(DETAILS_PATH.read_text(encoding="utf-8")).get("problems", {})
except (OSError, json.JSONDecodeError):
    _DETAILS = {}
try:
    _TRANSLATIONS = json.loads(TRANSLATIONS_PATH.read_text(encoding="utf-8")).get("translations", {})
except (OSError, json.JSONDecodeError):
    _TRANSLATIONS = {}
CODECHEF_CAREER_PATHS = _build_career_paths(list(_INDEX.get("questions", [])))


def _collect_specs() -> list[AlgorithmSpec]:
    data = _INDEX
    if not data:
        return []

    specs = []
    for question in data.get("questions", []):
        spec = _build_spec(question, _DETAILS.get(str(question.get("code", ""))))
        specs.append(spec)
    return specs


SPECS = _collect_specs()
