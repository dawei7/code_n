"""Tests for package-authored, code-free guided examples."""
from __future__ import annotations

from server.app.challenge_packages import leetcode_guided_example_path

from . import conftest


class GuidedExamplesTest(conftest._Base):
    AUTHORED = {
        "lc_1": "Two Sum",
        "lc_2": "Add Two Numbers",
        "lc_3": "Longest Substring Without Repeating Characters",
        "lc_4": "Median of Two Sorted Arrays",
        "lc_15": "3Sum",
    }

    def test_authored_guides_are_markdown_lessons(self) -> None:
        for challenge_id, title in self.AUTHORED.items():
            with self.subTest(challenge_id=challenge_id):
                response = self.client.get(
                    f"/api/docs/by-id/{challenge_id}/guided-example"
                )
                self.assertEqual(response.status_code, 200, response.text)
                self.assertTrue(
                    response.headers["content-type"].startswith("text/markdown")
                )
                markdown = response.text
                self.assertTrue(markdown.startswith(f"# Guided Example: {title}"))
                self.assertIn("## 1.", markdown)
                self.assertTrue(
                    "## Why the reasoning is correct" in markdown
                    or "## 5. Algorithmic Correctness" in markdown
                    or "## Algorithmic Correctness" in markdown
                )
                self.assertTrue(
                    "## Cost of the method" in markdown
                    or "## 7. Complexity Derivation" in markdown
                    or "## Complexity Derivation" in markdown
                )
                self.assertGreaterEqual(markdown.count("|---"), 2)
                self.assertGreaterEqual(len(markdown), 2_500)

    def test_guides_do_not_expose_solution_source(self) -> None:
        forbidden = (
            "class Solution",
            "def solve(",
            "def twoSum(",
            "solutions/",
            "```python",
            "```cpp",
            "```java",
            "```javascript",
        )
        for challenge_id in self.AUTHORED:
            with self.subTest(challenge_id=challenge_id):
                response = self.client.get(
                    f"/api/docs/by-id/{challenge_id}/guided-example"
                )
                self.assertEqual(response.status_code, 200, response.text)
                self.assertFalse(
                    any(marker in response.text for marker in forbidden),
                    response.text,
                )

    def test_challenge_summary_advertises_guided_example(self) -> None:
        for challenge_id in self.AUTHORED:
            with self.subTest(challenge_id=challenge_id):
                response = self.client.get(f"/api/challenges/{challenge_id}")
                self.assertEqual(response.status_code, 200, response.text)
                self.assertTrue(response.json()["has_guided_example"])

    def test_guided_example_path_is_package_local(self) -> None:
        path = leetcode_guided_example_path("lc_15")
        self.assertIsNotNone(path)
        assert path is not None
        self.assertEqual(path.name, "guided_example.md")
        self.assertEqual(path.parent.name, "0015_3sum")

    def test_missing_guided_example_returns_not_found(self) -> None:
        response = self.client.get("/api/docs/by-id/lc_99999/guided-example")
        self.assertEqual(response.status_code, 404, response.text)
        self.assertTrue(
            "not found" in response.json()["detail"].lower()
            or "no guided example" in response.json()["detail"].lower()
        )

