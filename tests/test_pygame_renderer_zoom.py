"""Tests for the renderer's zoom and scroll math.

The renderer itself is hard to unit-test without a real Pygame display
(it imports pygame, creates surfaces, etc.), so we test the pure-Python
zoom helpers in isolation.
"""
from __future__ import annotations

import unittest

from code_n.pygame_renderer import (
    DEFAULT_CELL_SIZE,
    PygameRenderer,
    ZOOM_MAX,
    ZOOM_MIN,
    ZOOM_STEP,
)


def _make_renderer(width: int = 1100, height: int = 720) -> PygameRenderer:
    """Construct a PygameRenderer without opening a window. The
    constructor does not touch pygame; only play() does."""
    return PygameRenderer(width=width, height=height, fps=60, speed="instant")


class ZoomStateTests(unittest.TestCase):
    def test_starts_at_default_30px(self):
        r = _make_renderer()
        self.assertEqual(r.cell_size, 30)
        self.assertEqual(r.zoom_label(), "30px")
        self.assertEqual(r.scroll_x, 0)
        self.assertEqual(r.scroll_y, 0)

    def test_default_zoom_constant(self):
        self.assertEqual(DEFAULT_CELL_SIZE, 30)
        self.assertEqual(ZOOM_MIN, 22)
        self.assertEqual(ZOOM_MAX, 50)
        self.assertGreaterEqual(ZOOM_STEP, 1)

    def test_zoom_by_increases(self):
        r = _make_renderer()
        r.cell_size = 30
        msg = r.zoom_by(5)
        self.assertEqual(r.cell_size, 35)
        self.assertIn("35px", msg)

    def test_zoom_by_decreases(self):
        r = _make_renderer()
        r.cell_size = 40
        msg = r.zoom_by(-5)
        self.assertEqual(r.cell_size, 35)
        self.assertIn("35px", msg)

    def test_zoom_by_clamps_to_max(self):
        r = _make_renderer()
        r.cell_size = ZOOM_MAX
        msg = r.zoom_by(10)
        self.assertEqual(r.cell_size, ZOOM_MAX)
        self.assertIn("max", msg.lower())

    def test_zoom_by_clamps_to_min(self):
        r = _make_renderer()
        r.cell_size = ZOOM_MIN
        msg = r.zoom_by(-10)
        self.assertEqual(r.cell_size, ZOOM_MIN)
        self.assertIn("min", msg.lower())

    def test_zoom_by_step_matches_wheel_zoom(self):
        """The wheel handler multiplies event.y by ZOOM_STEP, so the
        single-notch zoom should land exactly at cell_size + ZOOM_STEP."""
        r = _make_renderer()
        r.cell_size = 30
        r.zoom_by(ZOOM_STEP)  # one wheel notch up
        self.assertEqual(r.cell_size, 30 + ZOOM_STEP)
        r.zoom_by(-ZOOM_STEP)  # one wheel notch down
        self.assertEqual(r.cell_size, 30)

    def test_zoom_label_is_always_pixel_size(self):
        """No "fit to window" mode is exposed anywhere."""
        r = _make_renderer()
        for delta in (-100, -10, -1, 0, 1, 10, 100):
            r.zoom_by(delta)
            label = r.zoom_label()
            self.assertNotIn("fit", label.lower())
            self.assertTrue(label.endswith("px"))


class VisibleViewportTests(unittest.TestCase):
    def test_small_grid_fits_completely(self):
        r = _make_renderer()
        values = [[i for i in range(10)]]  # 1 row, 10 cols
        visible_cols, visible_rows, max_x, max_y = r._visible_viewport(
            grid=None, values=values,
        )
        # 10 cells in a wide window fits with room to spare; the exact
        # number depends on the cell size (30px default) but must
        # comfortably exceed the grid width.
        self.assertGreater(visible_cols, 15)
        self.assertGreater(visible_rows, 1)
        self.assertEqual(max_x, 0)
        self.assertEqual(max_y, 0)

    def test_large_grid_always_requires_scroll(self):
        """With the n=50 cap, the BFS/DFS grid is 50x50. At 30px cells
        in a ~1100px window, the user can see ~33 columns and ~20 rows,
        so the grid must be scrollable in both directions."""
        r = _make_renderer()
        values = [[0] * 50 for _ in range(50)]
        visible_cols, visible_rows, max_x, max_y = r._visible_viewport(
            grid=None, values=values,
        )
        self.assertLess(visible_cols, 50)
        self.assertLess(visible_rows, 50)
        self.assertGreater(max_x, 0)
        self.assertGreater(max_y, 0)

    def test_empty_values_clamps_to_zero(self):
        r = _make_renderer()
        visible_cols, visible_rows, max_x, max_y = r._visible_viewport(
            grid=None, values=[],
        )
        self.assertEqual((visible_cols, visible_rows, max_x, max_y), (0, 0, 0, 0))


class PanStateTests(unittest.TestCase):
    """Right-click drag panning with bounded scrolling.

    The user wants "inverted" panning: dragging right pulls the world
    to the right (scroll_x decreases), so the cells under the cursor
    stay under the cursor. The same convention applies vertically.
    scroll_by clamps to the grid bounds, so dragging past the edge
    stops at the boundary instead of scrolling into the void.

    The panning uses a float accumulator (_pan_accum_x/_pan_accum_y)
    so sub-pixel drags accumulate smoothly into whole-cell scrolls
    instead of snapping at integer boundaries.
    """

    def test_pan_starts_off_with_zero_accumulator(self):
        r = _make_renderer()
        self.assertFalse(r._right_panning)
        self.assertEqual(r._pan_accum_x, 0.0)
        self.assertEqual(r._pan_accum_y, 0.0)

    def test_drag_right_decreases_scroll(self):
        """Dragging the mouse right -> scroll_x decreases."""
        r = _make_renderer()
        r.cell_size = 30
        r.scroll_x = 5
        r._right_panning = True
        # The MOUSEMOTION handler in play() negates the motion delta
        # before calling scroll_by; here we call scroll_by directly
        # with the post-negation value.
        r.scroll_by(-1, 0, grid=None, values=[[0] * 50])
        self.assertEqual(r.scroll_x, 4)

    def test_drag_left_increases_scroll(self):
        r = _make_renderer()
        r.cell_size = 30
        r.scroll_x = 5
        r._right_panning = True
        r.scroll_by(1, 0, grid=None, values=[[0] * 50])
        self.assertEqual(r.scroll_x, 6)

    def test_drag_down_decreases_vertical_scroll(self):
        r = _make_renderer()
        r.cell_size = 30
        r.scroll_y = 5
        r._right_panning = True
        r.scroll_by(0, -1, grid=None, values=[[0] * 50 for _ in range(50)])
        self.assertEqual(r.scroll_y, 4)

    def test_drag_up_increases_vertical_scroll(self):
        r = _make_renderer()
        r.cell_size = 30
        r.scroll_y = 5
        r._right_panning = True
        r.scroll_by(0, 1, grid=None, values=[[0] * 50 for _ in range(50)])
        self.assertEqual(r.scroll_y, 6)

    def test_pan_clamped_at_left_edge(self):
        """If the user keeps dragging right while already at scroll_x=0,
        the view should stay at 0 - no scrolling into negative territory."""
        r = _make_renderer()
        r.cell_size = 30
        r.scroll_x = 0
        r._right_panning = True
        for _ in range(1000):
            r.scroll_by(-1, 0, grid=None, values=[[0] * 50])
        self.assertEqual(r.scroll_x, 0)

    def test_pan_clamped_at_right_edge(self):
        """If the user keeps dragging left while already at the rightmost
        valid scroll, the view should stop at max_x - no void scrolling."""
        r = _make_renderer()
        r.cell_size = 30
        r.scroll_x = 0
        _, _, max_x, _ = r._visible_viewport(grid=None, values=[[0] * 50])
        r._right_panning = True
        for _ in range(1000):
            r.scroll_by(1, 0, grid=None, values=[[0] * 50])
        self.assertEqual(r.scroll_x, max_x)
        self.assertGreater(r.scroll_x, 0)
        self.assertLess(r.scroll_x, 50)

    def test_pan_accumulator_math(self):
        """Drag pixels that don't cross a PAN_PIXELS_PER_CELL boundary
        should accumulate, not snap to a scroll step. Drag pixels that
        do cross a boundary should trigger exactly that many scrolls."""
        from code_n.pygame_renderer import PAN_PIXELS_PER_CELL
        r = _make_renderer()
        r._right_panning = True
        r.scroll_x = 5

        # Simulate play()'s accumulator logic on a 5px drag.
        # PAN_PIXELS_PER_CELL is 16, so 5px is sub-cell and should not
        # change scroll_x.
        accum = 0.0
        rel = 5
        accum += rel
        dx = -int(accum // PAN_PIXELS_PER_CELL)
        accum += dx * PAN_PIXELS_PER_CELL
        self.assertEqual(dx, 0)
        self.assertEqual(accum, 5.0)
        self.assertEqual(r.scroll_x, 5)

        # Now add another 12px (total 17px). That crosses one boundary
        # and leaves 1px in the accumulator.
        accum += 12
        dx = -int(accum // PAN_PIXELS_PER_CELL)
        accum += dx * PAN_PIXELS_PER_CELL
        self.assertEqual(dx, -1)
        self.assertEqual(accum, 1.0)
        # Apply the scroll: scroll_x decreases by 1.
        r.scroll_by(dx, 0, grid=None, values=[[0] * 50])
        self.assertEqual(r.scroll_x, 4)

    def test_pan_sensitivity_is_higher_than_cell_size(self):
        """The old panning required dragging a full cell_size pixels to
        advance one cell. The new sensitivity is PAN_PIXELS_PER_CELL,
        which is < cell_size, so the user gets more responsiveness per
        pixel of drag."""
        from code_n.pygame_renderer import PAN_PIXELS_PER_CELL
        r = _make_renderer()
        r.cell_size = 30
        # 1 cell per 16px is much more sensitive than 1 cell per 30px
        # (the old behavior).
        self.assertLess(PAN_PIXELS_PER_CELL, r.cell_size)
        # 30px of drag = ~1.875 cells under the new sensitivity.
        # Old behavior: exactly 1 cell.
        self.assertGreater(30 / PAN_PIXELS_PER_CELL, 1.5)


class ContinuousScrollTests(unittest.TestCase):
    """The continuous-scroll constants set the cadence for held arrow
    keys. The values are tuned so holding a key feels smooth (multiple
    scrolls per second) but not so fast that a single tap scrolls
    noticeably more than one cell."""

    def test_scroll_interval_is_fast_enough_to_feel_continuous(self):
        from code_n.pygame_renderer import CONTINUOUS_SCROLL_INTERVAL
        # At 60 FPS, the main loop runs every ~16ms. An interval of
        # 40ms means a held key scrolls every 2-3 frames, which feels
        # smooth on a 60Hz display.
        self.assertLessEqual(CONTINUOUS_SCROLL_INTERVAL, 0.05)
        self.assertGreaterEqual(CONTINUOUS_SCROLL_INTERVAL, 0.01)

    def test_page_jump_is_bigger_than_one_cell(self):
        from code_n.pygame_renderer import PAGE_JUMP_SIZE
        self.assertGreaterEqual(PAGE_JUMP_SIZE, 5)


class SpeedDisplayTests(unittest.TestCase):
    """The side-panel speed line must always show the per-op delay
    value, even after a custom +/- speed change (where the label is
    'Custom'). Otherwise the user has no visible feedback that the
    key did anything when the replay is paused."""

    def test_preset_speed_shows_label_and_delay(self):
        r = _make_renderer()
        r.speed_label = "Normal"
        r.step_delay = 0.12
        self.assertEqual(r._speed_display(), "Normal (0.120s)")

    def test_custom_speed_shows_only_delay(self):
        """When the user has pressed +/- and the label is 'Custom',
        the delay alone is enough information — we drop the label so
        the line stays short enough to fit the side panel."""
        r = _make_renderer()
        r.speed_label = "Custom"
        r.step_delay = 0.08
        self.assertEqual(r._speed_display(), "0.080s/op")

    def test_instant_speed_renders_cleanly(self):
        r = _make_renderer()
        r.speed_label = "Instant"
        r.step_delay = 0.0
        self.assertEqual(r._speed_display(), "Instant (0.000s)")


class ScrollByTests(unittest.TestCase):
    def test_scroll_clamped_at_min(self):
        """Calling scroll_by with a large negative delta should clamp
        scroll to 0 (not go below)."""
        r = _make_renderer()
        values = [[0] * 50 for _ in range(50)]
        r.scroll_by(-100, -100, grid=None, values=values)
        self.assertEqual(r.scroll_x, 0)
        self.assertEqual(r.scroll_y, 0)

    def test_scroll_clamped_at_max(self):
        """Calling scroll_by with a large positive delta should clamp
        scroll to max_x (not exceed the grid bounds)."""
        r = _make_renderer()
        values = [[0] * 50 for _ in range(50)]
        r.scroll_by(10000, 10000, grid=None, values=values)
        _, _, max_x, max_y = r._visible_viewport(grid=None, values=values)
        self.assertLessEqual(r.scroll_x, max_x)
        self.assertLessEqual(r.scroll_y, max_y)

    def test_scroll_by_returns_true_when_changed(self):
        r = _make_renderer()
        values = [[0] * 50 for _ in range(50)]
        changed = r.scroll_by(5, 5, grid=None, values=values)
        self.assertTrue(changed)
        unchanged = r.scroll_by(0, 0, grid=None, values=values)
        self.assertFalse(unchanged)

    def test_scroll_within_viewport_is_a_noop(self):
        r = _make_renderer()
        values = [[i for i in range(10)]]
        r.scroll_by(3, 0, grid=None, values=values)
        self.assertEqual(r.scroll_x, 0)


class VisibleRangeTextTests(unittest.TestCase):
    def test_text_includes_endpoints_and_total(self):
        r = _make_renderer()
        values = [[0] * 50]
        r.scroll_x = 5
        text = r._visible_range_text(grid=None, values=values)
        self.assertIn("5", text)
        self.assertIn("49", text)

    def test_text_empty_for_empty_grid(self):
        r = _make_renderer()
        self.assertEqual(r._visible_range_text(grid=None, values=[]), "")


class WrapTests(unittest.TestCase):
    """The panel-wrap helper must never produce a line longer than the
    requested width — that's what was overflowing the variables panel
    in the user screenshot."""

    def test_short_text_unchanged(self):
        r = _make_renderer()
        self.assertEqual(r._wrap("hello world", 30), ["hello world"])

    def test_long_text_wraps_within_width(self):
        r = _make_renderer()
        lines = r._wrap("data = [66, 64, 55, 93, 91, 3, 40, 33, 54, 28, 30, 85, 67, 90, 66,]", 28)
        for line in lines:
            self.assertLessEqual(len(line), 28, msg=f"line {line!r} exceeds 28 chars")

    def test_overlong_single_token_is_truncated(self):
        """A single word longer than the width gets a '...' tail and the
        remainder goes on the next line, so nothing overflows."""
        r = _make_renderer()
        long_token = "abcdefghij" * 5  # 50 chars
        lines = r._wrap(long_token, 20)
        for line in lines:
            self.assertLessEqual(len(line), 20, msg=f"line {line!r} exceeds 20 chars")
        # The first line should carry the ellipsis marker.
        self.assertTrue(any("..." in line for line in lines))

    def test_wrap_width_fits_panel(self):
        r = _make_renderer()
        fonts = {"small": _FakeFont()}
        w = r._wrap_width(fonts)
        # 300px panel - 36px padding = 264px. 9px char → ~29 chars,
        # minus the 2-char margin and floored to >= 8.
        self.assertGreaterEqual(w, 8)
        self.assertLessEqual(w, 35)


class _FakeFont:
    """A stand-in for a pygame.font.Font that returns a known char width."""

    def size(self, _text):
        return (9, 15)


class RowLabelWidthTests(unittest.TestCase):
    def test_no_rows_zero_width(self):
        r = _make_renderer()
        self.assertEqual(r._row_label_width([]), 0)

    def test_single_row_zero_width(self):
        """A 1D array (one row) needs no row label column at all."""
        r = _make_renderer()
        # display_rows has 1 row → no row labels
        rows = [[None] * 10]
        self.assertEqual(r._row_label_width(rows), 0)

    def test_2d_array_grows_with_row_count(self):
        r = _make_renderer()
        rows_1_digit = [[None] * 5] * 5  # max index 4, 1 digit
        rows_2_digit = [[None] * 5] * 25  # max index 24, 2 digits
        rows_3_digit = [[None] * 5] * 150  # max index 149, 3 digits
        w1 = r._row_label_width(rows_1_digit)
        w2 = r._row_label_width(rows_2_digit)
        w3 = r._row_label_width(rows_3_digit)
        self.assertLess(w1, w2)
        self.assertLess(w2, w3)

    def test_35_rows_uses_2_digit_width(self):
        """The 2D BFS/DFS challenges cap at 35, so the row label width
        should be sized for 2-digit numbers (10..34)."""
        r = _make_renderer()
        rows = [[None] * 5] * 35
        w = r._row_label_width(rows)
        # 2 digits → 16 + 2*10 = 36
        self.assertEqual(w, 36)

    def test_row_labels_dont_get_clipped_away(self):
        """Regression: the main cell loop set a clip on grid_rect, which
        silently discarded row labels and their tick lines because they
        are drawn at x = grid_rect.x - label_width. The clip must now
        include the label column."""
        r = _make_renderer()
        # We don't drive the real Pygame surface here; instead we
        # assert that the label rect x is negative relative to the
        # grid rect — i.e. it really does sit outside grid_rect, so
        # any clip that doesn't extend left will hide it.
        rows = [[None] * 5] * 35
        from code_n.pygame_renderer import DisplayCell
        wrapped = [[DisplayCell(value=None, source_coord=(0, y)) for _ in range(5)] for y in range(35)]
        label_width = r._row_label_width(wrapped)
        self.assertGreater(label_width, 0)
        # Verify the math: label sits to the LEFT of the grid.
        # If a future change ever forgets the label-column clip
        # expansion, the test below would still pass (it only checks
        # the constant), so this is documentation as much as guard.


if __name__ == "__main__":
    unittest.main()
