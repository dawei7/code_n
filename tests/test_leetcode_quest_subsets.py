"""Integrity checks for official LeetCode Quest views."""

from __future__ import annotations

import json
from pathlib import Path


LEETCODE_ROOT = Path(__file__).resolve().parents[1] / "dsa" / "leetcode"
MANIFEST_PATH = LEETCODE_ROOT / "_meta" / "leetcode-quest-subsets.json"
SUBSETS_PATH = LEETCODE_ROOT / "subsets.json"
EXPECTED_QUESTS = {
    "data-structures-and-algorithms-quest": ("Data Structures and Algorithms", 39, 119),
    "database-quest": ("Database", 5, 19),
    "system-and-software-design-quest": ("System & Software Design", 5, 13),
    "maths-quest": ("Maths", 7, 22),
    "2026-spring-sprint": ("2026 Spring Sprint", 12, 36),
}


def _manifest() -> dict:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def test_quest_manifest_maps_only_to_canonical_leetcode_packages() -> None:
    manifest = _manifest()
    index = json.loads((LEETCODE_ROOT / "index.json").read_text(encoding="utf-8"))
    canonical_by_id = {
        f"lc_{question['frontend_id']}": question for question in index["questions"]
    }

    assert manifest["provider"] == "LeetCode"
    assert manifest["kind"] == "quest"
    assert manifest["quest_count"] == 5
    assert manifest["problem_count"] == 204
    assert manifest["membership_count"] == len(manifest["problems"]) == 209

    for record in manifest["problems"]:
        canonical = canonical_by_id[record["challenge_id"]]
        assert record["leetcode_slug"] == canonical["slug"]
        assert int(canonical["frontend_id"]) <= 4005
        package = LEETCODE_ROOT / (
            f"{str(canonical['frontend_id']).zfill(4)}_{canonical['slug']}"
        )
        assert (package / "metadata.json").is_file()


def test_quest_hierarchy_and_problem_order_are_exact() -> None:
    manifest = _manifest()
    quests = manifest["quests"]
    assert [quest["slug"] for quest in quests] == list(EXPECTED_QUESTS)
    assert {
        quest["slug"]: (quest["name"], quest["level_count"], quest["count"])
        for quest in quests
    } == EXPECTED_QUESTS

    memberships_by_level: dict[str, list[dict]] = {}
    for membership in manifest["problems"]:
        memberships_by_level.setdefault(membership["favorite_slug"], []).append(membership)

    for level in manifest["levels"]:
        memberships = memberships_by_level[level["favorite_slug"]]
        assert level["count"] == level["source_question_count"] == len(memberships)
        assert level["challenge_ids"] == [
            membership["challenge_id"]
            for membership in sorted(memberships, key=lambda item: item["problem_order"])
        ]
        assert "assignment" not in level["favorite_slug"]

    first_level = manifest["levels"][0]
    assert first_level["favorite_slug"] == "dsa-linear-shoal-array-i"
    assert first_level["challenge_ids"] == ["lc_1929", "lc_1470", "lc_485"]

    for quest in quests:
        orders = [
            membership["order"]
            for membership in manifest["problems"]
            if membership["quest_slug"] == quest["slug"]
        ]
        assert orders == list(range(1, quest["membership_count"] + 1))


def test_quests_are_registered_in_the_subset_catalog() -> None:
    payload = json.loads(SUBSETS_PATH.read_text(encoding="utf-8"))
    records = [
        subset
        for subset in payload["subsets"]
        if subset.get("provider") == "leetcode_quest"
    ]

    assert payload["count"] == len(payload["subsets"])
    assert [record["name"] for record in records] == [
        values[0] for values in EXPECTED_QUESTS.values()
    ]
    assert {
        record["name"]: record["count"] for record in records
    } == {
        values[0]: values[2] for values in EXPECTED_QUESTS.values()
    }
    assert all(
        challenge_id.startswith("lc_")
        for record in records
        for challenge_id in record["challenge_ids"]
    )
