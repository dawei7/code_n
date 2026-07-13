"""Tests for standalone LeetCode practice-file export."""
from __future__ import annotations

import ast
import io
import zipfile

from . import conftest


class PracticeExportTest(conftest._Base):
    def test_single_export_is_standalone_python_file(self) -> None:
        response = self.client.get("/api/practice-export/challenges/lc_1")
        self.assertEqual(response.status_code, 200, response.text)
        self.assertIn('filename="Two Sum.py"', response.headers["content-disposition"])
        ast.parse(response.text)
        self.assertIn("TEST_CASES", response.text)
        self.assertIn("def solve(", response.text)
        self.assertNotIn("from challenges", response.text)

    def test_single_export_can_prefix_catalog_number(self) -> None:
        response = self.client.get(
            "/api/practice-export/challenges/lc_1?filename_prefix=0001"
        )
        self.assertEqual(response.status_code, 200, response.text)
        self.assertIn('filename="0001 Two Sum.py"', response.headers["content-disposition"])

    def test_bundle_export_preserves_requested_subset_path(self) -> None:
        response = self.client.post(
            "/api/practice-export/bundle",
            json={"entries": [{"id": "lc_1", "path": ["LeetCode", "Arrays"]}]},
        )
        self.assertEqual(response.status_code, 200, response.text)
        archive = zipfile.ZipFile(io.BytesIO(response.content))
        self.assertEqual(archive.namelist(), ["LeetCode/Arrays/Two Sum.py"])
