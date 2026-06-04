"""Tests for progress save/load and the PlayerProgress model.

Run with:
    .venv/Scripts/python.exe -m unittest tests.test_progress -v
"""
from __future__ import annotations

import json
import os
import tempfile
import unittest
from pathlib import Path

from code_n.progress import LevelRecord, PlayerProgress, load_progress, save_progress


class PlayerProgressModelTests(unittest.TestCase):
    def test_complete_records_first_attempt(self):
        p = PlayerProgress()
        p.complete("intro_01", ops=10, complexity="O(n)")
        self.assertIn("intro_01", p.completed)
        self.assertEqual(p.status_for("intro_01"), "done")
        rec = p.records["intro_01"]
        self.assertEqual(rec.best_ops, 10)
        self.assertEqual(rec.complexity_achieved, "O(n)")
        self.assertEqual(rec.attempts, 1)

    def test_complete_keeps_best_ops(self):
        p = PlayerProgress()
        p.complete("intro_01", ops=20, complexity="O(n)")
        p.complete("intro_01", ops=10, complexity="O(n)")  # better
        p.complete("intro_01", ops=15, complexity="O(n)")  # worse
        rec = p.records["intro_01"]
        self.assertEqual(rec.best_ops, 10)
        self.assertEqual(rec.attempts, 3)

    def test_fail_marks_status_without_dropping_record(self):
        p = PlayerProgress()
        p.complete("intro_01", ops=10, complexity="O(n)")
        p.fail("intro_01")
        # failed status overrides "done" for the latest view
        self.assertEqual(p.status_for("intro_01"), "failed")
        # but the record is preserved
        self.assertIn("intro_01", p.records)

    def test_reset_statuses_clears_everything(self):
        p = PlayerProgress(player_name="Alex")
        p.complete("intro_01", ops=10, complexity="O(n)")
        p.reset_statuses()
        self.assertEqual(p.completed, set())
        self.assertEqual(p.records, {})
        self.assertEqual(p.last_status, {})
        # player name is preserved
        self.assertEqual(p.player_name, "Alex")

    def test_serialization_round_trip(self):
        p = PlayerProgress(player_name="Alex")
        p.complete("intro_01", ops=10, complexity="O(n)")
        p.complete("search_01", ops=20, complexity="O(n)")
        p.fail("search_02")

        blob = p.to_dict()
        restored = PlayerProgress.from_dict(blob)

        self.assertEqual(restored.player_name, "Alex")
        self.assertIn("intro_01", restored.completed)
        self.assertIn("search_01", restored.completed)
        self.assertEqual(restored.status_for("search_02"), "failed")
        self.assertEqual(restored.records["intro_01"].best_ops, 10)


class SaveLoadFileTests(unittest.TestCase):
    def test_save_and_load_round_trip(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "progress.json")
            p = PlayerProgress(player_name="Test")
            p.complete("intro_01", ops=42, complexity="O(n)")
            save_progress(p, path=path)

            # File exists and is valid JSON
            self.assertTrue(os.path.exists(path))
            with open(path) as f:
                data = json.load(f)
            self.assertEqual(data["player_name"], "Test")

            loaded = load_progress(path=path)
            self.assertIn("intro_01", loaded.completed)
            self.assertEqual(loaded.records["intro_01"].best_ops, 42)

    def test_load_missing_returns_empty(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "does-not-exist.json")
            p = load_progress(path=path)
            self.assertEqual(p.completed, set())
            self.assertEqual(p.records, {})
            self.assertEqual(p.player_name, "")


class LegacyMigrationTests(unittest.TestCase):
    """Older progress.json files used a flat `completed` list without
    `last_status`. New code should treat them as 'done'."""

    def test_legacy_completed_migrated_to_done(self):
        legacy = {
            "player_name": "Legacy",
            "completed": ["intro_01", "search_01"],
            "records": {
                "intro_01": {
                    "challenge_id": "intro_01",
                    "best_ops": 5,
                    "complexity_achieved": "O(n)",
                    "attempts": 1,
                }
            },
        }
        p = PlayerProgress.from_dict(legacy)
        self.assertIn("intro_01", p.completed)
        self.assertIn("search_01", p.completed)
        self.assertEqual(p.status_for("intro_01"), "done")


if __name__ == "__main__":
    unittest.main()
