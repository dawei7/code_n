"""Tests for the navigator's Solve button.

Solve copies the canonical optimal solution from
``optimal_solutions/<id>.py`` into the player's
``solutions/<id>.py``, runs it to capture the actual op count,
and marks the challenge as done in progress.json.

These tests are lightweight: they exercise the solver action
directly (the full navigator Pygame loop is hard to drive
headlessly) and assert the side effects (file written, progress
updated, marked complete).
"""
from __future__ import annotations

import importlib.util
import os
import tempfile
import unittest
from pathlib import Path

import code_n.navigation as navigation_module
from challenges.registry import get_challenge
from code_n.navigation import ChallengeNavigator
from code_n.progress import load_progress, save_progress
from code_n.solutions import PROJECT_ROOT, SOLUTIONS_DIR


def _make_navigator():
    """Build a ChallengeNavigator with a fresh progress state.

    We bypass the constructor's call to load_progress() by using
    __new__ and assigning the same attributes the constructor would
    have, so tests don't touch the real progress.json.
    """
    nav = ChallengeNavigator.__new__(ChallengeNavigator)
    from code_n.tree import ChallengeTree
    from code_n.progress import PlayerProgress
    nav.tree = ChallengeTree()
    nav.progress = PlayerProgress()
    # Call _build_items so nav.items / nav.selected_index are
    # populated. The constructor does this too, but only after
    # loading progress; we replicate it here with a fresh
    # PlayerProgress so tests are deterministic.
    nav.selected_index = 0
    nav._progress_mtime = 0.0
    nav.items = nav._build_items()
    return nav


class SolveButtonTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        # Redirect progress I/O to a temp file. The save_progress/
        # load_progress functions live in code_n.progress and use
        # their module's PROGRESS_FILE constant, so we patch that
        # module (not code_n.navigation which just re-exports them).
        import code_n.progress as progress_module
        self._saved_progress = progress_module.PROGRESS_FILE
        self.progress_path = os.path.join(self.tmp.name, "progress.json")
        progress_module.PROGRESS_FILE = self.progress_path

    def tearDown(self):
        import code_n.progress as progress_module
        progress_module.PROGRESS_FILE = self._saved_progress

    def test_solve_copies_optimal_and_marks_done(self):
        nav = _make_navigator()
        nav.solve_selected_challenge()

        # The optimal intro_01 solution should now be in solutions/.
        target = os.path.join(SOLUTIONS_DIR, "intro_01.py")
        self.assertTrue(os.path.exists(target), msg=target)
        with open(target) as f:
            content = f.read()
        # Optimal solution should have the comment docstring.
        self.assertIn("Optimal solution for intro_01", content)
        self.assertIn("def solve(data):", content)

        # Progress should now mark intro_01 as done.
        progress = load_progress(path=self.progress_path)
        self.assertEqual(progress.status_for("intro_01"), "done")
        self.assertIn("intro_01", progress.completed)
        record = progress.records["intro_01"]
        self.assertGreater(record.best_ops, 0)
        self.assertEqual(record.complexity_achieved, "O(n)")

    def test_solve_message_includes_reset_hint(self):
        nav = _make_navigator()
        nav.solve_selected_challenge()
        # The user-facing message should tell the player how to try again.
        self.assertIn("Reset", nav.message)
        self.assertIn("try again", nav.message.lower())

    def test_solve_overwrites_existing_player_solution(self):
        # Pre-create a player-specific file that's NOT the optimal,
        # then verify Solve replaces it.
        target = os.path.join(SOLUTIONS_DIR, "intro_01.py")
        with open(target, "w", encoding="utf-8") as f:
            f.write("# this is the player's own attempt\ndef solve(data):\n    return 0\n")
        with open(target) as f:
            before = f.read()
        self.assertIn("player's own attempt", before)

        # Now click Solve.
        nav = _make_navigator()
        nav.solve_selected_challenge()
        with open(target) as f:
            after = f.read()
        # The optimal's docstring should have replaced the player's file.
        self.assertIn("Optimal solution for intro_01", after)
        self.assertNotIn("player's own attempt", after)

    def test_solve_noop_when_nothing_selected(self):
        nav = _make_navigator()
        # No items - simulate empty navigator.
        nav.items = []
        nav.solve_selected_challenge()
        # Progress is unchanged.
        progress = load_progress(path=self.progress_path)
        self.assertEqual(progress.completed, set())

    def test_all_registered_optimal_solutions_exist(self):
        """Every registered challenge has a corresponding optimal
        solution file the Solve button can copy."""
        from challenges.registry import CHALLENGE_REGISTRY
        for cid in CHALLENGE_REGISTRY:
            optimal = Path(PROJECT_ROOT) / "optimal_solutions" / f"{cid}.py"
            self.assertTrue(optimal.exists(), msg=f"missing: {optimal}")
            # Every optimal file must define `solve`.
            spec = importlib.util.spec_from_file_location(
                f"_opt_{cid}", optimal,
            )
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)  # type: ignore[union-attr]
            self.assertTrue(callable(getattr(mod, "solve", None)),
                            msg=f"no solve() in {optimal}")


if __name__ == "__main__":
    unittest.main()
