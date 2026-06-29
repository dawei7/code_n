"""Tests for ``GET /api/challenges`` and ``GET /api/challenges/{id}``."""
from __future__ import annotations

import math
from unittest.mock import patch

from . import conftest  # noqa: F401
from challenges.registry import CHALLENGE_REGISTRY
from challenges.algorithms.codechef import CODECHEF_CAREER_PATHS
from server.app.ast_ops import count_ops as ast_count_ops
from server.app import progress_store
from server.app.codechef_sources import best_codechef_source
from server.app.codechef_community import load_cached_source
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

    def test_codechef_visible_paths_are_selectable_and_deduplicated(self) -> None:
        progress = self.client.put("/api/progress", json={"active_set": "codechef"})
        self.assertEqual(progress.status_code, 200, progress.text)

        response = self.client.get("/api/challenges")
        self.assertEqual(response.status_code, 200, response.text)
        ids = [item["id"] for item in response.json()]
        self.assertEqual(len(ids), 1_646)
        self.assertEqual(len(ids), len(set(ids)))
        self.assertTrue(all(challenge_id.startswith("cc_") for challenge_id in ids))
        self.assertNotIn("cc_ATIME01", ids)
        self.assertNotIn("cc_BSMCQ1", ids)
        self.assertIn("cc_CWC23QUALIF", ids)
        self.assertIn("cc_AIRLINES", ids)
        self.assertFalse(
            {"cc_PTREE", "cc_MATDEF", "cc_MATMCQ1", "cc_MATTYPES"} & set(ids)
        )
        categories = {category for item in response.json() for category in item["categories"]}
        self.assertEqual(len(categories), 57)
        self.assertFalse(any("difficulty_rating_wise" in category for category in categories))
        self.assertFalse(any("star_wise_paths" in category for category in categories))
        self.assertTrue(any("become_5_star" in category for category in categories))
        self.assertTrue(any("data_structures_and_algorithms" in category for category in categories))
        airlines = next(item for item in response.json() if item["id"] == "cc_AIRLINES")
        self.assertEqual(airlines["difficulty_label"], "475")
        become_5_star_2500 = [
            category for category in categories
            if "codechef_become_5_star" in category and "2000_to_2500_difficulty_problems" in category
        ]
        self.assertEqual(len(become_5_star_2500), 1)

    def test_codechef_career_mode_gates_become_5_star_by_rating(self) -> None:
        progress = self.client.put(
            "/api/progress",
            json={"active_set": "codechef", "career_mode": True},
        )
        self.assertEqual(progress.status_code, 200, progress.text)

        response = self.client.get("/api/challenges")
        self.assertEqual(response.status_code, 200, response.text)
        body = response.json()
        unlocked = {item["id"] for item in body if item["unlocked"]}
        self.assertEqual(len(CODECHEF_CAREER_PATHS), 1)
        career_path = CODECHEF_CAREER_PATHS[0]
        self.assertIn(career_path[0], unlocked)
        self.assertNotIn(career_path[1], unlocked)
        self.assertTrue(
            any(
                item["id"] not in set(career_path)
                and any("codechef_data_structures_and_algorithms" in category for category in item["categories"])
                and item["unlocked"]
                for item in body
            )
        )

        ratings = [
            CHALLENGE_REGISTRY[challenge_id]()._spec.difficulty_label
            for challenge_id in career_path
        ]
        numeric_ratings = [int(rating) for rating in ratings if rating.isdigit()]
        self.assertEqual(numeric_ratings, sorted(numeric_ratings))

        locked_id = career_path[1]
        locked = self.client.get(f"/api/challenges/{locked_id}")
        self.assertEqual(locked.status_code, 403, locked.text)

        stored = progress_store.load()
        stored.complete(career_path[0], 1, "O(1)")
        progress_store.save(stored)
        advanced = self.client.get("/api/challenges")
        newly_unlocked = {item["id"] for item in advanced.json() if item["unlocked"]}
        self.assertIn(locked_id, newly_unlocked)

    def test_codechef_become_5_star_ladder_is_locked_even_when_global_career_off(self) -> None:
        self.client.put(
            "/api/progress",
            json={"active_set": "codechef", "career_mode": False},
        )
        response = self.client.get("/api/challenges")
        self.assertEqual(response.status_code, 200, response.text)
        body = response.json()
        career_path = CODECHEF_CAREER_PATHS[0]
        unlocked = {item["id"] for item in body if item["unlocked"]}
        self.assertIn(career_path[0], unlocked)
        self.assertNotIn(career_path[1], unlocked)
        self.assertTrue(
            any(
                item["unlocked"]
                for item in body
                if item["id"] not in set(career_path)
                and any("codechef_data_structures_and_algorithms" in category for category in item["categories"])
            )
        )

    def test_codechef_detail_preserves_official_story_text(self) -> None:
        progress = self.client.put(
            "/api/progress",
            json={"active_set": "codechef", "career_mode": False, "player_name": "Mira"},
        )
        self.assertEqual(progress.status_code, 200, progress.text)

        response = self.client.get("/api/challenges/cc_BWFPF01")
        self.assertEqual(response.status_code, 200, response.text)
        body = response.json()
        self.assertEqual(body["name"], "Chef Builds Subsets")
        self.assertIn("Chef has a list of integers", body["description"])
        self.assertEqual(body["optimal_source"], "")
        self.assertEqual(len(body["samples"]), 3)

    def test_codechef_python_solution_is_ast_reference_baseline(self) -> None:
        self.client.put(
            "/api/progress",
            json={"active_set": "codechef", "career_mode": False},
        )
        spec = CHALLENGE_REGISTRY["cc_BWFPF01"]()._spec
        self.assertIn("PYTH", spec.reference_language.upper())

        response = self.client.post(
            "/api/challenges/cc_BWFPF01/run",
            json={"source": "def solve(input_data):\n    return None\n", "n": 10, "mode": "practice"},
        )
        self.assertEqual(response.status_code, 200, response.text)
        reference_source = load_cached_source("cc_BWFPF01") or spec.reference_source
        self.assertEqual(
            response.json()["reference_ast_ops"],
            ast_count_ops(reference_source, 10),
        )

    def test_codechef_specs_generate_sample_shaped_stdin(self) -> None:
        challenge = CHALLENGE_REGISTRY["cc_AIRLINES"]()
        setup = challenge.setup(8, seed=1)

        self.assertEqual(list(setup), ["input_data"])
        lines = setup["input_data"].strip().splitlines()
        self.assertEqual(lines[0], "8")
        self.assertEqual(lines[1:5], ["2 15 10", "1 10 1", "5 60 100", "1 11 7"])
        self.assertEqual(lines[5:9], ["2 15 10", "1 10 1", "5 60 100", "1 11 7"])
        self.assertTrue(challenge.verify("150\n10\n5000\n70\n150\n10\n5000\n70"))

    def test_codechef_starter_template_separates_sample_test_cases(self) -> None:
        self.client.put(
            "/api/progress",
            json={"active_set": "codechef", "career_mode": False},
        )
        stored = progress_store.load()
        career_path = CODECHEF_CAREER_PATHS[0]
        for challenge_id in career_path[:career_path.index("cc_AIRLINES")]:
            stored.complete(challenge_id, 1, "O(1)")
        progress_store.save(stored)
        response = self.client.get("/api/challenges/cc_AIRLINES")
        self.assertEqual(response.status_code, 200, response.text)

        starter = response.json()["starter_source"]
        self.assertIn("Example 1 (official combined stdin/stdout):", starter)
        self.assertIn("Input:\n  4\n  2 15 10\n  1 10 1", starter)
        self.assertIn("Output:\n  150\n  10\n  5000\n  70", starter)
        self.assertIn("Separated test cases:", starter)
        self.assertIn("  Test case 1:\n    Input:\n      2 15 10\n    Output:\n      150", starter)
        self.assertIn("  Test case 4:\n    Input:\n      1 11 7\n    Output:\n      70", starter)

    def test_codechef_without_static_solution_has_no_fake_ast_baseline_when_uncached(self) -> None:
        self.client.put(
            "/api/progress",
            json={"active_set": "codechef", "career_mode": False},
        )
        stored = progress_store.load()
        career_path = CODECHEF_CAREER_PATHS[0]
        for challenge_id in career_path[:career_path.index("cc_ADIMAT")]:
            stored.complete(challenge_id, 1, "O(1)")
        progress_store.save(stored)
        with patch("server.app.codechef_community.load_cached_source", return_value=""):
            response = self.client.post(
                "/api/challenges/cc_ADIMAT/run",
                json={"source": "def solve(input_data):\n    return None\n", "n": 10, "mode": "practice"},
            )
        self.assertEqual(response.status_code, 200, response.text)
        self.assertIsNone(response.json()["reference_ast_ops"])

    def test_codechef_complexity_uses_upper_bound_without_lower_bound(self) -> None:
        self.client.put(
            "/api/progress",
            json={"active_set": "codechef", "career_mode": False},
        )
        source = (
            "def solve():\n"
            "    score = int(input())\n"
            "    print('Yes' if score >= 12 else 'No')\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    solve()\n"
        )

        response = self.client.post(
            "/api/challenges/cc_CWC23QUALIF/run",
            json={"source": source, "n": 2, "mode": "practice"},
        )

        self.assertEqual(response.status_code, 200, response.text)
        body = response.json()
        self.assertTrue(body["passed"], body)
        self.assertIsNone(body["reference_ci_low"])
        self.assertEqual(
            body["reference_ci_high"],
            max(math.ceil(body["reference_ast_ops"] * 1.5), body["reference_ast_ops"] + 20),
        )
        self.assertFalse(body["too_efficient"])

    def test_codechef_editorial_code_is_available_for_translation_workflow(self) -> None:
        spec = CHALLENGE_REGISTRY["cc_GSEQ"]()._spec
        candidate = best_codechef_source(spec.reference_metadata)
        self.assertIsNotNone(candidate)
        assert candidate is not None
        self.assertEqual(candidate["language"], "C++")
        self.assertIn("Editorialist's code", candidate["label"])
        self.assertIn("#include", candidate["source"])
        self.assertEqual(spec.reference_source, "")

    def test_codechef_cached_community_solution_overrides_ast_baseline(self) -> None:
        self.client.put(
            "/api/progress",
            json={"active_set": "codechef", "career_mode": False},
        )
        community_source = "def solve():\n    total = sum(range(10))\n    print(total)\n"

        with patch(
            "server.app.codechef_community.load_cached_source",
            return_value=community_source,
        ):
            response = self.client.post(
                "/api/challenges/cc_BWFPF01/run",
                json={"source": "def solve(input_data):\n    return None\n", "n": 10, "mode": "practice"},
            )

        self.assertEqual(response.status_code, 200, response.text)
        self.assertEqual(
            response.json()["reference_ast_ops"],
            ast_count_ops(community_source, 10),
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
