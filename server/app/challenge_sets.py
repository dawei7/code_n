from __future__ import annotations

import json
from functools import lru_cache
from typing import Literal

from server.app.config import LEETCODE_ROOT


AlgorithmSetId = Literal[
    "leetcode",
    "elo",
    "frequency",
    "leetcode_company",
    "leetcode_studyplan",
    "neetcode",
    "algomaster",
    "custom",
]
ResolvedAlgorithmSetId = AlgorithmSetId

KNOWN_ALGORITHM_SETS: set[str] = {
    "leetcode",
    "elo",
    "frequency",
    "leetcode_company",
    "leetcode_studyplan",
    "neetcode",
    "algomaster",
    "custom",
}
LEETCODE_VIEW_SETS: set[str] = {
    "leetcode",
    "elo",
    "frequency",
    "leetcode_company",
    "leetcode_studyplan",
}

ALGOMASTER_MANIFEST_PATH = LEETCODE_ROOT / "_meta" / "algomaster-subsets.json"


def normalize_algorithm_set(value: str | None) -> ResolvedAlgorithmSetId:
    if value in KNOWN_ALGORITHM_SETS:
        return value  # type: ignore[return-value]
    return "leetcode"


@lru_cache(maxsize=1)
def leetcode_metadata_by_id() -> dict[str, dict]:
    metadata: dict[str, dict] = {}
    if not LEETCODE_ROOT.exists():
        return metadata
    for metadata_path in LEETCODE_ROOT.glob("*/metadata.json"):
        try:
            payload = json.loads(metadata_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        challenge_id = str(payload.get("challenge_id") or "")
        if challenge_id:
            metadata[challenge_id] = payload
    return metadata


@lru_cache(maxsize=1)
def leetcode_id_by_slug() -> dict[str, str]:
    result: dict[str, str] = {}
    for challenge_id, metadata in leetcode_metadata_by_id().items():
        slug = str(metadata.get("slug") or "")
        if slug:
            result[slug] = challenge_id
    return result


def leetcode_metadata_for(challenge_id: str) -> dict:
    return leetcode_metadata_by_id().get(challenge_id, {})


def is_leetcode_challenge(challenge_id: str) -> bool:
    return challenge_id.startswith("lc_")


def is_neetcode_leetcode_challenge(challenge_id: str) -> bool:
    metadata = leetcode_metadata_for(challenge_id)
    memberships = metadata.get("neetcode_subsets")
    if isinstance(memberships, list) and memberships:
        return True
    subsets = metadata.get("subsets") if isinstance(metadata.get("subsets"), list) else []
    return "neetcode_250" in subsets or any(str(subset).startswith("neetcode:") for subset in subsets)


@lru_cache(maxsize=1)
def algomaster_manifest() -> dict:
    if not ALGOMASTER_MANIFEST_PATH.is_file():
        return {}
    try:
        payload = json.loads(ALGOMASTER_MANIFEST_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return payload if isinstance(payload, dict) else {}


@lru_cache(maxsize=1)
def algomaster_memberships_by_id() -> dict[str, tuple[dict, ...]]:
    manifest = algomaster_manifest()
    list_definitions = {
        str(item.get("slug") or ""): item
        for item in manifest.get("lists", [])
        if isinstance(item, dict) and item.get("slug")
    }
    by_challenge: dict[str, list[dict]] = {}
    for problem in manifest.get("problems", []):
        if not isinstance(problem, dict):
            continue
        challenge_id = str(problem.get("challenge_id") or "")
        if not challenge_id:
            continue
        memberships = by_challenge.setdefault(challenge_id, [])
        for list_slug in problem.get("lists", []):
            definition = list_definitions.get(str(list_slug))
            if definition is None:
                continue
            memberships.append(
                {
                    "kind": "algomaster",
                    "subset_slug": str(definition["slug"]),
                    "subset_name": str(definition.get("name") or definition["slug"]),
                    "subset_order": int(definition.get("order", 0) or 0),
                    "path": [str(problem.get("pattern") or "Uncategorized")],
                    "order": int(problem.get("order", 0) or 0),
                    "section_order": int(problem.get("pattern_order", 0) or 0),
                    "problem_order": int(problem.get("pattern_problem_order", 0) or 0),
                    "source_url": str(definition.get("source_url") or ""),
                    "leetcode_slug": str(problem.get("leetcode_slug") or ""),
                }
            )
    return {challenge_id: tuple(memberships) for challenge_id, memberships in by_challenge.items()}


def external_subset_memberships_for(challenge_id: str) -> list[dict]:
    memberships: list[dict] = []
    metadata = leetcode_metadata_for(challenge_id)
    raw_neetcode = metadata.get("neetcode_subsets")
    if isinstance(raw_neetcode, list):
        memberships.extend(
            dict(membership)
            for membership in raw_neetcode
            if isinstance(membership, dict) and str(membership.get("kind") or "") == "neetcode"
        )
    memberships.extend(dict(membership) for membership in algomaster_memberships_by_id().get(challenge_id, ()))
    return memberships


def is_algomaster_leetcode_challenge(challenge_id: str) -> bool:
    return challenge_id in algomaster_memberships_by_id()


def is_challenge_in_set(challenge_id: str, active_set: ResolvedAlgorithmSetId) -> bool:
    if active_set == "neetcode":
        return is_leetcode_challenge(challenge_id) and is_neetcode_leetcode_challenge(challenge_id)
    if active_set == "algomaster":
        return is_leetcode_challenge(challenge_id) and is_algomaster_leetcode_challenge(challenge_id)
    if active_set in LEETCODE_VIEW_SETS:
        return is_leetcode_challenge(challenge_id)
    return False


def challenge_set_label(set_id: str) -> str:
    labels = {
        "leetcode": "LeetCode problems",
        "elo": "LeetCode problems by Elo",
        "frequency": "LeetCode problems by Frequency",
        "leetcode_company": "LeetCode company subsets",
        "leetcode_studyplan": "LeetCode study-plan subsets",
        "neetcode": "NeetCode subsets of LeetCode",
        "algomaster": "AlgoMaster subsets of LeetCode",
        "custom": "Personal LeetCode problem sets",
    }
    return labels.get(set_id, set_id)
