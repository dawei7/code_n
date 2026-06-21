"""Tests for ``GET /api/challenges`` and ``GET /api/challenges/{id}``."""
from __future__ import annotations

from . import conftest  # noqa: F401


class ListChallengesTest(conftest._Base):
    def test_list_returns_all_registered(self) -> None:
        r = self.client.get("/api/challenges")
        self.assertEqual(r.status_code, 200, r.text)
        body = r.json()
        self.assertIsInstance(body, list)
        # The registry has 25+ entries (intro, sorting, searching, graphs, dynamic, greedy).
        self.assertGreaterEqual(len(body), 25, f"Got {len(body)} challenges; expected at least 25")
        ids = {c["id"] for c in body}
        self.assertIn("sort_01", ids)
        self.assertIn("search_01", ids)

    def test_summary_has_required_fields(self) -> None:
        r = self.client.get("/api/challenges")
        self.assertEqual(r.status_code, 200)
        summary = next(c for c in r.json() if c["id"] == "sort_01")
        for field in (
            "id", "name", "category", "difficulty", "required_complexity",
            "description", "max_n",
        ):
            self.assertIn(field, summary, f"missing field {field!r}")
        self.assertEqual(summary["id"], "sort_01")
        self.assertEqual(summary["required_complexity"], "O(n²)")

    def test_unknown_challenge_returns_404(self) -> None:
        r = self.client.get("/api/challenges/does_not_exist")
        self.assertEqual(r.status_code, 404)


class GetChallengeDetailTest(conftest._Base):
    def test_sort_01_detail(self) -> None:
        r = self.client.get("/api/challenges/sort_01")
        self.assertEqual(r.status_code, 200, r.text)
        body = r.json()
        self.assertEqual(body["id"], "sort_01")
        self.assertIn("params", body)
        # Sort challenges have `data` and `n` as parameters.
        param_names = {p["name"] for p in body["params"]}
        self.assertIn("data", param_names)
        self.assertIn("n", param_names)
        # The starter source is a `def solve(...)` template.
        self.assertIn("def solve(data, n):", body["starter_source"])
        # The optimal source is the canonical bubble sort.
        self.assertIn("data[i], data[i + 1] = data[i + 1], data[i]", body["optimal_source"])
        # samples are surfaced (sort_01 has at least 1).
        self.assertIsInstance(body["samples"], list)
