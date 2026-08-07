"""Validate hash-bound manual solution and deferred correctness-case reviews."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from engine.languages import (
    app_solution_filename,
    candidate_solution_filename,
    leetcode_solution_filename,
    normalize_language,
)


MANIFEST_NAME = "solution_quality.json"
SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SOLUTION_ASSERTIONS = (
    "correct",
    "required_complexity",
    "clear_and_concise",
    "conventional_structure",
    "interview_quality_naming",
    "app_contract_preserved",
    "approach_matches_target",
)
CASE_ASSERTIONS = (
    "source_examples",
    "contract_boundaries",
    "material_edge_cases",
    "expected_results",
    "all_correctness_cases_visible",
    "benchmarks_are_performance_only",
)


@dataclass(frozen=True)
class SolutionQualityStatus:
    solution_status: str
    case_status: str
    review_scope: str = ""
    verdict: str = ""
    target: str = ""
    candidate_path: str = ""
    findings: tuple[str, ...] = ()
    errors: tuple[str, ...] = ()

    @property
    def complete(self) -> bool:
        return self.solution_status == "complete" and self.case_status == "complete" and not self.errors


def _load_json(path: Path, errors: list[str]) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        errors.append(f"cannot read {path.name}: {exc}")
        return {}
    except json.JSONDecodeError as exc:
        errors.append(f"{path.name} is not valid JSON: {exc}")
        return {}
    if not isinstance(payload, dict):
        errors.append(f"{path.name} must contain a JSON object")
        return {}
    return payload


def _canonical_sha256(path: Path) -> str:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _assertions(section: dict[str, Any], names: tuple[str, ...], prefix: str, errors: list[str]) -> None:
    assertions = section.get("assertions")
    if not isinstance(assertions, dict):
        errors.append(f"{prefix}.assertions must be an object")
        return
    for name in names:
        if assertions.get(name) is not True:
            errors.append(f"{prefix}.assertions.{name} must be true")


def _case_rows(path: Path, errors: list[str]) -> list[dict[str, Any]]:
    payload = _load_json(path, errors)
    rows = payload.get("cases")
    if not isinstance(rows, list) or not rows:
        errors.append(f"{path.name} must contain a non-empty cases list")
        return []
    valid_rows = [row for row in rows if isinstance(row, dict)]
    if len(valid_rows) != len(rows):
        errors.append(f"{path.name} contains a non-object case")
    return valid_rows


def _validate_complexity_layout(package: Path, errors: list[str]) -> tuple[int, str]:
    benchmark_path = package / "benchmark.json"
    certificate_path = package / "complexity_certificate.json"
    benchmark_count = 0
    complexity_method = ""
    if benchmark_path.is_file():
        benchmarks = _case_rows(benchmark_path, errors)
        benchmark_count = len(benchmarks)
        complexity_method = "benchmark"
        for row in benchmarks:
            case_id = str(row.get("id") or "<missing id>")
            if row.get("kind") != "benchmark":
                errors.append(f"benchmark.json case {case_id} must use kind benchmark")
            if row.get("visible") is not False:
                errors.append(f"benchmark.json case {case_id} must be explicitly hidden")
    elif certificate_path.is_file():
        complexity_method = "certificate"
    else:
        errors.append("benchmark.json or complexity_certificate.json is required")
    return benchmark_count, complexity_method


def _complexity_artifact_method(package: Path, errors: list[str]) -> str:
    """Identify inherited complexity evidence without reading or recalibrating it."""

    if (package / "benchmark.json").is_file():
        return "benchmark"
    if (package / "complexity_certificate.json").is_file():
        return "certificate"
    errors.append("benchmark.json or complexity_certificate.json is required")
    return ""


def _validate_case_layout(package: Path, errors: list[str]) -> tuple[int, int, str]:
    cases = _case_rows(package / "cases.json", errors)
    for row in cases:
        case_id = str(row.get("id") or "<missing id>")
        if row.get("kind") not in {"sample", "trial"}:
            errors.append(f"cases.json case {case_id} must use kind sample or trial")
        if row.get("visible") is not True:
            errors.append(f"cases.json case {case_id} must be explicitly visible")

    benchmark_count, complexity_method = _validate_complexity_layout(package, errors)
    return len(cases), benchmark_count, complexity_method


def _expected_paths(package: Path, language: str, target: str, *, include_cases: bool = True) -> dict[str, Path]:
    optimal_folder = package / "variants" / "optimal"
    solutions = optimal_folder / "solutions"
    complexity_evidence = package / "benchmark.json"
    if not complexity_evidence.is_file():
        complexity_evidence = package / "complexity_certificate.json"
    current_src = optimal_folder / app_solution_filename(language)
    if not current_src.is_file():
        current_src = solutions / app_solution_filename(language)
    native_src = optimal_folder / leetcode_solution_filename(language)
    if not native_src.is_file():
        native_src = solutions / leetcode_solution_filename(language)
    if not native_src.is_file():
        native_src = current_src

    paths = {
        "current_source_sha256": current_src,
        "native_source_sha256": native_src,
        "approach_sha256": package / "variants" / "optimal" / "approach.md",
        "solution_variants_sha256": package / "solution_variants.json",
        "complexity_evidence_sha256": complexity_evidence,
    }
    if include_cases:
        paths["cases_sha256"] = package / "cases.json"
    if target == "candidate":
        paths["candidate_source_sha256"] = solutions / candidate_solution_filename(language)
    return paths


def review_hashes(package: Path, *, language: str, target: str, include_cases: bool = True) -> dict[str, str]:
    """Return the canonical artifact hashes required by a quality manifest."""

    return {
        name: _canonical_sha256(path)
        for name, path in _expected_paths(package, language, target, include_cases=include_cases).items()
    }


def validate_solution_quality(package: Path, *, check_cases: bool = True) -> SolutionQualityStatus:
    """Validate one package's manual solution and correctness-case review."""

    manifest_path = package / "variants" / "optimal" / MANIFEST_NAME
    if not manifest_path.is_file():
        return SolutionQualityStatus("unreviewed", "unreviewed")

    shared_errors: list[str] = []
    solution_errors: list[str] = []
    case_errors: list[str] = []
    solution_stale: list[str] = []
    case_stale: list[str] = []
    payload = _load_json(manifest_path, shared_errors)
    metadata = _load_json(package / "metadata.json", shared_errors)
    expected_challenge_id = str(metadata.get("challenge_id") or "")

    if payload.get("schema_version") != 1:
        shared_errors.append("schema_version must be 1")
    review_scope = str(payload.get("review_scope") or "solution_and_cases")
    if review_scope not in {"solution_and_cases", "solution_only"}:
        shared_errors.append("review_scope must be solution_and_cases or solution_only")
    solution_only = review_scope == "solution_only"
    if str(payload.get("challenge_id") or "") != expected_challenge_id:
        shared_errors.append("challenge_id does not match metadata.json")
    reviewed_on = str(payload.get("reviewed_on") or "")
    if not DATE_PATTERN.fullmatch(reviewed_on):
        shared_errors.append("reviewed_on must use YYYY-MM-DD")

    try:
        language = normalize_language(str(payload.get("language") or ""))
        primary_language = normalize_language(str(metadata.get("primary_language") or ""))
    except ValueError as exc:
        shared_errors.append(str(exc))
        language = "python"
        primary_language = "python"
    if language != primary_language:
        shared_errors.append("language does not match metadata.primary_language")

    solution_review = payload.get("solution_review")
    if not isinstance(solution_review, dict):
        solution_errors.append("solution_review must be an object")
        solution_review = {}
    case_review = payload.get("case_review")
    if solution_only:
        if case_review is not None:
            case_errors.append("case_review must be omitted for a solution_only review")
        case_review = {}
    elif not isinstance(case_review, dict):
        case_errors.append("case_review must be an object")
        case_review = {}

    if solution_review.get("status") != "complete":
        solution_errors.append("solution_review.status must be complete")
    _assertions(solution_review, SOLUTION_ASSERTIONS, "solution_review", solution_errors)
    if not solution_only:
        if case_review.get("status") != "complete":
            case_errors.append("case_review.status must be complete")
        _assertions(case_review, CASE_ASSERTIONS, "case_review", case_errors)

    verdict = str(solution_review.get("verdict") or "")
    target = str(solution_review.get("target") or "")
    if verdict not in {"good", "candidate_proposed"}:
        solution_errors.append("solution_review.verdict must be good or candidate_proposed")
    if target not in {"current", "candidate"}:
        solution_errors.append("solution_review.target must be current or candidate")
    if (verdict, target) not in {("good", "current"), ("candidate_proposed", "candidate")}:
        solution_errors.append("solution_review verdict and target are inconsistent")
    if str(solution_review.get("approach_target") or "") != target:
        solution_errors.append("solution_review.approach_target must match target")

    expected_candidate = package / "variants" / "optimal" / "solutions" / candidate_solution_filename(language)
    relative_candidate = str(expected_candidate.relative_to(package)).replace("\\", "/")
    recorded_candidate = str(solution_review.get("candidate") or "")
    if target == "candidate":
        if recorded_candidate != relative_candidate:
            solution_errors.append(f"solution_review.candidate must be {relative_candidate}")
        if not expected_candidate.is_file():
            solution_errors.append("the recorded candidate source is missing")
    else:
        if recorded_candidate:
            solution_errors.append("a good current-source review must not record a candidate")
        if expected_candidate.is_file():
            solution_errors.append("a good current-source review must not leave a candidate file")

    findings_payload = solution_review.get("findings")
    findings: list[str] = []
    if isinstance(findings_payload, list):
        for finding in findings_payload:
            if not isinstance(finding, dict) or not str(finding.get("reason") or "").strip():
                solution_errors.append("every solution finding must contain a reason")
                continue
            findings.append(str(finding["reason"]).strip())
    else:
        solution_errors.append("solution_review.findings must be a list")
    if target == "candidate" and not findings:
        solution_errors.append("a candidate proposal requires at least one material finding")

    if solution_only or not check_cases:
        correctness_count = None
        benchmark_count = None
        complexity_method = _complexity_artifact_method(package, solution_errors)
    else:
        coverage = case_review.get("coverage")
        if (
            not isinstance(coverage, list)
            or not coverage
            or not all(isinstance(item, str) and item.strip() for item in coverage)
        ):
            case_errors.append("case_review.coverage must be a non-empty list of reviewed behaviors")
        correctness_count, benchmark_count, complexity_method = _validate_case_layout(package, case_errors)

    validation = solution_review.get("validation")
    if not isinstance(validation, dict):
        solution_errors.append("solution_review.validation must be an object")
        validation = {}
    expected_validation: dict[str, object]
    if solution_only and target == "current" and validation.get("mode") == "expert_review":
        expected_validation = {
            "mode": "expert_review",
            "judge_run": False,
            "complexity_method": complexity_method,
            "complexity_evidence": "inherited",
        }
        result_fields = {
            "correctness_cases_passed",
            "correctness_cases_total",
            "performance_cases_passed",
            "performance_cases_total",
            "complexity_passed",
        }
        unexpected_results = sorted(result_fields.intersection(validation))
        if unexpected_results:
            solution_errors.append(
                "solution_only current-source expert reviews must not claim judge or calibration results: "
                + ", ".join(unexpected_results)
            )
    else:
        expected_validation = {
            "mode": "real_test",
            "complexity_method": complexity_method,
            "complexity_passed": True,
        }
        correctness_passed = validation.get("correctness_cases_passed")
        correctness_total = validation.get("correctness_cases_total")
        if (
            not isinstance(correctness_passed, int)
            or isinstance(correctness_passed, bool)
            or correctness_passed < 1
            or correctness_passed != correctness_total
        ):
            solution_errors.append(
                "solution_review.validation must record a positive, equal number of black-box correctness passes and total cases"
            )
        elif not solution_only and check_cases and correctness_total != correctness_count:
            solution_errors.append(
                f"solution_review.validation.correctness_cases_total must be {correctness_count!r}"
            )

        performance_passed = validation.get("performance_cases_passed")
        performance_total = validation.get("performance_cases_total")
        if not solution_only and check_cases:
            if performance_passed != benchmark_count or performance_total != benchmark_count:
                solution_errors.append(
                    "solution_review.validation performance pass counts must match benchmark.json"
                )
        elif complexity_method == "benchmark":
            if (
                not isinstance(performance_passed, int)
                or isinstance(performance_passed, bool)
                or performance_passed < 1
                or performance_passed != performance_total
            ):
                solution_errors.append(
                    "candidate or retained real-test validation must record a positive, equal number of black-box performance passes and total cases"
                )
        elif performance_passed != 0 or performance_total != 0:
            solution_errors.append(
                "certificate-backed real-test validation must record zero performance cases"
            )
    for name, expected in expected_validation.items():
        if validation.get(name) != expected:
            solution_errors.append(f"solution_review.validation.{name} must be {expected!r}")

    hashes = payload.get("hashes")
    if not isinstance(hashes, dict):
        shared_errors.append("hashes must be an object")
        hashes = {}
    try:
        paths = _expected_paths(package, language, target, include_cases=not solution_only and check_cases)
    except ValueError as exc:
        shared_errors.append(str(exc))
        paths = {}
    case_hashes = {"cases_sha256"}
    if not solution_only:
        case_hashes.add("complexity_evidence_sha256")
    for name, path in paths.items():
        hash_errors = case_errors if name in case_hashes else solution_errors
        recorded = str(hashes.get(name) or "")
        if not SHA256_PATTERN.fullmatch(recorded):
            hash_errors.append(f"hashes.{name} must be a lowercase SHA-256 digest")
            continue
        if not path.is_file():
            hash_errors.append(f"reviewed artifact is missing: {path.relative_to(package)}")
            continue
        if _canonical_sha256(path) != recorded:
            stale_message = f"{path.relative_to(package)} changed after review"
            solution_stale.append(stale_message)
            if name in case_hashes:
                case_stale.append(stale_message)
    skipped_hashes = {"cases_sha256"} if not check_cases and not solution_only else set()
    extra_hashes = set(hashes) - set(paths) - skipped_hashes
    if extra_hashes:
        shared_errors.append(f"hashes contains unexpected fields: {', '.join(sorted(extra_hashes))}")
    if target == "candidate" and expected_candidate.is_file():
        current_path = package / "variants" / "optimal" / "solutions" / app_solution_filename(language)
        if current_path.is_file() and _canonical_sha256(current_path) == _canonical_sha256(expected_candidate):
            solution_errors.append("candidate source must materially differ from the current source")

    def review_status(review_errors: list[str], stale_errors: list[str]) -> str:
        if shared_errors or review_errors:
            return "invalid"
        return "stale" if stale_errors else "complete"

    solution_status = review_status(solution_errors, solution_stale)
    case_status = "unreviewed" if solution_only and not shared_errors else review_status(case_errors, case_stale)
    all_errors = [*shared_errors, *solution_errors, *case_errors, *solution_stale, *case_stale]
    return SolutionQualityStatus(
        solution_status=solution_status,
        case_status=case_status,
        review_scope=review_scope,
        verdict=verdict,
        target=target,
        candidate_path=relative_candidate if target == "candidate" else "",
        findings=tuple(findings),
        errors=tuple(all_errors),
    )
