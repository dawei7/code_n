from __future__ import annotations

import json
import shutil
from pathlib import Path

from engine.solution_variants import validate_solution_variants
from server.app.engine_runner import run_player_code
from server.app.validated_cases import load_case_suite, select_cases_for_run
from tools import check_leetcode_dataset as completion_report_tool
from tools.check_leetcode_dataset import build_report, classify
from tools.audit_leetcode_migration import _cases_status
from tools.leetcode_solution_quality import review_hashes, validate_solution_quality


REPO_ROOT = Path(__file__).resolve().parents[1]
LONGEST_COMMON_PREFIX = REPO_ROOT / "dsa" / "leetcode" / "0014_longest-common-prefix"
TWO_SUM = REPO_ROOT / "dsa" / "leetcode" / "0001_two-sum"
APPLES_ORANGES = REPO_ROOT / "dsa" / "leetcode" / "1445_apples-oranges"


def _copy_package(tmp_path: Path, source: Path) -> Path:
    package = tmp_path / "dsa" / "leetcode" / source.name
    shutil.copytree(source, package)
    return package


def _copy_without_quality_review(tmp_path: Path) -> Path:
    package = _copy_package(tmp_path, TWO_SUM)
    (package / "variants" / "optimal" / "solution_quality.json").unlink()
    return package


def test_missing_solution_quality_review_is_unreviewed(tmp_path: Path) -> None:
    status = validate_solution_quality(_copy_without_quality_review(tmp_path))

    assert status.solution_status == "unreviewed"
    assert status.case_status == "unreviewed"


def test_longest_common_prefix_quality_review_is_complete() -> None:
    status = validate_solution_quality(LONGEST_COMMON_PREFIX)

    assert status.complete, status.errors
    assert status.verdict == "candidate_proposed"
    assert status.target == "candidate"
    assert status.candidate_path == "variants/optimal/solutions/candidate.py"


def test_solution_only_review_does_not_require_cases_json(tmp_path: Path) -> None:
    package = _copy_package(tmp_path, LONGEST_COMMON_PREFIX)
    (package / "cases.json").unlink()
    manifest_path = package / "variants" / "optimal" / "solution_quality.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["review_scope"] = "solution_only"
    manifest.pop("case_review")
    manifest["hashes"] = review_hashes(package, language="python", target="candidate", include_cases=False)
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    status = validate_solution_quality(package)

    assert status.solution_status == "complete", status.errors
    assert status.case_status == "unreviewed"
    assert status.review_scope == "solution_only"


def test_solution_only_current_review_does_not_inspect_cases_or_benchmark(tmp_path: Path) -> None:
    package = _copy_package(tmp_path, APPLES_ORANGES)
    (package / "cases.json").unlink()
    benchmark_path = package / "benchmark.json"
    benchmark_path.write_text("inherited artifact identity only\n", encoding="utf-8")
    manifest_path = package / "variants" / "optimal" / "solution_quality.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["review_scope"] = "solution_only"
    manifest.pop("case_review")
    manifest["solution_review"]["validation"] = {
        "mode": "expert_review",
        "judge_run": False,
        "complexity_method": "benchmark",
        "complexity_evidence": "inherited",
    }
    manifest["hashes"] = review_hashes(package, language="sql", target="current", include_cases=False)
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    status = validate_solution_quality(package)

    assert status.solution_status == "complete", status.errors
    assert status.case_status == "unreviewed"


def test_solution_only_current_review_rejects_claimed_judge_results(tmp_path: Path) -> None:
    package = _copy_package(tmp_path, APPLES_ORANGES)
    manifest_path = package / "variants" / "optimal" / "solution_quality.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["review_scope"] = "solution_only"
    manifest.pop("case_review")
    manifest["solution_review"]["validation"] = {
        "mode": "expert_review",
        "judge_run": False,
        "complexity_method": "benchmark",
        "complexity_evidence": "inherited",
        "complexity_passed": True,
    }
    manifest["hashes"] = review_hashes(package, language="sql", target="current", include_cases=False)
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    status = validate_solution_quality(package)

    assert status.solution_status == "invalid"
    assert any("must not claim judge or calibration results" in error for error in status.errors)


def test_solution_only_current_review_accepts_legacy_real_test_evidence(tmp_path: Path) -> None:
    package = _copy_package(tmp_path, APPLES_ORANGES)
    manifest_path = package / "variants" / "optimal" / "solution_quality.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["review_scope"] = "solution_only"
    manifest.pop("case_review")
    manifest["hashes"] = review_hashes(package, language="sql", target="current", include_cases=False)
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    status = validate_solution_quality(package)

    assert status.solution_status == "complete", status.errors
    assert status.case_status == "unreviewed"


def test_review_becomes_stale_when_a_bound_artifact_changes(tmp_path: Path) -> None:
    package = tmp_path / LONGEST_COMMON_PREFIX.name
    shutil.copytree(LONGEST_COMMON_PREFIX, package)
    candidate = package / "variants" / "optimal" / "solutions" / "candidate.py"
    candidate.write_text(candidate.read_text(encoding="utf-8") + "\n", encoding="utf-8")

    status = validate_solution_quality(package)

    assert status.solution_status == "stale"
    assert status.case_status == "complete"
    assert any("candidate.py changed after review" in error for error in status.errors)


def test_review_rejects_a_hidden_correctness_case_even_with_current_hashes(tmp_path: Path) -> None:
    package = tmp_path / LONGEST_COMMON_PREFIX.name
    shutil.copytree(LONGEST_COMMON_PREFIX, package)
    cases_path = package / "cases.json"
    cases = json.loads(cases_path.read_text(encoding="utf-8"))
    cases["cases"][-1]["visible"] = False
    cases_path.write_text(json.dumps(cases, indent=2) + "\n", encoding="utf-8")
    manifest_path = package / "variants" / "optimal" / "solution_quality.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["hashes"] = review_hashes(package, language="python", target="candidate")
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    status = validate_solution_quality(package)

    assert status.solution_status == "complete"
    assert status.case_status == "invalid"
    assert any("must be explicitly visible" in error for error in status.errors)


def test_candidate_is_not_exposed_as_an_active_solution() -> None:
    metadata = json.loads((LONGEST_COMMON_PREFIX / "metadata.json").read_text(encoding="utf-8"))
    status = validate_solution_variants(
        LONGEST_COMMON_PREFIX / "solution_variants.json",
        metadata=metadata,
        expected_challenge_id="lc_14",
    )

    assert status.complete, status.errors
    optimal = next(variant for variant in status.variants if variant.id == "optimal")
    assert optimal.solution_paths["python"].name == "solve.py"
    assert all(path.name != "candidate.py" for path in optimal.solution_paths.values())


def test_longest_common_prefix_cases_are_sufficiently_visible() -> None:
    suite = load_case_suite("lc_14")
    correctness = [case for case in suite if case.kind != "benchmark"]
    benchmarks = [case for case in suite if case.kind == "benchmark"]

    assert len(correctness) == 9
    assert all(case.kind in {"sample", "trial"} and case.visible for case in correctness)
    assert len(benchmarks) == 3
    assert all(not case.visible for case in benchmarks)


def test_migration_audit_accepts_the_all_visible_correctness_model() -> None:
    status = _cases_status(LONGEST_COMMON_PREFIX / "cases.json")

    assert status["complete"]
    assert status["visibility_model"] == "all_visible"


def test_longest_common_prefix_candidate_passes_full_judge() -> None:
    candidate = (LONGEST_COMMON_PREFIX / "variants" / "optimal" / "solutions" / "candidate.py").read_text(
        encoding="utf-8"
    )
    run_cases, benchmark_cases = select_cases_for_run("lc_14", mode="real_test")

    result = run_player_code(
        "lc_14",
        candidate,
        mode="real_test",
        language="python",
        run_cases=run_cases,
        benchmark_cases=benchmark_cases,
    )

    assert result.passed, result.message
    assert all(case.correct for case in result.case_results)
    assert result.runtime_check
    assert result.runtime_passed


def test_completion_report_tracks_both_quality_dimensions(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setattr(completion_report_tool, "REPO_ROOT", tmp_path)
    unreviewed = classify(_copy_without_quality_review(tmp_path) / "doc.md")
    reviewed = classify(_copy_package(tmp_path, LONGEST_COMMON_PREFIX) / "doc.md")
    report = build_report([unreviewed, reviewed])

    assert report["solution_quality_counts"] == {"unreviewed": 1, "complete": 1}
    assert report["case_quality_counts"] == {"unreviewed": 1, "complete": 1}
    assert report["solution_quality_verdict_counts"] == {"candidate_proposed": 1}
    assert report["first_incomplete_solution_quality"] == {
        "frontend_id": 1,
        "slug": "two-sum",
        "package": "dsa/leetcode/0001_two-sum",
    }
    assert report["first_incomplete_case_quality"] == report["first_incomplete_solution_quality"]
