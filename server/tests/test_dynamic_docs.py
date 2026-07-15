"""Tests for canonical LeetCode package documentation."""
from __future__ import annotations

from pathlib import Path

from challenges.algorithms.leetcode import _parse_complexity
from engine.counter import ComplexityClass
from server.app.challenge_packages import leetcode_package_dir, leetcode_package_id

from . import conftest


class DynamicDocsTest(conftest._Base):
    def test_latex_linearithmic_complexity_is_parsed(self) -> None:
        text = "### Required Complexity\n- **Time:** $O(n \\log n)$\n- **Space:** $O(n)$"
        self.assertEqual(_parse_complexity(text), ComplexityClass.O_N_LOG_N)

    def test_reference_doc_resolves_from_challenge_package(self) -> None:
        response = self.client.get("/api/docs/by-id/lc_1")
        self.assertEqual(response.status_code, 200, response.text)
        self.assertIn("# Two Sum", response.text)
        self.assertIn("Complexity", response.text)

    def test_overview_is_the_root_readme(self) -> None:
        response = self.client.get("/api/docs/overview")
        self.assertEqual(response.status_code, 200, response.text)
        self.assertIn("# cOde(n)", response.text)

    def test_translation_request_falls_back_to_canonical_doc(self) -> None:
        response = self.client.get("/api/docs/by-id/lc_1?lang=de")
        self.assertEqual(response.status_code, 200, response.text)
        self.assertIn("# Two Sum", response.text)

    def test_docs_index_contains_only_registry_challenges(self) -> None:
        response = self.client.get("/api/docs/index")
        self.assertEqual(response.status_code, 200, response.text)
        entries = response.json()
        self.assertGreater(len(entries), 3900)
        self.assertTrue(all(entry["id"].startswith("lc_") for entry in entries))

    def test_raw_docs_are_restricted_to_canonical_dsa(self) -> None:
        response = self.client.get("/api/docs/dsa/leetcode/0001_two-sum/doc.md")
        self.assertEqual(response.status_code, 200, response.text)
        self.assertIn("# Two Sum", response.text)

        legacy = self.client.get("/api/docs/algorithms/README.md")
        self.assertEqual(legacy.status_code, 404)

    def test_canonical_paths_are_padded_without_changing_challenge_ids(self) -> None:
        package = leetcode_package_dir("lc_1")
        self.assertIsNotNone(package)
        assert package is not None
        self.assertEqual(package.name, "0001_two-sum")
        self.assertEqual(leetcode_package_id(Path("0001_two-sum")), "lc_1")
