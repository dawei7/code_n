"""Standalone practice-file export.

The exported files are intentionally dependency-free: they contain a user
``solve`` stub, generated test cases, and a tiny local runner. They do not
include cOde(n)'s optimal source or complexity checks.
"""
from __future__ import annotations

import copy
import io
import json
import re
import zipfile
from typing import Any, Optional

from fastapi import APIRouter, HTTPException, Query, Response
from pydantic import BaseModel, Field

from challenges.registry import CHALLENGE_REGISTRY
from server.app.trace_codec import to_json_safe


router = APIRouter()


class PracticeExportEntry(BaseModel):
    id: str
    path: list[str] = Field(default_factory=list)
    n: Optional[int] = None
    seed: Optional[int] = None
    filename_prefix: Optional[str] = None
    test_count: Optional[int] = Field(None, ge=1, le=9)


class PracticeBundleRequest(BaseModel):
    entries: list[PracticeExportEntry]
    n: int = Field(16, ge=2, le=100)
    seed: Optional[int] = None
    test_count: int = Field(3, ge=1, le=9)


@router.get("/practice-export/challenges/{challenge_id}")
def export_challenge(
    challenge_id: str,
    n: int = Query(16, ge=2, le=100),
    seed: Optional[int] = Query(1),
    filename_prefix: Optional[str] = Query(None),
    test_count: int = Query(3, ge=1, le=9),
) -> Response:
    source, filename = generate_practice_file(
        challenge_id,
        n=n,
        seed=seed,
        filename_prefix=filename_prefix,
        test_count=test_count,
    )
    return Response(
        content=source,
        media_type="text/x-python; charset=utf-8",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )


@router.post("/practice-export/bundle")
def export_bundle(body: PracticeBundleRequest) -> Response:
    if not body.entries:
        raise HTTPException(status_code=400, detail="No challenges selected for export.")

    buffer = io.BytesIO()
    used_paths: set[str] = set()
    with zipfile.ZipFile(buffer, mode="w", compression=zipfile.ZIP_DEFLATED) as archive:
        for entry in body.entries:
            source, filename = generate_practice_file(
                entry.id,
                n=entry.n or body.n,
                seed=entry.seed if entry.seed is not None else body.seed,
                filename_prefix=entry.filename_prefix,
                test_count=entry.test_count or body.test_count,
            )
            parts = [_safe_filename(part) for part in entry.path if part.strip()]
            relative = "/".join([*parts, filename]) if parts else filename
            relative = _dedupe_zip_path(relative, used_paths)
            archive.writestr(relative, source)

    return Response(
        content=buffer.getvalue(),
        media_type="application/zip",
        headers={"Content-Disposition": 'attachment; filename="coden-practice-export.zip"'},
    )


def generate_practice_file(
    challenge_id: str,
    *,
    n: int,
    seed: Optional[int],
    filename_prefix: Optional[str] = None,
    test_count: int = 3,
) -> tuple[str, str]:
    cls = CHALLENGE_REGISTRY.get(challenge_id)
    if cls is None:
        raise HTTPException(status_code=404, detail=f"Challenge '{challenge_id}' not found.")

    challenge = cls()
    spec = getattr(challenge, "_spec", None)
    if spec is None:
        raise HTTPException(status_code=404, detail=f"Challenge '{challenge_id}' cannot be exported.")

    n = max(2, min(int(n), challenge.max_n))
    test_count = max(1, min(9, int(test_count)))
    cases = _generated_cases(challenge_id, cls, n=n, seed=seed, count=test_count)
    filename = f"{_safe_filename(spec.name)}.py"
    if filename_prefix:
        filename = f"{_safe_filename(filename_prefix)} {filename}"
    if challenge_id.startswith("cc_"):
        return _codechef_file(challenge_id, spec, n, seed, cases), filename
    return _function_file(challenge_id, spec, n, seed, cases), filename


def _generated_cases(
    challenge_id: str,
    cls,
    *,
    n: int,
    seed: Optional[int],
    count: int,
) -> list[dict[str, Any]]:
    cases: list[dict[str, Any]] = []
    for index in range(count):
        case_seed = None if seed is None else seed + index
        challenge = cls()
        try:
            setup = challenge.setup(n, case_seed)
        except (Exception, SystemExit):
            setup = _fallback_setup(challenge, challenge_id, index)
        if challenge_id.startswith("cc_"):
            expected = getattr(challenge, "_expected_output", None)
            if expected is None:
                expected = _fallback_expected_stdout(challenge, index)
            cases.append({
                "name": f"case {index + 1}",
                "stdin": str(setup.get("input_data") or ""),
                "expected_stdout": str(expected).strip(),
                "n": n,
                "seed": case_seed,
            })
            continue

        try:
            expected_value = challenge._reference_solve(**copy.deepcopy(setup))
        except Exception:
            expected_value = None
        cases.append({
            "name": f"case {index + 1}",
            "input": to_json_safe(setup),
            "expected": to_json_safe(expected_value),
            "n": n,
            "seed": case_seed,
        })
    return cases


def _fallback_setup(challenge, challenge_id: str, index: int) -> dict[str, Any]:
    if challenge_id.startswith("cc_"):
        samples = list(getattr(getattr(challenge, "_spec", None), "samples", []) or [])
        if samples:
            return {"input_data": str(samples[index % len(samples)].input_repr or "")}
        return {"input_data": ""}
    return {}


def _fallback_expected_stdout(challenge, index: int) -> str:
    samples = list(getattr(getattr(challenge, "_spec", None), "samples", []) or [])
    if not samples:
        return ""
    return str(samples[index % len(samples)].output_repr or "").strip()


def _function_file(challenge_id: str, spec, n: int, seed: Optional[int], cases: list[dict[str, Any]]) -> str:
    signature = ", ".join(spec.params)
    call_args = ", ".join(f"{param}=inputs[{json.dumps(param)}]" for param in spec.params)
    description = _doc_text(spec.description)
    return f'''"""
{spec.name}
{'=' * len(spec.name)}

Challenge id: {challenge_id}
Generated n: {n}
Generated seed: {seed}

{description}

This file is standalone. It contains generated tests and a runner, but no
cOde(n) imports, no optimal solution, and no complexity checks.
"""

from __future__ import annotations

import copy
import json


TEST_CASES = {json.dumps(cases, indent=2, ensure_ascii=False)}


def solve({signature}):
    """Write your solution here."""
    raise NotImplementedError("Implement solve(...)")


def _normalise(value):
    if isinstance(value, tuple):
        return [_normalise(item) for item in value]
    if isinstance(value, list):
        return [_normalise(item) for item in value]
    if isinstance(value, set):
        return sorted(_normalise(item) for item in value)
    if isinstance(value, dict):
        return {{str(key): _normalise(val) for key, val in value.items()}}
    return value


def _run_case(case):
    inputs = copy.deepcopy(case["input"])
    return solve({call_args})


def main():
    passed = 0
    for index, case in enumerate(TEST_CASES, start=1):
        try:
            actual = _run_case(case)
            ok = _normalise(actual) == _normalise(case["expected"])
        except Exception as exc:
            ok = False
            actual = f"{{type(exc).__name__}}: {{exc}}"

        status = "PASS" if ok else "FAIL"
        print(f"[{{status}}] {{index}}. {{case['name']}}")
        if not ok:
            print("  input:")
            print(json.dumps(case["input"], indent=2, ensure_ascii=False))
            print("  expected:")
            print(json.dumps(case["expected"], indent=2, ensure_ascii=False))
            print("  actual:")
            print(json.dumps(_normalise(actual), indent=2, ensure_ascii=False))
        passed += int(ok)

    print(f"\\n{{passed}}/{{len(TEST_CASES)}} test cases passed")
    raise SystemExit(0 if passed == len(TEST_CASES) else 1)


if __name__ == "__main__":
    main()
'''


def _codechef_file(challenge_id: str, spec, n: int, seed: Optional[int], cases: list[dict[str, Any]]) -> str:
    description = _doc_text(spec.description)
    return f'''"""
{spec.name}
{'=' * len(spec.name)}

Challenge id: {challenge_id}
Generated n: {n}
Generated seed: {seed}

{description}

This file is standalone. It contains generated stdin/stdout tests and a runner,
but no cOde(n) imports, no optimal solution, and no complexity checks.
"""

from __future__ import annotations

import contextlib
import io
import json
import sys


TEST_CASES = {json.dumps(cases, indent=2, ensure_ascii=False)}


def solve():
    """Write your CodeChef-style solution here.

    Use input() to read from stdin and print() to write the answer.
    """
    raise NotImplementedError("Implement solve()")


def _run_case(case):
    old_stdin = sys.stdin
    capture = io.StringIO()
    try:
        sys.stdin = io.StringIO(case["stdin"])
        with contextlib.redirect_stdout(capture):
            solve()
    finally:
        sys.stdin = old_stdin
    return capture.getvalue().strip()


def main():
    passed = 0
    for index, case in enumerate(TEST_CASES, start=1):
        try:
            actual = _run_case(case)
            ok = actual.strip() == case["expected_stdout"].strip()
        except Exception as exc:
            ok = False
            actual = f"{{type(exc).__name__}}: {{exc}}"

        status = "PASS" if ok else "FAIL"
        print(f"[{{status}}] {{index}}. {{case['name']}}")
        if not ok:
            print("  stdin:")
            print(case["stdin"])
            print("  expected stdout:")
            print(case["expected_stdout"])
            print("  actual stdout:")
            print(actual)
        passed += int(ok)

    print(f"\\n{{passed}}/{{len(TEST_CASES)}} test cases passed")
    raise SystemExit(0 if passed == len(TEST_CASES) else 1)


if __name__ == "__main__":
    main()
'''


def _doc_text(value: str, limit: int = 1800) -> str:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    if len(text) > limit:
        return text[: limit - 1].rstrip() + "…"
    return text


def _safe_filename(value: str) -> str:
    cleaned = re.sub(r'[<>:"/\\\\|?*]+', " ", str(value or "")).strip()
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned or "challenge"


def _dedupe_zip_path(path: str, used: set[str]) -> str:
    if path not in used:
        used.add(path)
        return path
    stem, dot, suffix = path.rpartition(".")
    if not dot:
        stem, suffix = path, ""
    else:
        suffix = f".{suffix}"
    index = 2
    while True:
        candidate = f"{stem} ({index}){suffix}"
        if candidate not in used:
            used.add(candidate)
            return candidate
        index += 1
