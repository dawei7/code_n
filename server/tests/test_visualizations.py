"""Tests for package-authored visual walkthroughs."""
from __future__ import annotations

from server.app.challenge_packages import leetcode_package_dir

from . import conftest


class VisualizationsTest(conftest._Base):
    def test_two_sum_visualization_is_valid_and_complete(self) -> None:
        response = self.client.get("/api/visualizations/lc_1")
        self.assertEqual(response.status_code, 200, response.text)
        definition = response.json()

        self.assertEqual(definition["challenge_id"], "lc_1")
        self.assertEqual(definition["version"], 2)
        self.assertEqual(definition["renderer"], "array-hash-map")
        self.assertEqual(definition["example"], {"nums": [3, 2, 4], "target": 6})
        self.assertGreaterEqual(len(definition["steps"]), 10)
        self.assertEqual(definition["steps"][-1]["state"]["result"], [1, 2])
        self.assertEqual(definition["steps"][-1]["state"]["event"], "returned")
        self.assertTrue(
            any(step["state"]["event"] == "miss" for step in definition["steps"])
        )
        self.assertTrue(
            any("seen" in step["state"]["changed"] for step in definition["steps"])
        )
        self.assertTrue(all(step["active_code"] for step in definition["steps"]))
        self.assertTrue(all(step["insight"] for step in definition["steps"]))
        self.assertEqual(
            {step["phase"] for step in definition["steps"]},
            {phase["id"] for phase in definition["phases"]},
        )

    def test_two_sum_visualization_uses_real_canonical_source(self) -> None:
        response = self.client.get("/api/visualizations/lc_1")
        self.assertEqual(response.status_code, 200, response.text)
        code = response.json()["code"]

        package = leetcode_package_dir("lc_1")
        self.assertIsNotNone(package)
        assert package is not None
        canonical_source = (package / "solutions" / "python.py").read_text(encoding="utf-8")
        self.assertEqual(code["source_path"], "solutions/python.py")
        self.assertEqual(code["source"], canonical_source)
        self.assertNotIn("lines", code)
        self.assertEqual(code["anchors"]["lookup"], {"start_line": 8, "end_line": 8})

    def test_median_visualization_exercises_both_partition_directions(self) -> None:
        response = self.client.get("/api/visualizations/lc_4")
        self.assertEqual(response.status_code, 200, response.text)
        definition = response.json()

        self.assertEqual(definition["challenge_id"], "lc_4")
        self.assertEqual(definition["renderer"], "binary-partition")
        self.assertEqual(
            definition["example"],
            {
                "nums1": [1, 3, 8, 12, 15],
                "nums2": [2, 4, 6, 9, 10, 11],
                "expected": 8.0,
            },
        )
        self.assertGreaterEqual(len(definition["steps"]), 12)
        self.assertEqual(definition["steps"][-1]["state"]["event"], "returned")
        self.assertEqual(definition["steps"][-1]["state"]["result"], 8.0)
        violations = {step["state"]["violation"] for step in definition["steps"]}
        self.assertIn("left1-too-large", violations)
        self.assertIn("left2-too-large", violations)
        self.assertIn("valid", violations)
        ranges = {
            (step["state"]["low"], step["state"]["high"])
            for step in definition["steps"]
            if step["state"]["low"] is not None
        }
        self.assertTrue({(0, 5), (3, 5), (3, 3)}.issubset(ranges))
        self.assertTrue(all(step["insight"] for step in definition["steps"]))
        self.assertEqual(
            {step["phase"] for step in definition["steps"]},
            {phase["id"] for phase in definition["phases"]},
        )

    def test_median_visualization_uses_real_canonical_source(self) -> None:
        response = self.client.get("/api/visualizations/lc_4")
        self.assertEqual(response.status_code, 200, response.text)
        code = response.json()["code"]

        package = leetcode_package_dir("lc_4")
        self.assertIsNotNone(package)
        assert package is not None
        canonical_source = (package / "solutions" / "python.py").read_text(encoding="utf-8")
        self.assertEqual(code["source"], canonical_source)
        self.assertNotIn("lines", code)
        self.assertEqual(
            code["anchors"]["valid_partition"],
            {"start_line": 17, "end_line": 17},
        )

    def test_challenge_summary_advertises_visualization_availability(self) -> None:
        response = self.client.get("/api/challenges/lc_1")
        self.assertEqual(response.status_code, 200, response.text)
        self.assertTrue(response.json()["has_visualization"])

        median = self.client.get("/api/challenges/lc_4")
        self.assertEqual(median.status_code, 200, median.text)
        self.assertTrue(median.json()["has_visualization"])

        without_visual = self.client.get("/api/challenges/lc_2")
        self.assertEqual(without_visual.status_code, 200, without_visual.text)
        self.assertFalse(without_visual.json()["has_visualization"])

    def test_missing_visualization_returns_not_found(self) -> None:
        response = self.client.get("/api/visualizations/lc_2")
        self.assertEqual(response.status_code, 404, response.text)
        self.assertIn("No visual walkthrough", response.json()["detail"])
