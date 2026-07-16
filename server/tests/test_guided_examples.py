"""Tests for package-authored, code-free guided examples."""
from __future__ import annotations

from server.app.challenge_packages import leetcode_guided_example_path

from . import conftest


class GuidedExamplesTest(conftest._Base):
    AUTHORED = {
        "lc_1": "Two Sum",
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
                self.assertIn("## Why the reasoning is correct", markdown)
                self.assertIn("## Cost of the method", markdown)
                self.assertGreaterEqual(markdown.count("|---"), 3)
                self.assertGreaterEqual(len(markdown), 4_000)

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

        without_guide = self.client.get("/api/challenges/lc_2")
        self.assertEqual(without_guide.status_code, 200, without_guide.text)
        self.assertFalse(without_guide.json()["has_guided_example"])

    def test_guided_example_path_is_package_local(self) -> None:
        path = leetcode_guided_example_path("lc_15")
        self.assertIsNotNone(path)
        assert path is not None
        self.assertEqual(path.name, "guided_example.md")
        self.assertEqual(path.parent.name, "0015_3sum")

    def test_missing_guided_example_returns_not_found(self) -> None:
        response = self.client.get("/api/docs/by-id/lc_2/guided-example")
        self.assertEqual(response.status_code, 404, response.text)
        self.assertIn("No guided example", response.json()["detail"])

