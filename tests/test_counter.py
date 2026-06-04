"""Unit tests for the operation counter and complexity classification.

Run with:
    .venv/Scripts/python.exe -m unittest tests.test_counter -v
"""
from __future__ import annotations

import unittest

from code_n.counter import (
    ComplexityClass,
    OperationCounter,
    OperationLimitExceeded,
    OpStats,
    get_counter,
    limit_for,
    reset_counter,
)


class CounterRecordTests(unittest.TestCase):
    def setUp(self):
        reset_counter()

    def tearDown(self):
        reset_counter()

    def test_each_record_increments_total(self):
        counter = OperationCounter()
        counter.compare("a < b")
        counter.read("list[0]")
        counter.write("list[1] = 2")
        counter.swap("list[0]<->list[1]")
        counter.call("len(data)")

        stats = counter.stats
        self.assertEqual(stats.comparisons, 1)
        self.assertEqual(stats.reads, 1)
        self.assertEqual(stats.writes, 1)
        self.assertEqual(stats.swaps, 1)
        self.assertEqual(stats.calls, 1)
        self.assertEqual(stats.total, 5)

    def test_disabled_counter_does_not_record(self):
        counter = OperationCounter()
        counter.enabled = False
        counter.compare("a < b")
        counter.read("list[0]")
        self.assertEqual(counter.total_ops, 0)

    def test_snapshots_record_current_length(self):
        counter = OperationCounter()
        counter.read("a")
        counter.snapshot()
        counter.read("b")
        counter.snapshot()
        self.assertEqual(counter._snapshots, [1, 2])

    def test_ops_log_returns_copy(self):
        counter = OperationCounter()
        counter.read("a")
        log = counter.ops_log
        log.clear()
        self.assertEqual(len(counter.ops_log), 1)

    def test_stats_is_cached_until_next_record(self):
        counter = OperationCounter()
        counter.read("a")
        counter.read("b")
        stats = counter.stats
        # Caching means the next access returns the same object until a new
        # record invalidates the cache.
        self.assertIs(counter.stats, stats)
        counter.read("c")
        self.assertIsNot(counter.stats, stats)
        self.assertEqual(counter.stats.reads, 3)

    def test_reset_invalidates_stats_cache(self):
        counter = OperationCounter()
        counter.read("a")
        counter.stats  # populates cache
        counter.reset()
        self.assertEqual(counter.stats.total, 0)
        self.assertEqual(counter.stats.reads, 0)


class CounterLimitTests(unittest.TestCase):
    def setUp(self):
        reset_counter()

    def tearDown(self):
        reset_counter()

    def test_limit_exceeded_raises(self):
        counter = get_counter()
        counter.set_operation_limit(2, ComplexityClass.O_N)
        counter.read("a")
        counter.read("b")
        with self.assertRaises(OperationLimitExceeded) as ctx:
            counter.read("c")
        self.assertEqual(ctx.exception.limit, 2)
        self.assertEqual(ctx.exception.complexity, ComplexityClass.O_N)

    def test_clearing_limit_allows_more_ops(self):
        counter = OperationCounter()
        counter.set_operation_limit(0, ComplexityClass.O_1)
        with self.assertRaises(OperationLimitExceeded):
            counter.read("a")
        # Op above the limit is recorded *before* the exception, so 1 op
        # is already counted.
        self.assertEqual(counter.total_ops, 1)
        counter.clear_operation_limit()
        counter.read("a")
        counter.read("b")
        counter.read("c")
        self.assertEqual(counter.total_ops, 4)


class CounterClassifyTests(unittest.TestCase):
    def setUp(self):
        reset_counter()

    def tearDown(self):
        reset_counter()

    def test_zero_ops_is_o1(self):
        self.assertEqual(OperationCounter().classify(100), ComplexityClass.O_1)

    def test_n_lt_eq_one_is_unknown(self):
        counter = OperationCounter()
        counter.read("a")
        self.assertEqual(counter.classify(1), ComplexityClass.UNKNOWN)

    def test_few_ops_classify_o1(self):
        counter = OperationCounter()
        for _ in range(3):
            counter.read("a")
        self.assertEqual(counter.classify(100), ComplexityClass.O_1)

    def test_classify_log_n(self):
        counter = OperationCounter()
        for _ in range(8):
            counter.read("a")
        # 8 ops at n=100 is well within 3*log2(100)+10 ~= 30
        self.assertEqual(counter.classify(100), ComplexityClass.O_LOG_N)

    def test_classify_n(self):
        counter = OperationCounter()
        for _ in range(200):
            counter.read("a")
        # 200 / 100 = 2.0 <= 4.0
        self.assertEqual(counter.classify(100), ComplexityClass.O_N)

    def test_classify_n_log_n(self):
        counter = OperationCounter()
        for _ in range(500):
            counter.read("a")
        # 500 > 4*100=400, < 8*10000=800000, but ratio 5.0 > 4.0;
        # only qualifies as n_log_n if 500 <= 6*n*log2(n) ~= 6*100*6.64 ~= 3987
        self.assertEqual(counter.classify(100), ComplexityClass.O_N_LOG_N)

    def test_classify_n2(self):
        counter = OperationCounter()
        for _ in range(50_000):
            counter.read("a")
        # 50_000 > 4*100=400, but < 8*10000=80000, so n^2
        self.assertEqual(counter.classify(100), ComplexityClass.O_N2)


class LimitForTests(unittest.TestCase):
    def test_o1_is_constant(self):
        self.assertEqual(limit_for(50, ComplexityClass.O_1), 10)
        self.assertEqual(limit_for(10_000, ComplexityClass.O_1), 10)

    def test_o_n_grows_linearly(self):
        self.assertEqual(limit_for(100, ComplexityClass.O_N), 410)
        self.assertEqual(limit_for(50, ComplexityClass.O_N), 210)

    def test_o_n2_grows_quadratically(self):
        self.assertEqual(limit_for(50, ComplexityClass.O_N2), 50 * 50 * 8 + 10)

    def test_unknown_is_huge(self):
        self.assertEqual(limit_for(10, ComplexityClass.UNKNOWN), 10**12)


class MaxNCapTests(unittest.TestCase):
    """The challenge runner caps --n at MAX_N so the visualizer always
    shows a grid that can be panned to fit on screen."""

    def test_max_n_is_50(self):
        from run_challenge import MAX_N
        self.assertEqual(MAX_N, 50)


if __name__ == "__main__":
    unittest.main()


class ThresholdTests(unittest.TestCase):
    """The threshold check is the load-bearing pass/fail test."""

    def setUp(self):
        reset_counter()

    def tearDown(self):
        reset_counter()

    def test_meets_threshold_within_budget(self):
        counter = OperationCounter()
        for _ in range(20):
            counter.read("a")
        # O_N at n=8 -> 8*4+10 = 42
        self.assertTrue(counter.meets_threshold(8, ComplexityClass.O_N))

    def test_meets_threshold_over_budget(self):
        counter = OperationCounter()
        for _ in range(50):
            counter.read("a")
        # O_N at n=8 -> 42
        self.assertFalse(counter.meets_threshold(8, ComplexityClass.O_N))

    def test_unknown_threshold_is_always_met(self):
        counter = OperationCounter()
        for _ in range(1_000_000):
            counter.read("a")
        self.assertTrue(counter.meets_threshold(100, ComplexityClass.UNKNOWN))


if __name__ == "__main__":
    unittest.main()
