"""Tests for ``GET /api/progress`` and ``PUT /api/progress``."""
from __future__ import annotations

import json

from . import conftest  # noqa: F401
from server.app import progress_store
from server.app.user_solutions import migrate_legacy_solutions, user_solution_dir


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
        self.assertEqual(body["active_custom_set_id"], "")
        self.assertEqual(body["pane_font_scales"], {})
        self.assertEqual(body["pane_sizes"], {})
        self.assertEqual(body["accent_colors"], {"light": "#0284c7", "dark": "#03dac6"})

    def test_active_personal_root_is_profile_persistent(self) -> None:
        response = self.client.put(
            "/api/progress",
            json={
                "active_set": "custom",
                "active_custom_set_id": "set_shared_interview_path",
            },
        )
        self.assertEqual(response.status_code, 200, response.text)
        self.assertEqual(response.json()["active_set"], "custom")
        self.assertEqual(
            response.json()["active_custom_set_id"],
            "set_shared_interview_path",
        )
        reloaded = self.client.get("/api/progress").json()
        self.assertEqual(reloaded["active_set"], "custom")
        self.assertEqual(
            reloaded["active_custom_set_id"],
            "set_shared_interview_path",
        )

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

    def _seed_scoped_reset_progress(self) -> None:
        for challenge_id in ("lc_1", "lc_2"):
            self.client.put(
                "/api/progress",
                json={
                    "mark": {
                        "challenge_id": challenge_id,
                        "ops": 50,
                        "complexity": "O(n)",
                    }
                },
            )
        progress = progress_store.load()
        progress.leetcode_solved = ["lc_1", "lc_2"]
        progress.unlocked_leetcode = ["lc_1", "lc_2"]
        progress.leetcode_submissions = {
            "lc_1": {"submission_id": "101", "status": "Accepted"},
            "lc_2": {"submission_id": "202", "status": "Accepted"},
        }
        progress.active_set = "neetcode"
        progress_store.save(progress)

        for challenge_id in ("lc_1", "lc_2"):
            response = self.client.get(f"/api/solutions/{challenge_id}?language=python")
            self.assertEqual(response.status_code, 200, response.text)
            directory = user_solution_dir(challenge_id)
            (directory / "python_v1.py").write_text(
                f"# personal {challenge_id}\n",
                encoding="utf-8",
            )
            (directory / "javascript_v1.js").write_text(
                f"// personal {challenge_id}\n",
                encoding="utf-8",
            )

        legacy_python = conftest._TEST_LEGACY_SOLUTIONS / "python"
        legacy_python.mkdir(parents=True, exist_ok=True)
        for challenge_id in ("lc_1", "lc_2"):
            (legacy_python / f"{challenge_id}.py").write_text(
                f"# legacy {challenge_id}\n",
                encoding="utf-8",
            )
        (conftest._TEST_LEGACY_SOLUTIONS / ".versions.json").write_text(
            json.dumps(
                {
                    "python:lc_1": {"active": 1},
                    "python:lc_2": {"active": 2},
                }
            ),
            encoding="utf-8",
        )

    def test_confirmed_coden_reset_is_scoped_and_preserves_leetcode(self) -> None:
        self._seed_scoped_reset_progress()

        r = self.client.post(
            "/api/progress/reset",
            json={
                "scope": "coden",
                "challenge_ids": ["lc_1"],
                "confirmation": "RESET",
            },
        )

        self.assertEqual(r.status_code, 200, r.text)
        body = r.json()
        self.assertEqual(body["completed"], ["lc_2"])
        self.assertNotIn("lc_1", body["last_status"])
        self.assertNotIn("lc_1", body["records"])
        self.assertIn("lc_1", body["leetcode_submissions"])
        self.assertEqual(body["active_set"], "neetcode")
        self.assertFalse(user_solution_dir("lc_1").exists())
        self.assertTrue(user_solution_dir("lc_2").is_dir())
        self.assertFalse(
            (conftest._TEST_LEGACY_SOLUTIONS / "python" / "lc_1.py").exists()
        )
        self.assertTrue(
            (conftest._TEST_LEGACY_SOLUTIONS / "python" / "lc_2.py").is_file()
        )
        legacy_state = json.loads(
            (conftest._TEST_LEGACY_SOLUTIONS / ".versions.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertNotIn("python:lc_1", legacy_state)
        self.assertIn("python:lc_2", legacy_state)

        migrate_legacy_solutions([conftest._TEST_LEGACY_SOLUTIONS])
        self.assertFalse(user_solution_dir("lc_1").exists())

    def test_confirmed_leetcode_reset_is_scoped_and_preserves_coden(self) -> None:
        self._seed_scoped_reset_progress()

        r = self.client.post(
            "/api/progress/reset",
            json={
                "scope": "leetcode",
                "challenge_ids": ["lc_1"],
                "confirmation": "RESET",
            },
        )

        self.assertEqual(r.status_code, 200, r.text)
        body = r.json()
        self.assertIn("lc_1", body["completed"])
        self.assertNotIn("lc_1", body["leetcode_solved"])
        self.assertNotIn("lc_1", body["unlocked_leetcode"])
        self.assertNotIn("lc_1", body["leetcode_submissions"])
        self.assertIn("lc_2", body["leetcode_submissions"])
        self.assertTrue(user_solution_dir("lc_1").is_dir())
        self.assertTrue(user_solution_dir("lc_2").is_dir())
        self.assertTrue(
            (conftest._TEST_LEGACY_SOLUTIONS / "python" / "lc_1.py").is_file()
        )

    def test_confirmed_all_reset_clears_both_scopes_only_for_selected_ids(self) -> None:
        self._seed_scoped_reset_progress()

        r = self.client.post(
            "/api/progress/reset",
            json={
                "scope": "all",
                "challenge_ids": ["lc_1", "lc_1"],
                "confirmation": "RESET",
            },
        )

        self.assertEqual(r.status_code, 200, r.text)
        body = r.json()
        self.assertEqual(body["completed"], ["lc_2"])
        self.assertNotIn("lc_1", body["leetcode_submissions"])
        self.assertIn("lc_2", body["leetcode_submissions"])
        self.assertEqual(body["active_set"], "neetcode")
        self.assertFalse(user_solution_dir("lc_1").exists())
        self.assertTrue(user_solution_dir("lc_2").is_dir())

    def test_confirmed_reset_rejects_non_exact_confirmation(self) -> None:
        self._seed_scoped_reset_progress()

        for confirmation in ("reset", " RESET", "RESET "):
            r = self.client.post(
                "/api/progress/reset",
                json={
                    "scope": "all",
                    "challenge_ids": ["lc_1"],
                    "confirmation": confirmation,
                },
            )
            self.assertEqual(r.status_code, 400, r.text)

        body = self.client.get("/api/progress").json()
        self.assertIn("lc_1", body["completed"])
        self.assertIn("lc_1", body["leetcode_submissions"])
        self.assertTrue(user_solution_dir("lc_1").is_dir())
        self.assertTrue(
            (conftest._TEST_LEGACY_SOLUTIONS / "python" / "lc_1.py").is_file()
        )
