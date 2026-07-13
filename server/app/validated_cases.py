"""Load hand-authored validated test cases for challenge runs.

Validated cases are the user-facing judge input source. The runner no longer
invents synthetic ``n``/``seed`` inputs for the HTTP run path; if a challenge
has no case suite, the route reports that directly.

Runtime benchmarks are deliberately explicit sidecar files. A normal
``<suite>.json`` contains sample, trial, and hidden real cases. Its optional
``<suite>.benchmark.json`` sibling contains benchmark cases only.
"""

from __future__ import annotations

import copy
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Literal

from server.app.challenge_packages import is_leetcode_id, leetcode_cases_path


CaseKind = Literal["sample", "trial", "real", "benchmark", "custom"]
ALL_TRIAL_CASES_ID = "__all_trial__"


class NoValidatedCases(Exception):
    """Raised when a challenge has no authored cases for the requested run."""


class InvalidCustomCase(Exception):
    """Raised when the user's custom JSON input does not match the challenge."""


@dataclass(frozen=True)
class ValidatedCase:
    id: str
    name: str
    kind: CaseKind
    input: dict[str, Any]
    expected: Any = None
    visible: bool = False
    tags: list[str] = field(default_factory=list)
    size: int | None = None
    timeout_ms: int | None = None
    validator: dict[str, Any] = field(default_factory=dict)

    def public_dict(self) -> dict[str, Any]:
        input_repr = _format_value(self.input)
        expected_repr = "" if self.expected is None else _format_value(self.expected)
        return {
            "id": self.id,
            "name": self.name,
            "kind": self.kind,
            "visible": self.visible,
            "input_repr": input_repr,
            "expected_repr": expected_repr,
            "tags": list(self.tags),
        }


def _format_value(value: Any) -> str:
    try:
        return json.dumps(value, ensure_ascii=False)
    except TypeError:
        return repr(value)


def _case_path(challenge_id: str) -> Path | None:
    return leetcode_cases_path(challenge_id) if is_leetcode_id(challenge_id) else None


def _benchmark_case_path(case_path: Path | None) -> Path | None:
    if case_path is None:
        return None
    if case_path.name == "cases.json":
        return case_path.with_name("benchmark.json")
    return case_path.with_name(f"{case_path.stem}.benchmark{case_path.suffix}")


def load_case_suite(challenge_id: str) -> list[ValidatedCase]:
    path = _case_path(challenge_id)
    if path is None or not path.is_file():
        return []
    result = _load_case_file(path, challenge_id, benchmark_sidecar=False)
    benchmark_path = _benchmark_case_path(path)
    if benchmark_path is not None and benchmark_path.is_file():
        result.extend(_load_case_file(benchmark_path, challenge_id, benchmark_sidecar=True))
    return result


def _load_case_file(path: Path, challenge_id: str, *, benchmark_sidecar: bool) -> list[ValidatedCase]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    payload_challenge_id = payload.get("challenge_id")
    if payload_challenge_id is not None and str(payload_challenge_id) != challenge_id:
        raise NoValidatedCases(
            f"{path}: challenge_id {payload_challenge_id!r} does not match {challenge_id!r}."
        )
    cases = payload.get("cases")
    if not isinstance(cases, list):
        raise NoValidatedCases(f"{path}: validated case file has no cases list.")
    result: list[ValidatedCase] = []
    for raw in cases:
        if not isinstance(raw, dict):
            continue
        raw_input = raw.get("input")
        if not isinstance(raw_input, dict):
            raise NoValidatedCases(f"{path}: case {raw.get('id')!r} input must be an object.")
        kind = str(raw.get("kind") or "trial")
        if kind not in {"sample", "trial", "real", "benchmark", "custom"}:
            raise NoValidatedCases(f"{path}: case {raw.get('id')!r} has invalid kind {kind!r}.")
        if benchmark_sidecar and kind != "benchmark":
            raise NoValidatedCases(
                f"{path}: benchmark sidecar case {raw.get('id')!r} must use kind 'benchmark'."
            )
        if not benchmark_sidecar and kind == "benchmark":
            benchmark_path = _benchmark_case_path(path)
            raise NoValidatedCases(
                f"{path}: benchmark case {raw.get('id')!r} must live in "
                f"{benchmark_path.name if benchmark_path else '<suite>.benchmark.json'}."
            )
        raw_size = raw.get("size")
        if raw_size is not None and (
            isinstance(raw_size, bool) or not isinstance(raw_size, int) or raw_size <= 0
        ):
            raise NoValidatedCases(
                f"{path}: benchmark size for case {raw.get('id')!r} must be a positive integer."
            )
        result.append(
            ValidatedCase(
                id=str(raw.get("id") or f"case-{len(result) + 1}"),
                name=str(raw.get("name") or raw.get("id") or f"Case {len(result) + 1}"),
                kind=kind,  # type: ignore[arg-type]
                input=copy.deepcopy(raw_input),
                expected=copy.deepcopy(raw.get("expected")),
                visible=bool(raw.get("visible", kind in {"sample", "trial"})),
                tags=[str(tag) for tag in raw.get("tags") or []],
                size=raw_size,
                timeout_ms=int(raw["timeout_ms"]) if raw.get("timeout_ms") is not None else None,
                validator=copy.deepcopy(raw.get("validator") or {}),
            )
        )
    if benchmark_sidecar and len(result) >= 2:
        if any(case.size is None or case.size <= 0 for case in result):
            raise NoValidatedCases(
                f"{path}: multi-tier benchmark cases require a positive integer size."
            )
        sizes = [int(case.size or 0) for case in result]
        if sizes != sorted(set(sizes)):
            raise NoValidatedCases(
                f"{path}: benchmark sizes must be unique and ordered from smallest to largest."
            )
        if sizes[-1] < sizes[0] * 4:
            raise NoValidatedCases(
                f"{path}: benchmark tiers must span at least 4x from smallest to largest."
            )
    return result


def visible_cases(challenge_id: str) -> list[dict[str, Any]]:
    return [case.public_dict() for case in load_case_suite(challenge_id) if case.visible]


def _custom_case(custom_input: dict[str, Any] | None) -> ValidatedCase | None:
    if custom_input is None:
        return None
    if not isinstance(custom_input, dict):
        raise InvalidCustomCase("Custom input must be a JSON object matching solve(...) parameters.")
    return ValidatedCase(
        id="custom",
        name="Custom input",
        kind="custom",
        input=copy.deepcopy(custom_input),
        visible=True,
    )


def _custom_cases(raw_cases: list[dict[str, Any]] | None) -> list[ValidatedCase]:
    result: list[ValidatedCase] = []
    seen: set[str] = set()
    for index, raw in enumerate(raw_cases or []):
        if not isinstance(raw, dict) or not isinstance(raw.get("input"), dict):
            raise InvalidCustomCase("Every custom case must contain an object input.")
        case_id = str(raw.get("id") or f"user-{index + 1}").strip()
        if not case_id or case_id in seen or case_id == ALL_TRIAL_CASES_ID:
            raise InvalidCustomCase(f"Invalid or duplicate custom case id: {case_id!r}.")
        seen.add(case_id)
        result.append(
            ValidatedCase(
                id=case_id,
                name=str(raw.get("name") or f"Custom case {index + 1}"),
                kind="custom",
                input=copy.deepcopy(raw["input"]),
                visible=True,
                tags=["user-defined"],
            )
        )
    return result


def select_cases_for_run(
    challenge_id: str,
    *,
    mode: str,
    selected_case_ids: list[str] | None = None,
    custom_input: dict[str, Any] | None = None,
    custom_cases: list[dict[str, Any]] | None = None,
) -> tuple[list[ValidatedCase], list[ValidatedCase]]:
    custom = _custom_case(custom_input)
    if custom is not None:
        return [custom], [custom]

    suite = load_case_suite(challenge_id)
    user_cases = _custom_cases(custom_cases)
    system_ids = {case.id for case in suite}
    collisions = system_ids & {case.id for case in user_cases}
    if collisions:
        raise InvalidCustomCase(
            f"Custom case ids cannot replace system cases: {', '.join(sorted(collisions))}."
        )
    if not suite and not user_cases:
        raise NoValidatedCases(
            f"{challenge_id} has no validated test cases yet. Add cases.json to its canonical LeetCode package before running."
        )

    if mode == "real_test":
        visible = [case for case in suite if case.visible and case.kind in {"sample", "trial"}]
        hidden = [case for case in suite if case.kind == "real"]
        benchmark_cases = [case for case in suite if case.kind == "benchmark"]
        if not hidden:
            raise NoValidatedCases(f"{challenge_id} has no hidden real-test cases.")
        if not benchmark_cases:
            raise NoValidatedCases(f"{challenge_id} has no benchmark cases for runtime gating.")
        run_cases = [*visible, *user_cases, *hidden, *benchmark_cases]
        return run_cases, benchmark_cases

    visible = [case for case in suite if case.visible]
    selectable = [*visible, *user_cases]
    if not selectable:
        raise NoValidatedCases(f"{challenge_id} has no visible practice cases.")

    selected = selected_case_ids or []
    if ALL_TRIAL_CASES_ID in selected:
        run_cases = [case for case in visible if case.kind in {"sample", "trial"}] + user_cases
    elif selected:
        wanted = set(selected)
        run_cases = [case for case in selectable if case.id in wanted]
        missing = wanted - {case.id for case in run_cases}
        if missing:
            raise NoValidatedCases(f"{challenge_id} has no visible case(s): {', '.join(sorted(missing))}")
    else:
        run_cases = [selectable[0]]

    if not run_cases:
        raise NoValidatedCases(f"{challenge_id} has no selected practice cases.")

    benchmark_cases = [case for case in suite if case.kind == "benchmark"]
    if not benchmark_cases:
        if user_cases:
            benchmark_cases = user_cases
        else:
            raise NoValidatedCases(f"{challenge_id} has no benchmark cases for runtime gating.")
    return run_cases, benchmark_cases
