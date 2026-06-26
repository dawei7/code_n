"""Tests for the dynamic documentation endpoints on NeetCode challenges."""
from __future__ import annotations

from . import conftest
from server.app.config import DOCS_ROOT


class DynamicDocsTest(conftest._Base):
    def test_neetcode_reference_docs_are_materialized(self) -> None:
        files = list((DOCS_ROOT / "algorithms" / "neetcode").glob("neetcode_*/nc_*.md"))
        self.assertEqual(len(files), 250)

    def test_dynamic_reference_doc(self) -> None:
        # Check first NeetCode challenge
        r = self.client.get("/api/docs/by-id/nc_1")
        self.assertEqual(r.status_code, 200, r.text)
        self.assertNotIn("Reference: ", r.text)
        self.assertNotIn("**Category**:", r.text)
        self.assertNotIn("LeetCode Reference", r.text)
        self.assertIn("Function Contract", r.text)
        self.assertIn("Example 1", r.text)
        self.assertIn("Example 2", r.text)
        self.assertIn("Example 3", r.text)
        self.assertIn("- Output: `[1, 2, 1, 1, 2, 1]`", r.text)
        self.assertNotIn("- Output: `[1,2,1,1,2,1]`", r.text)
        self.assertIn("Underlying Base Algorithm", r.text)
        self.assertNotIn("Strategy & Walkthrough", r.text)
        self.assertNotIn("Canonical solution shape:", r.text)
        self.assertNotIn("Self-check", r.text)
        self.assertNotIn("Pedagogic Hint", r.text)
        self.assertNotIn("Canonical Implementation", r.text)
        self.assertIn("Complexity Analysis", r.text)

    def test_leetcode_reference_doc_resolves_from_dataset_folder(self) -> None:
        r = self.client.get("/api/docs/by-id/lc_1002")
        self.assertEqual(r.status_code, 200, r.text)
        self.assertIn("# Find Common Characters", r.text)
        self.assertIn("words = [\"bella\", \"label\", \"roller\"]", r.text)
        self.assertIn("Frequency-count intersection", r.text)

    def test_dynamic_mathematical_doc(self) -> None:
        r = self.client.get("/api/math/by-id/nc_1")
        self.assertEqual(r.status_code, 404, r.text)

    def test_neetcode_examples_use_small_leetcode_style_values(self) -> None:
        r = self.client.get("/api/docs/by-id/nc_2")
        self.assertEqual(r.status_code, 200, r.text)
        self.assertIn("- Input: `nums = [1, 2, 3, 4]`", r.text)
        self.assertIn("- Output: `False`", r.text)
        self.assertIn("- Input: `nums = [4, 5, 6, 4]`", r.text)
        self.assertIn("- Output: `True`", r.text)
        self.assertNotIn("813382118", r.text)
        self.assertNotIn("-711454982", r.text)
        self.assertNotIn("222356005", r.text)

    def test_german_translation_headers(self) -> None:
        r = self.client.get("/api/docs/by-id/nc_1?lang=de")
        self.assertEqual(r.status_code, 200)
        self.assertNotIn("Reference: ", r.text)
        self.assertNotIn("**Category**:", r.text)
        self.assertIn("Underlying Base Algorithm", r.text)
        self.assertNotIn("Kanonische Implementierung", r.text)

        r2 = self.client.get("/api/math/by-id/nc_1?lang=de")
        self.assertEqual(r2.status_code, 404)
