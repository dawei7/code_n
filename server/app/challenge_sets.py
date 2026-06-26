from __future__ import annotations

from typing import Literal


AlgorithmSetId = Literal["neetcode", "leetcode", "gfg"]

KNOWN_ALGORITHM_SETS: set[str] = {"neetcode", "leetcode", "gfg"}


def normalize_algorithm_set(value: str | None) -> AlgorithmSetId:
    if value in KNOWN_ALGORITHM_SETS:
        return value  # type: ignore[return-value]
    return "neetcode"


def challenge_set_id(challenge_id: str) -> AlgorithmSetId:
    if challenge_id.startswith("nc_"):
        return "neetcode"
    if challenge_id.startswith(("lc_", "leetcode_")):
        return "leetcode"
    return "gfg"


def challenge_set_label(set_id: str) -> str:
    labels = {
        "neetcode": "NeetCode 250",
        "leetcode": "LeetCode",
        "gfg": "GeeksforGeeks",
    }
    return labels.get(set_id, set_id)
