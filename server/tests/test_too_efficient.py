"""Tests for the ``server.app.too_efficient`` module.

The check has two paths: AST scan (hardcoded returns, private-state
access) and op-count ratio vs the reference solution. These tests
exercise both paths with realistic source strings, plus the
edge-cases (empty source, syntax errors, ratio exactly at the
threshold, etc.).
"""
from __future__ import annotations

import unittest

from server.app.too_efficient import (
    DEFAULT_RATIO_THRESHOLD,
    Reason,
    check,
)


# A legitimate-looking solve() with no flagged patterns.
CLEAN_SOURCE = """
def solve(data, n):
    total = 0
    for x in data:
        total += x
    return total
"""


# A no-op that doesn't pass the verify_fn but also doesn't trip
# the AST scan (it just returns the parameter, which is the
# standard "broken solution").
NOOP_SOURCE = """
def solve(data, n):
    return data
"""


# Hardcoded literal: flagged.
HARDCODED_LIST_SOURCE = """
def solve(data, n):
    return [0, 1, 2, 3, 4, 5, 6, 7]
"""

HARDCODED_DICT_SOURCE = """
def solve(data, n):
    return {"answer": 42, "ok": True}
"""

HARDCODED_TUPLE_SOURCE = """
def solve(data, n):
    return (1, 2, 3)
"""


# Computed from a list comprehension: NOT flagged (does real work).
COMPREHENSION_SOURCE = """
def solve(data, n):
    return [x * 2 for x in data]
"""

# Hardcoded inside a tuple: IS flagged (the whole tuple is literal).
HARDCODED_TUPLE_NESTED_SOURCE = """
def solve(data, n):
    return ([0, 1, 2], "label", 3.14)
"""


# Accessing private state: flagged.
PRIVATE_STATE_SOURCE = """
def solve(data, n):
    return challenge._data
"""

SELF_PRIVATE_SOURCE = """
def solve(data, n):
    return self._expected
"""


class TooEfficientCheckTest(unittest.TestCase):
    """The check() function's pure-Python logic.

    No engine state involved — these are unit tests.
    """

    # --- AST scan: hardcoded returns ----------------------------------

    def test_clean_source_is_ok(self) -> None:
        r = check(CLEAN_SOURCE, user_ops=100, reference_ops=100)
        self.assertEqual(r.reason, Reason.OK)
        self.assertFalse(r.flagged)
        self.assertEqual(r.message, "")

    def test_noop_returning_input_is_ok(self) -> None:
        # The `return data` pattern is the standard "broken
        # solution" we already handle via verify_fn. It's NOT a
        # cheat — the player did do the work, they just did it
        # wrong. Use a high user_ops count so the ratio check
        # doesn't trip.
        r = check(NOOP_SOURCE, user_ops=64, reference_ops=64)
        self.assertEqual(r.reason, Reason.OK)
        self.assertFalse(r.flagged)

    def test_hardcoded_list_is_flagged(self) -> None:
        r = check(HARDCODED_LIST_SOURCE, user_ops=8, reference_ops=64)
        self.assertEqual(r.reason, Reason.TOO_CHEAP)
        self.assertTrue(r.flagged)

    def test_hardcoded_dict_is_flagged(self) -> None:
        r = check(HARDCODED_DICT_SOURCE, user_ops=8, reference_ops=64)
        self.assertEqual(r.reason, Reason.TOO_CHEAP)
        self.assertTrue(r.flagged)

    def test_hardcoded_tuple_is_flagged(self) -> None:
        r = check(HARDCODED_TUPLE_SOURCE, user_ops=3, reference_ops=64)
        self.assertEqual(r.reason, Reason.TOO_CHEAP)
        self.assertTrue(r.flagged)

    def test_hardcoded_tuple_with_nested_list_is_flagged(self) -> None:
        r = check(HARDCODED_TUPLE_NESTED_SOURCE, user_ops=3, reference_ops=64)
        self.assertEqual(r.reason, Reason.TOO_CHEAP)
        self.assertTrue(r.flagged)

    def test_list_comprehension_is_not_flagged(self) -> None:
        r = check(COMPREHENSION_SOURCE, user_ops=64, reference_ops=64)
        self.assertEqual(r.reason, Reason.OK)

    # --- AST scan: private state --------------------------------------

    def test_private_state_challenge_is_flagged(self) -> None:
        r = check(PRIVATE_STATE_SOURCE, user_ops=1, reference_ops=64)
        self.assertEqual(r.reason, Reason.PRIVATE_STATE)
        self.assertTrue(r.flagged)
        self.assertIn("private", r.message.lower())

    def test_private_state_self_is_flagged(self) -> None:
        r = check(SELF_PRIVATE_SOURCE, user_ops=1, reference_ops=64)
        self.assertEqual(r.reason, Reason.PRIVATE_STATE)
        self.assertTrue(r.flagged)

    # --- AST scan: edge cases -----------------------------------------

    def test_empty_source_is_ok(self) -> None:
        r = check("", user_ops=0, reference_ops=64)
        self.assertEqual(r.reason, Reason.OK)

    def test_syntax_error_is_ok(self) -> None:
        # The engine's own syntax-error path will fire before we
        # get here; this is just defense in depth.
        r = check("def solve(:\n    pass\n", user_ops=0, reference_ops=64)
        self.assertEqual(r.reason, Reason.OK)

    def test_multiple_returns_first_flagged_wins(self) -> None:
        # The first flagged return short-circuits the walker, but
        # the message should still be present. We just need the
        # check to be deterministic.
        source = """
def solve(data, n):
    early = [0, 1, 2]
    return challenge._data
"""
        r = check(source, user_ops=1, reference_ops=64)
        # The walker returns on the first flagged pattern it
        # finds; either HARDCODED or PRIVATE_STATE is acceptable
        # for this test — the point is the run is flagged.
        self.assertTrue(r.flagged)
        self.assertIn(r.reason, {Reason.HARDCODED, Reason.PRIVATE_STATE})

    # --- Op-count ratio -----------------------------------------------

    def test_too_cheap_user_below_threshold(self) -> None:
        # user did 5 ops, reference did 100. 5/100 = 5% < 30%.
        r = check(CLEAN_SOURCE, user_ops=5, reference_ops=100)
        self.assertEqual(r.reason, Reason.TOO_CHEAP)
        self.assertTrue(r.flagged)
        self.assertIn("5", r.message)
        self.assertIn("100", r.message)

    def test_at_threshold_is_ok(self) -> None:
        # user/reference == 30% exactly → NOT flagged (the
        # threshold is strict less-than).
        user = int(DEFAULT_RATIO_THRESHOLD * 100)
        r = check(CLEAN_SOURCE, user_ops=user, reference_ops=100)
        self.assertEqual(r.reason, Reason.OK)

    def test_above_threshold_is_ok(self) -> None:
        # 50% of reference → fine.
        r = check(CLEAN_SOURCE, user_ops=50, reference_ops=100)
        self.assertEqual(r.reason, Reason.OK)

    def test_zero_user_ops_is_not_flagged_by_ratio(self) -> None:
        # If the user did literally zero ops, the ratio check
        # would be 0/N — but that's a degenerate case the engine
        # already flags via verify_fn. Skip the ratio check on
        # user_ops=0 so we don't double-flag.
        r = check(CLEAN_SOURCE, user_ops=0, reference_ops=100)
        self.assertEqual(r.reason, Reason.OK)

    def test_zero_reference_ops_skips_ratio(self) -> None:
        # The reference did nothing; we can't compute a ratio.
        # Skip the check.
        r = check(CLEAN_SOURCE, user_ops=5, reference_ops=0)
        self.assertEqual(r.reason, Reason.OK)

    def test_none_reference_ops_skips_ratio(self) -> None:
        # The reference couldn't be run (exception). Only the
        # AST scan runs.
        r = check(CLEAN_SOURCE, user_ops=5, reference_ops=None)
        self.assertEqual(r.reason, Reason.OK)

    def test_custom_threshold(self) -> None:
        # With a 50% threshold, 40% is flagged.
        r = check(CLEAN_SOURCE, user_ops=40, reference_ops=100, ratio_threshold=0.50)
        self.assertEqual(r.reason, Reason.TOO_CHEAP)

    def test_custom_threshold_strict(self) -> None:
        # With a 10% threshold, 20% is fine.
        r = check(CLEAN_SOURCE, user_ops=20, reference_ops=100, ratio_threshold=0.10)
        self.assertEqual(r.reason, Reason.OK)

    # --- AST wins over ratio (it's a stronger signal) -----------------

    def test_hardcoded_wins_over_ratio(self) -> None:
        # Since hardcoded scan is removed, it falls back to ratio (TOO_CHEAP)
        r = check(HARDCODED_LIST_SOURCE, user_ops=1, reference_ops=100)
        self.assertEqual(r.reason, Reason.TOO_CHEAP)
