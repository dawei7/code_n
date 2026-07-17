"""Tests for the canonical LeetCode challenge API."""
from __future__ import annotations

from types import SimpleNamespace

from . import conftest
from challenges.registry import CHALLENGE_REGISTRY
from server.app.optimal_sources import organized_solution_path
from server.app.routes.challenges import get_unlocked_challenges


class ChallengesRouteTest(conftest._Base):
    def test_default_registry_contains_only_canonical_leetcode_ids(self) -> None:
        response = self.client.get("/api/challenges")
        self.assertEqual(response.status_code, 200, response.text)
        summaries = response.json()
        self.assertGreater(len(summaries), 3900)
        self.assertTrue(all(item["id"].startswith("lc_") for item in summaries))
        self.assertIn("lc_1", {item["id"] for item in summaries})

    def test_leetcode_views_share_the_canonical_base(self) -> None:
        canonical_ids = None
        for active_set in (
            "leetcode",
            "elo",
            "frequency",
            "leetcode_company",
            "leetcode_studyplan",
        ):
            progress = self.client.put("/api/progress", json={"active_set": active_set})
            self.assertEqual(progress.status_code, 200, progress.text)
            self.assertEqual(progress.json()["active_set"], active_set)
            response = self.client.get("/api/challenges")
            self.assertEqual(response.status_code, 200, response.text)
            ids = [item["id"] for item in response.json()]
            self.assertTrue(all(item.startswith("lc_") for item in ids))
            canonical_ids = canonical_ids or ids
            self.assertEqual(ids, canonical_ids)

    def test_neetcode_is_a_subset_of_canonical_leetcode(self) -> None:
        self.client.put("/api/progress", json={"active_set": "neetcode"})
        response = self.client.get("/api/challenges")
        self.assertEqual(response.status_code, 200, response.text)
        summaries = response.json()
        self.assertGreater(len(summaries), 3900)
        self.assertTrue(all(item["id"].startswith("lc_") for item in summaries))
        self.assertGreater(
            sum(
                any(membership.get("kind") == "neetcode" for membership in item["leetcode_external_subsets"])
                for item in summaries
            ),
            200,
        )

    def test_neetcode_career_sequence_unlocks_zero_order_first_problem(self) -> None:
        progress = SimpleNamespace(active_set="neetcode", completed=[])
        challenges = [challenge_cls() for challenge_cls in CHALLENGE_REGISTRY.values()]

        unlocked = get_unlocked_challenges(progress, challenges)

        self.assertIn("lc_217", unlocked)
        self.assertNotIn("lc_242", unlocked)

    def test_algomaster_lists_are_exact_subsets_of_canonical_leetcode(self) -> None:
        progress = self.client.put("/api/progress", json={"active_set": "algomaster"})
        self.assertEqual(progress.status_code, 200, progress.text)
        response = self.client.get("/api/challenges")
        self.assertEqual(response.status_code, 200, response.text)
        summaries = response.json()
        self.assertGreater(len(summaries), 3900)
        self.assertTrue(all(item["id"].startswith("lc_") for item in summaries))

        members_by_list = {slug: set() for slug in ("am-600", "am-300", "am-150", "am-75")}
        for summary in summaries:
            for membership in summary["leetcode_external_subsets"]:
                if membership.get("kind") == "algomaster":
                    members_by_list[membership["subset_slug"]].add(summary["id"])
        self.assertEqual(
            {slug: len(members) for slug, members in members_by_list.items()},
            {"am-600": 600, "am-300": 300, "am-150": 150, "am-75": 75},
        )

    def test_unknown_set_and_challenge_fall_back_cleanly(self) -> None:
        progress = self.client.put("/api/progress", json={"active_set": "retired-source"})
        self.assertEqual(progress.json()["active_set"], "leetcode")
        response = self.client.get("/api/challenges/not-a-challenge")
        self.assertEqual(response.status_code, 404)

    def test_two_sum_detail_uses_package_metadata_and_artifacts(self) -> None:
        self.client.put("/api/progress", json={"active_set": "leetcode"})
        response = self.client.get("/api/challenges/lc_1")
        self.assertEqual(response.status_code, 200, response.text)
        detail = response.json()
        self.assertEqual(detail["name"], "Two Sum")
        self.assertEqual(detail["leetcode_slug"], "two-sum")
        self.assertEqual(detail["leetcode_url"], "https://leetcode.com/problems/two-sum/")
        self.assertEqual(detail["primary_language"], "python")
        self.assertIn("def solve(nums, target):", detail["starter_source"])
        self.assertTrue(detail["test_cases"])
        self.assertTrue(detail["optimal_source"])
        self.assertEqual(detail["difficulty_label"], "Easy")
        self.assertIsNone(detail["elo_rating"])
        self.assertIsNotNone(detail["estimated_elo_rating"])
        self.assertEqual(detail["frequency"], 100.0)
        self.assertIsNone(detail["difficulty_estimate"])
        self.assertNotIn("difficulty", detail)

        path = organized_solution_path("lc_1", "python")
        self.assertIsNotNone(path)
        self.assertTrue(path.is_file())
        self.assertEqual(path.name, "python.py")

    def test_contest_problem_exposes_zerotrac_elo(self) -> None:
        response = self.client.get("/api/challenges/lc_1024")
        self.assertEqual(response.status_code, 200, response.text)
        detail = response.json()
        self.assertEqual(detail["difficulty_label"], "Medium")
        self.assertAlmostEqual(detail["elo_rating"], 1746.135917977)
        self.assertIsNone(detail["estimated_elo_rating"])
        self.assertIsNone(detail["difficulty_estimate"])

    def test_legacy_contest_problem_uses_acceptance_estimate_fallback(self) -> None:
        response = self.client.get("/api/challenges/lc_389")
        self.assertEqual(response.status_code, 200, response.text)
        detail = response.json()
        self.assertEqual(detail["difficulty_label"], "Easy")
        self.assertIsNone(detail["elo_rating"])
        self.assertIsNotNone(detail["estimated_elo_rating"])
        self.assertIsNotNone(detail["difficulty_estimate"])

    def test_unrated_non_contest_problem_has_no_numeric_fallback(self) -> None:
        response = self.client.get("/api/challenges/lc_2")
        self.assertEqual(response.status_code, 200, response.text)
        detail = response.json()
        self.assertEqual(detail["difficulty_label"], "Medium")
        self.assertIsNone(detail["elo_rating"])
        self.assertIsNotNone(detail["estimated_elo_rating"])
        self.assertIsNone(detail["difficulty_estimate"])

    def test_registry_specs_generate_contract_inputs(self) -> None:
        challenge = CHALLENGE_REGISTRY["lc_1002"]()
        setup = challenge.setup(16, seed=1)
        self.assertEqual(list(setup), ["words"])
        self.assertEqual(len(setup["words"]), 16)
