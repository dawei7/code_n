"""Resolve canonical LeetCode reference implementations."""

from __future__ import annotations

from pathlib import Path

from engine.languages import SUPPORTED_LANGUAGES, normalize_language
from challenges.spec import AlgorithmSpec
from server.app.challenge_packages import is_leetcode_id, leetcode_solution_path


def organized_solution_path(challenge_id: str, language: str | None = "python") -> Path | None:
    """Return the canonical package solution path for a LeetCode challenge."""
    language_id = normalize_language(language)
    return leetcode_solution_path(challenge_id, language_id) if is_leetcode_id(challenge_id) else None


def optimal_source_candidates(challenge_id: str, language: str | None = "python") -> list[Path]:
    organized = organized_solution_path(challenge_id, language)
    return [organized] if organized is not None else []


def load_optimal_source(
    challenge_id: str,
    spec: AlgorithmSpec,
    language: str | None = "python",
) -> str:
    """Load a file-backed reference source for a challenge."""
    language_id = normalize_language(language)

    for path in optimal_source_candidates(challenge_id, language_id):
        if path.exists():
            return path.read_text(encoding="utf-8")

    return ""


def load_optimal_sources_by_language(
    challenge_id: str,
    spec: AlgorithmSpec,
) -> dict[str, str]:
    return {
        language: load_optimal_source(challenge_id, spec, language=language)
        for language in SUPPORTED_LANGUAGES
    }
