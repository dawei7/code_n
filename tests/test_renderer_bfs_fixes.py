"""Regression tests for the three BFS Grid panel bugs the user hit
after the variables-panel snapshot fix landed.

1. ``nr`` not substituted in the Validated line for nested subscripts.
   The BFS Grid line ``if grid[nr][nc] == 0:`` came out as
   ``if grid[nr][18] == 0 = False`` - the inner Name ``nr`` was
   inside the value of the outer Subscript, and the AST
   NodeTransformers only recursed into slices, never into values.
2. ``nc`` cell cut off at the bottom of the Variables panel.
   The break condition in ``_draw_variables_section`` checked
   the label's top but not the cell that follows it.
3. No coloring on the grid cell the BFS just read.
   ``_walk_source_line`` only saw the inner Subscript
   (``grid[nr]``) and added the *row* to touched_cells. The
   TrackedGrid was also missed by the ``isinstance(container,
   (list, tuple))`` check, so even the row key never landed.
"""
from __future__ import annotations

import os
import tempfile
import unittest

from code_n.pygame_renderer import PygameRenderer


def _make_renderer() -> PygameRenderer:
    return PygameRenderer(width=1100, height=720, fps=60, speed="instant")


def _with_source(source: str, locals_dict=None, line_no: int = 1):
    """Write ``source`` to a temp file and return a TraceFrame pointing
    at ``line_no`` of it (the renderer's source helpers read the
    source line back off disk via ``trace_frame.source_file``).
    """
    from code_n.execution_trace import TraceFrame
    fd, path = tempfile.mkstemp(suffix=".py")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(source)
        return TraceFrame(
            op_index=1,
            line_no=line_no,
            event="line",
            locals=locals_dict or {},
            breakpoint=False,
            source_file=path,
        )
    except Exception:
        os.unlink(path)
        raise


class ValidatedLineNestedSubscriptTests(unittest.TestCase):
    """The BFS line ``if grid[nr][nc] == 0:`` must produce
    ``Validated: if grid[5][18] == 0 = False``, not
    ``Validated: if grid[nr][18] == 0 = False``.

    The AST for ``grid[nr][nc]`` is
    ``Subscript(value=Subscript(value=Name('grid'), slice=Name('nr')),
                slice=Name('nc'))``. The previous NodeTransformers
    visited only the slice of each Subscript, so the inner Name
    ``nr`` was inside the value of the outer Subscript and never
    got visited. The fix recurses into the value when it's itself
    a Subscript.
    """

    def setUp(self):
        self.r = _make_renderer()

    def test_if_grid_read_substitutes_both_indices(self):
        # Grid has to be big enough for nr=5, nc=18.
        # 19 columns wide, 6 rows tall. cell [5][18] = 0.
        grid = [[0] * 19 for _ in range(6)]
        frame = _with_source(
            "if grid[nr][nc] == 0:\n",
            locals_dict={"grid": grid, "nr": 5, "nc": 18},
            line_no=1,
        )
        validated = self.r._format_validated_line(
            "if grid[nr][nc] == 0:", frame.locals,
        )
        self.assertIn("grid[5][18]", validated,
                      f"Both nr and nc should be substituted, got: {validated!r}")
        self.assertNotIn("grid[nr]", validated,
                         f"nr should be substituted, got: {validated!r}")
        # The cell at [5][18] is 0, so the condition 0 == 0 is True.
        self.assertIn("= True", validated,
                      f"Result should be True (0 == 0), got: {validated!r}")

    def test_assignment_lhs_substitutes_nested_subscript_indices(self):
        """``grid[nr][nc] = 5`` - the LHS of an assignment should
        also see both indices substituted, so the Validated line
        reads ``grid[5][18] = 5`` not ``grid[nr][18] = 5``.
        """
        # Need a 19-wide, 6-tall grid for the indices to be in range.
        grid = [[0] * 19 for _ in range(6)]
        frame = _with_source(
            "grid[nr][nc] = 5\n",
            locals_dict={"grid": grid, "nr": 5, "nc": 18},
            line_no=1,
        )
        validated = self.r._format_validated_line(
            "grid[nr][nc] = 5", frame.locals,
        )
        self.assertIn("grid[5][18]", validated,
                      f"LHS should substitute both indices, got: {validated!r}")
        self.assertNotIn("grid[nr]", validated,
                         f"nr should be substituted in LHS, got: {validated!r}")

    def test_assignment_rhs_substitutes_nested_subscript_indices(self):
        """``x = grid[nr][nc]`` - the RHS of an assignment should
        also see both indices substituted on the read side.
        """
        frame = _with_source(
            "x = grid[nr][nc]\n",
            locals_dict={"grid": [[7]], "nr": 0, "nc": 0, "x": 0},
            line_no=1,
        )
        validated = self.r._format_validated_line(
            "x = grid[nr][nc]", frame.locals,
        )
        self.assertIn("grid[0][0]", validated,
                      f"RHS should substitute both indices, got: {validated!r}")
        self.assertIn("= 7", validated,
                      f"Result should be the grid value 7, got: {validated!r}")

    def test_single_subscript_still_works(self):
        """The fix for nested subscripts must not break the
        existing single-subscript path: ``candies[i]`` should
        still come out as ``candies[16]`` not ``[...][16]``.
        """
        frame = _with_source(
            "x = candies[i]\n",
            locals_dict={"candies": [1, 2, 3, 4], "i": 2, "x": 0},
            line_no=1,
        )
        validated = self.r._format_validated_line(
            "x = candies[i]", frame.locals,
        )
        self.assertIn("candies[2]", validated,
                      f"Single subscript should still work, got: {validated!r}")
        # The variable name should stay as a Name, not be
        # replaced by the list itself.
        self.assertNotIn("[1, 2, 3, 4][2]", validated,
                         f"List value should NOT be substituted, got: {validated!r}")


class WalkSourceLineNestedSubscriptTests(unittest.TestCase):
    """``_walk_source_line`` must add the (row, col) tuple to
    touched_cells for nested subscripts like ``grid[nr][nc]``,
    and must handle TrackedGrid (not just plain list-of-lists).
    """

    def setUp(self):
        self.r = _make_renderer()

    def test_nested_grid_subscript_adds_row_col_tuple(self):
        """The BFS's grid read ``if grid[nr][nc] == 0:`` with
        nr=5, nc=18 must produce touched[('grid', (5, 18))] so
        the renderer's grid cell flashes.
        """
        # A 6x19 plain list-of-lists grid. The walker should
        # add ('grid', (5, 18)) to the touched dict.
        grid = [[0] * 19 for _ in range(6)]
        frame = _with_source(
            "if grid[nr][nc] == 0:\n",
            locals_dict={"grid": grid, "nr": 5, "nc": 18},
            line_no=1,
        )
        touched = self.r._walk_source_line(frame, "COMPARE")
        self.assertIn(
            ("grid", (5, 18)), touched,
            f"Expected ('grid', (5, 18)) in touched, got keys: {list(touched.keys())}",
        )

    def test_nested_grid_subscript_with_tracked_grid(self):
        """Same as above, but the grid is a TrackedGrid. The
        walker must unwrap it (or otherwise recognize the 2D
        access) and add the (row, col) tuple.
        """
        from code_n.tracked import TrackedGrid
        # TrackedGrid(width, height) - width=19 columns,
        # height=6 rows, so grid[5][18] is valid.
        grid = TrackedGrid(19, 6)
        for y in range(6):
            for x in range(19):
                grid._data[y][x] = 0
        frame = _with_source(
            "if grid[nr][nc] == 0:\n",
            locals_dict={"grid": grid, "nr": 5, "nc": 18},
            line_no=1,
        )
        touched = self.r._walk_source_line(frame, "COMPARE")
        self.assertIn(
            ("grid", (5, 18)), touched,
            f"TrackedGrid nested access should produce ('grid', (5, 18)), "
            f"got keys: {list(touched.keys())}",
        )

    def test_single_subscript_on_list_still_works(self):
        """``data[i]`` should still produce ('data', 5) - the
        fix for nested subscripts mustn't break the 1D case.
        """
        frame = _with_source(
            "x = data[i]\n",
            locals_dict={"data": [10, 20, 30, 40, 50, 60], "i": 5, "x": 0},
            line_no=1,
        )
        touched = self.r._walk_source_line(frame, "READ")
        self.assertIn(
            ("data", 5), touched,
            f"1D subscript should still work, got: {list(touched.keys())}",
        )


if __name__ == "__main__":
    unittest.main()
