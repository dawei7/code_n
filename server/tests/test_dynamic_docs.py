"""Tests for canonical LeetCode package documentation."""
from __future__ import annotations

import tempfile
from pathlib import Path
from unittest.mock import patch

from challenges.algorithms.leetcode import _parse_complexity
from engine.counter import ComplexityClass
from server.app.challenge_packages import (
    leetcode_doc_markdown,
    leetcode_package_dir,
    leetcode_package_id,
)

from . import conftest


class DynamicDocsTest(conftest._Base):
    def test_latex_linearithmic_complexity_is_parsed(self) -> None:
        text = "### Required Complexity\n- **Time:** $O(n \\log n)$\n- **Space:** $O(n)$"
        self.assertEqual(_parse_complexity(text), ComplexityClass.O_N_LOG_N)

    def test_factorial_complexity_is_not_misclassified_as_linear(self) -> None:
        text = "### Required Complexity\n- **Time:** $O(n!)$\n- **Space:** $O(n)$"
        self.assertEqual(_parse_complexity(text), ComplexityClass.O_N_FACTORIAL)

    def test_k_to_n_complexity_is_not_misclassified_as_linear(self) -> None:
        text = "### Required Complexity\n- **Time:** $O(k^n)$\n- **Space:** $O(k+n)$"
        self.assertEqual(_parse_complexity(text), ComplexityClass.O_KN)

    def test_reference_doc_resolves_from_challenge_package(self) -> None:
        response = self.client.get("/api/docs/by-id/lc_1")
        self.assertEqual(response.status_code, 200, response.text)
        self.assertIn("# Two Sum", response.text)
        self.assertIn("## Description", response.text)
        self.assertIn("## Function Contract", response.text)
        self.assertIn("## Examples", response.text)
        self.assertIn("## Constraints", response.text)
        self.assertIn("## Follow-up", response.text)
        self.assertIn("| Supported Language | Python |", response.text)
        self.assertNotIn("Supported Languages", response.text)
        self.assertLess(response.text.index("## Description"), response.text.index("## Function Contract"))
        self.assertLess(response.text.index("## Function Contract"), response.text.index("## Examples"))
        self.assertLess(response.text.index("## Examples"), response.text.index("## Constraints"))
        self.assertLess(response.text.index("## Constraints"), response.text.index("## Follow-up"))
        self.assertNotIn("### Required Complexity", response.text)

    def test_reference_metadata_exposes_zerotrac_contest_source(self) -> None:
        response = self.client.get("/api/docs/by-id/lc_3693")

        self.assertEqual(response.status_code, 200, response.text)
        self.assertIn("| Contest Source | Biweekly Contest 166 |", response.text)
        self.assertIn("| Contest Problem | Q2 |", response.text)

    def test_legacy_monolithic_reference_docs_remain_supported(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            package = Path(temp_dir) / "9999_legacy"
            package.mkdir()
            (package / "doc.md").write_text(
                "# Legacy\n\n### Goal\n\nStill supported.\n",
                encoding="utf-8",
            )
            with patch(
                "server.app.challenge_packages.leetcode_package_dir",
                return_value=package,
            ):
                markdown = leetcode_doc_markdown("lc_9999")

        self.assertIsNotNone(markdown)
        assert markdown is not None
        self.assertIn("# Legacy", markdown)
        self.assertIn("### Goal", markdown)

    def test_legacy_metadata_is_normalized_to_one_supported_language(self) -> None:
        response = self.client.get("/api/docs/by-id/lc_764")

        self.assertEqual(response.status_code, 200, response.text)
        self.assertIn("| Supported Language | Python |", response.text)
        self.assertNotIn("Supported Languages", response.text)

    def test_reviewed_source_native_sections_keep_manifest_order(self) -> None:
        custom_judge = self.client.get("/api/docs/by-id/lc_26")
        self.assertEqual(custom_judge.status_code, 200, custom_judge.text)
        custom_headings = (
            "## Description",
            "## Function Contract",
            "## Custom Judge",
            "## Examples",
            "## Constraints",
        )
        self.assertEqual(
            sorted(custom_judge.text.index(heading) for heading in custom_headings),
            [custom_judge.text.index(heading) for heading in custom_headings],
        )

        note = self.client.get("/api/docs/by-id/lc_29")
        self.assertEqual(note.status_code, 200, note.text)
        self.assertLess(note.text.index("## Description"), note.text.index("## Note"))
        self.assertLess(note.text.index("## Note"), note.text.index("## Examples"))

    def test_reviewed_sql_doc_can_preserve_source_without_constraints(self) -> None:
        response = self.client.get("/api/docs/by-id/lc_175")

        self.assertEqual(response.status_code, 200, response.text)
        headings = (
            "## Person Table",
            "## Address Table",
            "## Description",
            "## Function Contract",
            "## Examples",
        )
        self.assertEqual(
            sorted(response.text.index(heading) for heading in headings),
            [response.text.index(heading) for heading in headings],
        )
        self.assertNotIn("## Constraints", response.text)
        self.assertIn("| Supported Language | SQL |", response.text)

    def test_overview_is_the_root_readme(self) -> None:
        response = self.client.get("/api/docs/overview")
        self.assertEqual(response.status_code, 200, response.text)
        self.assertIn("# cOde(n)", response.text)

    def test_documentation_endpoints_have_no_natural_language_selector(self) -> None:
        response = self.client.get("/openapi.json")
        self.assertEqual(response.status_code, 200, response.text)
        paths = response.json()["paths"]

        for route in ("/api/docs/overview", "/api/docs/by-id/{challenge_id}"):
            parameters = paths[route]["get"].get("parameters", [])
            self.assertNotIn("lang", {parameter["name"] for parameter in parameters})

    def test_docs_index_contains_only_registry_challenges(self) -> None:
        response = self.client.get("/api/docs/index")
        self.assertEqual(response.status_code, 200, response.text)
        entries = response.json()
        self.assertGreater(len(entries), 3900)
        self.assertTrue(all(entry["id"].startswith("lc_") for entry in entries))
        two_sum = next(entry for entry in entries if entry["id"] == "lc_1")
        self.assertEqual(
            two_sum["path"],
            "dsa/leetcode/0001_two-sum/reference/description.md",
        )

    def test_raw_docs_are_restricted_to_canonical_dsa(self) -> None:
        response = self.client.get(
            "/api/docs/dsa/leetcode/0001_two-sum/reference/description.md"
        )
        self.assertEqual(response.status_code, 200, response.text)
        self.assertIn("## Description", response.text)

        legacy = self.client.get("/api/docs/algorithms/README.md")
        self.assertEqual(legacy.status_code, 404)

    def test_canonical_paths_are_padded_without_changing_challenge_ids(self) -> None:
        package = leetcode_package_dir("lc_1")
        self.assertIsNotNone(package)
        assert package is not None
        self.assertEqual(package.name, "0001_two-sum")
        self.assertEqual(leetcode_package_id(Path("0001_two-sum")), "lc_1")
