"""Tests for profile-owned custom problem sets."""
from __future__ import annotations

from server.app.custom_problem_sets import safely_normalize_saved_custom_problem_sets

from . import conftest


class CustomProblemSetsTest(conftest._Base):
    def test_fresh_profile_has_no_custom_sets(self) -> None:
        response = self.client.get("/api/custom-problem-sets")
        self.assertEqual(response.status_code, 200, response.text)
        self.assertEqual(response.json(), {"version": 1, "sets": []})

    def test_saves_and_round_trips_three_group_levels(self) -> None:
        payload = {
            "sets": [
                {
                    "id": "set_interview",
                    "name": "Interview path",
                    "description": "A focused progression.",
                    "career_mode": True,
                    "nodes": [
                        {
                            "type": "group",
                            "id": "group_arrays",
                            "name": "Arrays",
                            "children": [
                                {
                                    "type": "group",
                                    "id": "group_windows",
                                    "name": "Windows",
                                    "children": [
                                        {
                                            "type": "group",
                                            "id": "group_review",
                                            "name": "Review",
                                            "children": [
                                                {
                                                    "type": "problem",
                                                    "id": "item_two_sum",
                                                    "challenge_id": "lc_1",
                                                }
                                            ],
                                        }
                                    ],
                                }
                            ],
                        },
                        {
                            "type": "problem",
                            "id": "item_add_two",
                            "challenge_id": "lc_2",
                        },
                    ],
                }
            ]
        }
        saved = self.client.put("/api/custom-problem-sets", json=payload)
        self.assertEqual(saved.status_code, 200, saved.text)
        self.assertEqual(saved.json()["sets"], payload["sets"])
        self.assertEqual(self.client.get("/api/custom-problem-sets").json()["sets"], payload["sets"])

    def test_rejects_a_fourth_group_level(self) -> None:
        node: dict = {
            "type": "problem",
            "id": "item_two_sum",
            "challenge_id": "lc_1",
        }
        for depth in range(4, 0, -1):
            node = {
                "type": "group",
                "id": f"group_{depth}",
                "name": f"Level {depth}",
                "children": [node],
            }
        response = self.client.put(
            "/api/custom-problem-sets",
            json={
                "sets": [
                    {
                        "id": "set_too_deep",
                        "name": "Too deep",
                        "description": "",
                        "nodes": [node],
                    }
                ]
            },
        )
        self.assertEqual(response.status_code, 422, response.text)
        self.assertIn("3 levels", response.json()["detail"])

    def test_rejects_unknown_problems_and_deduplicates_each_leaf(self) -> None:
        unknown = self.client.put(
            "/api/custom-problem-sets",
            json={
                "sets": [
                    {
                        "id": "set_unknown",
                        "name": "Unknown",
                        "description": "",
                        "nodes": [
                            {
                                "type": "problem",
                                "id": "item_unknown",
                                "challenge_id": "lc_99999999",
                            }
                        ],
                    }
                ]
            },
        )
        self.assertEqual(unknown.status_code, 422, unknown.text)
        self.assertIn("Unknown LeetCode problem", unknown.json()["detail"])

        repeated = self.client.put(
            "/api/custom-problem-sets",
            json={
                "sets": [
                    {
                        "id": "set_duplicate",
                        "name": "Duplicate",
                        "description": "",
                        "nodes": [
                            {"type": "problem", "id": "item_one", "challenge_id": "lc_1"},
                            {"type": "problem", "id": "item_two", "challenge_id": "lc_1"},
                            {
                                "type": "group",
                                "id": "group_second_leaf",
                                "name": "Second leaf",
                                "children": [
                                    {
                                        "type": "problem",
                                        "id": "item_three",
                                        "challenge_id": "lc_1",
                                    }
                                ],
                            },
                        ],
                    }
                ]
            },
        )
        self.assertEqual(repeated.status_code, 200, repeated.text)
        self.assertEqual(
            [
                node["challenge_id"]
                for node in repeated.json()["sets"][0]["nodes"]
                if node["type"] == "problem"
            ],
            ["lc_1"],
        )
        self.assertEqual(
            repeated.json()["sets"][0]["nodes"][1]["children"][0]["challenge_id"],
            "lc_1",
        )

    def test_limits_personal_to_five_root_sets(self) -> None:
        sets = [
            {
                "id": f"set_{index}",
                "name": f"Root {index}",
                "description": "",
                "nodes": [],
            }
            for index in range(6)
        ]
        response = self.client.put("/api/custom-problem-sets", json={"sets": sets})
        self.assertEqual(response.status_code, 422, response.text)
        self.assertIn("at most 5", response.json()["detail"])

    def test_reads_legacy_roots_without_silently_deleting_them(self) -> None:
        legacy_sets = [
            {
                "id": f"set_legacy_{index}",
                "name": f"Legacy root {index}",
                "description": "",
                "nodes": [],
            }
            for index in range(6)
        ]
        normalized = safely_normalize_saved_custom_problem_sets(legacy_sets)
        self.assertEqual(len(normalized), 6)
        self.assertTrue(all(set_data["career_mode"] is False for set_data in normalized))

    def test_custom_view_is_a_persisted_algorithm_set(self) -> None:
        response = self.client.put("/api/progress", json={"active_set": "custom"})
        self.assertEqual(response.status_code, 200, response.text)
        self.assertEqual(response.json()["active_set"], "custom")

    def test_custom_sets_are_isolated_per_profile(self) -> None:
        payload = {
            "sets": [
                {
                    "id": "set_default",
                        "name": "Default profile set",
                        "description": "",
                        "career_mode": False,
                    "nodes": [
                        {"type": "problem", "id": "item_one", "challenge_id": "lc_1"}
                    ],
                }
            ]
        }
        saved = self.client.put("/api/custom-problem-sets", json=payload)
        self.assertEqual(saved.status_code, 200, saved.text)

        created = self.client.post(
            "/api/profiles",
            json={"name": "Second", "career_mode": False, "leetcode_username": ""},
        )
        self.assertEqual(created.status_code, 200, created.text)
        self.assertEqual(self.client.get("/api/custom-problem-sets").json()["sets"], [])

        selected = self.client.post("/api/profiles/Default/select")
        self.assertEqual(selected.status_code, 200, selected.text)
        self.assertEqual(self.client.get("/api/custom-problem-sets").json()["sets"], payload["sets"])
