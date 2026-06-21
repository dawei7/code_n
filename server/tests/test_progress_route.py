"""Tests for ``GET /api/progress`` and ``PUT /api/progress``."""
from __future__ import annotations

from . import conftest  # noqa: F401


class ProgressTest(conftest._Base):
    def test_get_fresh_progress(self) -> None:
        r = self.client.get("/api/progress")
        self.assertEqual(r.status_code, 200)
        body = r.json()
        self.assertEqual(body["player_name"], "")
        self.assertEqual(body["completed"], [])
        self.assertEqual(body["last_status"], {})
        self.assertEqual(body["records"], {})

    def test_mark_challenge_done(self) -> None:
        r = self.client.put(
            "/api/progress",
            json={"mark": {"challenge_id": "sort_01", "ops": 1234, "complexity": "O(n²)"}},
        )
        self.assertEqual(r.status_code, 200, r.text)
        body = r.json()
        self.assertIn("sort_01", body["completed"])
        self.assertEqual(body["last_status"]["sort_01"], "done")
        self.assertIn("sort_01", body["records"])
        record = body["records"]["sort_01"]
        self.assertEqual(record["best_ops"], 1234)
        self.assertEqual(record["complexity_achieved"], "O(n²)")
        self.assertEqual(record["attempts"], 1)

    def test_get_reflects_mark(self) -> None:
        # PUT a mark, then GET to confirm persistence.
        self.client.put(
            "/api/progress",
            json={"mark": {"challenge_id": "search_01", "ops": 99, "complexity": "O(1)"}},
        )
        r = self.client.get("/api/progress")
        self.assertEqual(r.status_code, 200)
        body = r.json()
        self.assertIn("search_01", body["completed"])


    def test_fail_challenge(self) -> None:
        # Mark first (so it ends up in completed), then fail (which
        # removes from completed and records the failure).
        self.client.put(
            "/api/progress",
            json={"mark": {"challenge_id": "sort_01", "ops": 50, "complexity": "O(n²)"}},
        )
        r = self.client.put(
            "/api/progress",
            json={"fail": "sort_01"},
        )
        self.assertEqual(r.status_code, 200)
        body = r.json()
        self.assertNotIn("sort_01", body["completed"])
        self.assertEqual(body["last_status"]["sort_01"], "failed")

    def test_reset_clears_all(self) -> None:
        self.client.put(
            "/api/progress",
            json={"mark": {"challenge_id": "sort_01", "ops": 50, "complexity": "O(n²)"}},
        )
        r = self.client.put("/api/progress", json={"reset": True})
        self.assertEqual(r.status_code, 200)
        body = r.json()
        self.assertEqual(body["completed"], [])
        self.assertEqual(body["records"], {})
