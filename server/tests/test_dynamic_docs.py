"""Tests for canonical LeetCode package documentation."""
from __future__ import annotations

from . import conftest


class DynamicDocsTest(conftest._Base):
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
        response = self.client.get("/api/docs/dsa/leetcode/1_two-sum/doc.md")
        self.assertEqual(response.status_code, 200, response.text)
        self.assertIn("# Two Sum", response.text)

        legacy = self.client.get("/api/docs/algorithms/README.md")
        self.assertEqual(legacy.status_code, 404)
