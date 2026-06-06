"""Tests for the algorithm-fingerprint system.

The fingerprint lets a challenge distinguish between algorithms of
the same O-class. It is *advisory*: the player's solution can still
pass `passed = correct and within_threshold` even if the fingerprint
fires, but the result carries a teaching hint about which algorithm
they actually used.

These tests verify:
- `check_fingerprint` correctly counts substring matches
- BFS (queue-based) matches the BFS fingerprint
- BFS using a raw Python list (correct + within budget) is flagged
  by the fingerprint so the player sees the algorithm hint
- DFS (stack-based) matches the DFS fingerprint
- Each op is counted only against the first matching constraint
  (first-match-wins)

Note: We do NOT test sort fingerprints here. The substring approach
cannot reliably distinguish O(n^2) sort algorithms because:
  * Tuple-swap bubble sort records writes, not swaps.
  * Selection sort and insertion sort both have 0 swaps.
So the complexity check (O(n^2) budget) is the only reliable gate
for sorts; the fingerprint is left to the BFS/DFS case where
different data structures leave a clear signature.
"""
from __future__ import annotations

import unittest

from challenges.registry import get_challenge
from code_n.challenge import (
    OP_AT_LEAST,
    OP_AT_MOST,
    OP_EXACTLY,
    OperationConstraint,
    check_fingerprint,
)
from code_n.counter import OpRecord, OpType, reset_counter
from code_n.tracked import TrackedList


# ---- reference solutions for the fingerprint-tagged challenges -----


def _bfs_with_deque(grid, start, goal, size):
    """A BFS that uses collections.deque (the canonical way
    now that TrackedQueue is gone). Has the right complexity."""
    from collections import deque
    frontier = deque()
    frontier.append((start[0], start[1], 0))
    visited = set()
    while frontier:
        row, col, distance = frontier.popleft()
        if (row, col) in visited:
            continue
        visited.add((row, col))
        if (row, col) == goal:
            return distance
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < size and 0 <= nc < size and (nr, nc) not in visited:
                if grid[nr][nc] == 0:
                    frontier.append((nr, nc, distance + 1))
    return -1


def _bfs_with_raw_list(grid, start, goal, size):
    """A correct BFS that uses a regular Python list. Has the right
    complexity but its op log has no queue.enqueue, so the
    fingerprint should fire (advisory) while the result still
    passes."""
    frontier = []
    frontier.append((start[0], start[1], 0))
    visited = set()
    while frontier:
        row, col, distance = frontier.pop(0)
        if (row, col) in visited:
            continue
        visited.add((row, col))
        if (row, col) == goal:
            return distance
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < size and 0 <= nc < size and (nr, nc) not in visited:
                if grid[nr][nc] == 0:
                    frontier.append((nr, nc, distance + 1))
    return -1


def _dfs_with_list(grid, start, size):
    """A DFS that uses a plain list as a LIFO stack. TrackedStack
    is gone from the engine; a plain list works fine for the
    'last item popped first' semantics."""
    visited = set()
    stack = [start]
    while stack:
        row, col = stack.pop()
        if (row, col) in visited:
            continue
        visited.add((row, col))
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < size and 0 <= nc < size and (nr, nc) not in visited and grid[nr][nc] == 0:
                stack.append((nr, nc))
    return len(visited)


def _op(detail: str, op_type: OpType = OpType.READ) -> OpRecord:
    return OpRecord(op_type=op_type, detail=detail)


# ---- pure check_fingerprint tests --------------------------------


class CheckFingerprintTests(unittest.TestCase):
    def setUp(self):
        reset_counter()

    def tearDown(self):
        reset_counter()

    def test_empty_constraints_always_match(self):
        matched, reason = check_fingerprint([], [])
        self.assertTrue(matched)
        self.assertEqual(reason, "")

    def test_at_least_constraint(self):
        ops = [
            _op("queue.enqueue(1)"),
            _op("queue.enqueue(2)"),
            _op("list[0] = 5", OpType.WRITE),
        ]
        c = [OperationConstraint("queue.enqueue", OP_AT_LEAST, 2)]
        self.assertEqual(check_fingerprint(ops, c), (True, ""))

    def test_at_least_constraint_fails(self):
        ops = [_op("list[0] = 5", OpType.WRITE)]
        c = [OperationConstraint("queue.enqueue", OP_AT_LEAST, 1)]
        matched, reason = check_fingerprint(ops, c)
        self.assertFalse(matched)
        self.assertIn("expected at least 1 'queue.enqueue'", reason)
        self.assertIn("saw 0", reason)

    def test_at_most_constraint(self):
        ops = [_op("list[3]<->list[7]", OpType.SWAP)]
        c = [OperationConstraint("<->", OP_AT_MOST, 1)]
        self.assertEqual(check_fingerprint(ops, c), (True, ""))

    def test_at_most_constraint_fails(self):
        ops = [
            _op("list[3]<->list[7]", OpType.SWAP),
            _op("list[0]<->list[2]", OpType.SWAP),
        ]
        c = [OperationConstraint("<->", OP_AT_MOST, 1)]
        matched, reason = check_fingerprint(ops, c)
        self.assertFalse(matched)
        self.assertIn("expected at most 1 '<->'", reason)

    def test_exactly_constraint(self):
        ops = [_op("list[3]<->list[7]", OpType.SWAP)]
        c = [OperationConstraint("<->", OP_EXACTLY, 1)]
        self.assertEqual(check_fingerprint(ops, c), (True, ""))

    def test_exactly_constraint_fails(self):
        ops = [
            _op("list[3]<->list[7]", OpType.SWAP),
            _op("list[0]<->list[2]", OpType.SWAP),
        ]
        c = [OperationConstraint("<->", OP_EXACTLY, 1)]
        matched, reason = check_fingerprint(ops, c)
        self.assertFalse(matched)
        self.assertIn("expected exactly 1 '<->'", reason)

    def test_each_op_counted_only_against_first_match(self):
        """A swap op's detail 'list[3]<->list[7]' contains both '<->' and
        'list['. First-match-wins: the op contributes to whichever
        constraint comes first in the list, not to all of them."""
        ops = [_op("list[3]<->list[7]", OpType.SWAP)]
        c = [
            OperationConstraint("<->", OP_EXACTLY, 1),  # first match
            OperationConstraint("list[", OP_AT_LEAST, 1),  # would also match
        ]
        # The op is counted against <-> (1 == 1, ok). The "list["
        # constraint sees 0, fails at_least 1. So matched=False.
        matched, reason = check_fingerprint(ops, c)
        self.assertFalse(matched, msg=reason)
        self.assertIn("expected at least 1 'list['", reason)

    def test_first_match_wins_documented_order(self):
        """Same op, but constraints listed in a different order. Now
        'list[' comes first and gets the count; '<->' sees 0 and
        fails (we want exactly 1, but first-match gave it 0)."""
        ops = [_op("list[3]<->list[7]", OpType.SWAP)]
        c = [
            OperationConstraint("list[", OP_AT_LEAST, 1),  # first match
            OperationConstraint("<->", OP_EXACTLY, 1),  # would also match
        ]
        # The op is counted against 'list[' (first match); '<->' sees
        # 0 and fails. So matched=False, and the reason points at <->.
        matched, reason = check_fingerprint(ops, c)
        self.assertFalse(matched, msg=reason)
        self.assertIn("expected exactly 1 '<->'", reason)

    def test_op_with_no_detail_is_ignored(self):
        ops = [_op("", op_type=OpType.READ), _op("queue.enqueue(1)")]
        c = [OperationConstraint("queue.enqueue", OP_AT_LEAST, 1)]
        self.assertEqual(check_fingerprint(ops, c), (True, ""))

    def test_multiple_failures_are_concatenated(self):
        """When multiple constraints fail, every failure message is
        concatenated with '; ' so the player sees a complete picture
        in the algorithm-hint UI."""
        ops = [
            _op("queue.enqueue(1)"),
            _op("queue.dequeue()"),
        ]
        c = [
            OperationConstraint("queue.enqueue", OP_AT_LEAST, 5),
            OperationConstraint("queue.dequeue", OP_AT_LEAST, 5),
        ]
        matched, reason = check_fingerprint(ops, c)
        self.assertFalse(matched)
        self.assertIn("queue.enqueue", reason)
        self.assertIn("queue.dequeue", reason)
        # Two distinct failure messages separated by "; "
        self.assertIn("; ", reason)


# ---- end-to-end tests against real challenges -------------------


class BFSChallengeFingerprintTests(unittest.TestCase):
    """TrackedQueue is gone; the BFS challenge no longer has a
    queue-op fingerprint. The O(n^2) budget on grid reads /
    writes is the only gate."""

    def setUp(self):
        reset_counter()

    def tearDown(self):
        reset_counter()

    def test_challenge_has_no_queue_fingerprint(self):
        """The queue-op fingerprint is dropped (TrackedQueue
        no longer exists). Only the O(n^2) budget gates the
        challenge."""
        challenge = get_challenge("search_03")
        needles = {c.needle for c in challenge.info.expected_operations}
        self.assertNotIn("queue.enqueue", needles)
        self.assertNotIn("queue.dequeue", needles)

    def test_real_bfs_with_deque_passes(self):
        challenge = get_challenge("search_03")
        result = challenge.run(
            solve_fn=_bfs_with_deque, n=15, seed=1, animate=False,
        )
        self.assertTrue(result.passed, msg=result.message)

    def test_bfs_using_raw_list_still_passes(self):
        """A BFS with a regular Python list is correct + within
        threshold. The queue-op fingerprint is gone, so it just
        passes cleanly."""
        challenge = get_challenge("search_03")
        result = challenge.run(
            solve_fn=_bfs_with_raw_list, n=15, seed=1, animate=False,
        )
        self.assertTrue(result.passed, msg=result.message)


class DFSChallengeFingerprintTests(unittest.TestCase):
    """TrackedStack is gone; the DFS challenge no longer has a
    stack-op fingerprint. The O(n^2) budget on grid reads /
    writes is the only gate."""

    def setUp(self):
        reset_counter()

    def tearDown(self):
        reset_counter()

    def test_challenge_has_no_stack_fingerprint(self):
        challenge = get_challenge("search_04")
        needles = {c.needle for c in challenge.info.expected_operations}
        self.assertNotIn("queue.enqueue", needles)
        self.assertNotIn("queue.dequeue", needles)
        self.assertNotIn("stack.push", needles)

    def test_real_dfs_with_list_passes(self):
        challenge = get_challenge("search_04")
        result = challenge.run(
            solve_fn=_dfs_with_list, n=15, seed=1, animate=False,
        )
        self.assertTrue(result.passed, msg=result.message)


class FingerprintDocumentedLimitations(unittest.TestCase):
    """Known limitations of the substring-fingerprint approach.

    These tests document *why* we don't put a fingerprint on the sort
    challenges: the signal is too weak to reliably tell O(n^2) sorts
    apart. The complexity check is the real gate for those.
    """

    def test_bubble_sort_via_tuple_swap_records_writes_not_swaps(self):
        """The common Python idiom `data[i], data[j] = data[j], data[i]`
        on a TrackedList fires __setitem__ twice (writes), not the
        swap op. A fingerprint that looks for '<->' would miss
        bubble sort entirely."""
        reset_counter()
        data = TrackedList([3, 1, 2])
        # Tuple-swap idiom: 2 writes, 0 swaps.
        data[0], data[1] = data[1], data[0]
        from code_n.counter import get_counter
        counter = get_counter()
        self.assertGreaterEqual(counter.stats.writes, 2)
        self.assertEqual(counter.stats.swaps, 0)


if __name__ == "__main__":
    unittest.main()
