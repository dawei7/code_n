"""Regression tests for execution_trace._serialize_locals.

The BFS Grid challenge surfaced a bug where ``_serialize_locals`` stored
the player's mutable containers (list / set / dict) by reference. The
BFS mutates ``frontier`` and ``visited`` in place across all its
iterations, so by the time the renderer read the stored locals, every
captured frame showed the *final* state of the BFS - the variable
panel at step 0 would display the post-goal frontier and the full
visited set instead of the start state. The fix snapshots the
containers so each frame freezes the values at the moment of capture.
"""
from __future__ import annotations

import os
import tempfile
import textwrap
import unittest

from code_n.counter import OperationCounter
from code_n.execution_trace import run_with_trace


def _run_player(source: str, inputs: dict) -> tuple[list, OperationCounter]:
    """Write the player's source to a temp file, run it, return (trace.frames, counter)."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".py", delete=False, encoding="utf-8"
    ) as handle:
        handle.write(textwrap.dedent(source))
        path = handle.name
    try:
        counter = OperationCounter()
        # Use the same global counter so TrackedGrid reads are counted.
        import code_n.counter as ct
        ct._counter = counter
        # Load the module.
        import importlib.util
        spec = importlib.util.spec_from_file_location("player_bfs_under_test", path)
        module = importlib.util.module_from_spec(spec)
        import sys
        sys.modules["player_bfs_under_test"] = module
        spec.loader.exec_module(module)
        # Run with trace.
        _, trace = run_with_trace(module.solve, inputs, counter)
        return trace.frames, counter
    finally:
        os.unlink(path)


class TraceSnapshotTests(unittest.TestCase):
    def test_bfs_frontier_and_visited_are_frozen_at_each_line(self):
        """The earliest line event with both frontier and visited
        defined must show the START state, not the END state.

        The BFS Grid player uses a plain ``list`` for ``frontier``
        and a plain ``set`` for ``visited`` (TrackedQueue/Set are
        gone from the engine - see the search_03 source comment).
        Without the snapshot fix, every captured line event shared
        the live references and showed the BFS's final frontier
        and the full visited set.
        """
        # Use a tiny grid so the BFS is short and the test is
        # deterministic. start=(0,0), goal=(2,2), 3x3 grid, all open.
        from code_n.tracked import TrackedGrid
        grid = TrackedGrid(3, 3)
        for y in range(3):
            for x in range(3):
                grid._data[y][x] = 0

        source = """
            def solve(grid, start, goal, size):
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
                            if grid._data[nr][nc] == 0:
                                frontier.append((nr, nc, distance + 1))
                return -1
        """
        frames, counter = _run_player(
            source,
            {"grid": grid, "start": (0, 0), "goal": (2, 2), "size": 3},
        )
        # Find the earliest line event that has BOTH frontier
        # and visited defined. That's the frame just after
        # ``visited = set()`` runs (line 3 of the BFS). At that
        # point, the BFS has done: frontier = [], append start,
        # visited = set(). So frontier = [(0, 0, 0)] (1 cell)
        # and visited = set() (0 cells).
        start_frame = None
        for frame in frames:
            if (frame.locals.get("frontier") is not None
                    and frame.locals.get("visited") is not None):
                start_frame = frame
                break
        self.assertIsNotNone(
            start_frame,
            "Expected at least one line event with both frontier and visited defined",
        )
        # The BFS's start state: frontier has the start cell,
        # visited is empty. If the snapshot fix is broken, this
        # frame will show the END state (frontier empty after the
        # goal was popped, visited with 8 cells) - and the test
        # will fail on the size assertions below.
        self.assertEqual(
            len(start_frame.locals["frontier"]), 1,
            f"Start frame frontier should have 1 cell (the start), got "
            f"{len(start_frame.locals['frontier'])}: {start_frame.locals['frontier']}",
        )
        self.assertIn(
            (0, 0, 0), start_frame.locals["frontier"],
            f"Start frame frontier should contain (0, 0, 0), got "
            f"{start_frame.locals['frontier']}",
        )
        self.assertEqual(
            len(start_frame.locals["visited"]), 0,
            f"Start frame visited should be empty, got "
            f"{len(start_frame.locals['visited'])}: {start_frame.locals['visited']}",
        )
        # And the BUG check: the locals in the LAST frame must be
        # the END state of the BFS (visited = 9 cells for the
        # open 3x3 grid; the goal is added to visited just before
        # the function returns). If the snapshot fix was broken,
        # the locals at the start_frame above would have looked
        # like the end state too.
        last_frame = frames[-1]
        self.assertEqual(
            len(last_frame.locals.get("visited", set())), 9,
            f"End frame visited should have 9 cells on an open 3x3 grid, got "
            f"{len(last_frame.locals.get('visited', set()))}",
        )

    def test_serialize_locals_copies_lists(self):
        """Direct unit test: a list captured by _serialize_locals must
        be a NEW list, not a reference to the player's list.
        """
        from code_n.execution_trace import _serialize_locals
        original = [1, 2, 3]
        snapshot = _serialize_locals({"x": original})
        self.assertEqual(snapshot["x"], [1, 2, 3])
        # Mutate the original AFTER serialization. The snapshot
        # must still see the old values.
        original.append(99)
        self.assertEqual(snapshot["x"], [1, 2, 3])
        # And the snapshot must be a different object, so the
        # renderer could sort / consume it without touching the
        # player's list.
        self.assertIsNot(snapshot["x"], original)

    def test_serialize_locals_copies_sets(self):
        from code_n.execution_trace import _serialize_locals
        original = {1, 2, 3}
        snapshot = _serialize_locals({"v": original})
        self.assertEqual(snapshot["v"], {1, 2, 3})
        original.add(99)
        self.assertEqual(snapshot["v"], {1, 2, 3})
        self.assertIsNot(snapshot["v"], original)

    def test_serialize_locals_copies_dicts(self):
        from code_n.execution_trace import _serialize_locals
        original = {"a": 1}
        snapshot = _serialize_locals({"d": original})
        self.assertEqual(snapshot["d"], {"a": 1})
        original["b"] = 2
        self.assertEqual(snapshot["d"], {"a": 1})
        self.assertIsNot(snapshot["d"], original)

    def test_serialize_locals_leaves_immutable_alone(self):
        """Scalars, strings, and tuples don't need a copy - they
        can't be mutated. Verify _serialize_locals doesn't make
        a wasteful copy of them.
        """
        from code_n.execution_trace import _serialize_locals
        a_tuple = (1, 2, 3)
        a_string = "hello"
        snapshot = _serialize_locals(
            {"t": a_tuple, "s": a_string, "n": 42}
        )
        self.assertIs(snapshot["t"], a_tuple)
        self.assertIs(snapshot["s"], a_string)
        self.assertEqual(snapshot["n"], 42)


if __name__ == "__main__":
    unittest.main()
