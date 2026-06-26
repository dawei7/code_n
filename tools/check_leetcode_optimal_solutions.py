"""Report LeetCode docs that do or do not have organized optimal solutions."""

from __future__ import annotations

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_ROOT = REPO_ROOT / "docs" / "algorithms" / "leetcode"
OPTIMAL_ROOT = REPO_ROOT / "optimal_solutions" / "leetcode"
REPORT_PATH = OPTIMAL_ROOT / "_completion_report.json"
DOC_COMPLETION_REPORT = DOCS_ROOT / "_completion_report.json"

READY_STATUSES = {"manual_complete", "materialized_from_local_spec"}


def solution_path_for_doc(doc_path: Path) -> Path:
    return (OPTIMAL_ROOT / doc_path.relative_to(DOCS_ROOT)).with_suffix(".py")


def load_ready_docs() -> list[Path]:
    if DOC_COMPLETION_REPORT.exists():
        report = json.loads(DOC_COMPLETION_REPORT.read_text(encoding="utf-8"))
        paths = []
        for entry in report["entries"]:
            if entry["status"] in READY_STATUSES:
                paths.append(REPO_ROOT / entry["path"])
        return sorted(paths)

    return sorted(
        path
        for path in DOCS_ROOT.rglob("*.md")
        if path.name not in {"README.md", "_template.md"} and not path.stem.endswith("_de")
    )


def main() -> int:
    ready_docs = load_ready_docs()
    entries = []
    counts = {"has_optimal": 0, "missing_optimal": 0}
    for doc_path in ready_docs:
        solution_path = solution_path_for_doc(doc_path)
        has_optimal = solution_path.exists()
        status = "has_optimal" if has_optimal else "missing_optimal"
        counts[status] += 1
        entries.append(
            {
                "doc_path": str(doc_path.relative_to(REPO_ROOT)).replace("\\", "/"),
                "solution_path": str(solution_path.relative_to(REPO_ROOT)).replace("\\", "/"),
                "status": status,
            }
        )

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(
        json.dumps(
            {
                "total_ready_docs": len(ready_docs),
                "counts": counts,
                "entries": entries,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"total_ready_docs": len(ready_docs), "counts": counts}, indent=2))
    print(f"Wrote {REPORT_PATH.relative_to(REPO_ROOT)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
