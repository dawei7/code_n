"""Validation for non-scaling complexity-verification certificates.

Scaling benchmarks remain the default complexity judge. A certificate is
valid only for a source contract whose legal workload cannot support an
honest scaling verdict, or whose required bound is already matched by a
problem-level lower bound. Certificates record the replacement evidence; they
never contain runtime tiers or relax correctness checking.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


CERTIFICATE_METHODS = {
    "bounded_domain",
    "asymptotic_optimality",
    "bounded_concurrency",
}

CHECK_KINDS = {
    "bounded_work_proof",
    "exhaustive_domain",
    "boundary_property_cases",
    "lower_bound_proof",
    "upper_bound_proof",
    "scheduler_stress",
    "semantic_validator",
    "deadlock_timeout",
}

METHOD_CHECKS = {
    "bounded_domain": (
        {"bounded_work_proof"},
        ({"exhaustive_domain", "boundary_property_cases"},),
    ),
    "asymptotic_optimality": (
        {"lower_bound_proof", "upper_bound_proof", "boundary_property_cases"},
        (),
    ),
    "bounded_concurrency": (
        {"bounded_work_proof", "scheduler_stress", "semantic_validator", "deadlock_timeout"},
        (),
    ),
}


@dataclass(frozen=True)
class ComplexityCertificateStatus:
    complete: bool
    challenge_id: str = ""
    method: str = ""
    required_time: str = ""
    summary: str = ""
    check_kinds: tuple[str, ...] = ()
    errors: tuple[str, ...] = ()


def validate_complexity_certificate(
    payload: Any,
    *,
    expected_challenge_id: str = "",
    expected_required_time: str = "",
) -> ComplexityCertificateStatus:
    """Return a strict, machine-readable certificate status."""

    errors: list[str] = []
    if not isinstance(payload, dict):
        return ComplexityCertificateStatus(complete=False, errors=("certificate must be a JSON object",))

    if payload.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    challenge_id = str(payload.get("challenge_id") or "")
    if not challenge_id.startswith("lc_"):
        errors.append("challenge_id must use the lc_<frontend_id> form")
    if expected_challenge_id and challenge_id != expected_challenge_id:
        errors.append(f"challenge_id must match {expected_challenge_id}")
    if payload.get("status") != "verified":
        errors.append("status must be verified")

    method = str(payload.get("method") or "")
    if method not in CERTIFICATE_METHODS:
        errors.append(f"method must be one of {', '.join(sorted(CERTIFICATE_METHODS))}")
    required_time = str(payload.get("required_time") or "")
    if not (required_time.startswith("O(") and required_time.endswith(")")):
        errors.append("required_time must be an O(...) bound")
    if expected_required_time and required_time != expected_required_time:
        errors.append(f"required_time must match {expected_required_time}")
    summary = str(payload.get("summary") or "").strip()
    if len(summary) < 40:
        errors.append("summary must explain why scaling is not applicable")

    raw_checks = payload.get("replacement_checks")
    checks = raw_checks if isinstance(raw_checks, list) else []
    if not checks:
        errors.append("replacement_checks must be a non-empty list")
    check_kinds: list[str] = []
    for index, check in enumerate(checks):
        if not isinstance(check, dict):
            errors.append(f"replacement_checks[{index}] must be an object")
            continue
        kind = str(check.get("kind") or "")
        evidence = str(check.get("evidence") or "").strip()
        if kind not in CHECK_KINDS:
            errors.append(f"replacement_checks[{index}].kind is invalid")
        elif kind in check_kinds:
            errors.append(f"replacement check {kind} is duplicated")
        else:
            check_kinds.append(kind)
        if len(evidence) < 20:
            errors.append(f"replacement_checks[{index}].evidence is incomplete")

    if method in {"bounded_domain", "bounded_concurrency"}:
        bound = payload.get("workload_bound")
        if not isinstance(bound, dict):
            errors.append("workload_bound must be an object for bounded methods")
        else:
            if not str(bound.get("symbol") or "").strip():
                errors.append("workload_bound.symbol is required")
            maximum = bound.get("maximum")
            if not isinstance(maximum, int) or isinstance(maximum, bool) or maximum <= 0:
                errors.append("workload_bound.maximum must be a positive integer")
            if not str(bound.get("unit") or "").strip():
                errors.append("workload_bound.unit is required")
            if len(str(bound.get("source_constraint") or "").strip()) < 10:
                errors.append("workload_bound.source_constraint is incomplete")

    if method == "asymptotic_optimality":
        optimality = payload.get("optimality")
        if not isinstance(optimality, dict):
            errors.append("optimality must be an object for asymptotic_optimality")
        else:
            if not str(optimality.get("symbol") or "").strip():
                errors.append("optimality.symbol is required")
            if not str(optimality.get("lower_bound") or "").startswith("Omega("):
                errors.append("optimality.lower_bound must be an Omega(...) bound")
            if not str(optimality.get("upper_bound") or "").startswith("O("):
                errors.append("optimality.upper_bound must be an O(...) bound")
            if len(str(optimality.get("argument") or "").strip()) < 40:
                errors.append("optimality.argument is incomplete")

    required, alternatives = METHOD_CHECKS.get(method, (set(), ()))
    missing = required - set(check_kinds)
    if missing:
        errors.append(f"missing replacement checks: {', '.join(sorted(missing))}")
    for choices in alternatives:
        if not set(check_kinds) & choices:
            errors.append(f"one replacement check is required from: {', '.join(sorted(choices))}")

    return ComplexityCertificateStatus(
        complete=not errors,
        challenge_id=challenge_id,
        method=method,
        required_time=required_time,
        summary=summary,
        check_kinds=tuple(check_kinds),
        errors=tuple(errors),
    )
