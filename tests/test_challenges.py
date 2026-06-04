"""End-to-end tests for challenges: a known-correct solution passes,
a known-bad solution fails on correctness or on complexity, and the setup
is deterministic given a seed.

Run with:
    .venv/Scripts/python.exe -m unittest tests.test_challenges -v
"""
from __future__ import annotations

import unittest

from challenges.registry import get_challenge, list_challenges
from code_n.challenge import ChallengeResult
from code_n.counter import reset_counter


# ---- Reference solutions (correct, in the required complexity class) ----

def _intro_01(data):
    best = data[0]
    for i in range(1, len(data)):
        v = data[i]
        if v > best:
            best = v
    return best


def _search_01(data, target):
    for index, v in enumerate(data):
        if v == target:
            return index
    return -1


def _search_02(data, target, n):
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        v = data[mid]
        if v == target:
            return mid
        if v < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def _dp_01(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# ---- Reference solutions that intentionally violate complexity ----

def _search_02_bad(data, target, n):
    # Linear scan; will blow the O(log n) budget for large n.
    for index, v in enumerate(data):
        if v == target:
            return index
    return -1


class IntroHelloGridTests(unittest.TestCase):
    def setUp(self):
        reset_counter()

    def tearDown(self):
        reset_counter()

    def test_correct_solution_passes(self):
        challenge = get_challenge("intro_01")
        result = challenge.run(solve_fn=_intro_01, n=32, seed=1, animate=False)
        self.assertTrue(result.passed, msg=result.message)
        self.assertTrue(result.correct)
        self.assertTrue(result.within_threshold)
        self.assertEqual(result.actual_complexity.value, "O(n)")

    def test_wrong_answer_fails(self):
        def wrong(data):
            return 0  # never finds the max

        challenge = get_challenge("intro_01")
        result = challenge.run(solve_fn=wrong, n=16, seed=1, animate=False)
        self.assertFalse(result.passed)
        self.assertFalse(result.correct)
        self.assertIn("Incorrect", result.message)

    def test_result_dataclass_fields(self):
        challenge = get_challenge("intro_01")
        result = challenge.run(solve_fn=_intro_01, n=8, seed=1, animate=False)
        self.assertIsInstance(result, ChallengeResult)
        self.assertEqual(result.n, 8)
        self.assertGreater(result.stats.total, 0)


class SearchChallengeTests(unittest.TestCase):
    def setUp(self):
        reset_counter()

    def tearDown(self):
        reset_counter()

    def test_linear_search_passes(self):
        challenge = get_challenge("search_01")
        result = challenge.run(solve_fn=_search_01, n=20, seed=2, animate=False)
        self.assertTrue(result.passed, msg=result.message)

    def test_binary_search_passes(self):
        challenge = get_challenge("search_02")
        result = challenge.run(solve_fn=_search_02, n=64, seed=3, animate=False)
        self.assertTrue(result.passed, msg=result.message)
        self.assertEqual(result.actual_complexity.value, "O(log n)")

    def test_linear_search_fails_binary_challenge(self):
        challenge = get_challenge("search_02")
        # At n=128, O(n) is 4*128+10=522, O(log n) is 3*7+10=31. The
        # linear scan will run out of budget.
        result = challenge.run(solve_fn=_search_02_bad, n=128, seed=3, animate=False)
        self.assertFalse(result.passed)
        self.assertFalse(result.within_threshold)


class DynamicProgrammingTests(unittest.TestCase):
    def setUp(self):
        reset_counter()

    def tearDown(self):
        reset_counter()

    def test_fibonacci_passes(self):
        challenge = get_challenge("dp_01")
        result = challenge.run(solve_fn=_dp_01, n=20, seed=1, animate=False)
        self.assertTrue(result.passed, msg=result.message)


class RegistryTests(unittest.TestCase):
    def test_list_challenges_non_empty(self):
        ids = list_challenges()
        self.assertGreater(len(ids), 0)
        # Every id should resolve.
        for cid in ids:
            self.assertIsNotNone(get_challenge(cid), msg=f"missing: {cid}")

    def test_intro_01_present(self):
        self.assertIn("intro_01", list_challenges())


class MaxNCapTests(unittest.TestCase):
    """1D challenges accept up to 50; 2D grid challenges (BFS, DFS)
    cap at 35 because a 50x50 grid is too dense to be useful even at
    the smallest zoom."""

    def test_1d_challenges_default_to_50(self):
        from code_n.challenge import Challenge
        for cid in ("intro_01", "sort_01", "search_01", "search_02",
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
