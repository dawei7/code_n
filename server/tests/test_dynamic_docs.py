"""Tests for the dynamic documentation endpoints on NeetCode challenges."""
from __future__ import annotations

from . import conftest


class DynamicDocsTest(conftest._Base):
    def test_dynamic_reference_doc(self) -> None:
        # Check first NeetCode challenge
        r = self.client.get("/api/docs/by-id/nc_1")
        self.assertEqual(r.status_code, 200, r.text)
        self.assertIn("Reference: ", r.text)
        self.assertIn("**Category**:", r.text)
        self.assertIn("Underlying Base Algorithm", r.text)
        self.assertNotIn("Canonical Implementation", r.text)
        self.assertIn("Complexity Analysis", r.text)

    def test_dynamic_mathematical_doc(self) -> None:
        # Check first NeetCode challenge math doc
        r = self.client.get("/api/math/by-id/nc_1")
        self.assertEqual(r.status_code, 200, r.text)
        self.assertIn("Mathematical Foundation: ", r.text)
        self.assertIn("Mathematical Core", r.text)
        self.assertIn("Recurrence & Equations", r.text)

    def test_german_translation_headers(self) -> None:
        r = self.client.get("/api/docs/by-id/nc_1?lang=de")
        self.assertEqual(r.status_code, 200)
        self.assertIn("Referenz: ", r.text)
        self.assertIn("**Kategorie**:", r.text)
        self.assertIn("Unterliegende Basisalgorithmen", r.text)
        self.assertNotIn("Kanonische Implementierung", r.text)

        r2 = self.client.get("/api/math/by-id/nc_1?lang=de")
        self.assertEqual(r2.status_code, 200)
        self.assertIn("Mathematische Grundlagen: ", r2.text)
        self.assertIn("Mathematischer Kern", r2.text)
        self.assertIn("Formeln & Gleichungen", r2.text)
