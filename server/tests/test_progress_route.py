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
        self.assertEqual(body["active_set"], "leetcode")
        self.assertEqual(body["pane_font_scales"], {})
        self.assertEqual(body["pane_sizes"], {})
        self.assertEqual(body["accent_colors"], {"light": "#0284c7", "dark": "#03dac6"})

    def test_pane_font_scales_are_profile_persistent_and_clamped(self) -> None:
        response = self.client.put(
            "/api/progress",
            json={"pane_font_scales": {"sidebar": 1.2, "workspace:reference": 9}},
        )
        self.assertEqual(response.status_code, 200, response.text)
        self.assertEqual(
            response.json()["pane_font_scales"],
            {"sidebar": 1.2, "workspace:reference": 1.5},
        )
        self.assertEqual(
            self.client.get("/api/progress").json()["pane_font_scales"],
            {"sidebar": 1.2, "workspace:reference": 1.5},
        )

    def test_pane_sizes_are_profile_persistent_and_clamped(self) -> None:
        response = self.client.put(
            "/api/progress",
            json={"pane_sizes": {"coden.debugPanelWidth": 512, "too-large": 9000}},
        )
        self.assertEqual(response.status_code, 200, response.text)
        self.assertEqual(
            response.json()["pane_sizes"],
            {"coden.debugPanelWidth": 512.0, "too-large": 1600.0},
        )
        self.assertEqual(
            self.client.get("/api/progress").json()["pane_sizes"],
            {"coden.debugPanelWidth": 512.0, "too-large": 1600.0},
        )

    def test_accent_colors_are_profile_persistent_and_sanitized(self) -> None:
        response = self.client.put(
            "/api/progress",
            json={"accent_colors": {"light": "#AABBCC", "dark": "rgba(12, 34, 56, 0.75)"}},
        )
        self.assertEqual(response.status_code, 200, response.text)
        self.assertEqual(
            response.json()["accent_colors"],
            {"light": "#aabbcc", "dark": "rgba(12, 34, 56, 0.75)"},
        )
        self.assertEqual(
            self.client.get("/api/progress").json()["accent_colors"],
            {"light": "#aabbcc", "dark": "rgba(12, 34, 56, 0.75)"},
        )

        invalid = self.client.put(
            "/api/progress",
            json={"accent_colors": {"light": "url(javascript:bad)", "dark": "rgba(999, 0, 0, 1)"}},
        )
        self.assertEqual(invalid.status_code, 200, invalid.text)
        self.assertEqual(
            invalid.json()["accent_colors"],
            {"light": "#0284c7", "dark": "#03dac6"},
        )

    def test_mark_challenge_done(self) -> None:
        r = self.client.put(
            "/api/progress",
            json={"mark": {"challenge_id": "lc_1", "ops": 1234, "complexity": "O(n²)"}},
        )
        self.assertEqual(r.status_code, 200, r.text)
        body = r.json()
        self.assertIn("lc_1", body["completed"])
        self.assertEqual(body["last_status"]["lc_1"], "done")
        self.assertIn("lc_1", body["records"])
        record = body["records"]["lc_1"]
        self.assertEqual(record["best_ops"], 1234)
        self.assertEqual(record["complexity_achieved"], "O(n²)")
        self.assertEqual(record["attempts"], 1)

    def test_get_reflects_mark(self) -> None:
        # PUT a mark, then GET to confirm persistence.
        self.client.put(
            "/api/progress",
            json={"mark": {"challenge_id": "lc_704", "ops": 99, "complexity": "O(1)"}},
        )
        r = self.client.get("/api/progress")
        self.assertEqual(r.status_code, 200)
        body = r.json()
        self.assertIn("lc_704", body["completed"])


    def test_fail_challenge(self) -> None:
        # Mark first (so it ends up in completed), then fail (which
        # removes from completed and records the failure).
        self.client.put(
            "/api/progress",
            json={"mark": {"challenge_id": "lc_1", "ops": 50, "complexity": "O(n²)"}},
        )
        r = self.client.put(
            "/api/progress",
            json={"fail": "lc_1"},
        )
        self.assertEqual(r.status_code, 200)
        body = r.json()
        self.assertNotIn("lc_1", body["completed"])
        self.assertEqual(body["last_status"]["lc_1"], "failed")

    def test_reset_clears_all(self) -> None:
        self.client.put(
            "/api/progress",
            json={"mark": {"challenge_id": "lc_1", "ops": 50, "complexity": "O(n²)"}},
        )
        r = self.client.put("/api/progress", json={"reset": True})
        self.assertEqual(r.status_code, 200)
        body = r.json()
        self.assertEqual(body["completed"], [])
        self.assertEqual(body["records"], {})
