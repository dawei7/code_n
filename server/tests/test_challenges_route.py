"""Tests for ``GET /api/challenges`` and ``GET /api/challenges/{id}``."""
from __future__ import annotations

from . import conftest  # noqa: F401
from challenges.registry import CHALLENGE_REGISTRY
from server.app.optimal_sources import organized_solution_path
from server.app.leetcode_mapping import LEETCODE_MAPPING


class ListChallengesTest(conftest._Base):
    def test_list_returns_all_registered(self) -> None:
        r = self.client.get("/api/challenges")
        self.assertEqual(r.status_code, 200, r.text)
        body = r.json()
        self.assertIsInstance(body, list)
        # The registry has 25+ entries (intro, sorting, searching, graphs, dynamic, greedy).
        self.assertGreaterEqual(len(body), 25, f"Got {len(body)} challenges; expected at least 25")
        ids = {c["id"] for c in body}
        self.assertIn("sort_01", ids)
        self.assertIn("search_01", ids)

    def test_summary_has_required_fields(self) -> None:
        r = self.client.get("/api/challenges")
        self.assertEqual(r.status_code, 200)
        summary = next(c for c in r.json() if c["id"] == "sort_01")
        for field in (
            "id", "name", "category", "difficulty", "required_complexity",
            "description", "max_n",
        ):
            self.assertIn(field, summary, f"missing field {field!r}")
        self.assertEqual(summary["id"], "sort_01")
        self.assertEqual(summary["required_complexity"], "O(n²)")

    def test_unknown_challenge_returns_404(self) -> None:
        r = self.client.get("/api/challenges/does_not_exist")
        self.assertEqual(r.status_code, 404)

    def test_leetcode_set_is_selectable_and_filtered(self) -> None:
        progress = self.client.put("/api/progress", json={"active_set": "leetcode"})
        self.assertEqual(progress.status_code, 200, progress.text)
        self.assertEqual(progress.json()["active_set"], "leetcode")

        r = self.client.get("/api/challenges")
        self.assertEqual(r.status_code, 200, r.text)
        ids = [c["id"] for c in r.json()]
        self.assertGreater(len(ids), 100)
        self.assertTrue(all(cid.startswith(("lc_", "leetcode_")) for cid in ids))

        detail = self.client.get("/api/challenges/sort_01")
        self.assertEqual(detail.status_code, 404)
        self.assertIn("LeetCode", detail.text)

    def test_leetcode_specs_generate_sized_inputs_from_contract(self) -> None:
        challenge = CHALLENGE_REGISTRY["lc_1002"]()
        setup = challenge.setup(16, seed=1)

        self.assertEqual(list(setup), ["words"])
        self.assertEqual(len(setup["words"]), 16)
        self.assertTrue(all(isinstance(word, str) and word for word in setup["words"]))
        self.assertNotEqual(setup["words"], [])

    def test_leetcode_difficulty_uses_ten_level_acceptance_bands(self) -> None:
        self.client.put("/api/progress", json={"active_set": "leetcode"})
        response = self.client.get("/api/challenges")
        self.assertEqual(response.status_code, 200, response.text)

        summaries = response.json()
        expected_ranges = {"Easy": range(1, 4), "Medium": range(4, 7), "Hard": range(7, 11)}
        seen_levels: set[int] = set()
        for summary in summaries:
            label = summary["difficulty_label"]
            self.assertIn(label, expected_ranges)
            self.assertIn(summary["difficulty"], expected_ranges[label])
            self.assertIsInstance(summary["acceptance_rate"], float)
            seen_levels.add(summary["difficulty"])

        self.assertEqual(seen_levels, set(range(1, 11)))

    def test_leetcode_summary_preserves_all_topic_categories(self) -> None:
        self.client.put("/api/progress", json={"active_set": "leetcode"})
        response = self.client.get("/api/challenges")
        self.assertEqual(response.status_code, 200, response.text)

        two_sum = next(item for item in response.json() if item["id"] == "lc_1")
        self.assertEqual(two_sum["category"], "leetcode_array")
        self.assertEqual(
            two_sum["categories"],
            ["leetcode_array", "leetcode_hash_table"],
        )

    def test_unknown_algorithm_set_falls_back_to_neetcode(self) -> None:
        progress = self.client.put("/api/progress", json={"active_set": "mystery"})
        self.assertEqual(progress.status_code, 200, progress.text)
        self.assertEqual(progress.json()["active_set"], "neetcode")

    def test_neetcode_leetcode_slugs_match_problem_urls(self) -> None:
        self.assertEqual(LEETCODE_MAPPING["nc_1"]["slug"], "concatenation-of-array")
        self.assertEqual(LEETCODE_MAPPING["nc_2"]["slug"], "contains-duplicate")

        for challenge_id, leetcode in LEETCODE_MAPPING.items():
            if not challenge_id.startswith("nc_"):
                continue
            slug = leetcode["url"].rstrip("/").split("/")[-1]
            self.assertEqual(
                leetcode["slug"],
                slug,
                f"{challenge_id} should use the LeetCode title slug",
            )


class GetChallengeDetailTest(conftest._Base):
    def test_sort_01_detail(self) -> None:
        r = self.client.get("/api/challenges/sort_01")
        self.assertEqual(r.status_code, 200, r.text)
        body = r.json()
        self.assertEqual(body["id"], "sort_01")
        self.assertIn("params", body)
        # Sort challenges have `data` and `n` as parameters.
        param_names = {p["name"] for p in body["params"]}
        self.assertIn("data", param_names)
        self.assertIn("n", param_names)
        # The starter source is a `def solve(...)` template.
        self.assertTrue(body["starter_source"].startswith('"""\nDescription\n-----------\n'))
        self.assertIn("def solve(data, n):", body["starter_source"])
        self.assertIn("\nExamples\n--------\n", body["starter_source"])
        self.assertNotIn("1. Description", body["starter_source"])
        self.assertNotIn("2. Examples", body["starter_source"])
        self.assertNotIn("Inputs passed to solve():", body["starter_source"])
        self.assertNotIn("\nGoal:\n", body["starter_source"])
        # The optimal source is the canonical bubble sort.
        self.assertIn("data[i], data[i + 1] = data[i + 1], data[i]", body["optimal_source"])
        # samples are surfaced (sort_01 has at least 1).
        self.assertIsInstance(body["samples"], list)

    def test_optimal_source_uses_organized_docs_mirror_path(self) -> None:
        path = organized_solution_path("sort_01")
        self.assertIsNotNone(path)
        self.assertEqual(
            path.parts[-3:],
            ("geeksforgeeks", "sorting", "sort_01_bubble-sort.py"),
        )
        self.assertTrue(path.exists(), f"missing organized optimal source: {path}")

        r = self.client.get("/api/challenges/sort_01")
        self.assertEqual(r.status_code, 200, r.text)
        self.assertIn("data[i], data[i + 1] = data[i + 1], data[i]", r.json()["optimal_source"])
