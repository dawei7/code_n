"""Standalone practice-file export.

The exported files are intentionally dependency-free: they contain a user
``solve`` stub, authored validated test cases, and a tiny local runner. They do not
include cOde(n)'s optimal source or complexity checks.
"""
from __future__ import annotations

import io
import json
import pprint
import re
import zipfile
from typing import Any, Optional

from fastapi import APIRouter, HTTPException, Query, Response
from pydantic import BaseModel, Field

from challenges.registry import CHALLENGE_REGISTRY
from server.app.trace_codec import to_json_safe
from server.app.validated_cases import NoValidatedCases, ValidatedCase, load_case_suite


router = APIRouter()


class PracticeExportEntry(BaseModel):
    id: str
    path: list[str] = Field(default_factory=list)
    filename_prefix: Optional[str] = None


class PracticeBundleRequest(BaseModel):
    entries: list[PracticeExportEntry]


@router.get("/practice-export/challenges/{challenge_id}")
def export_challenge(
    challenge_id: str,
    filename_prefix: Optional[str] = Query(None),
) -> Response:
    source, filename = generate_practice_file(
        challenge_id,
        filename_prefix=filename_prefix,
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
                filename_prefix=entry.filename_prefix,
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
    filename_prefix: Optional[str] = None,
) -> tuple[str, str]:
    cls = CHALLENGE_REGISTRY.get(challenge_id)
    if cls is None:
        raise HTTPException(status_code=404, detail=f"Challenge '{challenge_id}' not found.")

    challenge = cls()
    spec = getattr(challenge, "_spec", None)
    if spec is None:
        raise HTTPException(status_code=404, detail=f"Challenge '{challenge_id}' cannot be exported.")

    cases = _validated_export_cases(challenge_id)
    filename = f"{_safe_filename(spec.name)}.py"
    if filename_prefix:
        filename = f"{_safe_filename(filename_prefix)} {filename}"
    return _function_file(challenge_id, spec, cases), filename


def _validated_export_cases(challenge_id: str) -> list[dict[str, Any]]:
    try:
        suite = load_case_suite(challenge_id)
    except NoValidatedCases as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    export_cases = [case for case in suite if case.kind != "benchmark"]
    if not export_cases:
        raise HTTPException(
            status_code=422,
            detail=f"{challenge_id} has no authored non-benchmark cases to export.",
        )
    return [_export_case(case) for case in export_cases]


def _export_case(case: ValidatedCase) -> dict[str, Any]:
    base = {
        "id": case.id,
        "name": case.name,
        "kind": case.kind,
        "visible": case.visible,
        "tags": list(case.tags),
    }
    return {
        **base,
        "input": to_json_safe(case.input),
        "expected": to_json_safe(case.expected),
    }


def _function_file(challenge_id: str, spec, cases: list[dict[str, Any]]) -> str:
    signature = ", ".join(spec.params)
    call_args = ", ".join(f"{param}=inputs[{json.dumps(param)}]" for param in spec.params)
    description = _doc_text(spec.description)
    return f'''"""
{spec.name}
{'=' * len(spec.name)}

Challenge id: {challenge_id}
Validated cases: {len(cases)}

{description}

This file is standalone. It contains authored validated tests and a runner, but no
cOde(n) imports, no optimal solution, and no complexity checks.
"""

from __future__ import annotations

import copy
import json


TEST_CASES = {_python_literal(cases)}


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

def _doc_text(value: str, limit: int = 1800) -> str:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    if len(text) > limit:
        return text[: limit - 1].rstrip() + "…"
    return text


def _python_literal(value: Any) -> str:
    return pprint.pformat(value, width=100, sort_dicts=False)


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
