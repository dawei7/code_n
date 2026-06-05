"""Tests for the touched-cell extraction logic in the pygame renderer.

`_touched_from_call` and `_infer_call_kind` are the pure-Python heart of
the touched-cell coloring: given a trace frame (op_index + source line +
locals snapshot), they figure out which cells the player just looked at
so the variable strip can flash them in the op-type color.

The renderer itself is hard to test without a real pygame surface, but
these two helpers are pure-Python: they parse the player's source line
with stdlib ``ast`` and read locals from the trace frame. We exercise
them with a small temporary source file so the function can read the
actual line text (it depends on ``trace_frame.source_file``).
"""
from __future__ import annotations

import os
import tempfile
import unittest

from code_n.pygame_renderer import PygameRenderer
from code_n.execution_trace import TraceFrame


def _make_renderer() -> PygameRenderer:
    """Construct a PygameRenderer without opening a window. The
    constructor does not touch pygame; only play() does."""
    return PygameRenderer(width=1100, height=720, fps=60, speed="instant")


def _with_source(source: str, locals_dict: dict | None = None,
                 line_no: int = 1, breakpoint: bool = False) -> TraceFrame:
    """Write ``source`` to a temp file and return a TraceFrame pointing
    at ``line_no`` of it. The renderer's touched-cell helpers read the
    source line back off disk via ``trace_frame.source_file``.
    """
    fd, path = tempfile.mkstemp(suffix=".py")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(source)
        return TraceFrame(
            op_index=1,
            line_no=line_no,
            event="line",
            locals=locals_dict or {},
            breakpoint=breakpoint,
            source_file=path,
        )
    except Exception:
        os.unlink(path)
        raise


class _Op:
    """Minimal stand-in for an OpRecord so we can pass it to
    ``_touched_from_call``. Only ``op_type`` is read by the
    CALL-branch dispatcher, and we always exercise the CALL path
    directly in these tests, so an enum-like value is enough."""
    def __init__(self):
        from code_n.counter import OpType
        self.op_type = OpType.CALL


class InferCallKindTests(unittest.TestCase):
    """`_infer_call_kind` guesses READ / WRITE / COMPARE / SWAP from
    the player's source line when the engine only records a CALL
    (line-based tracing). The bug it had: an ``if``/``elif``/``while``
    header line fails to parse in exec mode (no body), so the helper
    fell through to ``READ`` and the touched cells were colored
    blue instead of red. The fix detects the keyword first.
    """

    def test_if_line_is_compare(self):
        self.assertEqual(PygameRenderer._infer_call_kind("if x > 0:"), "COMPARE")

    def test_elif_line_is_compare(self):
        self.assertEqual(PygameRenderer._infer_call_kind("elif x > 0:"), "COMPARE")

    def test_while_line_is_compare(self):
        self.assertEqual(PygameRenderer._infer_call_kind("while x > 0:"), "COMPARE")

    def test_assignment_is_write(self):
        self.assertEqual(PygameRenderer._infer_call_kind("x = 5"), "WRITE")

    def test_aug_assign_is_write(self):
        self.assertEqual(PygameRenderer._infer_call_kind("total += 1"), "WRITE")

    def test_bare_expression_is_read(self):
        self.assertEqual(PygameRenderer._infer_call_kind("len(arr)"), "READ")


class TouchedFromCallTests(unittest.TestCase):
    """`_touched_from_call` returns a dict of (var_name, key) -> op_type
    for every cell the current source line touches.
    """

    def setUp(self):
        self.r = _make_renderer()
        self.op = _Op()

    def test_scalar_name_is_touched_with_none_key(self):
        """``total = 5`` references the scalar ``total``; the touched
        cell key uses None as the index so the single-cell scalar
        visual can match it. Without this, the ``n: 30`` /
        ``total: 48`` / ``i: 2`` cells never flashed.
        """
        frame = _with_source(
            "total = 5\n",
            locals_dict={"total": 0},
            line_no=1,
        )
        touched = self.r._touched_from_call(self.op, frame)
        self.assertEqual(touched.get(("total", None)), "WRITE")

    def test_scalar_used_in_condition_is_touched(self):
        """``if ratings[i] > ratings[i+1]:`` references the scalar
        ``i`` as a bare Name (not inside a subscript). The new Name
        walker should mark it as touched with the COMPARE color.
        """
        frame = _with_source(
            "if ratings[i] > ratings[i + 1]:\n",
            locals_dict={
                "ratings": [4, 5, 6, 7],
                "i": 2,
            },
            line_no=1,
        )
        touched = self.r._touched_from_call(self.op, frame)
        self.assertEqual(touched.get(("i", None)), "COMPARE")
        self.assertEqual(touched.get(("ratings", 2)), "COMPARE")
        self.assertEqual(touched.get(("ratings", 3)), "COMPARE")

    def test_list_subscript_read_is_touched(self):
        """``value = data[i]`` touches ``data[i]`` and the scalar
        ``value`` and ``i``. The whole statement is an Assign, so
        the op_kind is WRITE (line-level classification) - the
        cells don't get a separate READ color for the RHS read;
        the same WRITE color is applied to every cell the line
        touched.
        """
        frame = _with_source(
            "value = data[i]\n",
            locals_dict={"data": [10, 20, 30, 40], "i": 1, "value": 0},
            line_no=1,
        )
        touched = self.r._touched_from_call(self.op, frame)
        self.assertEqual(touched.get(("data", 1)), "WRITE")
        # The LHS scalar is also marked, via the Store-context
        # Name walker.
        self.assertEqual(touched.get(("value", None)), "WRITE")
        self.assertEqual(touched.get(("i", None)), "WRITE")

    def test_list_subscript_write_is_touched(self):
        """``candies[i] = max(...)`` has a Subscript with Store
        context. The previous Load-only walker missed it, so
        ``candies[i]`` was never colored as WRITE.
        """
        frame = _with_source(
            "candies[i] = max(candies[i], candies[i + 1] + 1)\n",
            locals_dict={"candies": [1, 2, 3, 4], "i": 2},
            line_no=1,
        )
        touched = self.r._touched_from_call(self.op, frame)
        # LHS: Store-context subscript
        self.assertEqual(touched.get(("candies", 2)), "WRITE")
        # RHS reads of the same list at i and i+1
        self.assertEqual(touched.get(("candies", 2)), "WRITE")
        self.assertEqual(touched.get(("candies", 3)), "WRITE")

    def test_dict_subscript_read_is_touched_by_key(self):
        """``d["foo"]`` should mark the dict entry whose key is the
        string ``"foo"``, not an integer index. The dict visual
        matches by key, so the touched dict must use the same key.
        The statement is an Assign, so the line-level op_kind is
        WRITE.
        """
        frame = _with_source(
            "value = d['foo']\n",
            locals_dict={"d": {"foo": 1, "bar": 2}, "value": 0},
            line_no=1,
        )
        touched = self.r._touched_from_call(self.op, frame)
        self.assertEqual(touched.get(("d", "foo")), "WRITE")

    def test_dict_subscript_write_is_touched_by_key(self):
        """``d["foo"] = 5`` (Store context) is the dict-write case
        the old Load-only walker silently missed.
        """
        frame = _with_source(
            "d['foo'] = 5\n",
            locals_dict={"d": {"foo": 1, "bar": 2}},
            line_no=1,
        )
        touched = self.r._touched_from_call(self.op, frame)
        self.assertEqual(touched.get(("d", "foo")), "WRITE")

    def test_set_membership_test_marks_element(self):
        """``x in my_set`` reads the set and tests the element ``x``.
        The set is unordered, so the touched dict uses the element
        value (not an index) as the key. The renderer's set visual
        then matches by element value.
        """
        frame = _with_source(
            "if x in my_set:\n",
            locals_dict={"my_set": {1, 2, 3, 4}, "x": 3},
            line_no=1,
        )
        touched = self.r._touched_from_call(self.op, frame)
        self.assertEqual(touched.get(("my_set", 3)), "COMPARE")
        # Other set elements are NOT touched.
        self.assertNotIn(("my_set", 1), touched)
        self.assertNotIn(("my_set", 2), touched)
        self.assertNotIn(("my_set", 4), touched)

    def test_tuple_subscript_is_treated_like_list(self):
        """Tuples are immutable but the player can still subscript
        them. The touched dict uses the integer index, same as a
        list, so the list-like rendering of tuples still colors the
        right cell. The whole statement is an Assign so the
        op_kind is WRITE.
        """
        frame = _with_source(
            "value = t[2]\n",
            locals_dict={"t": (10, 20, 30, 40), "value": 0},
            line_no=1,
        )
        touched = self.r._touched_from_call(self.op, frame)
        self.assertEqual(touched.get(("t", 2)), "WRITE")

    def test_non_subscript_name_does_not_collide(self):
        """Two locals at different indices must not be confused: a
        line that says ``arr[3] = 5`` touches ``arr[3]`` only, not
        ``other[3]`` even though both are in scope. The new AST
        walker uses the actual variable name (not a wildcard), so
        this regression is locked in.
        """
        frame = _with_source(
            "arr[3] = 5\n",
            locals_dict={"arr": [0, 0, 0, 0, 0], "other": [0, 0, 0, 0, 0]},
            line_no=1,
        )
        touched = self.r._touched_from_call(self.op, frame)
        self.assertEqual(touched.get(("arr", 3)), "WRITE")
        self.assertNotIn(("other", 3), touched)


if __name__ == "__main__":
    unittest.main()
