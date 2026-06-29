"""Tests for the dynamic documentation endpoints on NeetCode challenges."""
from __future__ import annotations

from . import conftest
from server.app.config import DOCS_ROOT
from server.app import progress_store


class DynamicDocsTest(conftest._Base):
    def test_neetcode_reference_docs_are_materialized(self) -> None:
        files = list((DOCS_ROOT / "algorithms" / "neetcode").glob("neetcode_*/nc_*.md"))
        self.assertEqual(len(files), 250)

    def test_codechef_markdown_docs_are_utf8_clean(self) -> None:
        files = list((DOCS_ROOT / "algorithms" / "codechef").rglob("cc_*.md"))
        self.assertGreaterEqual(len(files), 1646)
        bad: list[str] = []
        mojibake_markers = (
            "\ufffd",
            "\u00e2\u20ac",
            "\u00c3\u00a9",
            "\u00c3\u00a8",
            "\u00c3\u00b6",
            "\u00c3\u00bc",
            "\u00c2\u00a0",
        )
        for path in files:
            text = path.read_text(encoding="utf-8")
            if any(marker in text for marker in mojibake_markers):
                bad.append(str(path.relative_to(DOCS_ROOT)))
        self.assertEqual(bad[:10], [])

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

    def test_codechef_reference_uses_static_official_data(self) -> None:
        progress = progress_store.load()
        progress.player_name = "Mira"
        progress_store.save(progress)

        r = self.client.get("/api/docs/by-id/cc_BWFPF01")
        self.assertEqual(r.status_code, 200, r.text)
        self.assertIn("# Chef Builds Subsets", r.text)
        self.assertIn("## Problem Statement", r.text)
        self.assertIn("Chef has a list of integers", r.text)
        self.assertIn("Example 1", r.text)
        self.assertIn("Example 2", r.text)
        self.assertIn("Example 3", r.text)
        self.assertNotIn("## Official Solution", r.text)
        self.assertNotIn("Underlying Base Algorithm", r.text)
        self.assertIn("<summary>Official Editorial</summary>", r.text)
        self.assertIn("Complexity Analysis", r.text)

    def test_codechef_reference_shows_official_numeric_difficulty_rating(self) -> None:
        r = self.client.get("/api/docs/by-id/cc_AIRLINES")
        self.assertEqual(r.status_code, 200, r.text)
        self.assertIn("| Difficulty Rating | 475 |", r.text)
        self.assertIn("| Difficulty Band | 500 difficulty rating |", r.text)

    def test_codechef_samples_include_readable_separated_test_cases(self) -> None:
        r = self.client.get("/api/docs/by-id/cc_AIRLINES")
        self.assertEqual(r.status_code, 200, r.text)
        self.assertIn("**Separated test cases**", r.text)
        self.assertIn("#### Test case 1", r.text)
        self.assertIn("**Input for this case**\n\n```text\n2 15 10\n```", r.text)
        self.assertIn("**Output for this case**\n\n```text\n150\n```", r.text)
        self.assertIn("#### Test case 4", r.text)
        self.assertNotIn('class="codechef-sample-case"', r.text)

    def test_codechef_reference_collapses_full_official_editorial(self) -> None:
        r = self.client.get("/api/docs/by-id/cc_GSEQ")
        self.assertEqual(r.status_code, 200, r.text)
        self.assertIn("| Difficulty Rating | 2451 |", r.text)
        self.assertIn("<summary>Official Editorial</summary>", r.text)
        self.assertIn("prefix sums", r.text.lower())
        self.assertIn("dynamic programming", r.text.lower())
        self.assertIn("replace every 0 in the array with -1", r.text)
        self.assertIn("PROBLEM LINK", r.text)
        self.assertIn("DIFFICULTY", r.text)
        self.assertIn("Editorialist's code", r.text)
        self.assertIn("#include", r.text)
        self.assertIn("using namespace std", r.text)

    def test_codechef_editorial_front_matter_is_collapsed_with_editorial(self) -> None:
        r = self.client.get("/api/docs/by-id/cc_CWC23QUALIF")
        self.assertEqual(r.status_code, 200, r.text)
        self.assertIn("<summary>Official Editorial</summary>", r.text)
        self.assertIn("PROBLEM LINK", r.text)
        self.assertIn("DIFFICULTY", r.text)
        self.assertIn("TBD", r.text)
        self.assertIn("Tester:", r.text)
        self.assertIn("Editorialist:", r.text)

    def test_codechef_admit_solution_tab_reference_keeps_full_walkthrough(self) -> None:
        r = self.client.get("/api/docs/by-id/cc_ADMIT")
        self.assertEqual(r.status_code, 200, r.text)

        self.assertIn("<summary>Official Editorial</summary>", r.text)
        self.assertIn("PREREQUISITES", r.text)
        self.assertIn("Implementation", r.text)
        self.assertIn("PROBLEM", r.text)
        self.assertIn("QUICK EXPLANATION", r.text)
        self.assertIn("EXPLANATION", r.text)
        self.assertIn("class Student", r.text)
        self.assertIn("PROBLEM LINK", r.text)
        self.assertIn("DIFFICULTY", r.text)
        self.assertIn("Setter's Solution", r.text)
        self.assertIn("#include", r.text)

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
