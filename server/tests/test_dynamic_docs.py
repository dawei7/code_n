import tempfile
from pathlib import Path
from unittest.mock import patch

from challenges.algorithms.leetcode import _parse_complexity
from engine.counter import ComplexityClass
from server.app.challenge_packages import (
    leetcode_doc_markdown,
    leetcode_metadata,
    leetcode_optimal_approach_path,
    leetcode_package_dir,
    leetcode_package_id,
)

from . import conftest


class DynamicDocsTest(conftest._Base):
    def test_canonical_editorials_omit_videos_and_toc_markers(self) -> None:
        leetcode_root = Path(__file__).resolve().parents[2] / "dsa" / "leetcode"
        editorials = sorted(leetcode_root.glob("*/reference/editorial.md"))
        violations: list[str] = []

        self.assertEqual(len(editorials), 4005)
        for editorial in editorials:
            text = editorial.read_text(encoding="utf-8")
            lowered = text.lower()
            lines = {line.strip().lower() for line in text.splitlines()}
            has_video_heading = any(
                line.startswith("#")
                and line.lstrip("#").strip() in {"video", "video solution"}
                for line in lines
            )
            has_video_markup = any(
                marker in lowered
                for marker in (
                    "<video",
                    "player.vimeo.com",
                    "youtube.com/embed",
                    "youtube-nocookie.com/embed",
                    "youtu.be/",
                    ".mp4",
                    ".webm",
                )
            )
            if (
                has_video_markup
                or has_video_heading
                or "[toc]" in lines
            ):
                violations.append(str(editorial.relative_to(leetcode_root)))

        self.assertEqual(violations, [])

    def test_latex_linearithmic_complexity_is_parsed(self) -> None:
        text = "### Required Complexity\n- **Time:** $O(n \\log n)$\n- **Space:** $O(n)$"
        self.assertEqual(_parse_complexity(text), ComplexityClass.O_N_LOG_N)

    def test_factorial_complexity_is_not_misclassified_as_linear(self) -> None:
        text = "### Required Complexity\n- **Time:** $O(n!)$\n- **Space:** $O(n)$"
        self.assertEqual(_parse_complexity(text), ComplexityClass.O_N_FACTORIAL)

    def test_k_to_n_complexity_is_not_misclassified_as_linear(self) -> None:
        text = "### Required Complexity\n- **Time:** $O(k^n)$\n- **Space:** $O(k+n)$"
        self.assertEqual(_parse_complexity(text), ComplexityClass.O_KN)

    def test_numeric_base_exponential_complexity_is_not_misclassified_as_linear(self) -> None:
        text = "### Required Complexity\n- **Time:** $O(9^E)$\n- **Space:** $O(E)$"
        self.assertEqual(_parse_complexity(text), ComplexityClass.O_KN)

    def test_reference_doc_resolves_from_challenge_package(self) -> None:
        response = self.client.get("/api/docs/by-id/lc_1")
        self.assertEqual(response.status_code, 200, response.text)
        self.assertIn("# Two Sum", response.text)
        self.assertIn("### 1. Description", response.text)
        self.assertIn("### 2. Function Contract", response.text)
        self.assertIn("### 3. Examples", response.text)
        self.assertIn("### 4. Constraints", response.text)
        self.assertIn("### 5. Follow-up", response.text)
        self.assertIn("| Supported Language | Python |", response.text)
        self.assertNotIn("Supported Languages", response.text)
        ordered_sections = (
            "### 1. Description",
            "### 2. Function Contract",
            "### 3. Examples",
            "### 4. Constraints",
            "### 5. Follow-up",
        )
        self.assertEqual(
            sorted(response.text.index(section) for section in ordered_sections),
            [response.text.index(section) for section in ordered_sections],
        )
        self.assertNotIn("### Required Complexity", response.text)

    def test_reference_metadata_exposes_zerotrac_contest_source(self) -> None:
        response = self.client.get("/api/docs/by-id/lc_3693")

        self.assertEqual(response.status_code, 200, response.text)
        self.assertIn("| Contest Source | Biweekly Contest 166 |", response.text)
        self.assertIn("| Contest Problem | Q2 |", response.text)

    def test_pdf_sources_expose_only_the_optimal_approach_and_editorial(self) -> None:
        package = leetcode_package_dir("lc_1502")
        self.assertIsNotNone(package)
        assert package is not None

        approach = self.client.get("/api/docs/by-id/lc_1502/optimal-approach")
        self.assertEqual(approach.status_code, 200, approach.text)
        approach_path = leetcode_optimal_approach_path("lc_1502")
        self.assertIsNotNone(approach_path)
        assert approach_path is not None
        self.assertEqual(
            approach.text,
            approach_path.read_text(encoding="utf-8"),
        )

        editorial = self.client.get("/api/docs/by-id/lc_1502/editorial")
        self.assertEqual(editorial.status_code, 200, editorial.text)
        self.assertEqual(
            editorial.text,
            (package / "reference" / "editorial.md").read_text(encoding="utf-8"),
        )

    def test_monolithic_reference_images_are_served_as_doc_assets(self) -> None:
        response = self.client.get(
            "/api/docs/by-id/lc_2/assets/images/addtwonumber1.jpg"
        )
        self.assertEqual(response.status_code, 200, response.text)
        self.assertEqual(response.headers["content-type"], "image/jpeg")
        self.assertGreater(len(response.content), 0)

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

    def test_composed_metadata_exposes_one_supported_language(self) -> None:
        response = self.client.get("/api/docs/by-id/lc_764")

        self.assertEqual(response.status_code, 200, response.text)
        self.assertIn("| Supported Language | Python |", response.text)
        self.assertNotIn("Supported Languages", response.text)

    def test_monolithic_source_native_sections_keep_numbered_order(self) -> None:
        custom_judge = self.client.get("/api/docs/by-id/lc_26")
        self.assertEqual(custom_judge.status_code, 200, custom_judge.text)
        custom_headings = (
            "### 1. Description",
            "### 2. Function Contract",
            "### 3. Custom Judge",
            "### 4. Examples",
            "### 5. Constraints",
        )
        self.assertEqual(
            sorted(custom_judge.text.index(heading) for heading in custom_headings),
            [custom_judge.text.index(heading) for heading in custom_headings],
        )

        note = self.client.get("/api/docs/by-id/lc_29")
        self.assertEqual(note.status_code, 200, note.text)
        self.assertLess(note.text.index("### 1. Description"), note.text.index("### 3. Note"))
        self.assertLess(note.text.index("### 3. Note"), note.text.index("### 4. Examples"))

    def test_monolithic_sql_doc_preserves_source_order_without_constraints(self) -> None:
        response = self.client.get("/api/docs/by-id/lc_175")

        self.assertEqual(response.status_code, 200, response.text)
        signposts = (
            "### 1. Description",
            "Table: `Person`",
            "Table: `Address`",
            "### 2. Function Contract",
            "### 3. Examples",
        )
        self.assertEqual(
            sorted(response.text.index(signpost) for signpost in signposts),
            [response.text.index(signpost) for signpost in signposts],
        )
        self.assertNotIn("### 4. Constraints", response.text)
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

    def test_docs_index_contains_every_canonical_registry_challenge(self) -> None:
        response = self.client.get("/api/docs/index")
        self.assertEqual(response.status_code, 200, response.text)
        entries = response.json()
        lc_entries = [entry for entry in entries if str(entry["id"]).startswith("lc_")]
        self.assertEqual(len(lc_entries), 4005)
        self.assertEqual(
            {entry["id"] for entry in lc_entries},
            {f"lc_{frontend_id}" for frontend_id in range(1, 4006)},
        )
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
        package = leetcode_package_dir("lc_1")
        self.assertIsNotNone(package)
        assert package is not None
        expected = (package / "reference" / "description.md").read_text(
            encoding="utf-8"
        )
        self.assertEqual(response.text, expected)

        legacy = self.client.get("/api/docs/algorithms/README.md")
        self.assertEqual(legacy.status_code, 404)

    def test_canonical_paths_are_padded_without_changing_challenge_ids(self) -> None:
        package = leetcode_package_dir("lc_1")
        self.assertIsNotNone(package)
        assert package is not None
        self.assertEqual(package.name, "0001_two-sum")
        self.assertEqual(leetcode_package_id(Path("0001_two-sum")), "lc_1")
