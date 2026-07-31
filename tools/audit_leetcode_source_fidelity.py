"""Audit statement fidelity separately from package completion.

This local audit does not infer fidelity from prose shape. A package is only
verified when its reviewed ``source_fidelity.json`` manifest passes validation.
The structural snapshot is triage evidence for the next review batch.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

try:
    from tools.leetcode_source_fidelity import (
        local_structure_snapshot,
        validate_source_fidelity,
    )
except ModuleNotFoundError:  # Direct ``python tools/audit_*.py`` use.
    from leetcode_source_fidelity import (
        local_structure_snapshot,
        validate_source_fidelity,
    )


REPO_ROOT = Path(__file__).resolve().parents[1]
LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"
REPORT_PATH = LEETCODE_ROOT / "_reports" / "_source_fidelity_report.json"


def _frontend_id(package: Path) -> int | None:
    match = re.match(r"^(\d+)_", package.name)
    return int(match.group(1)) if match else None


def audit(max_frontend_id: int) -> dict[str, object]:
    packages = sorted(
        package
        for package in LEETCODE_ROOT.iterdir()
        if package.is_dir()
        and (package / "metadata.json").is_file()
        and (_frontend_id(package) or max_frontend_id + 1) <= max_frontend_id
    )
    counts = {"verified": 0, "unverified": 0, "invalid": 0}
    triage = {
        "without_constraints_section": 0,
        "without_marked_example_explanations": 0,
        "with_exactly_three_examples": 0,
        "with_local_images": 0,
        "with_non_metadata_tables": 0,
        "with_local_diagrams": 0,
    }
    entries: list[dict[str, object]] = []
    for package in packages:
        status = validate_source_fidelity(package)
        counts[status.status] += 1
        snapshot = local_structure_snapshot(package)
        if not snapshot["has_constraints"]:
            triage["without_constraints_section"] += 1
        if snapshot["explained_example_count"] == 0:
            triage["without_marked_example_explanations"] += 1
        if snapshot["example_count"] == 3:
            triage["with_exactly_three_examples"] += 1
        if snapshot["image_count"]:
            triage["with_local_images"] += 1
        if snapshot["table_count"]:
            triage["with_non_metadata_tables"] += 1
        if snapshot["diagram_count"]:
            triage["with_local_diagrams"] += 1
        entry: dict[str, object] = {
            "frontend_id": _frontend_id(package),
            "package": str(package.relative_to(REPO_ROOT)).replace("\\", "/"),
            "status": status.status,
            "local_structure": snapshot,
        }
        if status.errors:
            entry["errors"] = list(status.errors)
        entries.append(entry)
    return {
        "scope": {
            "frontend_id_max": max_frontend_id,
            "package_count": len(packages),
        },
        "counts": counts,
        "triage": triage,
        "meaning": {
            "verified": "reviewed against a hashed live source and structurally validated",
            "unverified": "package may be complete, but source fidelity has not been reviewed",
            "invalid": "a claimed review manifest is inconsistent with its package",
        },
        "entries": entries,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--max-frontend-id",
        type=int,
        default=500,
        help="Audit the first review batch through this frontend id (default: 500)",
    )
    args = parser.parse_args()
    if args.max_frontend_id < 1:
        parser.error("--max-frontend-id must be positive")

    report = audit(args.max_frontend_id)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "scope": report["scope"],
                "counts": report["counts"],
                "triage": report["triage"],
            },
            indent=2,
        )
    )
    print(f"Wrote {REPORT_PATH.relative_to(REPO_ROOT)}.")
    return 1 if report["counts"]["invalid"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
