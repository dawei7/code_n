"""Report completion status for the local LeetCode docs dataset."""

from __future__ import annotations

import json
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"
REPORT_PATH = LEETCODE_ROOT / "_reports" / "_completion_report.json"

PLACEHOLDER_MARKERS = (
    "Write an original local summary",
    "TODO",
)
LOCAL_SOURCE_MARKER = "| Local Source |"
REQUIRED_SECTIONS = (
    "## Problem Description",
    "### Goal",
    "### Function Contract",
    "### Examples",
)
APPROACH_HEADINGS = ("General", "Complexity detail", "Alternatives and edge cases")


def is_doc(path: Path) -> bool:
    return path.name == "doc.md"


def classify(path: Path) -> dict[str, str | bool]:
    text = path.read_text(encoding="utf-8")
    package = path.parent
    approach_path = package / "variants" / "optimal" / "approach.md"
    approach = approach_path.read_text(encoding="utf-8") if approach_path.is_file() else ""
    manifest_path = package / "solution_variants.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        manifest = {}
    rows = manifest.get("variants") if isinstance(manifest, dict) else []
    valid_rows = rows if isinstance(rows, list) else []
    optimal = next(
        (
            row
            for row in valid_rows
            if isinstance(row, dict) and row.get("id") == "optimal"
        ),
        {},
    )
    time_complexity = str(optimal.get("time_complexity") or "")
    space_complexity = str(optimal.get("space_complexity") or "")
    approach_headings = tuple(
        re.findall(r"^##\s+(.+?)\s*$", approach, flags=re.MULTILINE)
    )
    has_placeholder = (
        any(marker in text or marker in approach for marker in PLACEHOLDER_MARKERS)
        or time_complexity == "O(...)"
        or space_complexity == "O(...)"
    )
    has_required_sections = all(section in text for section in REQUIRED_SECTIONS)
    has_variant_artifacts = (
        isinstance(optimal, dict)
        and time_complexity.startswith("O")
        and space_complexity.startswith("O")
        and approach_headings == APPROACH_HEADINGS
        and "### Required Complexity" not in text
        and "<summary>Approach</summary>" not in text
    )
    from_local_spec = LOCAL_SOURCE_MARKER in text
    if has_placeholder:
        status = "needs_authoring"
    elif has_required_sections and has_variant_artifacts and from_local_spec:
        status = "materialized_from_local_spec"
    elif has_required_sections and has_variant_artifacts:
        status = "manual_complete"
    else:
        status = "needs_authoring"
    return {
        "path": str(path.relative_to(REPO_ROOT)).replace("\\", "/"),
        "status": status,
        "has_placeholder": has_placeholder,
        "has_required_sections": has_required_sections,
        "has_variant_artifacts": has_variant_artifacts,
        "from_local_spec": from_local_spec,
    }


def main() -> int:
    entries = [classify(path) for path in sorted(LEETCODE_ROOT.glob("*/doc.md")) if is_doc(path)]
    counts: dict[str, int] = {}
    for entry in entries:
        status = str(entry["status"])
        counts[status] = counts.get(status, 0) + 1

    report = {
        "total_docs": len(entries),
        "counts": counts,
        "entries": entries,
    }
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"total_docs": len(entries), "counts": counts}, indent=2))
    print(f"Wrote {REPORT_PATH.relative_to(REPO_ROOT)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
