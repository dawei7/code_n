"""Smoke tests for the challenge registry and the max-n caps.

End-to-end ``run + verify`` tests against the complexity budget
used to live here, calling ``Challenge.run(solve_fn=...)``.
``Challenge.run`` was removed in v0.8.5 along with the runtime
op counter — the equivalent path is now the server's
``run_player_code`` function, tested in ``server/tests/``.

What's left here is a small set of registry / constant tests
that don't depend on the execution pipeline.
"""
from __future__ import annotations

import unittest

from challenges.registry import get_challenge, list_challenges


class RegistryTests(unittest.TestCase):
    def test_list_challenges_non_empty(self):
        ids = list_challenges()
        self.assertGreater(len(ids), 0)
        # Every id should resolve.
        for cid in ids:
            self.assertIsNotNone(get_challenge(cid), msg=f"missing: {cid}")

class MaxNCapTests(unittest.TestCase):
    """1D challenges accept up to 50; 2D grid challenges (BFS, DFS)
    cap at 35 because a 50x50 grid is too dense to be useful even at
    the smallest zoom."""

    def test_1d_challenges_default_to_50(self):
        for cid in ("sort_01", "search_01", "search_02",
                    "dp_01", "dp_02"):

            ch = get_challenge(cid)
            self.assertIsNotNone(ch, msg=f"missing: {cid}")
            self.assertEqual(ch.max_n, 50, msg=f"{cid} should cap at 50")

    def test_2d_grid_challenges_cap_at_35(self):
        for cid in ("search_03", "search_04"):
            ch = get_challenge(cid)
            self.assertIsNotNone(ch, msg=f"missing: {cid}")
            self.assertEqual(ch.max_n, 35, msg=f"{cid} should cap at 35")
            self.assertLess(ch.max_n, ch.MAX_N)


if __name__ == "__main__":
    unittest.main()
