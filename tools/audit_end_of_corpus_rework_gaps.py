"""Generate the deferred end-of-corpus LeetCode rework inventory.

The verified-solution queue intentionally stays ahead of legacy Reference
rework. This report makes every deferred package-level gap explicit so the
cleanup pass can begin from live audit evidence after frontend ID 4005.
"""

from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.audit_leetcode_migration import build_report  # noqa: E402
from tools.audit_leetcode_source_fidelity import audit as audit_fidelity  # noqa: E402


CORPUS_CEILING = 4005
REPORT_ROOT = REPO_ROOT / "dsa" / "leetcode" / "_reports"
JSON_PATH = REPORT_ROOT / "END_OF_CORPUS_REWORK_GAPS.json"
MARKDOWN_PATH = REPORT_ROOT / "END_OF_CORPUS_REWORK_GAPS.md"

COMPLETION_GATES = (
    "doc",
    "cases",
    "complexity",
    "solution_variants",
    "optimal_solution",
    "leetcode_submission",
)

KNOWN_REGRESSION_GROUPS = (
    {
        "category": "generic_certificate_route_has_no_python_or_sql_reference",
        "frontend_ids": (
            2648,
            2649,
            2650,
            2665,
            2666,
            2667,
            2676,
            2690,
            2803,
            2804,
            2805,
            2821,
        ),
        "last_observed": "2026-07-29",
        "detail": (
            "The repository-wide certificate real-test sweep selects only a "
            "Python or SQL app-local reference. These packages currently expose "
            "another runtime shape or lack that selectable reference, so their "
            "subtests fail before certificate behavior can be proven."
        ),
    },
    {
        "category": "certificate_route_not_selected",
        "frontend_ids": (2670, 3285),
        "last_observed": "2026-07-29",
        "detail": (
            "The real-test request reaches runtime scaling instead of the package's "
            "verified non-scaling certificate path."
        ),
    },
    {
        "category": "reference_hits_python_step_cap",
        "frontend_ids": (3690,),
        "last_observed": "2026-07-29",
        "detail": (
            "The stored reference reaches the Python execution step cap in the "
            "repository-wide certificate real-test sweep."
        ),
    },
)


def _entry_id(entry: dict[str, Any]) -> int:
    return int(entry["frontend_id"])


def _missing_gates(entry: dict[str, Any]) -> list[str]:
    checks = entry["checks"]
    return [gate for gate in COMPLETION_GATES if not checks[gate]["complete"]]


def _active_entry(entry: dict[str, Any]) -> dict[str, Any]:
    checks = entry["checks"]
    return {
        "frontend_id": _entry_id(entry),
        "title": entry["title"],
        "package": entry["package"],
        "missing_gates": _missing_gates(entry),
        "doc": {
            "has_placeholder": checks["doc"]["has_placeholder"],
            "missing_sections": checks["doc"]["missing_sections"],
            "goal_word_count": checks["doc"]["goal_word_count"],
            "goal_minimum_words": checks["doc"]["goal_minimum_words"],
            "goal_paragraph_count": checks["doc"]["goal_paragraph_count"],
            "goal_minimum_paragraphs": checks["doc"]["goal_minimum_paragraphs"],
        },
        "case_count": checks["cases"]["total"],
        "complexity_method": checks["complexity"]["method"],
        "variant_errors": checks["solution_variants"]["errors"],
        "submission_status": checks["leetcode_submission"]["status"],
    }


def _documentation_entry(entry: dict[str, Any]) -> dict[str, Any]:
    doc = entry["checks"]["doc"]
    return {
        "frontend_id": _entry_id(entry),
        "title": entry["title"],
        "package": entry["package"],
        "missing_gates": _missing_gates(entry),
        "has_placeholder": doc["has_placeholder"],
        "missing_sections": doc["missing_sections"],
        "goal_narrative_complete": doc["goal_narrative_complete"],
        "goal_word_count": doc["goal_word_count"],
        "goal_minimum_words": doc["goal_minimum_words"],
        "goal_paragraph_count": doc["goal_paragraph_count"],
        "goal_minimum_paragraphs": doc["goal_minimum_paragraphs"],
        "uses_reference_sections": bool(doc.get("uses_reference_sections")),
    }


def _fidelity_entry(entry: dict[str, Any]) -> dict[str, Any]:
    status = str(entry["status"])
    return {
        "frontend_id": int(entry["frontend_id"]),
        "package": entry["package"],
        "status": status,
        "reason": (
            "source_fidelity.json is missing"
            if status == "unverified"
            else "source_fidelity.json is invalid"
        ),
        "errors": list(entry.get("errors", [])),
        "local_structure": entry["local_structure"],
    }


def _regression_entries(
    entries_by_id: dict[int, dict[str, Any]],
) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for group in KNOWN_REGRESSION_GROUPS:
        packages: list[dict[str, Any]] = []
        for frontend_id in group["frontend_ids"]:
            entry = entries_by_id[frontend_id]
            checks = entry["checks"]
            packages.append(
                {
                    "frontend_id": frontend_id,
                    "title": entry["title"],
                    "package": entry["package"],
                    "reference_language": checks["optimal_solution"]["language"],
                    "complexity_method": checks["complexity"]["method"],
                }
            )
        result.append(
            {
                "category": group["category"],
                "last_observed": group["last_observed"],
                "detail": group["detail"],
                "packages": packages,
            }
        )
    return result


def build_gap_report() -> dict[str, Any]:
    migration = build_report()
    fidelity = audit_fidelity(CORPUS_CEILING)
    migration_entries = sorted(migration["entries"], key=_entry_id)
    entries_by_id = {_entry_id(entry): entry for entry in migration_entries}

    active = [
        entry
        for entry in migration_entries
        if not entry["checks"]["leetcode_submission"]["complete"]
    ]
    deferred_docs = [
        entry
        for entry in migration_entries
        if entry["checks"]["leetcode_submission"]["complete"]
        and not entry["local_complete"]
    ]
    other_completion = [
        entry
        for entry in migration_entries
        if not entry["local_complete"]
        and entry not in active
        and entry not in deferred_docs
    ]

    fidelity_gaps = [
        _fidelity_entry(entry)
        for entry in fidelity["entries"]
        if entry["status"] != "verified"
    ]
    active_ids = {_entry_id(entry) for entry in active}
    deferred_doc_ids = {_entry_id(entry) for entry in deferred_docs}
    fidelity_ids = {entry["frontend_id"] for entry in fidelity_gaps}
    invalid_ids = {
        entry["frontend_id"]
        for entry in fidelity_gaps
        if entry["status"] == "invalid"
    }

    unverified_structures = [
        entry["local_structure"]
        for entry in fidelity_gaps
        if entry["status"] == "unverified"
    ]
    fidelity_triage = {
        "without_constraints_section": sum(
            not structure["has_constraints"] for structure in unverified_structures
        ),
        "without_marked_example_explanations": sum(
            structure["explained_example_count"] == 0
            for structure in unverified_structures
        ),
        "with_local_images": sum(
            structure["image_count"] > 0 for structure in unverified_structures
        ),
        "with_non_metadata_tables": sum(
            structure["table_count"] > 0 for structure in unverified_structures
        ),
        "with_local_diagrams": sum(
            structure["diagram_count"] > 0 for structure in unverified_structures
        ),
    }

    phase_order = (
        [
            "finish every remotely unverified Optimal submission through frontend ID 4005",
            "regenerate this inventory from the live worktree",
            "repair deferred documentation-completeness failures",
            "review every unverified or invalid source-fidelity manifest",
            "clear the repository-wide regression debt and rerun the full suite",
        ]
        if active
        else [
            "repair deferred documentation-completeness failures",
            "review every unverified or invalid source-fidelity manifest",
            "clear the repository-wide regression debt and rerun the full suite",
        ]
    )

    return {
        "schema_version": 1,
        "generated_on": date.today().isoformat(),
        "corpus_ceiling": CORPUS_CEILING,
        "phase_order": phase_order,
        "summary": {
            "packages": migration["counts"]["packages"],
            "fully_complete_and_remotely_verified": migration["counts"][
                "fully_complete_and_verified"
            ],
            "not_fully_complete": sum(
                not entry["local_complete"] for entry in migration_entries
            ),
            "active_verified_solution_queue": len(active),
            "deferred_documentation_only": len(deferred_docs),
            "other_completion_gaps": len(other_completion),
            "source_fidelity_verified": fidelity["counts"]["verified"],
            "source_fidelity_unverified": fidelity["counts"]["unverified"],
            "source_fidelity_invalid": fidelity["counts"]["invalid"],
            "known_regression_packages": sum(
                len(group["frontend_ids"]) for group in KNOWN_REGRESSION_GROUPS
            ),
        },
        "active_verified_solution_queue": [_active_entry(entry) for entry in active],
        "deferred_documentation_only": [
            _documentation_entry(entry) for entry in deferred_docs
        ],
        "other_completion_gaps": [
            {
                "frontend_id": _entry_id(entry),
                "title": entry["title"],
                "package": entry["package"],
                "missing_gates": _missing_gates(entry),
            }
            for entry in other_completion
        ],
        "source_fidelity": {
            "counts": fidelity["counts"],
            "unverified_triage_signals": fidelity_triage,
            "overlap": {
                "active_verified_solution_queue": len(fidelity_ids & active_ids),
                "deferred_documentation_only": len(fidelity_ids & deferred_doc_ids),
                "otherwise_locally_complete": len(
                    fidelity_ids - active_ids - deferred_doc_ids
                ),
                "invalid_manifest_ids": sorted(invalid_ids),
            },
            "entries": fidelity_gaps,
        },
        "known_repository_regressions": _regression_entries(entries_by_id),
    }


def _cell(value: object) -> str:
    if isinstance(value, list):
        text = ", ".join(str(item) for item in value) or "—"
    else:
        text = str(value)
    return text.replace("|", "\\|").replace("\n", " ")


def _markdown(report: dict[str, Any]) -> str:
    summary = report["summary"]
    source = report["source_fidelity"]
    lines = [
        "# End-of-Corpus Rework Gaps",
        "",
        f"Generated: {report['generated_on']}",
        "",
        (
            "This generated inventory records every known remaining package and "
            "repository gap. Regenerate it from the live worktree instead of "
            "hand-editing counts or package rows."
        ),
        "",
        "## Summary",
        "",
        "| Gap | Packages |",
        "|---|---:|",
        f"| Not fully complete | {summary['not_fully_complete']} |",
        (
            "| Active verified-solution queue | "
            f"{summary['active_verified_solution_queue']} |"
        ),
        (
            "| Deferred documentation-only failures | "
            f"{summary['deferred_documentation_only']} |"
        ),
        f"| Other completion failures | {summary['other_completion_gaps']} |",
        (
            "| Source-fidelity unverified | "
            f"{summary['source_fidelity_unverified']} |"
        ),
        f"| Source-fidelity invalid | {summary['source_fidelity_invalid']} |",
        (
            "| Known repository-regression packages | "
            f"{summary['known_regression_packages']} |"
        ),
        "",
        "## Required end-of-corpus order",
        "",
    ]
    lines.extend(
        f"{index}. {step}"
        for index, step in enumerate(report["phase_order"], start=1)
    )

    lines.extend(
        [
            "",
            "## Active verified-solution queue",
            "",
            (
                "These packages still lack a remotely verified Optimal submission. "
                "Their rows show every completion gate currently missing."
            ),
            "",
            "| ID | Title | Missing gates | Cases | Submission | Variant errors | Package |",
            "|---:|---|---|---:|---|---|---|",
        ]
    )
    for entry in report["active_verified_solution_queue"]:
        lines.append(
            "| {frontend_id} | {title} | {missing} | {cases} | {submission} | "
            "{errors} | `{package}` |".format(
                frontend_id=entry["frontend_id"],
                title=_cell(entry["title"]),
                missing=_cell(entry["missing_gates"]),
                cases=entry["case_count"],
                submission=_cell(entry["submission_status"]),
                errors=_cell(entry["variant_errors"]),
                package=entry["package"],
            )
        )

    lines.extend(
        [
            "",
            "## Deferred documentation-only failures",
            "",
            (
                "These packages already pass cases, complexity, variant, app-source, "
                "and remote-submission gates. Their only local-completion failure is "
                "the current narrative-depth requirement."
            ),
            "",
            "| ID | Title | Words | Required | Paragraphs | Required | Section mode | Package |",
            "|---:|---|---:|---:|---:|---:|---|---|",
        ]
    )
    for entry in report["deferred_documentation_only"]:
        lines.append(
            "| {frontend_id} | {title} | {words} | {minimum_words} | {paragraphs} | "
            "{minimum_paragraphs} | {section_mode} | `{package}` |".format(
                frontend_id=entry["frontend_id"],
                title=_cell(entry["title"]),
                words=entry["goal_word_count"],
                minimum_words=entry["goal_minimum_words"],
                paragraphs=entry["goal_paragraph_count"],
                minimum_paragraphs=entry["goal_minimum_paragraphs"],
                section_mode="reference/" if entry["uses_reference_sections"] else "legacy doc.md",
                package=entry["package"],
            )
        )

    if report["other_completion_gaps"]:
        lines.extend(
            [
                "",
                "## Other completion failures",
                "",
                "| ID | Title | Missing gates | Package |",
                "|---:|---|---|---|",
            ]
        )
        for entry in report["other_completion_gaps"]:
            lines.append(
                f"| {entry['frontend_id']} | {_cell(entry['title'])} | "
                f"{_cell(entry['missing_gates'])} | `{entry['package']}` |"
            )

    overlap = source["overlap"]
    triage = source["unverified_triage_signals"]
    lines.extend(
        [
            "",
            "## Source-fidelity backlog",
            "",
            (
                f"Verified: {summary['source_fidelity_verified']}; unverified: "
                f"{summary['source_fidelity_unverified']}; invalid: "
                f"{summary['source_fidelity_invalid']}. A missing manifest means no "
                "live-source review has been claimed; it is not evidence that the "
                "existing prose is wrong. Structural values below are triage signals, "
                "not substitutes for live review."
            ),
            "",
            "### Overlap with completion work",
            "",
            "| Bucket | Source-fidelity gaps |",
            "|---|---:|",
            f"| Active verified-solution queue | {overlap['active_verified_solution_queue']} |",
            f"| Deferred documentation-only queue | {overlap['deferred_documentation_only']} |",
            f"| Otherwise locally complete | {overlap['otherwise_locally_complete']} |",
            "",
            "### Unverified triage signals",
            "",
            "| Signal | Packages |",
            "|---|---:|",
            f"| No local Constraints heading | {triage['without_constraints_section']} |",
            (
                "| No locally marked example explanation | "
                f"{triage['without_marked_example_explanations']} |"
            ),
            f"| Has local images | {triage['with_local_images']} |",
            f"| Has non-metadata tables | {triage['with_non_metadata_tables']} |",
            f"| Has local diagrams | {triage['with_local_diagrams']} |",
            "",
            "### Package inventory",
            "",
            "| ID | Status | Reason | Constraints | Examples | Explained | Images | Tables | Diagrams | Package |",
            "|---:|---|---|---|---:|---:|---:|---:|---:|---|",
        ]
    )
    for entry in source["entries"]:
        structure = entry["local_structure"]
        reason = entry["reason"]
        if entry["errors"]:
            reason = f"{reason}: {'; '.join(entry['errors'])}"
        lines.append(
            "| {frontend_id} | {status} | {reason} | {constraints} | {examples} | "
            "{explained} | {images} | {tables} | {diagrams} | `{package}` |".format(
                frontend_id=entry["frontend_id"],
                status=entry["status"],
                reason=_cell(reason),
                constraints="yes" if structure["has_constraints"] else "no",
                examples=structure["example_count"],
                explained=structure["explained_example_count"],
                images=structure["image_count"],
                tables=structure["table_count"],
                diagrams=structure["diagram_count"],
                package=entry["package"],
            )
        )

    lines.extend(
        [
            "",
            "## Known repository-wide regression debt",
            "",
            (
                "These failures are separate from the active submission queue. Their "
                "last-observed dates are retained so the final cleanup pass knows when "
                "fresh full-suite evidence is required."
            ),
            "",
            "| Category | Last observed | ID | Title | Reference | Complexity | Detail | Package |",
            "|---|---|---:|---|---|---|---|---|",
        ]
    )
    for group in report["known_repository_regressions"]:
        for package in group["packages"]:
            lines.append(
                "| {category} | {observed} | {frontend_id} | {title} | {language} | "
                "{method} | {detail} | `{package}` |".format(
                    category=_cell(group["category"]),
                    observed=group["last_observed"],
                    frontend_id=package["frontend_id"],
                    title=_cell(package["title"]),
                    language=_cell(package["reference_language"]),
                    method=_cell(package["complexity_method"]),
                    detail=_cell(group["detail"]),
                    package=package["package"],
                )
            )

    lines.extend(
        [
            "",
            "## Regeneration",
            "",
            "```powershell",
            ".\\.venv\\Scripts\\python.exe tools\\audit_leetcode_migration.py",
            ".\\.venv\\Scripts\\python.exe tools\\audit_leetcode_source_fidelity.py --max-frontend-id 4005",
            ".\\.venv\\Scripts\\python.exe tools\\audit_end_of_corpus_rework_gaps.py",
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    report = build_gap_report()
    REPORT_ROOT.mkdir(parents=True, exist_ok=True)
    JSON_PATH.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    MARKDOWN_PATH.write_text(_markdown(report), encoding="utf-8")
    print(json.dumps(report["summary"], indent=2))
    print(f"Wrote {JSON_PATH.relative_to(REPO_ROOT)}.")
    print(f"Wrote {MARKDOWN_PATH.relative_to(REPO_ROOT)}.")
    return 1 if report["summary"]["source_fidelity_invalid"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
