"""Tests for standalone practice-file export."""
from __future__ import annotations

import ast
import io
import zipfile

from . import conftest  # noqa: F401


def _test_cases_from_source(source: str) -> list[dict]:
    module = ast.parse(source)
    for node in module.body:
        if not isinstance(node, ast.Assign):
            continue
        if any(isinstance(target, ast.Name) and target.id == "TEST_CASES" for target in node.targets):
            return ast.literal_eval(node.value)
    raise AssertionError("TEST_CASES assignment not found")


class PracticeExportTest(conftest._Base):
    def test_single_export_is_standalone_python_file(self) -> None:
        response = self.client.get("/api/practice-export/challenges/sort_01?n=4&seed=1")

        self.assertEqual(response.status_code, 200, response.text)
        self.assertIn('filename="Bubble Sort.py"', response.headers["content-disposition"])
        ast.parse(response.text)
        self.assertIn("TEST_CASES", response.text)
        self.assertIn("def solve(", response.text)
        self.assertNotIn("from challenges", response.text)
        self.assertNotIn("server.app", response.text)

    def test_single_export_can_prefix_filename_with_catalog_number(self) -> None:
        response = self.client.get(
            "/api/practice-export/challenges/sort_01?n=4&seed=1&filename_prefix=0007",
        )

        self.assertEqual(response.status_code, 200, response.text)
        self.assertIn('filename="0007 Bubble Sort.py"', response.headers["content-disposition"])

    def test_single_export_respects_requested_test_count(self) -> None:
        response = self.client.get("/api/practice-export/challenges/sort_01?n=4&seed=1&test_count=5")

        self.assertEqual(response.status_code, 200, response.text)
        self.assertEqual(len(_test_cases_from_source(response.text)), 5)

    def test_codechef_export_uses_stdin_stdout_harness(self) -> None:
        response = self.client.get("/api/practice-export/challenges/cc_CWC23QUALIF?n=4&seed=1")

        self.assertEqual(response.status_code, 200, response.text)
        ast.parse(response.text)
        self.assertIn("def solve():", response.text)
        self.assertIn("input()", response.text)
        self.assertIn("expected_stdout", response.text)
        self.assertNotIn("from challenges", response.text)
        self.assertNotIn("server.app", response.text)

    def test_bundle_export_preserves_requested_folder_paths(self) -> None:
        response = self.client.post(
            "/api/practice-export/bundle",
            json={
                "n": 4,
                "seed": 1,
                "entries": [
                    {"id": "sort_01", "path": ["Algorithms", "Sorting"], "filename_prefix": "0007"},
                    {"id": "cc_CWC23QUALIF", "path": ["CodeChef", "Career"], "filename_prefix": "0001"},
                ],
            },
        )

        self.assertEqual(response.status_code, 200, response.text)
        archive = zipfile.ZipFile(io.BytesIO(response.content))
        self.assertEqual(
            sorted(archive.namelist()),
            [
                "Algorithms/Sorting/0007 Bubble Sort.py",
                "CodeChef/Career/0001 Cricket World Cup Qualifier.py",
            ],
        )
        for name in archive.namelist():
            ast.parse(archive.read(name).decode("utf-8"))
