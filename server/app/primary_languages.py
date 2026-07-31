"""Resolve each LeetCode problem's sole user-facing programming language.

The verified native submission is authoritative.  Provider language names such
as ``python3`` and ``mysql`` are mapped to the four language families exposed by
the application: Python, JavaScript, SQL, and Bash.
"""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from engine.languages import PrimaryLanguage
from server.app.challenge_packages import leetcode_submission_manifest_path


_SUBMISSION_LANGUAGE_FAMILIES: dict[str, PrimaryLanguage] = {
    "python": "python",
    "python3": "python",
    "javascript": "javascript",
    "javascript20": "javascript",
    "js": "javascript",
    "node": "javascript",
    "nodejs": "javascript",
    "sql": "sql",
    "mysql": "sql",
    "postgresql": "sql",
    "mssql": "sql",
    "oracle": "sql",
    "bash": "bash",
    "shell": "bash",
    "sh": "bash",
}


def submission_language_family(language: object) -> PrimaryLanguage | None:
    """Map a provider language name to its cOde(n) primary language family."""

    return _SUBMISSION_LANGUAGE_FAMILIES.get(str(language or "").strip().lower())


def _read_manifest(path: Path | None) -> dict[str, object]:
    if path is None or not path.is_file():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return payload if isinstance(payload, dict) else {}


def _metadata_fallback(reference_metadata: dict[str, object] | None) -> PrimaryLanguage:
    metadata = reference_metadata or {}
    configured = submission_language_family(metadata.get("primary_language"))
    if configured is not None:
        return configured
    category = str(metadata.get("category") or "").strip().lower()
    if category in {"database", "sql", "pandas"}:
        return "sql"
    if category in {"shell", "bash"}:
        return "bash"
    if category in {"javascript", "javascript_concurrency"}:
        return "javascript"
    return "python"


@lru_cache(maxsize=4096)
def _verified_primary_language(challenge_id: str) -> PrimaryLanguage | None:
    payload = _read_manifest(leetcode_submission_manifest_path(challenge_id))
    if str(payload.get("status") or "").strip().lower() != "verified":
        return None
    return submission_language_family(payload.get("language"))


def primary_language_for_challenge(
    challenge_id: str,
    reference_metadata: dict[str, object] | None = None,
) -> PrimaryLanguage:
    """Return the verified submission family, with a safe legacy fallback."""

    return _verified_primary_language(challenge_id) or _metadata_fallback(reference_metadata)


def verified_native_submission_source(
    manifest_path: Path | None,
) -> tuple[PrimaryLanguage, str] | None:
    """Read the exact source referenced by a verified submission manifest."""

    payload = _read_manifest(manifest_path)
    if str(payload.get("status") or "").strip().lower() != "verified":
        return None
    language = submission_language_family(payload.get("language"))
    source_name = str(payload.get("source") or "").strip()
    if language is None or not source_name or manifest_path is None:
        return None

    variant_root = manifest_path.parent.resolve()
    source_path = (variant_root / source_name).resolve()
    if not source_path.is_relative_to(variant_root) or not source_path.is_file():
        return None
    try:
        return language, source_path.read_text(encoding="utf-8")
    except OSError:
        return None


def optimal_native_submission_source(challenge_id: str) -> tuple[PrimaryLanguage, str] | None:
    """Return the exact verified Optimal LeetCode submission source."""

    return verified_native_submission_source(leetcode_submission_manifest_path(challenge_id))
