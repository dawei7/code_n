"""Validation for profile-owned custom LeetCode problem sets."""
from __future__ import annotations

import re
from collections.abc import Iterable

from server.app.challenge_sets import leetcode_metadata_by_id


CUSTOM_PROBLEM_SETS_VERSION = 1
MAX_CUSTOM_SETS = 40
MAX_GROUP_DEPTH = 3
MAX_TOTAL_NODES = 10_000
MAX_NODES_PER_SET = 4_000
MAX_NAME_LENGTH = 80
MAX_DESCRIPTION_LENGTH = 500
_ID_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]{0,79}$")


class CustomProblemSetValidationError(ValueError):
    """Raised when a custom-set payload cannot be stored safely."""


def _clean_id(value: object, label: str) -> str:
    result = str(value or "").strip()
    if not _ID_PATTERN.fullmatch(result):
        raise CustomProblemSetValidationError(
            f"{label} must be 1-80 letters, numbers, underscores, or hyphens."
        )
    return result


def _clean_name(value: object, label: str) -> str:
    result = str(value or "").strip()
    if not result:
        raise CustomProblemSetValidationError(f"{label} cannot be empty.")
    if len(result) > MAX_NAME_LENGTH:
        raise CustomProblemSetValidationError(
            f"{label} cannot exceed {MAX_NAME_LENGTH} characters."
        )
    return result


def _clean_description(value: object) -> str:
    result = str(value or "").strip()
    if len(result) > MAX_DESCRIPTION_LENGTH:
        raise CustomProblemSetValidationError(
            f"Set descriptions cannot exceed {MAX_DESCRIPTION_LENGTH} characters."
        )
    return result


def normalize_custom_problem_sets(
    raw_sets: object,
    *,
    known_challenge_ids: Iterable[str] | None = None,
) -> list[dict]:
    """Return a compact, validated copy of a custom-set payload."""

    if not isinstance(raw_sets, list):
        raise CustomProblemSetValidationError("Custom problem sets must be a list.")
    if len(raw_sets) > MAX_CUSTOM_SETS:
        raise CustomProblemSetValidationError(
            f"A profile can store at most {MAX_CUSTOM_SETS} custom problem sets."
        )

    known_ids = (
        set(known_challenge_ids)
        if known_challenge_ids is not None
        else set(leetcode_metadata_by_id())
    )
    seen_ids: set[str] = set()
    total_nodes = 0
    normalized_sets: list[dict] = []

    def normalize_nodes(
        raw_nodes: object,
        *,
        set_name: str,
        group_depth: int,
        per_set_count: list[int],
    ) -> list[dict]:
        nonlocal total_nodes
        if not isinstance(raw_nodes, list):
            raise CustomProblemSetValidationError(
                f'"{set_name}" contains a folder with an invalid item list.'
            )

        normalized: list[dict] = []
        for raw_node in raw_nodes:
            if not isinstance(raw_node, dict):
                raise CustomProblemSetValidationError(
                    f'"{set_name}" contains an invalid tree item.'
                )
            total_nodes += 1
            per_set_count[0] += 1
            if total_nodes > MAX_TOTAL_NODES:
                raise CustomProblemSetValidationError(
                    f"A profile can store at most {MAX_TOTAL_NODES} custom tree items."
                )
            if per_set_count[0] > MAX_NODES_PER_SET:
                raise CustomProblemSetValidationError(
                    f'"{set_name}" can contain at most {MAX_NODES_PER_SET} tree items.'
                )

            node_type = str(raw_node.get("type") or "").strip()
            node_id = _clean_id(raw_node.get("id"), "Tree item id")
            if node_id in seen_ids:
                raise CustomProblemSetValidationError(
                    f'Duplicate custom tree item id "{node_id}".'
                )
            seen_ids.add(node_id)

            if node_type == "problem":
                challenge_id = str(raw_node.get("challenge_id") or "").strip()
                if challenge_id not in known_ids:
                    raise CustomProblemSetValidationError(
                        f'Unknown LeetCode problem "{challenge_id}" in "{set_name}".'
                    )
                normalized.append(
                    {
                        "type": "problem",
                        "id": node_id,
                        "challenge_id": challenge_id,
                    }
                )
                continue

            if node_type != "group":
                raise CustomProblemSetValidationError(
                    f'"{set_name}" contains an unsupported tree item type.'
                )
            next_depth = group_depth + 1
            if next_depth > MAX_GROUP_DEPTH:
                raise CustomProblemSetValidationError(
                    f'Folders in "{set_name}" cannot be nested deeper than '
                    f"{MAX_GROUP_DEPTH} levels."
                )
            normalized.append(
                {
                    "type": "group",
                    "id": node_id,
                    "name": _clean_name(raw_node.get("name"), "Folder name"),
                    "children": normalize_nodes(
                        raw_node.get("children", []),
                        set_name=set_name,
                        group_depth=next_depth,
                        per_set_count=per_set_count,
                    ),
                }
            )
        return normalized

    for raw_set in raw_sets:
        if not isinstance(raw_set, dict):
            raise CustomProblemSetValidationError("Every custom problem set must be an object.")
        set_id = _clean_id(raw_set.get("id"), "Problem-set id")
        if set_id in seen_ids:
            raise CustomProblemSetValidationError(f'Duplicate custom set id "{set_id}".')
        seen_ids.add(set_id)
        set_name = _clean_name(raw_set.get("name"), "Problem-set name")
        normalized_sets.append(
            {
                "id": set_id,
                "name": set_name,
                "description": _clean_description(raw_set.get("description")),
                "nodes": normalize_nodes(
                    raw_set.get("nodes", []),
                    set_name=set_name,
                    group_depth=0,
                    per_set_count=[0],
                ),
            }
        )

    return normalized_sets


def safely_normalize_saved_custom_problem_sets(raw_sets: object) -> list[dict]:
    """Read old or hand-edited profile data without breaking application startup."""

    try:
        return normalize_custom_problem_sets(raw_sets)
    except CustomProblemSetValidationError:
        return []
