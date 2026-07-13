"""Canonical challenge package paths.

LeetCode is stored as one folder per challenge under the DSA root. The numeric
prefix is zero-padded to four digits so filesystem and GitHub ordering match
frontend-ID order:

``dsa/leetcode/<frontend_id:04d>_<slug>/``
    ``metadata.json``
    ``doc.md``
    ``doc_de.md`` (optional)
    ``cases.json``
    ``benchmark.json``
    ``solutions/<language>.<ext>``

These packages are the sole source for challenge metadata and artifacts.
"""

from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path
from typing import Any

from engine.languages import language_extension, normalize_language
from server.app.config import LEETCODE_ROOT


LEETCODE_ID_PREFIX = "lc_"
LEETCODE_PACKAGE_ID_WIDTH = 4


def is_leetcode_id(challenge_id: str) -> bool:
    return challenge_id.startswith(LEETCODE_ID_PREFIX)


def leetcode_frontend_id(challenge_id: str) -> str:
    return challenge_id.removeprefix(LEETCODE_ID_PREFIX)


def _safe_slug(value: str) -> str:
    lowered = value.strip().lower()
    lowered = re.sub(r"[^a-z0-9]+", "-", lowered)
    return lowered.strip("-") or "challenge"


@lru_cache(maxsize=1)
def leetcode_index() -> dict[str, Any]:
    path = LEETCODE_ROOT / "index.json"
    if not path.is_file():
        return {"questions": []}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"questions": []}
    questions = payload.get("questions")
    if not isinstance(questions, list):
        return {"questions": []}
    return payload


@lru_cache(maxsize=1)
def leetcode_questions_by_frontend_id() -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for raw in leetcode_index().get("questions", []):
        if not isinstance(raw, dict):
            continue
        frontend_id = str(raw.get("frontend_id") or "")
        if frontend_id:
            result[frontend_id] = raw
    return result


def leetcode_question(challenge_id: str) -> dict[str, Any] | None:
    return leetcode_questions_by_frontend_id().get(leetcode_frontend_id(challenge_id))


def _leetcode_problem_name(challenge_id: str, *, pad_frontend_id: bool) -> str | None:
    frontend_id = leetcode_frontend_id(challenge_id)
    question = leetcode_question(challenge_id)
    slug = ""
    if question is not None:
        slug = str(question.get("slug") or question.get("title_slug") or "")
    if not slug:
        return None
    directory_id = (
        frontend_id.zfill(LEETCODE_PACKAGE_ID_WIDTH)
        if pad_frontend_id
        else frontend_id
    )
    return f"{directory_id}_{_safe_slug(slug)}"


def leetcode_package_name(challenge_id: str) -> str | None:
    """Return the zero-padded canonical resource-package name."""
    return _leetcode_problem_name(challenge_id, pad_frontend_id=True)


def leetcode_user_package_name(challenge_id: str) -> str | None:
    """Return the stable, unpadded package name used by existing user data."""
    return _leetcode_problem_name(challenge_id, pad_frontend_id=False)


def leetcode_package_dir(challenge_id: str) -> Path | None:
    name = leetcode_package_name(challenge_id)
    if name is None:
        return None
    return LEETCODE_ROOT / name


def leetcode_metadata_path(challenge_id: str) -> Path | None:
    package_dir = leetcode_package_dir(challenge_id)
    return None if package_dir is None else package_dir / "metadata.json"


@lru_cache(maxsize=4096)
def leetcode_metadata(challenge_id: str) -> dict[str, Any]:
    path = leetcode_metadata_path(challenge_id)
    if path is None or not path.is_file():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return payload if isinstance(payload, dict) else {}


def leetcode_supported_languages(challenge_id: str) -> list[str]:
    languages = leetcode_metadata(challenge_id).get("supported_languages")
    if not isinstance(languages, list):
        return []
    return [str(language) for language in languages if isinstance(language, str)]


def leetcode_runnable_in_coden(challenge_id: str) -> bool:
    metadata = leetcode_metadata(challenge_id)
    if "runnable_in_coden" not in metadata:
        return True
    return bool(metadata.get("runnable_in_coden"))


def leetcode_doc_path(challenge_id: str, lang: str = "en") -> Path | None:
    package_dir = leetcode_package_dir(challenge_id)
    if package_dir is None:
        return None
    if lang == "de":
        translated = package_dir / "doc_de.md"
        if translated.is_file():
            return translated
    doc = package_dir / "doc.md"
    return doc if doc.is_file() else None


def leetcode_solution_path(challenge_id: str, language: str | None = "python") -> Path | None:
    package_dir = leetcode_package_dir(challenge_id)
    if package_dir is None:
        return None
    language_id = normalize_language(language)
    extension = language_extension(language_id)
    return package_dir / "solutions" / f"{language_id}.{extension}"


def leetcode_cases_path(challenge_id: str) -> Path | None:
    package_dir = leetcode_package_dir(challenge_id)
    return None if package_dir is None else package_dir / "cases.json"


def leetcode_benchmark_path(challenge_id: str) -> Path | None:
    package_dir = leetcode_package_dir(challenge_id)
    return None if package_dir is None else package_dir / "benchmark.json"


def leetcode_submission_manifest_path(challenge_id: str) -> Path | None:
    package_dir = leetcode_package_dir(challenge_id)
    return None if package_dir is None else package_dir / "submission.json"


def iter_leetcode_package_dirs() -> list[Path]:
    if not LEETCODE_ROOT.is_dir():
        return []
    return sorted(
        path
        for path in LEETCODE_ROOT.iterdir()
        if path.is_dir() and (path / "metadata.json").is_file()
    )


def iter_leetcode_doc_paths() -> list[Path]:
    return [path / "doc.md" for path in iter_leetcode_package_dirs() if (path / "doc.md").is_file()]


def leetcode_package_id(package_dir: Path) -> str | None:
    metadata_path = package_dir / "metadata.json"
    if metadata_path.is_file():
        try:
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            metadata = {}
        challenge_id = str(metadata.get("challenge_id") or "")
        if challenge_id:
            return challenge_id
    match = re.match(r"^(\d+)_", package_dir.name)
    if match:
        return f"lc_{int(match.group(1))}"
    return None
