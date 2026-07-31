"""Report completion status for the local LeetCode docs dataset."""

from __future__ import annotations

import json
import re
from pathlib import Path

try:
    from tools.leetcode_source_fidelity import validate_source_fidelity
except ModuleNotFoundError:  # Direct ``python tools/check_leetcode_dataset.py`` use.
    from leetcode_source_fidelity import validate_source_fidelity


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
REFERENCE_SECTIONS = (
    ("description.md", "## Description"),
    ("contract.md", "## Function Contract"),
    ("examples.md", "## Examples"),
    ("constraints.md", "## Constraints"),
)
APPROACH_HEADINGS = ("General", "Complexity detail", "Alternatives and edge cases")


def is_doc(path: Path) -> bool:
    return path.name == "doc.md"


def classify(path: Path) -> dict[str, object]:
    package = path.parent
    reference_dir = package / "reference"
    uses_reference_sections = reference_dir.is_dir()
    source_fidelity = validate_source_fidelity(package)
    if uses_reference_sections and source_fidelity.verified:
        manifest = json.loads((package / "source_fidelity.json").read_text(encoding="utf-8"))
        source_sections = manifest["structure"]["sections"]
        filenames: list[str] = []
        for section in source_sections:
            filenames.append(f"{section}.md")
            if section == "description":
                filenames.append("contract.md")
        section_paths = tuple(reference_dir / filename for filename in filenames)
        sections_complete = all(section.is_file() for section in section_paths)
        if sections_complete:
            text = "\n\n".join(
                section.read_text(encoding="utf-8") for section in section_paths
            )
            has_required_sections = all(
                required in filenames
                for required in ("description.md", "contract.md", "examples.md")
            )
        else:
            text = path.read_text(encoding="utf-8")
            has_required_sections = False
    else:
        section_paths = tuple(
            reference_dir / filename for filename, _heading in REFERENCE_SECTIONS
        )
        sections_complete = uses_reference_sections and all(
            section.is_file() for section in section_paths
        )
        if sections_complete:
            section_texts = tuple(
                section.read_text(encoding="utf-8") for section in section_paths
            )
            text = "\n\n".join(section_texts)
            has_required_sections = all(
                section_text.lstrip().startswith(heading)
                for section_text, (_filename, heading) in zip(
                    section_texts,
                    REFERENCE_SECTIONS,
                    strict=True,
                )
            )
        else:
            text = path.read_text(encoding="utf-8")
            has_required_sections = (
                not uses_reference_sections
                and all(section in text for section in REQUIRED_SECTIONS)
            )
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
    result: dict[str, object] = {
        "path": str(path.relative_to(REPO_ROOT)).replace("\\", "/"),
        "status": status,
        "has_placeholder": has_placeholder,
        "has_required_sections": has_required_sections,
        "has_variant_artifacts": has_variant_artifacts,
        "from_local_spec": from_local_spec,
        "source_fidelity_status": source_fidelity.status,
    }
    if source_fidelity.errors:
        result["source_fidelity_errors"] = list(source_fidelity.errors)
    if uses_reference_sections:
        result["uses_reference_sections"] = True
    return result


def main() -> int:
    entries = [classify(path) for path in sorted(LEETCODE_ROOT.glob("*/doc.md")) if is_doc(path)]
    counts: dict[str, int] = {}
    source_fidelity_counts: dict[str, int] = {}
    for entry in entries:
        status = str(entry["status"])
        counts[status] = counts.get(status, 0) + 1
        fidelity_status = str(entry["source_fidelity_status"])
        source_fidelity_counts[fidelity_status] = (
            source_fidelity_counts.get(fidelity_status, 0) + 1
        )

    report = {
        "total_docs": len(entries),
        "counts": counts,
        "source_fidelity_counts": source_fidelity_counts,
        "entries": entries,
    }
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "total_docs": len(entries),
                "counts": counts,
                "source_fidelity_counts": source_fidelity_counts,
            },
            indent=2,
        )
    )
    print(f"Wrote {REPORT_PATH.relative_to(REPO_ROOT)}.")
    return 1 if source_fidelity_counts.get("invalid") else 0


if __name__ == "__main__":
    raise SystemExit(main())
