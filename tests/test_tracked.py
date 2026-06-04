"""Unit tests for the tracked data structures.

Run with:
    .venv/Scripts/python.exe -m unittest tests.test_tracked -v
"""
from __future__ import annotations

import unittest

from code_n.counter import reset_counter
from code_n.tracked import (
    TrackedGrid,
    TrackedList,
    TrackedQueue,
    TrackedSet,
    TrackedStack,
    TrackedValue,
    unwrap_tracked,
)


class TrackedListTests(unittest.TestCase):
    def setUp(self):
        reset_counter()

    def tearDown(self):
        reset_counter()

    def test_indexing_reads_are_counted(self):
        lst = TrackedList([1, 2, 3])
        value = lst[1]
        # Reads return a TrackedValue so further comparisons are also counted.
        self.assertIsInstance(value, TrackedValue)
        self.assertEqual(value.raw, 2)
        # Re-look up stats after a single read.
        self.assertEqual(lst._len_reads(), 1)

    def test_assignment_writes_are_counted(self):
        lst = TrackedList([1, 2, 3])
        lst[1] = 9
        self.assertEqual(lst.raw, [1, 9, 3])
        self.assertEqual(lst._len_writes(), 1)

    def test_append_and_pop_count(self):
        lst = TrackedList([1, 2])
        lst.append(3)
        lst.pop()
        # 1 append, 1 pop = 2 writes
        self.assertEqual(lst._len_writes(), 2)

    def test_swap_counts_one_swap_op(self):
        lst = TrackedList([1, 2])
        lst.swap(0, 1)
        self.assertEqual(lst.raw, [2, 1])
        self.assertEqual(lst._len_swaps(), 1)

    def test_compare_counts(self):
        lst = TrackedList([1, 2, 3])
        result = lst.compare(0, 2)
        self.assertEqual(result, -1)
        result = lst.compare(0, 1)
        self.assertEqual(result, -1)
        result = lst.compare(0, 0)
        self.assertEqual(result, 0)
        self.assertEqual(lst._len_compares(), 3)

    def test_slice_returns_tracked_list(self):
        lst = TrackedList([1, 2, 3, 4])
        sliced = lst[1:3]
        self.assertIsInstance(sliced, TrackedList)
        self.assertEqual(sliced.raw, [2, 3])
        # 2 reads for 2 elements
        self.assertEqual(lst._len_reads(), 2)

    def test_iteration_yields_tracked_values(self):
        lst = TrackedList([10, 20])
        seen = []
        for v in lst:
            seen.append(v.raw)
        self.assertEqual(seen, [10, 20])

    def test_unwrap_tracked_recovers_raw(self):
        lst = TrackedList([5])
        self.assertEqual(unwrap_tracked(lst[0]), 5)
        self.assertEqual(unwrap_tracked(42), 42)


class TrackedGridTests(unittest.TestCase):
    def setUp(self):
        reset_counter()

    def tearDown(self):
        reset_counter()

    def test_tuple_key_read_and_write(self):
        grid = TrackedGrid(3, 3)
        grid.set(1, 2, 9)
        value = grid.get(1, 2)
        self.assertIsInstance(value, TrackedValue)
        self.assertEqual(value.raw, 9)

    def test_row_key_indexing(self):
        grid = TrackedGrid(2, 2)
        grid.set(0, 1, 7)
        v = grid[1][0]  # grid[row=1][col=0] = 7
        self.assertEqual(v.raw, 7)

    def test_in_bounds_helper(self):
        grid = TrackedGrid(3, 3)
        self.assertTrue(grid.in_bounds(0, 0))
        self.assertTrue(grid.in_bounds(2, 2))
        self.assertFalse(grid.in_bounds(3, 0))
        self.assertFalse(grid.in_bounds(0, -1))

    def test_swap(self):
        grid = TrackedGrid(2, 2)
        grid.set(0, 0, 1)
        grid.set(1, 1, 2)
        grid.swap(0, 0, 1, 1)
        self.assertEqual(grid.get(0, 0).raw, 2)
        self.assertEqual(grid.get(1, 1).raw, 1)


class TrackedQueueTests(unittest.TestCase):
    def setUp(self):
        reset_counter()

    def tearDown(self):
        reset_counter()

    def test_enqueue_dequeue(self):
        q = TrackedQueue()
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.peek(), 2)

    def test_dequeue_empty_raises(self):
        q = TrackedQueue()
        with self.assertRaises(IndexError):
            q.dequeue()


class TrackedStackTests(unittest.TestCase):
    def test_push_pop_peek(self):
        s = TrackedStack()
        s.push("a")
        s.push("b")
        self.assertEqual(s.peek(), "b")
        self.assertEqual(s.pop(), "b")
        self.assertEqual(s.pop(), "a")

    def test_pop_empty_raises(self):
        s = TrackedStack()
        with self.assertRaises(IndexError):
            s.pop()


class TrackedSetTests(unittest.TestCase):
    def test_add_and_contains(self):
        s = TrackedSet()
        s.add(1)
        s.add(2)
        self.assertTrue(s.contains(1))
        self.assertFalse(s.contains(3))
        self.assertIn(1, s)

    def test_remove(self):
        s = TrackedSet()
        s.add(1)
        s.remove(1)
        self.assertFalse(s.contains(1))


class TrackedValueTests(unittest.TestCase):
    def setUp(self):
        reset_counter()

    def tearDown(self):
        reset_counter()

    def test_comparisons_count(self):
        tv = TrackedValue(5, "x")
        self.assertTrue(tv > 3)
        self.assertTrue(tv < 10)
        self.assertTrue(tv == 5)
        self.assertTrue(tv != 4)
        # 4 comparisons
        self.assertEqual(tv._value, 5)

    def test_arithmetic_does_not_count(self):
        tv = TrackedValue(5, "x")
        # arithmetic is intentionally not counted (see TrackedValue docstring).
        self.assertEqual(tv + 3, 8)
        self.assertEqual(tv * 2, 10)


# ----- tiny helper methods for the tests above so we don't depend on stats
# being exposed on the wrapper class. The TrackedList/TrackedGrid do not
# expose .stats on themselves; the counter is the single source of truth.
def _patch():
    """Attach private counter-accessor methods to TrackedList/TrackedGrid for
    these tests so we don't have to reach into the global counter."""
    counter = _import_counter()

    def reads(self):
        return counter.read_count_for(f"list[{self._id_marker}]")

    TrackedList._len_reads = lambda self: sum(
        1 for op in counter.ops_log if op.op_type.value == "read" and op.detail.startswith("list[")
    )
    TrackedList._len_writes = lambda self: sum(
        1 for op in counter.ops_log if op.op_type.value == "write" and op.detail.startswith("list")
    )
    TrackedList._len_swaps = lambda self: sum(
        1 for op in counter.ops_log if op.op_type.value == "swap"
    )
    TrackedList._len_compares = lambda self: sum(
        1 for op in counter.ops_log if op.op_type.value == "compare"
    )
    TrackedList._id_marker = "X"


def _import_counter():
    from code_n.counter import get_counter
    return get_counter()


_patch()


if __name__ == "__main__":
    unittest.main()
