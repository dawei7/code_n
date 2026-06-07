"""Tests for the Variables panel refactor:
- default cell size 28px (zoom buttons, no wheel zoom)
- per-variable visibility toggle
- per-variable view mode (full / 10 / custom)
- vertical 1D rendering for list / set / tuple
- truncation sentinel for the "..." cell in 10 / custom modes
"""
from __future__ import annotations

import unittest

from code_n.pygame_renderer import (
    DEFAULT_CELL_SIZE,
    PygameRenderer,
    WHEEL_SCROLL_PIXELS,
    ZOOM_PRESETS,
    _TruncationSentinel,
)


def _make_renderer() -> PygameRenderer:
    return PygameRenderer(width=1100, height=720, fps=60, speed="instant")


class DefaultCellSizeTests(unittest.TestCase):
    """The default cell size is now 28px (was 22). The user
    wanted "fix everything on zoom 28px" - the +/- buttons in
    the Variables panel header step through ZOOM_PRESETS, not
    the wheel.
    """

    def test_default_is_28px(self):
        self.assertEqual(DEFAULT_CELL_SIZE, 28)

    def test_renderer_starts_at_28px(self):
        r = _make_renderer()
        self.assertEqual(r.cell_size, 28)
        self.assertEqual(r.zoom_label(), "28px")

    def test_zoom_presets_include_28(self):
        self.assertIn(28, ZOOM_PRESETS)


class ZoomStepTests(unittest.TestCase):
    """The +/- zoom buttons step through ZOOM_PRESETS, not
    arbitrary sizes. The wheel used to change cell size; it
    now only scrolls vertically.
    """

    def test_zoom_step_preserves_preset(self):
        r = _make_renderer()
        r.cell_size = 28
        r.zoom_step(+1)
        # 28 is in ZOOM_PRESETS - the next preset up.
        self.assertIn(r.cell_size, ZOOM_PRESETS)
        self.assertGreater(r.cell_size, 28)

    def test_zoom_step_down_preserves_preset(self):
        r = _make_renderer()
        r.cell_size = 28
        r.zoom_step(-1)
        self.assertIn(r.cell_size, ZOOM_PRESETS)
        self.assertLess(r.cell_size, 28)

    def test_zoom_step_clamps_at_top_preset(self):
        r = _make_renderer()
        r.cell_size = ZOOM_PRESETS[-1]
        r.zoom_step(+1)
        self.assertEqual(r.cell_size, ZOOM_PRESETS[-1])

    def test_zoom_step_clamps_at_bottom_preset(self):
        r = _make_renderer()
        r.cell_size = ZOOM_PRESETS[0]
        r.zoom_step(-1)
        self.assertEqual(r.cell_size, ZOOM_PRESETS[0])

    def test_zoom_step_snaps_arbitrary_size_to_closest_preset(self):
        """If the renderer starts at an arbitrary in-between size
        (e.g. the result of a wheel-zoom legacy state), the
        first +/- click should snap it to the nearest preset
        rather than to a different arbitrary size.
        """
        r = _make_renderer()
        r.cell_size = 25  # between 24 and 28
        r.zoom_step(+1)
        # 25 isn't in the presets; the next preset up is 28.
        self.assertEqual(r.cell_size, 28)

    def test_wheel_scroll_pixels_constant(self):
        """The wheel now scrolls, not zooms. The scroll step
        matches a single cell-row height at the default size.
        """
        self.assertEqual(WHEEL_SCROLL_PIXELS, 28)


class PerVariableVisibilityTests(unittest.TestCase):
    """Each variable has a visibility toggle stored in
    ``_hidden_vars``. ``_apply_view_mode`` is a no-op for
    scalars (the name is irrelevant to a single cell), but the
    hidden flag is honored at draw time.
    """

    def test_default_state_is_visible(self):
        r = _make_renderer()
        self.assertEqual(r._hidden_vars, set())

    def test_can_hide_a_variable(self):
        r = _make_renderer()
        r._hidden_vars.add("frontier")
        self.assertIn("frontier", r._hidden_vars)

    def test_can_show_a_hidden_variable(self):
        r = _make_renderer()
        r._hidden_vars.add("frontier")
        r._hidden_vars.discard("frontier")
        self.assertNotIn("frontier", r._hidden_vars)


class PerVariableViewModeTests(unittest.TestCase):
    """Each variable has a view mode: "full" (default), "10"
    (first 10 + last 1 with ... sentinel), or "custom"
    (first 5 + last 5). The apply function returns a new
    collection with a ``_TruncationSentinel`` marker between
    the head and tail slices.
    """

    def setUp(self):
        self.r = _make_renderer()

    def test_default_mode_is_full(self):
        # A mode lookup for an unset name returns "full".
        self.assertEqual(self.r._var_view_modes.get("frontier", "full"), "full")

    def test_full_mode_returns_unchanged(self):
        items = list(range(20))
        self.assertEqual(self.r._apply_view_mode("x", items), items)

    def test_10_mode_truncates_long_lists(self):
        items = list(range(50))
        self.r._var_view_modes["x"] = "10"
        result = self.r._apply_view_mode("x", items)
        # Head 10, then a sentinel, then tail 1.
        self.assertEqual(len(result), 10 + 1 + 1)
        self.assertEqual(result[:10], list(range(10)))
        self.assertIsInstance(result[10], _TruncationSentinel)
        self.assertEqual(result[11], 49)

    def test_10_mode_does_not_truncate_short_lists(self):
        items = list(range(5))
        self.r._var_view_modes["x"] = "10"
        result = self.r._apply_view_mode("x", items)
        # 5 items is less than head+tail+1 (12), so no truncation.
        self.assertEqual(result, items)

    def test_custom_mode_uses_5_plus_5(self):
        items = list(range(100))
        self.r._var_view_modes["x"] = "custom"
        result = self.r._apply_view_mode("x", items)
        # Head 5, sentinel, tail 5.
        self.assertEqual(len(result), 5 + 1 + 5)
        self.assertEqual(result[:5], [0, 1, 2, 3, 4])
        self.assertIsInstance(result[5], _TruncationSentinel)
        self.assertEqual(result[6:], [95, 96, 97, 98, 99])

    def test_view_mode_works_for_tuples(self):
        items = tuple(range(50))
        self.r._var_view_modes["x"] = "10"
        result = self.r._apply_view_mode("x", items)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 10 + 1 + 1)

    def test_view_mode_works_for_sets(self):
        items = set(range(50))
        self.r._var_view_modes["x"] = "10"
        result = self.r._apply_view_mode("x", items)
        self.assertIsInstance(result, set)
        # Set is unordered; we just check the count is right.
        self.assertEqual(len(result), 10 + 1 + 1)

    def test_view_mode_returns_scalar_unchanged(self):
        # Scalars have no head/tail.
        self.assertEqual(self.r._apply_view_mode("x", 42), 42)
        self.assertEqual(self.r._apply_view_mode("x", "hello"), "hello")
        self.assertEqual(self.r._apply_view_mode("x", None), None)


class TruncationSentinelTests(unittest.TestCase):
    """The ``_TruncationSentinel`` is a private marker that the
    renderer detects and draws as a single ``...`` cell in the
    gap between the head and tail slices.
    """

    def test_repr_is_ellipsis(self):
        self.assertEqual(repr(_TruncationSentinel()), "...")

    def test_distinct_instances_compare_equal(self):
        # Two sentinels should be "the same" for the purpose of
        # the truncation check (a == b).
        a = _TruncationSentinel()
        b = _TruncationSentinel()
        self.assertEqual(a, b)


class ClassificationHeightTests(unittest.TestCase):
    """The classifier's reported height for a list / set must
    account for the new vertical layout (N rows of cells,
    plus a header row) so the scroll math stays correct.
    """

    def test_list_height_is_one_header_plus_n_rows(self):
        r = _make_renderer()
        # A 1D list of 4 scalars at cell_size 28. Each row is
        # cell_size + 2; header is one cell_size. Total
        # = cell_size + 4 * (cell_size + 2) = 5*28 + 8 = 148.
        kind, _, h = r._classify_variable(
            [1, 2, 3, 4], content_w=400, cell_size=28,
        )
        self.assertEqual(kind, "list")
        self.assertEqual(h, 28 + 4 * (28 + 2))

    def test_list_of_tuples_height_includes_subvalue_rows(self):
        r = _make_renderer()
        # 2 tuples of length 3, each cell is 3 cell-heights tall.
        # Total = cell_size + 2 * (3*cell_size + 2) = 28 + 2*86 = 200.
        kind, _, h = r._classify_variable(
            [(1, 2, 3), (4, 5, 6)], content_w=400, cell_size=28,
        )
        self.assertEqual(kind, "list")
        # Each row: 3 sub-values stacked vertically = 3*cell_size+2
        expected = 28 + 2 * (3 * 28 + 2)
        self.assertEqual(h, expected)


if __name__ == "__main__":
    unittest.main()
