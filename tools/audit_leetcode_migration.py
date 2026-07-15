"""Audit progress toward the Two Sum quality bar for every LeetCode package.

The report is intentionally local and reproducible.  It does not claim that a
submission is verified unless the package manifest records an Accepted remote
submission.  Run this after every migrated package or batch.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.complexity_certificates import validate_complexity_certificate  # noqa: E402


LEETCODE_ROOT = ROOT / "dsa" / "leetcode"
REPORT_ROOT = LEETCODE_ROOT / "_reports"
REPORT_JSON = REPORT_ROOT / "two_sum_migration_progress.json"
REPORT_MD = REPORT_ROOT / "two_sum_migration_progress.md"
BLOCKERS_JSON = REPORT_ROOT / "two_sum_migration_blockers.json"

PLACEHOLDERS = ("Write an original local summary", "TODO")
DOC_SECTIONS = (
    "## Problem Description",
    "### Goal",
    "### Function Contract",
    "### Examples",
    "### Required Complexity",
    "<details>",
    "<summary>Approach</summary>",
    "#### General",
    "#### Complexity detail",
    "#### Alternatives and edge cases",
)
APPROACH_HEADINGS = ("General", "Complexity detail", "Alternatives and edge cases")
MIN_GOAL_WORDS = 60
MIN_GOAL_PARAGRAPHS = 2
EXTENSIONS = {
    "python": "py",
    "cpp": "cpp",
    "java": "java",
    "csharp": "cs",
    "javascript": "js",
    "go": "go",
    "kotlin": "kt",
    "sql": "sql",
    "bash": "sh",
}


def _load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def _package_sort_key(path: Path) -> tuple[int, str]:
    prefix = path.name.split("_", 1)[0]
    return (int(prefix), path.name) if prefix.isdigit() else (10**9, path.name)


def _case_rows(payload: Any) -> list[dict[str, Any]]:
    if not isinstance(payload, dict) or not isinstance(payload.get("cases"), list):
        return []
    return [row for row in payload["cases"] if isinstance(row, dict)]


def _doc_status(path: Path) -> dict[str, Any]:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        text = ""
    positions = [text.find(section) for section in DOC_SECTIONS]
    complete = bool(text) and not any(marker in text for marker in PLACEHOLDERS)
    complete = complete and all(position >= 0 for position in positions)
    required_positions = positions[:5]
    complete = complete and required_positions == sorted(required_positions)
    goal_match = re.search(
        r"^### Goal\s*$\s*(.*?)(?=^### Function Contract\s*$)",
        text,
        flags=re.MULTILINE | re.DOTALL,
    )
    goal_text = goal_match.group(1).strip() if goal_match else ""
    goal_paragraphs = [
        paragraph.strip()
        for paragraph in re.split(r"\n\s*\n", goal_text)
        if paragraph.strip()
    ]
    goal_word_count = len(re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", goal_text))
    goal_narrative_complete = (
        goal_word_count >= MIN_GOAL_WORDS
        and len(goal_paragraphs) >= MIN_GOAL_PARAGRAPHS
    )
    complete = complete and goal_narrative_complete
    approach_start = text.find("<summary>Approach</summary>")
    approach_end = text.find("</details>", approach_start)
    approach_text = text[approach_start:approach_end] if approach_start >= 0 and approach_end >= 0 else ""
    approach_headings = tuple(re.findall(r"^####\s+(.+?)\s*$", approach_text, flags=re.MULTILINE))
    complete = complete and approach_headings == APPROACH_HEADINGS
    alternatives_match = re.search(
        r"^#### Alternatives and edge cases\s*$\s*(.*)\Z",
        approach_text,
        flags=re.MULTILINE | re.DOTALL,
    )
    alternatives_text = alternatives_match.group(1).strip() if alternatives_match else ""
    alternatives_lines = [line for line in alternatives_text.splitlines() if line.strip()]
    alternative_bullet_count = sum(line.startswith("- ") for line in alternatives_lines)
    alternatives_as_list = alternative_bullet_count >= 2 and all(
        line.startswith("- ") or line.startswith("  ") for line in alternatives_lines
    )
    complete = complete and alternatives_as_list
    time_match = re.search(r"^- \*\*Time:\*\* \$(O\([^$]+\))\$\s*$", text, flags=re.MULTILINE)
    return {
        "complete": complete,
        "missing_sections": [
            section for section, position in zip(DOC_SECTIONS, positions, strict=True) if position < 0
        ],
        "has_placeholder": any(marker in text for marker in PLACEHOLDERS),
        "goal_narrative_complete": goal_narrative_complete,
        "goal_word_count": goal_word_count,
        "goal_paragraph_count": len(goal_paragraphs),
        "goal_minimum_words": MIN_GOAL_WORDS,
        "goal_minimum_paragraphs": MIN_GOAL_PARAGRAPHS,
        "approach_headings": list(approach_headings),
        "alternatives_as_list": alternatives_as_list,
        "alternative_bullet_count": alternative_bullet_count,
        "required_time": time_match.group(1) if time_match else "",
    }


def _cases_status(path: Path) -> dict[str, Any]:
    rows = _case_rows(_load_json(path))
    counts = Counter(str(row.get("kind") or "") for row in rows)
    complete = all(counts[kind] > 0 for kind in ("sample", "trial", "real"))
    complete = complete and all(
        row.get("visible") is False for row in rows if row.get("kind") == "real"
    )
    return {"complete": complete, "total": len(rows), "kinds": dict(sorted(counts.items()))}


def _benchmark_status(path: Path) -> dict[str, Any]:
    rows = _case_rows(_load_json(path))
    sizes = [row.get("size") for row in rows]
    integer_sizes = all(isinstance(size, int) and not isinstance(size, bool) and size > 0 for size in sizes)
    ordered = integer_sizes and sizes == sorted(sizes) and len(set(sizes)) == len(sizes)
    span_ok = integer_sizes and bool(sizes) and sizes[-1] >= sizes[0] * 4
    benchmark_only = bool(rows) and all(row.get("kind") == "benchmark" for row in rows)
    complete = len(rows) == 3 and benchmark_only and ordered and span_ok
    return {
        "complete": complete,
        "tiers": len(rows),
        "sizes": sizes,
        "benchmark_only": benchmark_only,
        "ordered_unique_positive_sizes": ordered,
        "span_at_least_4x": span_ok,
    }


def _complexity_certificate_status(
    path: Path,
    challenge_id: str,
    required_time: str,
) -> dict[str, Any]:
    if not path.is_file():
        return {
            "complete": False,
            "method": "",
            "required_time": "",
            "summary": "",
            "replacement_checks": [],
            "errors": [],
            "path": str(path.relative_to(ROOT)).replace("\\", "/"),
        }
    payload = _load_json(path)
    status = validate_complexity_certificate(
        payload,
        expected_challenge_id=challenge_id,
        expected_required_time=required_time,
    )
    return {
        "complete": status.complete,
        "method": status.method,
        "required_time": status.required_time,
        "summary": status.summary,
        "replacement_checks": list(status.check_kinds),
        "errors": list(status.errors),
        "path": str(path.relative_to(ROOT)).replace("\\", "/"),
    }


def _complexity_status(benchmark: dict[str, Any], certificate: dict[str, Any]) -> dict[str, Any]:
    conflict = bool(benchmark["complete"] and certificate["complete"])
    if benchmark["complete"]:
        method = "scaling_benchmark"
    elif certificate["complete"]:
        method = str(certificate["method"])
    else:
        method = ""
    return {
        "complete": bool((benchmark["complete"] or certificate["complete"]) and not conflict),
        "method": method,
        "benchmark_complete": bool(benchmark["complete"]),
        "certificate_complete": bool(certificate["complete"]),
        "conflict": conflict,
    }


def _solution_status(package: Path, metadata: dict[str, Any]) -> dict[str, Any]:
    primary = str(metadata.get("primary_language") or "").strip().lower()
    if not primary:
        supported = metadata.get("supported_languages")
        primary = str(supported[0]).lower() if isinstance(supported, list) and supported else ""
    extension = EXTENSIONS.get(primary, "")
    path = package / "solutions" / f"{primary}.{extension}" if extension else package / "solutions" / primary
    return {
        "complete": bool(extension and path.is_file() and path.stat().st_size > 0),
        "language": primary,
        "path": str(path.relative_to(ROOT)).replace("\\", "/"),
    }


def _submission_status(package: Path, metadata: dict[str, Any]) -> dict[str, Any]:
    manifest = _load_json(package / "submission.json")
    if not isinstance(manifest, dict):
        return {"complete": False, "status": "missing", "paid_only": bool(metadata.get("paid_only"))}
    source_value = str(manifest.get("source") or "")
    source = package / source_value if source_value else package / "__missing__"
    verified = (
        manifest.get("status") == "verified"
        and bool(str(manifest.get("verified_submission_id") or ""))
        and source.is_file()
    )
    return {
        "complete": verified,
        "status": str(manifest.get("status") or "invalid"),
        "language": str(manifest.get("language") or ""),
        "source": source_value,
        "source_exists": source.is_file(),
        "verified_submission_id": str(manifest.get("verified_submission_id") or ""),
        "paid_only": bool(manifest.get("paid_only", metadata.get("paid_only", False))),
    }


def _load_blockers() -> dict[str, dict[str, Any]]:
    payload = _load_json(BLOCKERS_JSON)
    if not isinstance(payload, dict) or not isinstance(payload.get("blockers"), dict):
        return {}
    return {
        str(key): value
        for key, value in payload["blockers"].items()
        if isinstance(value, dict)
    }


def _write_blockers(blockers: dict[str, dict[str, Any]]) -> None:
    REPORT_ROOT.mkdir(parents=True, exist_ok=True)
    payload = {"schema_version": 1, "blockers": dict(sorted(blockers.items(), key=lambda item: int(item[0])))}
    BLOCKERS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def build_report() -> dict[str, Any]:
    blockers = _load_blockers()
    packages = sorted(
        (path for path in LEETCODE_ROOT.iterdir() if path.is_dir() and (path / "metadata.json").is_file()),
        key=_package_sort_key,
    )
    entries: list[dict[str, Any]] = []
    for package in packages:
        metadata = _load_json(package / "metadata.json")
        metadata = metadata if isinstance(metadata, dict) else {}
        frontend_id = str(metadata.get("frontend_id") or package.name.split("_", 1)[0])
        doc = _doc_status(package / "doc.md")
        benchmark = _benchmark_status(package / "benchmark.json")
        certificate = _complexity_certificate_status(
            package / "complexity_certificate.json",
            str(metadata.get("challenge_id") or f"lc_{int(frontend_id)}"),
            str(doc.get("required_time") or ""),
        )
        checks = {
            "doc": doc,
            "cases": _cases_status(package / "cases.json"),
            "benchmarks": benchmark,
            "complexity_certificate": certificate,
            "complexity": _complexity_status(benchmark, certificate),
            "optimal_solution": _solution_status(package, metadata),
            "leetcode_submission": _submission_status(package, metadata),
        }
        local_complete = all(
            checks[name]["complete"]
            for name in ("doc", "cases", "complexity", "optimal_solution")
        )
        complete = local_complete and checks["leetcode_submission"]["complete"]
        blocker = blockers.get(frontend_id)
        entries.append(
            {
                "frontend_id": frontend_id,
                "title": str(metadata.get("title") or ""),
                "slug": str(metadata.get("slug") or ""),
                "package": str(package.relative_to(ROOT)).replace("\\", "/"),
                "local_complete": local_complete,
                "complete": complete,
                "blocked": blocker is not None,
                "blocker": blocker,
                "checks": checks,
            }
        )

    counts = {
        "packages": len(entries),
        "local_complete": sum(entry["local_complete"] for entry in entries),
        "fully_complete_and_verified": sum(entry["complete"] for entry in entries),
        "blocked": sum(entry["blocked"] for entry in entries),
    }
    for name in ("doc", "cases", "benchmarks", "optimal_solution", "leetcode_submission"):
        counts[f"{name}_complete"] = sum(entry["checks"][name]["complete"] for entry in entries)
    counts["complexity_certified"] = sum(
        entry["checks"]["complexity_certificate"]["complete"] for entry in entries
    )
    counts["complexity_complete"] = sum(entry["checks"]["complexity"]["complete"] for entry in entries)
    first_incomplete = next((entry for entry in entries if not entry["complete"] and not entry["blocked"]), None)
    return {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "scope": "All canonical packages in ascending numeric LeetCode frontend-ID order; IDs are sparse.",
        "exemplar": "dsa/leetcode/0001_two-sum",
        "counts": counts,
        "first_actionable_incomplete": None if first_incomplete is None else {
            "frontend_id": first_incomplete["frontend_id"],
            "title": first_incomplete["title"],
            "package": first_incomplete["package"],
        },
        "entries": entries,
    }


def _write_report(report: dict[str, Any]) -> None:
    REPORT_ROOT.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    counts = report["counts"]
    first = report["first_actionable_incomplete"]
    lines = [
        "# Two Sum Migration Progress",
        "",
        f"Generated: {report['generated_at']}",
        "",
        report["scope"],
        "",
        "## Completion criteria",
        "",
        "A package is locally complete only when its canonical document (including a source-like Goal narrative of at least two paragraphs and 60 words), visible/hidden cases, complexity verification, and optimal app-local solution pass the audit. Complexity verification normally requires exactly three ordered benchmark tiers; a strictly validated `complexity_certificate.json` replaces scaling only when the legal source domain cannot support an honest scaling verdict. Full completion additionally requires an exact platform-native source recorded as remotely Accepted in `submission.json`.",
        "",
        "## Counts",
        "",
        "| Metric | Count |",
        "| --- | ---: |",
    ]
    lines.extend(f"| {key.replace('_', ' ')} | {value} |" for key, value in counts.items())
    lines.extend(["", "## Next package", ""])
    if first:
        lines.append(f"- {first['frontend_id']} — {first['title']} (`{first['package']}`)")
    else:
        lines.append("- None")
    blocked = [entry for entry in report["entries"] if entry["blocked"]]
    lines.extend(["", "## Recorded blockers", ""])
    if blocked:
        for entry in blocked:
            lines.append(f"- {entry['frontend_id']} — {entry['title']}: {entry['blocker'].get('reason', '')}")
    else:
        lines.append("- None")
    lines.extend(["", "The JSON report contains the per-package check details.", ""])
    REPORT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--block", metavar="FRONTEND_ID")
    parser.add_argument("--reason")
    parser.add_argument("--clear-block", metavar="FRONTEND_ID")
    args = parser.parse_args()
    blockers = _load_blockers()
    if args.block:
        if not args.reason:
            parser.error("--block requires --reason")
        blockers[args.block] = {
            "reason": args.reason,
            "recorded_at": datetime.now(timezone.utc).isoformat(),
        }
        _write_blockers(blockers)
    if args.clear_block:
        blockers.pop(args.clear_block, None)
        _write_blockers(blockers)
    report = build_report()
    _write_report(report)
    print(json.dumps({"counts": report["counts"], "first_actionable_incomplete": report["first_actionable_incomplete"]}, indent=2))
    print(f"Wrote {REPORT_JSON.relative_to(ROOT)} and {REPORT_MD.relative_to(ROOT)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
