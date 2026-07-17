"""Writable, versioned user-solution overlay for LeetCode packages.

Canonical ``dsa/leetcode`` data can live in a read-only installation. Personal
work therefore mirrors each problem below ``CODEN_HOME`` instead::

    <user-data>/dsa/leetcode/1_two-sum/user_solutions/python_v1.py
    <user-data>/dsa/leetcode/1_two-sum/user_solutions/python_v2.py
    <user-data>/dsa/leetcode/1_two-sum/user_solutions/python_v3.py

There is deliberately no unversioned "active" alias. The selected slot is
metadata, and every editor, runner, and debugger resolves that real file.
"""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path
from typing import Any, Iterable

from engine.languages import SupportedLanguage, language_extension, normalize_language
from server.app.challenge_packages import leetcode_user_package_name
from server.app.config import LEGACY_SOLUTIONS_DIR, PROJECT_ROOT, USER_LEETCODE_ROOT


SOLUTION_VERSIONS = (1, 2, 3)
_LEGACY_FILE_RE = re.compile(r"^(lc_\d+?)(?:_v([123]))?\.([A-Za-z0-9]+)$")


def _require_version(version: int) -> int:
    if version not in SOLUTION_VERSIONS:
        raise ValueError("Version must be between 1 and 3")
    return version


def user_problem_dir(challenge_id: str, *, create: bool = False) -> Path:
    package_name = leetcode_user_package_name(challenge_id)
    if package_name is None:
        raise ValueError(f"Unknown LeetCode challenge: {challenge_id}")
    path = USER_LEETCODE_ROOT / package_name
    if create:
        path.mkdir(parents=True, exist_ok=True)
    return path


def user_solution_dir(challenge_id: str, *, create: bool = False) -> Path:
    path = user_problem_dir(challenge_id, create=create) / "user_solutions"
    if create:
        path.mkdir(parents=True, exist_ok=True)
    return path


def user_solution_path(
    challenge_id: str,
    language: str | None = "python",
    version: int = 1,
    *,
    create: bool = False,
) -> Path:
    language_id = normalize_language(language)
    version = _require_version(version)
    directory = user_solution_dir(challenge_id, create=create)
    extension = language_extension(language_id)
    return directory / f"{language_id}_v{version}.{extension}"


def relative_user_solution_path(
    challenge_id: str,
    language: str | None = "python",
    version: int = 1,
) -> str:
    path = user_solution_path(challenge_id, language, version)
    return str(path.relative_to(USER_LEETCODE_ROOT.parent.parent)).replace("\\", "/")


def _state_path(challenge_id: str, *, create: bool = False) -> Path:
    return user_solution_dir(challenge_id, create=create) / "versions.json"


def _read_state(challenge_id: str) -> dict[str, Any]:
    path = _state_path(challenge_id)
    if not path.is_file():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return payload if isinstance(payload, dict) else {}


def _write_state(challenge_id: str, state: dict[str, Any]) -> None:
    path = _state_path(challenge_id, create=True)
    path.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _language_state(state: dict[str, Any], language: SupportedLanguage) -> dict[str, Any]:
    value = state.get(language)
    if not isinstance(value, dict):
        value = {"active": 1, "names": {}}
        state[language] = value
    if value.get("active") not in SOLUTION_VERSIONS:
        value["active"] = 1
    if not isinstance(value.get("names"), dict):
        value["names"] = {}
    return value


def active_version(challenge_id: str, language: str | None = "python") -> int:
    language_id = normalize_language(language)
    value = _read_state(challenge_id).get(language_id)
    if not isinstance(value, dict) or value.get("active") not in SOLUTION_VERSIONS:
        return 1
    return int(value["active"])


def set_active_version(challenge_id: str, language: str | None, version: int) -> None:
    language_id = normalize_language(language)
    version = _require_version(version)
    state = _read_state(challenge_id)
    _language_state(state, language_id)["active"] = version
    _write_state(challenge_id, state)


def version_names(challenge_id: str, language: str | None = "python") -> dict[int, str]:
    language_id = normalize_language(language)
    value = _read_state(challenge_id).get(language_id)
    if not isinstance(value, dict) or not isinstance(value.get("names"), dict):
        return {}
    result: dict[int, str] = {}
    for raw_version, raw_name in value["names"].items():
        try:
            version = int(raw_version)
        except (TypeError, ValueError):
            continue
        if version in SOLUTION_VERSIONS and isinstance(raw_name, str) and raw_name.strip():
            result[version] = raw_name.strip()
    return result


def set_version_name(
    challenge_id: str,
    language: str | None,
    version: int,
    name: str,
) -> None:
    language_id = normalize_language(language)
    version = _require_version(version)
    state = _read_state(challenge_id)
    names = _language_state(state, language_id)["names"]
    cleaned = name.strip()
    if cleaned:
        names[str(version)] = cleaned
    else:
        names.pop(str(version), None)
    _write_state(challenge_id, state)


def ensure_solution_versions(
    challenge_id: str,
    language: str | None,
    starter: str,
) -> list[Path]:
    """Create the three real version files for one language if needed."""
    language_id = normalize_language(language)
    paths: list[Path] = []
    for version in SOLUTION_VERSIONS:
        path = user_solution_path(challenge_id, language_id, version, create=True)
        if not path.exists():
            path.write_text(starter, encoding="utf-8")
        paths.append(path)
    return paths


def active_solution_path(
    challenge_id: str,
    language: str | None = "python",
    *,
    create: bool = False,
) -> Path:
    language_id = normalize_language(language)
    return user_solution_path(
        challenge_id,
        language_id,
        active_version(challenge_id, language_id),
        create=create,
    )


def _solution_deletion_targets(challenge_ids: Iterable[str]) -> list[tuple[str, Path, Path]]:
    """Resolve and validate scoped user-solution directories before deletion."""

    root = USER_LEETCODE_ROOT.resolve()
    targets: list[tuple[str, Path, Path]] = []
    for challenge_id in dict.fromkeys(str(value) for value in challenge_ids):
        problem_dir = user_problem_dir(challenge_id)
        resolved_problem_dir = problem_dir.resolve()
        if resolved_problem_dir.parent != root:
            raise RuntimeError("User solution path escaped the configured LeetCode root")

        solution_dir = problem_dir / "user_solutions"
        resolved_solution_dir = solution_dir.resolve()
        if resolved_solution_dir.parent != resolved_problem_dir or solution_dir.is_symlink():
            raise RuntimeError("User solution path failed the deletion safety check")
        if solution_dir.exists() and not solution_dir.is_dir():
            raise RuntimeError("User solution path is not a directory")
        targets.append((challenge_id, problem_dir, solution_dir))
    return targets


def _delete_legacy_user_solutions(challenge_ids: set[str]) -> int:
    """Remove matching pre-overlay files so startup migration cannot restore them."""

    if not LEGACY_SOLUTIONS_DIR.is_dir():
        return 0

    root = LEGACY_SOLUTIONS_DIR.resolve()
    deleted = 0
    for language_dir in list(LEGACY_SOLUTIONS_DIR.iterdir()):
        if not language_dir.is_dir() or language_dir.is_symlink():
            continue
        resolved_language_dir = language_dir.resolve()
        if resolved_language_dir.parent != root:
            raise RuntimeError("Legacy solution path escaped the configured user-data root")

        for source_path in list(language_dir.iterdir()):
            if not source_path.is_file() or source_path.is_symlink():
                continue
            match = _LEGACY_FILE_RE.match(source_path.name)
            if match and match.group(1) in challenge_ids:
                source_path.unlink()
                deleted += 1

        try:
            language_dir.rmdir()
        except OSError:
            pass

    state_path = LEGACY_SOLUTIONS_DIR / ".versions.json"
    if state_path.is_file() and not state_path.is_symlink():
        state = _legacy_state(state_path)
        keys_to_remove = [
            key
            for key in state
            if isinstance(key, str) and key.rsplit(":", 1)[-1] in challenge_ids
        ]
        if keys_to_remove:
            for key in keys_to_remove:
                state.pop(key, None)
            state_path.write_text(
                json.dumps(state, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
    return deleted


def delete_user_solutions(challenge_ids: Iterable[str]) -> int:
    """Delete all personal solution versions for selected LeetCode problems.

    Canonical package solutions are outside ``USER_LEETCODE_ROOT`` and are
    deliberately never considered. Matching legacy user-data files are also
    removed so the startup migration cannot recreate deleted personal work.
    """

    targets = _solution_deletion_targets(challenge_ids)
    selected_ids = {challenge_id for challenge_id, _problem_dir, _solution_dir in targets}

    deleted = 0
    for _challenge_id, problem_dir, solution_dir in targets:
        if solution_dir.is_dir():
            shutil.rmtree(solution_dir)
            deleted += 1
        try:
            problem_dir.rmdir()
        except OSError:
            pass

    return deleted + _delete_legacy_user_solutions(selected_ids)


def _legacy_state(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return payload if isinstance(payload, dict) else {}


def _legacy_active_and_names(
    state: dict[str, Any],
    challenge_id: str,
    language: str,
) -> tuple[int, dict[str, str]]:
    value = state.get(f"{language}:{challenge_id}", 1)
    if isinstance(value, dict):
        raw_active = value.get("active", 1)
        raw_names = value.get("names", {})
    else:
        raw_active = value
        raw_names = {}
    try:
        parsed_active = int(raw_active)
    except (TypeError, ValueError):
        parsed_active = 1
    active = parsed_active if parsed_active in SOLUTION_VERSIONS else 1
    names = raw_names if isinstance(raw_names, dict) else {}
    return active, {str(k): str(v) for k, v in names.items() if str(v).strip()}


def _legacy_roots(roots: Iterable[Path] | None = None) -> list[Path]:
    roots = list(roots) if roots is not None else [
        LEGACY_SOLUTIONS_DIR,
        PROJECT_ROOT / "solutions",
    ]
    unique: list[Path] = []
    seen: set[Path] = set()
    for root in roots:
        resolved = root.resolve()
        if resolved not in seen:
            seen.add(resolved)
            unique.append(root)
    return unique


def migrate_legacy_solutions(roots: Iterable[Path] | None = None) -> int:
    """Copy legacy aliases/backups into the version-only user overlay.

    Existing destinations win. Legacy files are not removed here because an
    application upgrade must never destroy user data. The repository cleanup
    removes its old tracked examples after this migration has been exercised.
    """
    migrated = 0
    for root in _legacy_roots(roots):
        if not root.is_dir() or root.resolve() == USER_LEETCODE_ROOT.resolve():
            continue
        state = _legacy_state(root / ".versions.json")
        grouped: dict[tuple[str, str], dict[int | None, Path]] = {}
        for language_dir in root.iterdir():
            if not language_dir.is_dir():
                continue
            try:
                language_id = normalize_language(language_dir.name)
            except ValueError:
                continue
            expected_extension = language_extension(language_id)
            for source_path in language_dir.iterdir():
                if not source_path.is_file():
                    continue
                match = _LEGACY_FILE_RE.match(source_path.name)
                if not match or match.group(3).lower() != expected_extension.lower():
                    continue
                challenge_id = match.group(1)
                if leetcode_user_package_name(challenge_id) is None:
                    continue
                version = int(match.group(2)) if match.group(2) else None
                grouped.setdefault((challenge_id, language_id), {})[version] = source_path

        for (challenge_id, language_id), sources in grouped.items():
            active, names = _legacy_active_and_names(state, challenge_id, language_id)
            assignments: dict[int, Path] = {}
            unversioned = sources.get(None)
            if unversioned is not None:
                assignments[active] = unversioned

            explicit_versions = {version for version in sources if version is not None}
            for version in SOLUTION_VERSIONS:
                source_path = sources.get(version)
                if source_path is None:
                    continue
                occupied = assignments.get(version)
                if occupied is None or occupied.read_bytes() == source_path.read_bytes():
                    assignments[version] = source_path
                    continue
                # Direct edits could leave the alias newer than its backup.
                # Preserve both in the next free slot instead of discarding code.
                spare = next(
                    (
                        candidate
                        for candidate in reversed(SOLUTION_VERSIONS)
                        if candidate not in assignments and candidate not in explicit_versions
                    ),
                    None,
                )
                if spare is not None:
                    assignments[spare] = source_path

            for version, source_path in assignments.items():
                destination = user_solution_path(challenge_id, language_id, version, create=True)
                if not destination.exists():
                    destination.write_bytes(source_path.read_bytes())
                    migrated += 1

            new_state = _read_state(challenge_id)
            language_state = _language_state(new_state, language_id)
            language_state["active"] = active
            if names and not language_state["names"]:
                language_state["names"] = names
            _write_state(challenge_id, new_state)
    return migrated
