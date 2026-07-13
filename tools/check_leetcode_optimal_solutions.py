"""Report LeetCode challenge packages with or without Python optimal solutions."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"
REPORT_PATH = LEETCODE_ROOT / "_reports" / "python_optimal_completion_report.json"

def solution_path_for_doc(doc_path: Path) -> Path:
    return doc_path.parent / "solutions" / "python.py"


def load_package_metadata(doc_path: Path) -> dict[str, Any]:
    metadata_path = doc_path.parent / "metadata.json"
    if not metadata_path.is_file():
        return {}
    try:
        payload = json.loads(metadata_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return payload if isinstance(payload, dict) else {}


def python_optimal_applicable(metadata: dict[str, Any]) -> bool:
    languages = metadata.get("supported_languages")
    if not isinstance(languages, list):
        return True
    return bool(metadata.get("runnable_in_coden")) and "python" in languages


def load_doc_statuses() -> dict[str, str]:
    doc_completion_report = LEETCODE_ROOT / "_reports" / "_completion_report.json"
    if doc_completion_report.exists():
        try:
            report = json.loads(doc_completion_report.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return {}
        return {
            str(entry.get("path") or ""): str(entry.get("status") or "")
            for entry in report.get("entries", [])
            if isinstance(entry, dict)
        }
    return {}


def load_docs() -> list[Path]:
    return sorted(
        path
        for path in LEETCODE_ROOT.glob("*/doc.md")
    )


def main() -> int:
    docs = load_docs()
    doc_statuses = load_doc_statuses()
    entries = []
    counts = {
        "python_applicable": 0,
        "python_not_applicable": 0,
        "has_optimal": 0,
        "missing_optimal": 0,
        "not_applicable": 0,
    }
    for doc_path in docs:
        metadata = load_package_metadata(doc_path)
        solution_path = solution_path_for_doc(doc_path)
        applicable = python_optimal_applicable(metadata)
        has_optimal = applicable and solution_path.exists()
        if applicable:
            counts["python_applicable"] += 1
            status = "has_optimal" if has_optimal else "missing_optimal"
        else:
            counts["python_not_applicable"] += 1
            status = "not_applicable"
        counts[status] += 1
        entries.append(
            {
                "doc_path": str(doc_path.relative_to(REPO_ROOT)).replace("\\", "/"),
                "solution_path": str(solution_path.relative_to(REPO_ROOT)).replace("\\", "/"),
                "doc_status": doc_statuses.get(str(doc_path.relative_to(REPO_ROOT)).replace("\\", "/"), ""),
                "category": str(metadata.get("category") or ""),
                "category_title": str(metadata.get("category_title") or ""),
                "supported_languages": metadata.get("supported_languages") or [],
                "runnable_in_coden": bool(metadata.get("runnable_in_coden")),
                "python_optimal_applicable": applicable,
                "status": status,
            }
        )

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(
        json.dumps(
            {
                "total_docs": len(docs),
                "counts": counts,
                "entries": entries,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"total_docs": len(docs), "counts": counts}, indent=2))
    print(f"Wrote {REPORT_PATH.relative_to(REPO_ROOT)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
