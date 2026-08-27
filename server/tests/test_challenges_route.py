"""Tests for the canonical LeetCode challenge API."""
from __future__ import annotations

import ast
import json
from types import SimpleNamespace

from . import conftest
from challenges.registry import CHALLENGE_REGISTRY
from engine.languages import app_solution_filename
from server.app.challenge_packages import (
    leetcode_package_dir,
    leetcode_solution_path,
    leetcode_solution_variants_status,
    leetcode_submission_manifest_path,
    leetcode_template_path,
    leetcode_variant_solution_path,
)
from server.app.optimal_sources import organized_solution_path
from server.app.routes.challenges import get_unlocked_challenges


class ChallengesRouteTest(conftest._Base):
    def test_default_registry_contains_only_canonical_leetcode_ids(self) -> None:
        response = self.client.get("/api/challenges")
        self.assertEqual(response.status_code, 200, response.text)
        summaries = response.json()
        self.assertGreater(len(summaries), 3900)
        self.assertTrue(all(item["id"].startswith("lc_") or item["id"].startswith("euler_") for item in summaries))
        self.assertTrue(
            all(
                item["supported_languages"] == [item["primary_language"]]
                and item["primary_language"] in {"python", "javascript", "sql", "bash"}
                for item in summaries
            )
        )
        self.assertIn("lc_1", {item["id"] for item in summaries})

    def test_leetcode_views_share_the_canonical_base(self) -> None:
        canonical_ids = None
        for active_set in (
            "leetcode",
            "leetcode_id",
            "elo",
            "elo_buckets",
            "frequency",
            "frequency_buckets",
            "leetcode_company",
            "leetcode_studyplan",
            "leetcode_quest",
        ):
            progress = self.client.put("/api/progress", json={"active_set": active_set})
            self.assertEqual(progress.status_code, 200, progress.text)
            self.assertEqual(progress.json()["active_set"], active_set)
            response = self.client.get("/api/challenges")
            self.assertEqual(response.status_code, 200, response.text)
            ids = [item["id"] for item in response.json()]
            self.assertTrue(all(item.startswith("lc_") or item.startswith("euler_") for item in ids))
            canonical_ids = canonical_ids or ids
            self.assertEqual(ids, canonical_ids)

    def test_neetcode_is_a_subset_of_canonical_leetcode(self) -> None:
        self.client.put("/api/progress", json={"active_set": "neetcode"})
        response = self.client.get("/api/challenges")
        self.assertEqual(response.status_code, 200, response.text)
        summaries = response.json()
        self.assertGreater(len(summaries), 3900)
        self.assertTrue(all(item["id"].startswith("lc_") or item["id"].startswith("euler_") for item in summaries))
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
        self.assertTrue(all(item["id"].startswith("lc_") or item["id"].startswith("euler_") for item in summaries))

        members_by_list = {slug: set() for slug in ("am-600", "am-300", "am-150", "am-75")}
        for summary in summaries:
            for membership in summary["leetcode_external_subsets"]:
                if membership.get("kind") == "algomaster":
                    members_by_list[membership["subset_slug"]].add(summary["id"])
        self.assertEqual(
            {slug: len(members) for slug, members in members_by_list.items()},
            {"am-600": 600, "am-300": 300, "am-150": 150, "am-75": 75},
        )

    def test_leetcode_quests_are_exact_subsets_of_canonical_leetcode(self) -> None:
        progress = self.client.put("/api/progress", json={"active_set": "leetcode_quest"})
        self.assertEqual(progress.status_code, 200, progress.text)
        response = self.client.get("/api/challenges")
        self.assertEqual(response.status_code, 200, response.text)
        summaries = response.json()
        members_by_quest = {
            slug: set()
            for slug in (
                "data-structures-and-algorithms-quest",
                "database-quest",
                "system-and-software-design-quest",
                "maths-quest",
                "2026-spring-sprint",
            )
        }
        for summary in summaries:
            for membership in summary["leetcode_external_subsets"]:
                if membership.get("kind") == "leetcode_quest":
                    members_by_quest[membership["subset_slug"]].add(summary["id"])
        self.assertEqual(
            {slug: len(members) for slug, members in members_by_quest.items()},
            {
                "data-structures-and-algorithms-quest": 119,
                "database-quest": 19,
                "system-and-software-design-quest": 13,
                "maths-quest": 22,
                "2026-spring-sprint": 36,
            },
        )

    def test_leetcode_quest_career_sequence_unlocks_in_level_order(self) -> None:
        challenges = [challenge_cls() for challenge_cls in CHALLENGE_REGISTRY.values()]

        initially_unlocked = get_unlocked_challenges(
            SimpleNamespace(active_set="leetcode_quest", completed=[]),
            challenges,
        )
        self.assertIn("lc_1929", initially_unlocked)
        self.assertNotIn("lc_1470", initially_unlocked)

        after_first = get_unlocked_challenges(
            SimpleNamespace(active_set="leetcode_quest", completed=["lc_1929"]),
            challenges,
        )
        self.assertIn("lc_1470", after_first)

    def test_unknown_set_and_challenge_fall_back_cleanly(self) -> None:
        progress = self.client.put("/api/progress", json={"active_set": "retired-source"})
        self.assertEqual(progress.json()["active_set"], "leetcode")
        response = self.client.get("/api/challenges/not-a-challenge")
        self.assertEqual(response.status_code, 404)

    def test_details_document_canonical_package_templates(self) -> None:
        for challenge_id, language in (
            ("lc_1", "python"),
            ("lc_175", "sql"),
            ("lc_1114", "python"),
            ("lc_1188", "python"),
            ("lc_1279", "python"),
        ):
            with self.subTest(challenge_id=challenge_id):
                template_path = leetcode_template_path(challenge_id, language)
                self.assertIsNotNone(template_path)
                assert template_path is not None
                expected = template_path.read_text(encoding="utf-8")

                response = self.client.get(f"/api/challenges/{challenge_id}")
                self.assertEqual(response.status_code, 200, response.text)
                detail = response.json()
                starter = detail["starter_source"]
                self.assertEqual(detail["starter_sources"][language], starter)
                self.assertTrue(starter.endswith(expected))
                comment_prefix = "# " if language == "python" else ""
                self.assertIn(
                    f"{comment_prefix}Description\n{comment_prefix}-----------",
                    starter,
                )
                self.assertIn(
                    f"{comment_prefix}Examples\n{comment_prefix}--------",
                    starter,
                )
                self.assertIn(
                    f"{comment_prefix}Required Complexity\n{comment_prefix}-------------------",
                    starter,
                )
                self.assertIn("Time: ", starter)
                self.assertIn("Space: ", starter)
                if language == "python":
                    ast.parse(starter)

    def test_documented_starters_use_language_appropriate_comments(self) -> None:
        cases = (
            ("lc_1", "python", "# Description"),
            ("lc_175", "sql", "/*\nDescription"),
            ("lc_192", "bash", "#!/usr/bin/env bash\n\n# Description"),
            ("lc_2694", "javascript", "/*\nDescription"),
        )
        for challenge_id, language, prefix in cases:
            with self.subTest(challenge_id=challenge_id):
                response = self.client.get(f"/api/challenges/{challenge_id}")
                self.assertEqual(response.status_code, 200, response.text)
                starter = response.json()["starter_sources"][language]
                self.assertTrue(starter.startswith(prefix))
                self.assertIn("Examples", starter)
                self.assertIn("Required Complexity", starter)
                self.assertIn("Time: ", starter)
                self.assertIn("Space: ", starter)

    def test_documented_starters_find_examples_nested_in_source_sections(self) -> None:
        source_example_facts = {
            "lc_192": "the day is sunny the the",
            "lc_3703": 'Input: s = "(())", k = 1',
            "lc_3933": "Input: matrix = [[0,0,0,0,0,0,0]",
        }
        for challenge_id, expected_fact in source_example_facts.items():
            with self.subTest(challenge_id=challenge_id):
                response = self.client.get(f"/api/challenges/{challenge_id}")
                self.assertEqual(response.status_code, 200, response.text)
                starter = response.json()["starter_source"]
                self.assertNotIn("No source examples are provided.", starter)
                self.assertRegex(starter, r"Example(?: 1)?:")
                self.assertIn(expected_fact, starter)

    def test_two_sum_detail_uses_package_metadata_and_artifacts(self) -> None:
        self.client.put("/api/progress", json={"active_set": "leetcode"})
        response = self.client.get("/api/challenges/lc_1")
        self.assertEqual(response.status_code, 200, response.text)
        detail = response.json()
        self.assertEqual(detail["name"], "Two Sum")
        self.assertEqual(detail["leetcode_slug"], "two-sum")
        self.assertEqual(detail["leetcode_url"], "https://leetcode.com/problems/two-sum/")
        self.assertEqual(detail["primary_language"], "python")
        self.assertEqual(detail["supported_languages"], ["python"])
        self.assertEqual(set(detail["starter_sources"]), {"python"})
        self.assertEqual(set(detail["optimal_sources"]), {"python"})
        self.assertEqual(set(detail["leetcode_optimal_sources"]), {"python"})
        self.assertIn("class Solution", detail["optimal_source"])
        self.assertIn("class Solution", detail["leetcode_optimal_source"])
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
        self.assertEqual(path.name, app_solution_filename("python"))

    def test_details_expose_coden_and_exact_verified_native_submissions(self) -> None:
        for challenge_id, expected_language in (
            ("lc_175", "sql"),
            ("lc_192", "bash"),
            ("lc_2694", "javascript"),
        ):
            response = self.client.get(f"/api/challenges/{challenge_id}")
            self.assertEqual(response.status_code, 200, response.text)
            detail = response.json()
            self.assertEqual(detail["primary_language"], expected_language)
            self.assertEqual(detail["supported_languages"], [expected_language])
            self.assertEqual(set(detail["starter_sources"]), {expected_language})
            self.assertEqual(set(detail["optimal_sources"]), {expected_language})
            self.assertEqual(set(detail["leetcode_optimal_sources"]), {expected_language})

            coden_path = organized_solution_path(challenge_id, expected_language)
            self.assertIsNotNone(coden_path)
            assert coden_path is not None
            expected_coden_source = coden_path.read_text(encoding="utf-8")

            manifest_path = leetcode_submission_manifest_path(challenge_id)
            self.assertIsNotNone(manifest_path)
            assert manifest_path is not None
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            expected_source = (manifest_path.parent / manifest["source"]).read_text(
                encoding="utf-8"
            )
            self.assertEqual(detail["optimal_source"], expected_coden_source)
            self.assertEqual(detail["optimal_sources"][expected_language], expected_coden_source)
            self.assertEqual(detail["leetcode_optimal_source"], expected_source)
            self.assertEqual(
                detail["leetcode_optimal_sources"][expected_language],
                expected_source,
            )

    def test_run_rejects_a_non_primary_language(self) -> None:
        response = self.client.post(
            "/api/challenges/lc_1/run",
            json={"source": "", "language": "javascript", "mode": "practice"},
        )
        self.assertEqual(response.status_code, 422, response.text)
        self.assertEqual(
            response.json()["detail"]["error"],
            "language_not_primary_for_challenge",
        )

    def test_contest_problem_exposes_zerotrac_elo(self) -> None:
        response = self.client.get("/api/challenges/lc_1024")
        self.assertEqual(response.status_code, 200, response.text)
        detail = response.json()
        self.assertEqual(detail["difficulty_label"], "Medium")
        self.assertAlmostEqual(detail["elo_rating"], 1746.135917977)
        self.assertIsNone(detail["estimated_elo_rating"])
        self.assertIsNone(detail["difficulty_estimate"])

    def test_1502_exposes_verified_and_simplified_solution_tabs(self) -> None:
        response = self.client.get("/api/challenges/lc_1502")
        self.assertEqual(response.status_code, 200, response.text)
        detail = response.json()

        self.assertEqual(detail["default_solution_variant"], "optimal")
        self.assertEqual(
            [variant["id"] for variant in detail["solution_variants"]],
            ["optimal", "simplified"],
        )
        self.assertEqual(
            [variant["kind"] for variant in detail["solution_variants"]],
            ["optimal", "simplified"],
        )
        self.assertAlmostEqual(detail["solution_variant_effective_elo"], 1154.828067979)
        self.assertEqual(detail["solution_variant_elo_source"], "elo_rating")
        self.assertEqual(detail["simplified_solution_elo_ceiling"], 1500)

        optimal, simplified = detail["solution_variants"]
        self.assertIn("endpoint", optimal["summary"].lower())
        self.assertEqual(optimal["time_complexity"], "O(n)")
        self.assertEqual(optimal["space_complexity"], "O(n)")
        self.assertNotIn("expected", optimal["time_complexity"].lower())
        self.assertEqual(simplified["time_complexity"], "O(n \\log n)")
        self.assertEqual(simplified["space_complexity"], "O(n)")
        self.assertIn("sorted(arr)", simplified["sources"]["python"])
        self.assertIn("class Solution", optimal["leetcode_sources"]["python"])
        self.assertNotEqual(optimal["approach_markdown"], simplified["approach_markdown"])
        self.assertNotEqual(optimal["sources"]["python"], simplified["sources"]["python"])

    def test_1502_default_paths_resolve_to_optimal_branch(self) -> None:
        package = leetcode_package_dir("lc_1502")
        self.assertIsNotNone(package)
        assert package is not None

        status = leetcode_solution_variants_status("lc_1502")
        self.assertTrue(status.complete, status.errors)
        optimal = leetcode_variant_solution_path("lc_1502", "optimal", "python")
        simplified = leetcode_variant_solution_path("lc_1502", "simplified", "python")
        self.assertEqual(leetcode_solution_path("lc_1502", "python"), optimal)
        self.assertEqual(
            leetcode_submission_manifest_path("lc_1502"),
            package / "variants" / "optimal" / "submission.json",
        )
        self.assertEqual(
            leetcode_submission_manifest_path("lc_1502", "simplified"),
            package / "variants" / "simplified" / "submission.json",
        )
        self.assertTrue(optimal and optimal.is_file())
        self.assertTrue(simplified and simplified.is_file())
        self.assertFalse((package / "solutions" / "solve.py").is_file())
        self.assertFalse((package / "submission.json").is_file())

    def test_1502_both_branches_pass_the_unchanged_shared_real_test(self) -> None:
        package = leetcode_package_dir("lc_1502")
        self.assertIsNotNone(package)
        assert package is not None
        benchmark = json.loads(
            (package / "benchmark.json").read_text(encoding="utf-8")
        )
        self.assertEqual(
            [case["size"] for case in benchmark["cases"]],
            [64, 256, 1000],
        )

        for variant_id in ("optimal", "simplified"):
            source_path = leetcode_variant_solution_path("lc_1502", variant_id, "python")
            self.assertIsNotNone(source_path)
            assert source_path is not None
            response = self.client.post(
                "/api/challenges/lc_1502/run",
                json={
                    "source": source_path.read_text(encoding="utf-8"),
                    "language": "python",
                    "mode": "real_test",
                },
            )
            self.assertEqual(response.status_code, 200, response.text)
            body = response.json()
            self.assertTrue(body["correct"], (variant_id, body))
            self.assertTrue(body["runtime_check"], (variant_id, body))
            self.assertTrue(body["runtime_passed"], (variant_id, body))
            self.assertTrue(body["passed"], (variant_id, body))

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
