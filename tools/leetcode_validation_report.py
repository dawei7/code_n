"""Build LeetCode optimal-solution and validated-case coverage reports.

This is the dashboard for the long-running LeetCode validation goal:

* every registered LeetCode challenge should have a Python optimal source;
* every LeetCode challenge should have an authored validated case suite;
* every Python optimal source should eventually have an official LeetCode
  grader result, with the latest accepted result recorded in the local jsonl.

The report is intentionally offline. It consumes local files only, including
``dsa/leetcode/_reports/leetcode_submission_results.jsonl`` when present.
Use ``tools/submit_leetcode_optimal_solutions.py`` to append official grader
results.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from challenges.registry import CHALLENGE_REGISTRY  # noqa: E402
from server.app.challenge_packages import leetcode_metadata  # noqa: E402
from server.app.optimal_sources import organized_solution_path  # noqa: E402
from server.app.validated_cases import load_case_suite  # noqa: E402


RESULTS_PATH = ROOT / "dsa" / "leetcode" / "_reports" / "leetcode_submission_results.jsonl"
JSON_REPORT_PATH = ROOT / "dsa" / "leetcode" / "_reports" / "validation_status.json"
MD_REPORT_PATH = ROOT / "dsa" / "leetcode" / "_reports" / "validation_status.md"


@dataclass(frozen=True)
class SubmissionStatus:
    status: str
    accepted: bool
    verdict: str
    submission_id: str
    source_url: str
    task_finish_time: int | None
    error: str = ""


def _frontend_number(challenge_id: str) -> int:
    try:
        return int(challenge_id.removeprefix("lc_"))
    except ValueError:
        return 10**9


def _challenge_slug(challenge: Any) -> str:
    spec = getattr(challenge, "_spec", None)
    url = str(getattr(spec, "source_url", "") or "")
    marker = "/problems/"
    if marker not in url:
        return ""
    return url.split(marker, 1)[1].strip("/").split("/", 1)[0]


def _load_submission_statuses(path: Path) -> dict[str, SubmissionStatus]:
    by_challenge: dict[str, list[dict[str, Any]]] = {}
    if not path.is_file():
        return {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue
        challenge_id = str(record.get("challenge_id") or "")
        if not challenge_id:
            continue
        by_challenge.setdefault(challenge_id, []).append(record)

    result: dict[str, SubmissionStatus] = {}
    for challenge_id, records in by_challenge.items():
        accepted_records = [record for record in records if bool(record.get("accepted"))]
        chosen = accepted_records[-1] if accepted_records else records[-1]
        verdict_payload = chosen.get("verdict") if isinstance(chosen.get("verdict"), dict) else {}
        error = str(chosen.get("error") or "")
        verdict = str(verdict_payload.get("status_msg") or verdict_payload.get("state") or "")
        if chosen.get("accepted"):
            status = "accepted"
        elif error:
            status = "submit_error"
            verdict = verdict or "Submit Error"
        else:
            status = "failed"
        result[challenge_id] = SubmissionStatus(
            status=status,
            accepted=bool(chosen.get("accepted")),
            verdict=verdict,
            submission_id=str(chosen.get("submission_id") or ""),
            source_url=str(chosen.get("source_url") or ""),
            task_finish_time=verdict_payload.get("task_finish_time"),
            error=error,
        )
    return result


def _case_counts(challenge_id: str) -> dict[str, Any]:
    cases = load_case_suite(challenge_id)
    counts = Counter(case.kind for case in cases)
    return {
        "has_cases": bool(cases),
        "total": len(cases),
        "sample": counts.get("sample", 0),
        "trial": counts.get("trial", 0),
        "real": counts.get("real", 0),
        "benchmark": counts.get("benchmark", 0),
        "visible": sum(1 for case in cases if case.visible),
        "complete_for_judge": bool(cases) and counts.get("real", 0) > 0 and counts.get("benchmark", 0) > 0,
    }


def build_report() -> dict[str, Any]:
    submissions = _load_submission_statuses(RESULTS_PATH)
    entries: list[dict[str, Any]] = []
    for challenge_id in sorted(
        (cid for cid in CHALLENGE_REGISTRY if cid.startswith("lc_")),
        key=_frontend_number,
    ):
        challenge = CHALLENGE_REGISTRY[challenge_id]()
        spec = challenge._spec
        metadata = leetcode_metadata(challenge_id)
        supported_languages = [
            str(language)
            for language in metadata.get("supported_languages", [])
            if isinstance(language, str)
        ]
        runnable_in_coden = bool(metadata.get("runnable_in_coden", True))
        python_optimal_applicable = runnable_in_coden and (
            not supported_languages or "python" in supported_languages
        )
        optimal_path = organized_solution_path(challenge_id, "python")
        has_optimal = bool(python_optimal_applicable and optimal_path and optimal_path.is_file())
        case_info = _case_counts(challenge_id)
        submission = submissions.get(challenge_id)
        official_status = submission.status if submission else "not_submitted"
        entries.append(
            {
                "challenge_id": challenge_id,
                "frontend_id": challenge_id.removeprefix("lc_"),
                "title": challenge.info.name,
                "slug": _challenge_slug(challenge),
                "difficulty": getattr(challenge.info, "difficulty_label", ""),
                "source_url": spec.source_url,
                "category": str(metadata.get("category") or ""),
                "category_title": str(metadata.get("category_title") or ""),
                "supported_languages": supported_languages,
                "runnable_in_coden": runnable_in_coden,
                "python_optimal_applicable": python_optimal_applicable,
                "optimal_path": str(optimal_path.relative_to(ROOT)).replace("\\", "/") if optimal_path else "",
                "has_python_optimal": has_optimal,
                "validated_cases": case_info,
                "official_status": official_status,
                "official_verdict": submission.verdict if submission else "",
                "official_submission_id": submission.submission_id if submission else "",
                "official_source_url": submission.source_url if submission else "",
                "official_task_finish_time": submission.task_finish_time if submission else None,
                "official_error": submission.error if submission else "",
            }
        )

    counts = {
        "total_leetcode": len(entries),
        "python_optimal_applicable": sum(1 for entry in entries if entry["python_optimal_applicable"]),
        "python_optimal_not_applicable": sum(1 for entry in entries if not entry["python_optimal_applicable"]),
        "python_optimal_present": sum(1 for entry in entries if entry["has_python_optimal"]),
        "python_optimal_missing": sum(
            1
            for entry in entries
            if entry["python_optimal_applicable"] and not entry["has_python_optimal"]
        ),
        "validated_case_suites": sum(1 for entry in entries if entry["validated_cases"]["has_cases"]),
        "validated_case_suites_missing": sum(1 for entry in entries if not entry["validated_cases"]["has_cases"]),
        "judge_complete_case_suites": sum(1 for entry in entries if entry["validated_cases"]["complete_for_judge"]),
        "official_not_applicable": sum(1 for entry in entries if not entry["python_optimal_applicable"]),
        "official_accepted": sum(
            1
            for entry in entries
            if entry["python_optimal_applicable"] and entry["official_status"] == "accepted"
        ),
        "official_failed_latest": sum(
            1
            for entry in entries
            if entry["python_optimal_applicable"] and entry["official_status"] == "failed"
        ),
        "official_submit_error_latest": sum(
            1
            for entry in entries
            if entry["python_optimal_applicable"] and entry["official_status"] == "submit_error"
        ),
        "official_not_submitted": sum(
            1
            for entry in entries
            if entry["python_optimal_applicable"] and entry["official_status"] == "not_submitted"
        ),
        "ready_for_official_submission": sum(
            1
            for entry in entries
            if entry["python_optimal_applicable"] and entry["has_python_optimal"] and entry["official_status"] != "accepted"
        ),
        "ready_for_case_authoring": sum(
            1
            for entry in entries
            if entry["python_optimal_applicable"] and entry["has_python_optimal"] and not entry["validated_cases"]["has_cases"]
        ),
    }
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "counts": counts,
        "entries": entries,
    }


def _first_entries(entries: list[dict[str, Any]], predicate, limit: int) -> list[dict[str, Any]]:
    return [entry for entry in entries if predicate(entry)][:limit]


def _write_markdown(report: dict[str, Any], path: Path, limit: int) -> None:
    counts = report["counts"]
    entries = report["entries"]
    lines = [
        "# LeetCode Validation Status",
        "",
        f"Generated: {report['generated_at']}",
        "",
        "## Summary",
        "",
        "| Metric | Count |",
        "| --- | ---: |",
    ]
    for key, value in counts.items():
        lines.append(f"| {key.replace('_', ' ')} | {value} |")

    lines.extend([
        "",
        "## Benchmark Case Authoring Note",
        "",
        "- Benchmark cases are for runtime and complexity gating, not standalone practice export.",
        "- Prefer one representative adversarial input shape over repeating tiny toy cases.",
        "- Store benchmark cases explicitly in a separate sidecar file named `<case-suite>.benchmark.json`; benchmark cases are not allowed inside the normal user-facing `<case-suite>.json` file.",
        "- For complexity checks, author at least two benchmark tiers with positive, increasing `size` values spanning at least 4x; three tiers are recommended. A one-case sidecar retains the legacy fixed-runtime check.",
        "- Keep the sidecar benchmark-only; the loader merges that file with the main authored suite before running `solve`.",
    ])

    sections = [
        (
            "Missing Python Optimal",
            _first_entries(
                entries,
                lambda entry: entry["python_optimal_applicable"] and not entry["has_python_optimal"],
                limit,
            ),
            lambda entry: entry["optimal_path"] or "(no organized path)",
        ),
        (
            "Missing Validated Case Suite",
            _first_entries(
                entries,
                lambda entry: entry["has_python_optimal"] and not entry["validated_cases"]["has_cases"],
                limit,
            ),
            lambda entry: entry["optimal_path"],
        ),
        (
            "Not Yet Accepted By Official LeetCode",
            _first_entries(
                entries,
                lambda entry: entry["has_python_optimal"] and entry["official_status"] != "accepted",
                limit,
            ),
            lambda entry: entry["official_status"],
        ),
        (
            "Latest Official Failures",
            _first_entries(entries, lambda entry: entry["official_status"] == "failed", limit),
            lambda entry: entry["official_verdict"],
        ),
        (
            "Latest Official Submit Errors",
            _first_entries(entries, lambda entry: entry["official_status"] == "submit_error", limit),
            lambda entry: entry["official_error"] or entry["official_verdict"],
        ),
    ]
    for title, rows, detail_fn in sections:
        lines.extend(["", f"## {title}", ""])
        if not rows:
            lines.append("- None")
            continue
        for entry in rows:
            lines.append(
                f"- `{entry['challenge_id']}` | {entry['title']} | {detail_fn(entry)}"
            )

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=JSON_REPORT_PATH)
    parser.add_argument("--markdown", type=Path, default=MD_REPORT_PATH)
    parser.add_argument("--limit", type=int, default=40, help="Rows per markdown detail section.")
    parser.add_argument("--no-markdown", action="store_true")
    args = parser.parse_args()

    report = build_report()
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if not args.no_markdown:
        _write_markdown(report, args.markdown, args.limit)

    print(json.dumps(report["counts"], indent=2))
    print(f"Wrote {args.json.relative_to(ROOT)}.")
    if not args.no_markdown:
        print(f"Wrote {args.markdown.relative_to(ROOT)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
