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

    def test_tracked_list_is_unwrapped_to_plain_list(self):
        """The engine passes TrackedList (not a real list) as the
        challenge input. The renderer's variables panel unwraps
        it to a plain list for drawing, so the touched-cells dict
        has to use the same key shape - integer index into a
        list. Without the TrackedList unwrap, the Subscript
        walker's ``isinstance(container, (list, tuple))`` check
        was False, so ``data[i]`` produced no touched cell and
        nothing ever colored. The user noticed this with bubble
        sort (``if data[i] > data[i + 1]:``) where every data
        cell stayed gray no matter the op.
        """
        from code_n.tracked import TrackedList
        tracked = TrackedList([10, 20, 30, 40, 50])
        frame = _with_source(
            "if data[i] > data[i + 1]:\n",
            locals_dict={"data": tracked, "i": 2},
            line_no=1,
        )
        touched = self.r._touched_from_call(self.op, frame)
        # The unwrap happens inside the function, so the
        # touched_cells dict should now contain the integer-index
        # entries the renderer's _draw_variable_strip looks up.
        self.assertEqual(touched.get(("data", 2)), "COMPARE")
        self.assertEqual(touched.get(("data", 3)), "COMPARE")
        # The Name walker should still pick up the scalar ``i``.
        self.assertEqual(touched.get(("i", None)), "COMPARE")
        # The TrackedList itself must not appear as a scalar
        # touched entry (that was the buggy behavior: ``data``
        # got a ``(data, None)`` entry the renderer can't color).
        self.assertNotIn(("data", None), touched)


class ExtractTouchedCellsTests(unittest.TestCase):
    """``_extract_touched_cells`` is the dispatcher: it routes
    CALL ops to ``_touched_from_call`` (line-based tracing) and
    handles READ / WRITE / COMPARE / SWAP ops itself via the
    engine's hardcoded ``list[i] = v`` detail format.

    The non-CALL path had the same TrackedList bug as the
    SUBSCRIPT walker: the wildcard loop checked
    ``isinstance(value, (list, tuple))`` and TrackedList is
    neither, so for challenges whose only list is the engine's
    TrackedList input (bubble sort, selection sort, ...) every
    op produced no touched cells. Bubble sort's
    ``if data[i] > data[i+1]:`` records READ + READ + COMPARE
    ops, all of which go through this path.
    """

    def setUp(self):
        self.r = _make_renderer()

    def test_read_op_with_tracked_list(self):
        """A READ op with detail ``list[5]`` should mark cell 5
        of any list-like local, including TrackedList."""
        from code_n.counter import OpRecord, OpType
        from code_n.tracked import TrackedList
        op = OpRecord(op_type=OpType.READ, detail="list[5]")
        frame = _with_source(
            "",
            locals_dict={"data": TrackedList([10, 20, 30, 40, 50, 60, 70, 80])},
            line_no=1,
        )
        touched = self.r._extract_touched_cells(op, frame)
        self.assertEqual(touched.get(("data", 5)), "READ")

    def test_compare_op_with_tracked_list_two_indices(self):
        """A COMPARE op detail like ``list[5]=X vs list[6]=Y``
        captures both indices; both cells should be touched."""
        from code_n.counter import OpRecord, OpType
        from code_n.tracked import TrackedList
        op = OpRecord(op_type=OpType.COMPARE, detail="list[5]=X vs list[6]=Y")
        frame = _with_source(
            "",
            locals_dict={"data": TrackedList([10, 20, 30, 40, 50, 60, 70, 80])},
            line_no=1,
        )
        touched = self.r._extract_touched_cells(op, frame)
        self.assertEqual(touched.get(("data", 5)), "COMPARE")
        self.assertEqual(touched.get(("data", 6)), "COMPARE")

    def test_write_op_with_tracked_list(self):
        """A WRITE op with detail ``list[5] = 99`` marks the cell."""
        from code_n.counter import OpRecord, OpType
        from code_n.tracked import TrackedList
        op = OpRecord(op_type=OpType.WRITE, detail="list[5] = 99")
        frame = _with_source(
            "",
            locals_dict={"data": TrackedList([10, 20, 30, 40, 50, 60, 70, 80])},
            line_no=1,
        )
        touched = self.r._extract_touched_cells(op, frame)
        self.assertEqual(touched.get(("data", 5)), "WRITE")

    def test_non_call_op_touches_scalars_from_source_line(self):
        """User directive: 'I don't see the single variables
        blinking if they are used'. The non-CALL path used to
        only regex the engine's op.detail (which is hardcoded
        ``list[i] = v`` for tracked ops and never names the
        scalars). The source line ``if data[i] > data[i + 1]:``
        also references the scalar ``i``, and that touch was
        silently dropped - the ``i: 2`` cell stayed gray.

        Fix: _extract_touched_cells also walks the source
        line (via _walk_source_line) for the non-CALL path so
        Name references to scalars in the line get marked
        just like they are for CALL ops. The line is read
        from trace_frame.source_file at trace_frame.line_no.
        """
        from code_n.counter import OpRecord, OpType
        from code_n.tracked import TrackedList
        op = OpRecord(op_type=OpType.READ, detail="list[5]")
        frame = _with_source(
            "if data[i] > data[i + 1]:\n",
            locals_dict={
                "data": TrackedList([10, 20, 30, 40, 50, 60, 70, 80]),
                "i": 5,
            },
            line_no=1,
        )
        touched = self.r._extract_touched_cells(op, frame)
        # The TrackedList element at index 5 (still wrapped to
        # plain list inside the walker).
        self.assertEqual(touched.get(("data", 5)), "READ")
        # The scalar ``i`` was referenced in the source line.
        self.assertEqual(touched.get(("i", None)), "READ")

    def test_non_call_op_touches_scalars_written_by_aug_assign(self):
        """Augmented assignment ``total += 1`` writes to a scalar
        on the LHS. The Name walker handles Store context, so
        ``total`` should be marked as touched even though the
        engine didn't record anything for the scalar (no
        tracked data structure involved)."""
        from code_n.counter import OpRecord, OpType
        op = OpRecord(op_type=OpType.WRITE, detail="list.append(1)")
        frame = _with_source(
            "total += 1\n",
            locals_dict={"total": 0},
            line_no=1,
        )
        touched = self.r._extract_touched_cells(op, frame)
        self.assertEqual(touched.get(("total", None)), "WRITE")


class SerializeLocalsTests(unittest.TestCase):
    """``_serialize_locals`` runs on every Python line event
    inside the player's ``solve`` function. It unwraps
    TrackedValue proxies so the renderer gets the underlying
    int/str/etc. (TrackedList is left alone so the variables
    panel can render it like a list.)

    The bug the user hit: the unwrap did ``value = value.value``,
    but TrackedValue's public attribute is ``.raw`` - ``.value``
    doesn't exist, and accessing it routes through
    ``TrackedValue.__getattr__`` to the wrapped object. For an
    underlying int that becomes ``getattr(int_instance, 'value')``
    which raises ``AttributeError: 'int' object has no attribute
    'value'``. The error fired on quicksort's first line
    (``pivot = items[high]``) because that line is the first one
    across the whole catalog to put a TrackedValue into the
    local variables. Earlier sorts only had TrackedList as a
    local, which is not a TrackedValue so the buggy branch was
    skipped.
    """

    def test_tracked_value_is_unwrapped_to_underlying_int(self):
        from code_n.execution_trace import _serialize_locals
        from code_n.tracked import TrackedValue
        tv = TrackedValue(42, "list[5]")
        result = _serialize_locals({"pivot": tv, "n": 20})
        self.assertEqual(result["pivot"], 42)
        self.assertNotIsInstance(result["pivot"], TrackedValue)
        self.assertEqual(result["n"], 20)

    def test_tracked_value_with_string_underlying(self):
        from code_n.execution_trace import _serialize_locals
        from code_n.tracked import TrackedValue
        tv = TrackedValue("hello", "x")
        result = _serialize_locals({"name": tv})
        self.assertEqual(result["name"], "hello")

    def test_tracked_list_is_left_alone(self):
        from code_n.execution_trace import _serialize_locals
        from code_n.tracked import TrackedList
        tl = TrackedList([1, 2, 3])
        result = _serialize_locals({"data": tl})
        # TrackedList is not a TrackedValue, so it should pass
        # through unchanged (the variables panel unwraps it
        # itself).
        self.assertIs(result["data"], tl)

    def test_mixed_locals_with_tracked_value_and_list(self):
        """Quicksort's partition_3way has pivot (TrackedValue)
        and items (TrackedList) and several int locals. All of
        them must serialize without raising."""
        from code_n.execution_trace import _serialize_locals
        from code_n.tracked import TrackedList, TrackedValue
        result = _serialize_locals({
            "items": TrackedList([3, 1, 4, 1, 5, 9, 2, 6]),
            "pivot": TrackedValue(9, "list[5]"),
            "low": 0,
            "high": 7,
            "lt": 0,
            "i": 0,
            "gt": 7,
        })
        self.assertEqual(result["pivot"], 9)
        self.assertEqual(result["high"], 7)
        # The TrackedList reference is preserved (not copied).
        self.assertIsInstance(result["items"], TrackedList)


class ClassifyVariableTests(unittest.TestCase):
    """``_classify_variable`` is the dispatcher that picks a
    rendering strategy for each local. BFS exposes the full
    spread of types: TrackedGrid, TrackedQueue, plain scalars,
    and a set of (row, col) tuples for ``visited``. Each one
    needs a different visual (2D grid, horizontal strip, 2D
    overlay, single cell) and the classification has to pick
    the right one."""

    def setUp(self):
        from code_n.pygame_renderer import PygameRenderer
        self.r = PygameRenderer(speed="instant")

    def test_tracked_grid_classifies_as_grid(self):
        from code_n.tracked import TrackedGrid
        grid = TrackedGrid(5, 5, default=0)
        kind, payload, h = self.r._classify_variable(grid, content_w=200, cell_size=18)
        self.assertEqual(kind, "grid")
        # Payload is (raw_data, cell_size).
        raw, grid_cell = payload
        self.assertEqual(len(raw), 5)
        self.assertEqual(len(raw[0]), 5)
        # Cell size is bounded so a 35x35 grid still fits in the
        # panel width; max is 14 so values stay readable.
        self.assertLessEqual(grid_cell, 14)
        self.assertGreaterEqual(grid_cell, 8)
        # Height = rows * (cell + gap) + small bottom padding.
        self.assertGreater(h, 0)

    def test_tracked_queue_classifies_as_queue(self):
        from code_n.tracked import TrackedQueue
        q = TrackedQueue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        kind, payload, h = self.r._classify_variable(q, content_w=200, cell_size=18)
        self.assertEqual(kind, "queue")
        items, _ = payload
        self.assertEqual(items, [1, 2, 3])
        self.assertGreater(h, 0)

    def test_tracked_stack_classifies_as_stack(self):
        from code_n.tracked import TrackedStack
        s = TrackedStack()
        s.push(10)
        s.push(20)
        kind, payload, h = self.r._classify_variable(s, content_w=200, cell_size=18)
        self.assertEqual(kind, "stack")
        items, _ = payload
        self.assertEqual(items, [10, 20])

    def test_set_of_2tuples_classifies_as_set2d(self):
        """BFS's ``visited`` is a set of (row, col) tuples; the
        renderer should detect this and treat it as a 2D overlay
        rather than dumping the tuples as one giant line of text.
        """
        visited = {(0, 0), (0, 1), (1, 0), (1, 1)}
        kind, payload, h = self.r._classify_variable(visited, content_w=200, cell_size=18)
        self.assertEqual(kind, "set2d")
        value_set, max_r, max_c, grid_cell = payload
        self.assertEqual(value_set, visited)
        # The grid extent is inferred from the data (max + 1).
        self.assertEqual(max_r, 2)
        self.assertEqual(max_c, 2)
        self.assertLessEqual(grid_cell, 14)

    def test_list_of_2tuples_also_classifies_as_set2d(self):
        """``frontier`` in BFS is a TrackedQueue of (row, col, dist)
        tuples, but plain lists of (row, col) pairs should also
        be detected as a 2D overlay."""
        frontier = [(0, 0), (0, 1), (1, 0), (2, 3)]
        kind, payload, h = self.r._classify_variable(frontier, content_w=200, cell_size=18)
        self.assertEqual(kind, "set2d")

    def test_list_classifies_as_list(self):
        kind, payload, h = self.r._classify_variable([1, 2, 3], content_w=200, cell_size=18)
        self.assertEqual(kind, "list")

    def test_dict_classifies_as_dict(self):
        kind, payload, h = self.r._classify_variable({"a": 1, "b": 2}, content_w=200, cell_size=18)
        self.assertEqual(kind, "dict")

    def test_set_of_non_tuples_classifies_as_set(self):
        """A set of plain ints (or strings) is a regular set, not
        a 2D overlay. The 2D detection requires 2-tuple of ints."""
        kind, payload, h = self.r._classify_variable({1, 2, 3}, content_w=200, cell_size=18)
        self.assertEqual(kind, "set")

    def test_scalar_classifies_as_scalar(self):
        kind, payload, h = self.r._classify_variable(42, content_w=200, cell_size=18)
        self.assertEqual(kind, "scalar")
        self.assertEqual(payload, 42)

    def test_tracked_list_classifies_as_list(self):
        from code_n.tracked import TrackedList
        tl = TrackedList([1, 2, 3])
        kind, payload, h = self.r._classify_variable(tl, content_w=200, cell_size=18)
        self.assertEqual(kind, "list")

    def test_empty_collections_get_empty_kind(self):
        """An empty list / dict / set still occupies one cell-row
        of vertical space so the player sees the variable exists.
        """
        for empty in ([], {}, set()):
            kind, payload, h = self.r._classify_variable(empty, content_w=200, cell_size=18)
            self.assertEqual(kind, "empty")


if __name__ == "__main__":
    unittest.main()
