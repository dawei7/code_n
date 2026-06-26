"""Report completion status for the local LeetCode docs dataset."""

from __future__ import annotations

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
LEETCODE_ROOT = REPO_ROOT / "docs" / "algorithms" / "leetcode"
REPORT_PATH = LEETCODE_ROOT / "_completion_report.json"

PLACEHOLDER_MARKERS = (
    "Write an original local summary",
    "TODO",
)
LOCAL_SOURCE_MARKER = "| Local Source |"
REQUIRED_SECTIONS = (
    "## Problem Description & Examples",
    "## Underlying Base Algorithm(s)",
    "## Complexity Analysis",
)


def is_doc(path: Path) -> bool:
    return path.suffix == ".md" and path.name not in {"README.md", "_template.md"}


def classify(path: Path) -> dict[str, str | bool]:
    text = path.read_text(encoding="utf-8")
    has_placeholder = any(marker in text for marker in PLACEHOLDER_MARKERS)
    has_required_sections = all(section in text for section in REQUIRED_SECTIONS)
    from_local_spec = LOCAL_SOURCE_MARKER in text
    if has_placeholder:
        status = "needs_authoring"
    elif has_required_sections and from_local_spec:
        status = "materialized_from_local_spec"
    elif has_required_sections:
        status = "manual_complete"
    else:
        status = "needs_authoring"
    return {
        "path": str(path.relative_to(REPO_ROOT)).replace("\\", "/"),
        "status": status,
        "has_placeholder": has_placeholder,
        "has_required_sections": has_required_sections,
        "from_local_spec": from_local_spec,
    }


def main() -> int:
    entries = [classify(path) for path in sorted(LEETCODE_ROOT.rglob("*.md")) if is_doc(path)]
    counts: dict[str, int] = {}
    for entry in entries:
        status = str(entry["status"])
        counts[status] = counts.get(status, 0) + 1

    report = {
        "total_docs": len(entries),
        "counts": counts,
        "entries": entries,
    }
    REPORT_PATH.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"total_docs": len(entries), "counts": counts}, indent=2))
    print(f"Wrote {REPORT_PATH.relative_to(REPO_ROOT)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
