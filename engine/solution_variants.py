"""Validation for canonical per-problem solution-approach variants."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from engine.languages import language_extension, normalize_language


VARIANT_KINDS = {"optimal", "simplified", "alternative"}
APPROACH_HEADINGS = ("General", "Complexity detail", "Alternatives and edge cases")
DEFAULT_SIMPLIFIED_ELO_CEILING = 1500.0
COMPLEXITY_BOUND_RE = re.compile(r"^O(?:\(|\\left\()")


@dataclass(frozen=True)
class SolutionVariant:
    id: str
    label: str
    kind: str
    summary: str
    directory: str
    time_complexity: str
    space_complexity: str
    approach_path: Path
    solution_paths: dict[str, Path]
    submission_path: Path
    submission_status: str
    verified_submission_id: str


@dataclass(frozen=True)
class SolutionVariantStatus:
    complete: bool
    default_variant: str = ""
    variants: tuple[SolutionVariant, ...] = ()
    errors: tuple[str, ...] = ()
    effective_elo: float | None = None
    elo_source: str = ""
    simplified_elo_ceiling: float | None = None


def _load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def _safe_relative_path(root: Path, value: Any) -> tuple[Path | None, str]:
    relative = Path(str(value or ""))
    if not str(value or "").strip() or relative.is_absolute():
        return None, "must be a non-empty relative path"
    target = (root / relative).resolve()
    try:
        target.relative_to(root.resolve())
    except ValueError:
        return None, "must stay inside the challenge package"
    return target, ""


def _effective_elo(metadata: dict[str, Any]) -> tuple[float | None, str]:
    for field in ("elo_rating", "estimated_elo_rating"):
        value = metadata.get(field)
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            return float(value), field
    return None, ""


def _validate_approach(path: Path) -> list[str]:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return ["approach.md is missing"]
    headings = tuple(re.findall(r"^##\s+(.+?)\s*$", text, flags=re.MULTILINE))
    errors: list[str] = []
    if headings != APPROACH_HEADINGS:
        errors.append(
            "approach.md headings must be General, Complexity detail, and "
            "Alternatives and edge cases in that order"
        )
        return errors
    alternatives = text.split("## Alternatives and edge cases", 1)[1].strip()
    bullets = [line for line in alternatives.splitlines() if line.startswith("- ")]
    if len(bullets) < 2:
        errors.append("approach.md must include at least two alternative or edge-case bullets")
    return errors


def _submission_status(
    path: Path,
    *,
    challenge_id: str,
    frontend_id: str,
    title_slug: str,
    variant_root: Path,
    require_verified: bool,
) -> tuple[str, str, list[str]]:
    payload = _load_json(path)
    if not isinstance(payload, dict):
        errors = ["submission.json is missing or invalid"] if require_verified else []
        return "missing", "", errors
    errors: list[str] = []
    status = str(payload.get("status") or "")
    if require_verified and status != "verified":
        errors.append("submission.json must be remotely verified")
    if str(payload.get("frontend_id") or "") != frontend_id:
        errors.append("submission frontend_id does not match metadata")
    if str(payload.get("title_slug") or "") != title_slug:
        errors.append("submission title_slug does not match metadata")
    source, source_error = _safe_relative_path(path.parent, payload.get("source"))
    if source_error:
        errors.append(f"submission source {source_error}")
    elif source is not None:
        try:
            source.relative_to(variant_root.resolve())
        except ValueError:
            errors.append("submission source must stay inside its variant")
        if not source.is_file():
            errors.append("submission source file is missing")
    verified_submission_id = str(payload.get("verified_submission_id") or "")
    if status == "verified" and not verified_submission_id:
        errors.append("submission verified_submission_id is missing")
    if status == "verified" and not str(payload.get("verified_at") or ""):
        errors.append("submission verified_at is missing")
    try:
        derived_challenge_id = f"lc_{int(frontend_id)}"
    except (TypeError, ValueError):
        derived_challenge_id = ""
    if challenge_id != derived_challenge_id:
        errors.append("challenge_id does not match frontend_id")
    return status or "missing", verified_submission_id, errors


def validate_solution_variants(
    manifest_path: Path,
    *,
    metadata: dict[str, Any],
    expected_challenge_id: str,
) -> SolutionVariantStatus:
    """Validate one canonical solution-variant manifest and every owned artifact."""

    payload = _load_json(manifest_path)
    if not isinstance(payload, dict):
        return SolutionVariantStatus(complete=False, errors=("solution_variants.json is missing or invalid",))

    package_root = manifest_path.parent
    errors: list[str] = []
    common_doc = package_root / "doc.md"
    try:
        common_doc_text = common_doc.read_text(encoding="utf-8")
    except OSError:
        common_doc_text = ""
    if "<summary>Approach</summary>" in common_doc_text:
        errors.append("the shared doc.md must not contain a branch-specific Approach")
    if "### Required Complexity" in common_doc_text:
        errors.append("the shared doc.md must not contain branch-specific Required Complexity")
    if (package_root / "solutions").exists():
        errors.append("a canonical package must not keep a root solutions directory")
    if (package_root / "submission.json").is_file():
        errors.append("a canonical package must not keep submission.json at the package root")
    if payload.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if str(payload.get("challenge_id") or "") != expected_challenge_id:
        errors.append("challenge_id does not match the package")

    metadata_config = metadata.get("solution_variants")
    if not isinstance(metadata_config, dict):
        errors.append("metadata.solution_variants must point to the variant manifest")
        metadata_config = {}
    if str(metadata_config.get("manifest") or "") != manifest_path.name:
        errors.append("metadata solution-variant manifest path does not match")

    default_variant = str(payload.get("default_variant") or "")
    if default_variant != "optimal":
        errors.append("default_variant must be optimal")
    if str(metadata_config.get("default") or "") != default_variant:
        errors.append("metadata default solution variant does not match the manifest")

    raw_alternatives_root = str(payload.get("alternatives_root") or "").strip()
    alternatives_root: Path | None = None
    if raw_alternatives_root:
        alternatives_root, alternatives_error = _safe_relative_path(
            package_root,
            raw_alternatives_root,
        )
        if alternatives_error:
            errors.append(f"alternatives_root {alternatives_error}")
        elif alternatives_root is not None and not (alternatives_root / "README.md").is_file():
            errors.append("alternatives_root must contain README.md")

    raw_policy = payload.get("simplified_policy")
    policy = raw_policy if isinstance(raw_policy, dict) else {}
    ceiling_value = policy.get("maximum_effective_elo", DEFAULT_SIMPLIFIED_ELO_CEILING)
    ceiling = (
        float(ceiling_value)
        if isinstance(ceiling_value, (int, float)) and not isinstance(ceiling_value, bool)
        else None
    )
    if ceiling is None or ceiling <= 0:
        errors.append("simplified_policy.maximum_effective_elo must be positive")
    effective_elo, elo_source = _effective_elo(metadata)

    raw_variants = payload.get("variants")
    rows = raw_variants if isinstance(raw_variants, list) else []
    if not rows:
        errors.append("variants must be a non-empty list")

    variants: list[SolutionVariant] = []
    seen_ids: set[str] = set()
    supported_languages = {
        normalize_language(str(language))
        for language in metadata.get("supported_languages", [])
        if isinstance(language, str)
    }
    primary_language = normalize_language(str(metadata.get("primary_language") or "python"))
    frontend_id = str(metadata.get("frontend_id") or "")
    title_slug = str(metadata.get("slug") or "")
    seen_directories: set[Path] = set()
    for index, raw in enumerate(rows):
        if not isinstance(raw, dict):
            errors.append(f"variant {index} must be an object")
            continue
        variant_id = str(raw.get("id") or "")
        prefix = f"variant {variant_id or index}"
        if not re.fullmatch(r"[a-z][a-z0-9_-]*", variant_id):
            errors.append(f"{prefix} id is invalid")
            continue
        if variant_id in seen_ids:
            errors.append(f"{prefix} is duplicated")
            continue
        seen_ids.add(variant_id)

        kind = str(raw.get("kind") or "")
        if kind not in VARIANT_KINDS:
            errors.append(f"{prefix} kind must be optimal, simplified, or alternative")
        if variant_id == "optimal" and kind != "optimal":
            errors.append("variant optimal must have kind optimal")
        if kind == "optimal" and variant_id != "optimal":
            errors.append(f"{prefix} is an extra optimal variant")
        if kind == "simplified" and variant_id != "simplified":
            errors.append(f"{prefix} must use the reserved simplified id")
        label = str(raw.get("label") or "").strip()
        summary = str(raw.get("summary") or "").strip()
        time_complexity = str(raw.get("time_complexity") or "").strip()
        space_complexity = str(raw.get("space_complexity") or "").strip()
        if not label:
            errors.append(f"{prefix} label is missing")
        if len(summary) < 30:
            errors.append(f"{prefix} summary is too short")
        if not COMPLEXITY_BOUND_RE.match(time_complexity):
            errors.append(f"{prefix} time_complexity must be an O(...) bound")
        if not COMPLEXITY_BOUND_RE.match(space_complexity):
            errors.append(f"{prefix} space_complexity must be an O(...) bound")

        directory = str(raw.get("directory") or "")
        variant_root, directory_error = _safe_relative_path(package_root, directory)
        if directory_error:
            errors.append(f"{prefix} directory {directory_error}")
            continue
        assert variant_root is not None
        resolved_variant_root = variant_root.resolve()
        if resolved_variant_root in seen_directories:
            errors.append(f"{prefix} directory is duplicated")
        seen_directories.add(resolved_variant_root)
        if alternatives_root is not None and resolved_variant_root == alternatives_root.resolve():
            errors.append(f"{prefix} cannot use alternatives_root as a published branch")
        if not variant_root.is_dir():
            errors.append(f"{prefix} directory is missing")

        approach_path = variant_root / "approach.md"
        errors.extend(f"{prefix}: {error}" for error in _validate_approach(approach_path))

        solution_paths: dict[str, Path] = {}
        for language in supported_languages:
            extension = language_extension(language)
            candidate = variant_root / "solutions" / f"{language}.{extension}"
            if candidate.is_file():
                solution_paths[language] = candidate
        if primary_language not in solution_paths:
            errors.append(f"{prefix} has no {primary_language} app-local solution")

        submission_path = variant_root / "submission.json"
        submission_status, submission_id, submission_errors = _submission_status(
            submission_path,
            challenge_id=expected_challenge_id,
            frontend_id=frontend_id,
            title_slug=title_slug,
            variant_root=variant_root,
            require_verified=kind != "optimal",
        )
        errors.extend(f"{prefix}: {error}" for error in submission_errors)

        if kind == "simplified":
            if str(metadata.get("difficulty") or "") not in {"Easy", "Medium"}:
                errors.append(f"{prefix} is allowed only for Easy or Medium problems")
            if effective_elo is None:
                errors.append(f"{prefix} requires real or estimated Elo")
            elif ceiling is not None and effective_elo > ceiling:
                errors.append(
                    f"{prefix} effective Elo {effective_elo:.2f} exceeds {ceiling:.2f}"
                )

        variants.append(
            SolutionVariant(
                id=variant_id,
                label=label,
                kind=kind,
                summary=summary,
                directory=directory,
                time_complexity=time_complexity,
                space_complexity=space_complexity,
                approach_path=approach_path,
                solution_paths=solution_paths,
                submission_path=submission_path,
                submission_status=submission_status,
                verified_submission_id=submission_id,
            )
        )

    if "optimal" not in seen_ids:
        errors.append("an optimal variant is required")
    if default_variant and default_variant not in seen_ids:
        errors.append("default_variant does not exist")
    if rows and isinstance(rows[0], dict) and str(rows[0].get("id") or "") != "optimal":
        errors.append("the optimal variant must be listed first")

    return SolutionVariantStatus(
        complete=not errors,
        default_variant=default_variant,
        variants=tuple(variants),
        errors=tuple(errors),
        effective_elo=effective_elo,
        elo_source=elo_source,
        simplified_elo_ceiling=ceiling,
    )
