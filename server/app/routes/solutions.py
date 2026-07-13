"""Read and write the player's three versioned solution files.

Canonical problem assets stay under the packaged ``dsa/leetcode`` tree. User
files live in the writable overlay configured by ``USER_LEETCODE_ROOT`` and
are grouped by the same problem package name.
"""
from __future__ import annotations

from pathlib import Path

from fastapi import APIRouter, HTTPException

from challenges.registry import CHALLENGE_REGISTRY
from engine.languages import SupportedLanguage, normalize_language
from engine.solutions import _solution_template
from engine.special_environments import starter_source as environment_starter_source
from server.app.schemas import (
    SolutionGet,
    SolutionPut,
    SolutionVersionsGet,
    VersionRenameRequest,
    VersionSwitchRequest,
)
from server.app.user_solutions import (
    SOLUTION_VERSIONS,
    active_solution_path,
    active_version,
    ensure_solution_versions,
    relative_user_solution_path,
    set_active_version,
    set_version_name,
    user_solution_path,
    version_names,
)


router = APIRouter()


def _get_starter(challenge, language: str | None = "python") -> str:
    spec = getattr(challenge, "_spec", None)
    if spec:
        metadata = getattr(spec, "reference_metadata", {}) or {}
        environment_starter = environment_starter_source(
            str(metadata.get("category") or ""),
            str(getattr(spec, "name", "") or spec.id),
        )
        if environment_starter and normalize_language(language) == environment_starter[0]:
            return environment_starter[1]
        return _solution_template(
            spec.id,
            heading=f"{spec.id}: {spec.name}",
            description=spec.description,
            language=language,
        )
    return ""


def _require_challenge(challenge_id: str):
    challenge_cls = CHALLENGE_REGISTRY.get(challenge_id)
    if challenge_cls is None:
        raise HTTPException(status_code=404, detail=f"Challenge '{challenge_id}' not found")
    return challenge_cls()


def _solution_path(
    challenge_id: str,
    language: str | None = "python",
    *,
    create: bool = False,
) -> Path:
    """Return the selected version file (never an unversioned alias)."""
    return active_solution_path(challenge_id, language, create=create)


def _version_path(challenge_id: str, version: int, language: str | None = "python") -> Path:
    return user_solution_path(challenge_id, language, version)


def _modified_versions(challenge_id: str, language: str, starter: str) -> list[int]:
    return [
        version
        for version in SOLUTION_VERSIONS
        if user_solution_path(challenge_id, language, version).read_text(encoding="utf-8") != starter
    ]


def _solution_response(challenge_id: str, language: str) -> SolutionVersionsGet:
    challenge = _require_challenge(challenge_id)
    starter = _get_starter(challenge, language)
    ensure_solution_versions(challenge_id, language, starter)
    selected = active_version(challenge_id, language)
    path = user_solution_path(challenge_id, language, selected)
    return SolutionVersionsGet(
        challenge_id=challenge_id,
        language=language,
        active_version=selected,
        versions=list(SOLUTION_VERSIONS),
        version_names=version_names(challenge_id, language),
        modified_versions=_modified_versions(challenge_id, language, starter),
        source=path.read_text(encoding="utf-8"),
        starter_source=starter,
        filename=relative_user_solution_path(challenge_id, language, selected),
    )


@router.get("/solutions/{challenge_id}")
def get_solution(
    challenge_id: str,
    language: SupportedLanguage = "python",
) -> SolutionVersionsGet:
    language_id = normalize_language(language)
    return _solution_response(challenge_id, language_id)


@router.put("/solutions/{challenge_id}")
def put_solution(
    challenge_id: str,
    body: SolutionPut,
    language: SupportedLanguage = "python",
) -> SolutionGet:
    challenge = _require_challenge(challenge_id)
    language_id = normalize_language(language)
    starter = _get_starter(challenge, language_id)
    ensure_solution_versions(challenge_id, language_id, starter)
    path = active_solution_path(challenge_id, language_id)
    path.write_text(body.source, encoding="utf-8")
    return SolutionGet(
        challenge_id=challenge_id,
        language=language_id,
        source=body.source,
        exists=True,
    )


@router.post("/solutions/{challenge_id}/versions/switch")
def switch_version(
    challenge_id: str,
    body: VersionSwitchRequest,
    language: SupportedLanguage = "python",
) -> SolutionVersionsGet:
    challenge = _require_challenge(challenge_id)
    language_id = normalize_language(language)
    try:
        ensure_solution_versions(
            challenge_id,
            language_id,
            _get_starter(challenge, language_id),
        )
        set_active_version(challenge_id, language_id, body.version)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return _solution_response(challenge_id, language_id)


@router.put("/solutions/{challenge_id}/versions/{version}/rename")
def rename_version(
    challenge_id: str,
    version: int,
    body: VersionRenameRequest,
    language: SupportedLanguage = "python",
) -> SolutionVersionsGet:
    _require_challenge(challenge_id)
    language_id = normalize_language(language)
    try:
        set_version_name(challenge_id, language_id, version, body.name)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return _solution_response(challenge_id, language_id)


@router.post("/solutions/{challenge_id}/versions/{version}/reset")
def reset_version(
    challenge_id: str,
    version: int,
    language: SupportedLanguage = "python",
) -> SolutionVersionsGet:
    challenge = _require_challenge(challenge_id)
    language_id = normalize_language(language)
    try:
        path = user_solution_path(challenge_id, language_id, version, create=True)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    path.write_text(_get_starter(challenge, language_id), encoding="utf-8")
    set_version_name(challenge_id, language_id, version, "")
    return _solution_response(challenge_id, language_id)
