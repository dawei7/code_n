"""Report completion status for the local LeetCode docs dataset."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

try:
    from tools.leetcode_source_fidelity import validate_source_fidelity
    from tools.leetcode_solution_quality import validate_solution_quality
except ModuleNotFoundError:  # Direct ``python tools/check_leetcode_dataset.py`` use.
    from leetcode_source_fidelity import validate_source_fidelity
    from leetcode_solution_quality import validate_solution_quality

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


def classify(path: Path, *, check_cases: bool = True) -> dict[str, object]:
    package = path.parent
    reference_dir = package / "reference"
    uses_reference_sections = reference_dir.is_dir()
    source_fidelity = validate_source_fidelity(package)
    solution_quality = validate_solution_quality(package, check_cases=check_cases)
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
            text = "\n\n".join(section.read_text(encoding="utf-8") for section in section_paths)
            has_required_sections = all(
                required in filenames for required in ("description.md", "contract.md", "examples.md")
            )
        else:
            text = path.read_text(encoding="utf-8")
            has_required_sections = False
    else:
        section_paths = tuple(reference_dir / filename for filename, _heading in REFERENCE_SECTIONS)
        sections_complete = uses_reference_sections and all(section.is_file() for section in section_paths)
        if sections_complete:
            section_texts = tuple(section.read_text(encoding="utf-8") for section in section_paths)
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
            has_required_sections = not uses_reference_sections and all(
                section in text for section in REQUIRED_SECTIONS
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
        (row for row in valid_rows if isinstance(row, dict) and row.get("id") == "optimal"),
        {},
    )
    time_complexity = str(optimal.get("time_complexity") or "")
    space_complexity = str(optimal.get("space_complexity") or "")
    approach_headings = tuple(re.findall(r"^##\s+(.+?)\s*$", approach, flags=re.MULTILINE))
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
        "solution_quality_status": solution_quality.solution_status,
        "case_quality_status": solution_quality.case_status,
    }
    if source_fidelity.errors:
        result["source_fidelity_errors"] = list(source_fidelity.errors)
    if uses_reference_sections:
        result["uses_reference_sections"] = True
    if solution_quality.verdict:
        result["solution_quality_verdict"] = solution_quality.verdict
        result["solution_quality_target"] = solution_quality.target
    if solution_quality.review_scope:
        result["solution_quality_review_scope"] = solution_quality.review_scope
    if solution_quality.candidate_path:
        result["candidate_path"] = str(package.relative_to(REPO_ROOT) / solution_quality.candidate_path).replace(
            "\\", "/"
        )
    if solution_quality.findings:
        result["solution_quality_findings"] = list(solution_quality.findings)
    if solution_quality.errors:
        result["solution_quality_errors"] = list(solution_quality.errors)
    return result


def _review_pointer(entry: dict[str, object] | None) -> dict[str, object] | None:
    if entry is None:
        return None
    path = Path(str(entry["path"]))
    package_name = path.parent.name
    prefix, _, slug = package_name.partition("_")
    return {
        "frontend_id": int(prefix),
        "slug": slug,
        "package": str(path.parent).replace("\\", "/"),
    }


def build_report(entries: list[dict[str, object]]) -> dict[str, object]:
    counts: dict[str, int] = {}
    source_fidelity_counts: dict[str, int] = {}
    solution_quality_counts: dict[str, int] = {}
    case_quality_counts: dict[str, int] = {}
    solution_quality_verdict_counts: dict[str, int] = {}
    for entry in entries:
        status = str(entry["status"])
        counts[status] = counts.get(status, 0) + 1
        fidelity_status = str(entry["source_fidelity_status"])
        source_fidelity_counts[fidelity_status] = source_fidelity_counts.get(fidelity_status, 0) + 1
        solution_status = str(entry["solution_quality_status"])
        solution_quality_counts[solution_status] = solution_quality_counts.get(solution_status, 0) + 1
        case_status = str(entry["case_quality_status"])
        case_quality_counts[case_status] = case_quality_counts.get(case_status, 0) + 1
        verdict = str(entry.get("solution_quality_verdict") or "")
        if verdict:
            solution_quality_verdict_counts[verdict] = solution_quality_verdict_counts.get(verdict, 0) + 1

    first_incomplete_solution = next(
        (entry for entry in entries if entry["solution_quality_status"] != "complete"),
        None,
    )
    first_incomplete_cases = next(
        (entry for entry in entries if entry["case_quality_status"] != "complete"),
        None,
    )

    return {
        "total_docs": len(entries),
        "counts": counts,
        "source_fidelity_counts": source_fidelity_counts,
        "solution_quality_counts": solution_quality_counts,
        "case_quality_counts": case_quality_counts,
        "solution_quality_verdict_counts": solution_quality_verdict_counts,
        "first_incomplete_solution_quality": _review_pointer(first_incomplete_solution),
        "first_incomplete_case_quality": _review_pointer(first_incomplete_cases),
        "entries": entries,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--solution-only",
        action="store_true",
        help="regenerate solution-quality status without reading or validating cases.json",
    )
    args = parser.parse_args()
    entries = [
        classify(path, check_cases=not args.solution_only)
        for path in sorted(LEETCODE_ROOT.glob("*/doc.md"))
        if is_doc(path)
    ]
    report = build_report(entries)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "total_docs": len(entries),
                "counts": report["counts"],
                "source_fidelity_counts": report["source_fidelity_counts"],
                "solution_quality_counts": report["solution_quality_counts"],
                "case_quality_counts": report["case_quality_counts"],
                "solution_quality_verdict_counts": report["solution_quality_verdict_counts"],
                "first_incomplete_solution_quality": report["first_incomplete_solution_quality"],
                "first_incomplete_case_quality": report["first_incomplete_case_quality"],
            },
            indent=2,
        )
    )
    print(f"Wrote {REPORT_PATH.relative_to(REPO_ROOT)}.")
    has_invalid_review = any(
        counts.get(status)
        for counts in (report["solution_quality_counts"], report["case_quality_counts"])
        for status in ("invalid", "stale")
    )
    return 1 if report["source_fidelity_counts"].get("invalid") or has_invalid_review else 0


if __name__ == "__main__":
    raise SystemExit(main())
