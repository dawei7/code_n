"""Integrity checks for AlgoMaster views over canonical LeetCode packages."""

from __future__ import annotations

import json
from pathlib import Path


LEETCODE_ROOT = Path(__file__).resolve().parents[1] / "dsa" / "leetcode"
MANIFEST_PATH = LEETCODE_ROOT / "_meta" / "algomaster-subsets.json"
SUBSETS_PATH = LEETCODE_ROOT / "subsets.json"
EXPECTED_COUNTS = {"am-600": 600, "am-300": 300, "am-150": 150, "am-75": 75}


def test_algomaster_manifest_maps_to_canonical_leetcode_packages() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    index = json.loads((LEETCODE_ROOT / "index.json").read_text(encoding="utf-8"))
    canonical_by_id = {f"lc_{question['frontend_id']}": question for question in index["questions"]}
    records = manifest["problems"]

    assert manifest["problem_count"] == 600
    assert len(records) == 600
    assert len({record["challenge_id"] for record in records}) == 600
    assert [record["order"] for record in records] == list(range(1, 601))

    for record in records:
        canonical = canonical_by_id[record["challenge_id"]]
        assert record["leetcode_slug"] == canonical["slug"]
        frontend_id = str(canonical["frontend_id"]).zfill(4)
        package = LEETCODE_ROOT / f"{frontend_id}_{canonical['slug']}"
        assert (package / "metadata.json").is_file()


def test_algomaster_lists_have_exact_nested_membership() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    memberships = {
        slug: {
            record["challenge_id"]
            for record in manifest["problems"]
            if slug in record["lists"]
        }
        for slug in EXPECTED_COUNTS
    }

    assert {item["slug"]: item["count"] for item in manifest["lists"]} == EXPECTED_COUNTS
    assert {slug: len(challenge_ids) for slug, challenge_ids in memberships.items()} == EXPECTED_COUNTS
    assert memberships["am-75"] < memberships["am-150"] < memberships["am-300"] < memberships["am-600"]

    by_slug = {record["leetcode_slug"]: record for record in manifest["problems"]}
    assert by_slug["linked-list-cycle-ii"]["challenge_id"] == "lc_142"
    assert by_slug["boats-to-save-people"]["challenge_id"] == "lc_881"


def test_algomaster_lists_are_registered_in_the_subset_catalog() -> None:
    payload = json.loads(SUBSETS_PATH.read_text(encoding="utf-8"))
    records = {
        subset["slug"]: subset
        for subset in payload["subsets"]
        if subset.get("provider") == "algomaster"
    }

    assert payload["count"] == len(payload["subsets"])
    assert {record["name"] for record in records.values()} == {
        "AlgoMaster 600",
        "AlgoMaster 300",
        "AlgoMaster 150",
        "AlgoMaster 75",
    }
    assert {record["count"] for record in records.values()} == {600, 300, 150, 75}
