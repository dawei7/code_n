"""Tests for mutable LeetCode metadata and weekly-import helpers."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from tools import sync_leetcode_dataset
from tools.update_leetcode_metrics import calculate_estimated_elos, load_metrics_snapshot


def _question(
    frontend_id: str,
    difficulty: str,
    acceptance_rate: float,
) -> dict[str, object]:
    return {
        "frontend_id": frontend_id,
        "slug": f"problem-{frontend_id}",
        "difficulty": difficulty,
        "acceptance_rate": acceptance_rate,
    }


class EstimatedEloModelTest(unittest.TestCase):
    def setUp(self) -> None:
        self.questions: list[dict[str, object]] = []
        self.ratings: dict[str, float] = {}
        tier_values = {
            "Easy": [1000, 1100, 1200, 1300, 1400],
            "Medium": [1500, 1600, 1700, 1800, 1900],
            "Hard": [2200, 2300, 2400, 2500, 2600],
        }
        for difficulty, values in tier_values.items():
            prefix = difficulty[0].lower()
            for index, rating in enumerate(values):
                frontend_id = f"{prefix}{index}"
                self.questions.append(_question(frontend_id, difficulty, 20 + index * 15))
                self.ratings[frontend_id] = float(rating)
            self.questions.extend([
                _question(f"{prefix}-legacy", difficulty, 50),
                _question(f"{prefix}-low-acceptance", difficulty, 10),
                _question(f"{prefix}-high-acceptance", difficulty, 90),
            ])

    def test_estimates_are_banded_calibrated_and_sparse(self) -> None:
        legacy_ids = {"e-legacy", "m-legacy", "h-legacy"}
        estimates, models = calculate_estimated_elos(
            self.questions,
            self.ratings,
            legacy_ids,
        )

        self.assertTrue(set(self.ratings).isdisjoint(estimates))
        self.assertLess(models["Easy"].maximum, models["Medium"].minimum)
        self.assertLess(models["Medium"].maximum, models["Hard"].minimum)
        self.assertLess(models["Hard"].maximum, models["Hard"].real_maximum)

        for difficulty, prefix in (("Easy", "e"), ("Medium", "m"), ("Hard", "h")):
            model = models[difficulty]
            self.assertAlmostEqual(estimates[f"{prefix}-legacy"], model.base, places=6)
            self.assertGreater(
                estimates[f"{prefix}-low-acceptance"],
                estimates[f"{prefix}-high-acceptance"],
            )
            self.assertGreaterEqual(estimates[f"{prefix}-high-acceptance"], model.minimum)
            self.assertLessEqual(estimates[f"{prefix}-low-acceptance"], model.maximum)


class DatasetSyncMetricPreservationTest(unittest.TestCase):
    def test_signed_in_rest_snapshot_normalizes_frequency_like_leetcode_ui(self) -> None:
        payload = {
            "num_total": 2,
            "stat_status_pairs": [
                {
                    "stat": {
                        "frontend_question_id": 1,
                        "question__title": "Two Sum",
                        "question__title_slug": "two-sum",
                        "total_acs": 75,
                        "total_submitted": 100,
                    },
                    "difficulty": {"level": 1},
                    "frequency": 8.0,
                },
                {
                    "stat": {
                        "frontend_question_id": 2,
                        "question__title": "Add Two Numbers",
                        "question__title_slug": "add-two-numbers",
                        "total_acs": 50,
                        "total_submitted": 100,
                    },
                    "difficulty": {"level": 2},
                    "frequency": 4.0,
                },
            ],
        }
        with tempfile.TemporaryDirectory() as temporary:
            snapshot_path = Path(temporary) / "leetcode-rest.json"
            snapshot_path.write_text(json.dumps(payload), encoding="utf-8")

            questions = load_metrics_snapshot(snapshot_path)

        self.assertEqual(
            questions,
            [
                {
                    "frontend_id": "1",
                    "title": "Two Sum",
                    "slug": "two-sum",
                    "difficulty": "Easy",
                    "acceptance_rate": 75.0,
                    "frequency": 100.0,
                },
                {
                    "frontend_id": "2",
                    "title": "Add Two Numbers",
                    "slug": "add-two-numbers",
                    "difficulty": "Medium",
                    "acceptance_rate": 50.0,
                    "frequency": 50.0,
                },
            ],
        )

    def test_new_metadata_declares_mutable_metric_fields(self) -> None:
        question = {
            "frontend_id": "9999",
            "title": "Example",
            "slug": "example",
            "difficulty": "Easy",
            "acceptance_rate": 50.0,
            "category": "algorithms",
            "category_title": "Algorithms",
            "topics": [],
            "url": "https://leetcode.com/problems/example/",
            "supported_languages": ["python"],
            "primary_language": "python",
            "runnable_in_coden": True,
        }

        metadata = sync_leetcode_dataset.metadata_for_question(question)

        self.assertIn("frequency", metadata)
        self.assertIn("elo_rating", metadata)
        self.assertIn("estimated_elo_rating", metadata)
        self.assertIsNone(metadata["frequency"])
        self.assertIsNone(metadata["elo_rating"])
        self.assertIsNone(metadata["estimated_elo_rating"])

    def test_index_refresh_preserves_existing_mutable_metrics(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            index_path = Path(temporary) / "index.json"
            index_path.write_text(
                json.dumps({
                    "questions": [{
                        "frontend_id": "1",
                        "slug": "two-sum",
                        "frequency": 87.5,
                        "elo_rating": 1350.25,
                        "estimated_elo_rating": 1234.5,
                    }],
                }),
                encoding="utf-8",
            )
            refreshed = [{
                "frontend_id": "1",
                "slug": "two-sum",
                "difficulty": "Easy",
                "acceptance_rate": 58.0,
            }]

            with patch.object(sync_leetcode_dataset, "INDEX_PATH", index_path):
                sync_leetcode_dataset.write_index(refreshed)

            stored = json.loads(index_path.read_text(encoding="utf-8"))["questions"][0]
            self.assertEqual(stored["frequency"], 87.5)
            self.assertEqual(stored["elo_rating"], 1350.25)
            self.assertEqual(stored["estimated_elo_rating"], 1234.5)

    def test_metadata_sync_preserves_solution_variant_pointer(self) -> None:
        question = {
            "frontend_id": "1502",
            "slug": "can-make-arithmetic-progression-from-sequence",
            "title": "Can Make Arithmetic Progression From Sequence",
        }
        variant_pointer = {
            "manifest": "solution_variants.json",
            "default": "optimal",
        }
        refreshed_metadata = {
            "challenge_id": "lc_1502",
            "frontend_id": "1502",
            "slug": question["slug"],
            "title": question["title"],
        }

        with tempfile.TemporaryDirectory() as temporary:
            leetcode_root = Path(temporary)
            package = leetcode_root / "1502_can-make-arithmetic-progression-from-sequence"
            package.mkdir()
            (package / "metadata.json").write_text(
                json.dumps({"solution_variants": variant_pointer}),
                encoding="utf-8",
            )
            with patch.object(sync_leetcode_dataset, "LEETCODE_ROOT", leetcode_root):
                sync_leetcode_dataset.write_package(
                    question,
                    refreshed_metadata,
                    scaffold_docs=False,
                )

            stored = json.loads((package / "metadata.json").read_text(encoding="utf-8"))
            self.assertEqual(stored["solution_variants"], variant_pointer)

    def test_weekly_import_creates_only_new_packages(self) -> None:
        def full_question(frontend_id: str, slug: str, title: str) -> dict[str, object]:
            return {
                "frontend_id": frontend_id,
                "title": title,
                "slug": slug,
                "difficulty": "Easy",
                "acceptance_rate": 50.0,
                "category": "algorithms",
                "category_title": "Algorithms",
                "topics": [{"name": "Array", "slug": "array"}],
                "url": f"https://leetcode.com/problems/{slug}/",
                "supported_languages": ["python"],
                "primary_language": "python",
                "runnable_in_coden": True,
            }

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            leetcode_root = root / "dsa" / "leetcode"
            existing = full_question("1", "two-sum", "Two Sum")
            new = full_question("4000", "new-weekly-problem", "New Weekly Problem")
            index_path = leetcode_root / "index.json"
            subsets_path = leetcode_root / "subsets.json"
            template_path = leetcode_root / "_template.md"
            approach_template_path = leetcode_root / "_approach_template.md"
            report_path = leetcode_root / "_reports" / "sync_report.json"
            existing_dir = leetcode_root / "0001_two-sum"
            existing_dir.mkdir(parents=True)
            existing_metadata = '{"sentinel": "do not rewrite"}\n'
            (existing_dir / "metadata.json").write_text(existing_metadata, encoding="utf-8")
            (existing_dir / "doc.md").write_text("# Existing\n", encoding="utf-8")
            index_path.write_text(
                json.dumps({"questions": [existing]}),
                encoding="utf-8",
            )
            template_path.write_text(
                (
                    "# {title}\n"
                    "{frontend_id} {difficulty} {topics} {slug} {url}\n"
                    "$\\sum_{w \\in W} \\lvert w \\rvert$\n"
                ),
                encoding="utf-8",
            )
            approach_template_path.write_text(
                (
                    "## General\n\nTODO\n\n"
                    "## Complexity detail\n\nTODO\n\n"
                    "## Alternatives and edge cases\n\n"
                    "- **Alternative:** TODO\n"
                    "- Edge case TODO\n"
                ),
                encoding="utf-8",
            )

            with (
                patch.object(sync_leetcode_dataset, "LEETCODE_ROOT", leetcode_root),
                patch.object(sync_leetcode_dataset, "INDEX_PATH", index_path),
                patch.object(sync_leetcode_dataset, "SUBSETS_PATH", subsets_path),
                patch.object(sync_leetcode_dataset, "TEMPLATE_PATH", template_path),
                patch.object(
                    sync_leetcode_dataset,
                    "APPROACH_TEMPLATE_PATH",
                    approach_template_path,
                ),
                patch.object(sync_leetcode_dataset, "REPORT_PATH", report_path),
                patch.object(
                    sync_leetcode_dataset,
                    "fetch_questions",
                    return_value=[existing, new],
                ),
                patch(
                    "tools.update_leetcode_metrics.update_metrics",
                    return_value={"estimated_elo_count": 1, "frequency_count": 0},
                ),
            ):
                report = sync_leetcode_dataset.sync_new_problems(
                    SimpleNamespace(page_size=100),
                )

            self.assertEqual(report["new_frontend_ids"], ["4000"])
            self.assertEqual(
                (existing_dir / "metadata.json").read_text(encoding="utf-8"),
                existing_metadata,
            )
            new_dir = leetcode_root / "4000_new-weekly-problem"
            self.assertTrue((new_dir / "metadata.json").is_file())
            self.assertTrue((new_dir / "solution_variants.json").is_file())
            self.assertTrue(
                (new_dir / "variants" / "optimal" / "approach.md").is_file()
            )
            self.assertIn(
                "# New Weekly Problem",
                (new_dir / "doc.md").read_text(encoding="utf-8"),
            )
            self.assertIn(
                r"\sum_{w \in W}",
                (new_dir / "doc.md").read_text(encoding="utf-8"),
            )
            stored_index = json.loads(index_path.read_text(encoding="utf-8"))
            self.assertEqual(stored_index["count"], 2)

    def test_weekly_import_with_no_new_ids_does_not_rewrite_dataset(self) -> None:
        existing = {
            "frontend_id": "1",
            "slug": "two-sum",
            "estimated_elo_rating": 1234.0,
            "frequency": 90.0,
        }
        with tempfile.TemporaryDirectory() as temporary:
            temporary_root = Path(temporary)
            report_path = temporary_root / "sync_report.json"
            with (
                patch.object(sync_leetcode_dataset, "LEETCODE_ROOT", temporary_root),
                patch.object(
                    sync_leetcode_dataset,
                    "fetch_questions",
                    return_value=[existing],
                ),
                patch.object(
                    sync_leetcode_dataset,
                    "load_questions_from_index",
                    return_value=[existing],
                ),
                patch.object(sync_leetcode_dataset, "REPORT_PATH", report_path),
                patch.object(sync_leetcode_dataset, "write_index") as write_index,
                patch.object(sync_leetcode_dataset, "write_subsets") as write_subsets,
            ):
                report = sync_leetcode_dataset.sync_new_problems(
                    SimpleNamespace(page_size=100),
                )

            self.assertEqual(report["new_problem_count"], 0)
            self.assertEqual(report["frequency_count"], 1)
            write_index.assert_not_called()
            write_subsets.assert_not_called()


if __name__ == "__main__":
    unittest.main()
