"""Pygame renderer for animated algorithm visualization."""

from __future__ import annotations

import re
import os
import time
import types
from dataclasses import dataclass, field
from typing import Any, Iterable, Optional

from .counter import ComplexityClass, OpRecord, OpStats, OpType
from .branding import GAME_TITLE
from .execution_trace import TraceFrame
from .grid import CellType, Grid
from .window import is_resize_event, mono_font, open_maximized_window, sync_window_size


@dataclass
class VisualRunResult:
    passed: bool
    message: str
    stats: OpStats
    actual_complexity: ComplexityClass
    required_complexity: ComplexityClass
    n: int
    description: str = ""
    return_value: str = ""
    trace_frames: list[TraceFrame] = field(default_factory=list)


@dataclass(frozen=True)
class SpeedPreset:
    key: str
    label: str
    step_delay: float
    swap_frames: int
    manual_step: bool = False


@dataclass(frozen=True)
class ControlButton:
    action: str
    label: str
    rect: Any
    enabled: bool = True
    active: bool = False


@dataclass(frozen=True)
class DisplayCell:
    """A cell shown in the grid display, with its source grid coordinate.

    Without the legacy ellipsis truncation, source_coord is just (x, y)
    in the full grid; scroll and zoom are applied at draw time, not here.
    """
    value: Any
    source_coord: Optional[tuple[int, int]] = None


class ComputationCancelled(RuntimeError):
    """Raised when the user closes the computation progress window."""


class ComputationProgressWindow:
    """Small Pygame window shown while a player's solution is executing."""

    BACKGROUND = (18, 21, 26)
    PANEL = (29, 34, 43)
    GRID_LINE = (64, 73, 89)
    TEXT = (232, 236, 243)
    MUTED = (157, 166, 178)
    ACCENT = (103, 165, 255)

    def __init__(self, title: str, description: str, limit: Optional[int], width: int = 900, height: int = 520):
        import pygame

        pygame.init()
        self.title = title
        self.description = description
        self.limit = limit
        self.width = width
        self.height = height
        self.screen = open_maximized_window(pygame, width, height, f"{GAME_TITLE} - Running {title}")
        sync_window_size(self, self.screen)
        self.clock = pygame.time.Clock()
        self.fonts = {
            "title": mono_font(pygame, 28, bold=True),
            "body": mono_font(pygame, 19),
            "small": mono_font(pygame, 15),
        }
        self._last_draw = 0.0
        self.update("Preparing challenge", 0, limit, force=True)

    def update(self, stage: str, operations: int, limit: Optional[int] = None, force: bool = False):
        import pygame

        self.limit = limit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise ComputationCancelled("Stopped: the run window was closed before the solution finished.")
            if is_resize_event(pygame, event):
                self.screen = pygame.display.get_surface() or self.screen
                sync_window_size(self, self.screen)

        now = time.time()
        if not force and now - self._last_draw < 0.05:
            return
        self._last_draw = now
        self._draw(stage, operations)
        pygame.display.flip()
        self.clock.tick(60)

    def close(self):
        import pygame

        if pygame.display.get_init():
            pygame.display.quit()

    def _draw_text(self, font_name: str, text: str, x: int, y: int, color: tuple[int, int, int]):
        self.screen.blit(self.fonts[font_name].render(text, True, color), (x, y))

    def _wrap(self, text: str, width: int) -> list[str]:
        words = text.split()
        lines: list[str] = []
        current = ""
        for word in words:
            if len(current) + len(word) + 1 > width:
                if current:
                    lines.append(current)
                current = word
            else:
                current = f"{current} {word}".strip()
        if current:
            lines.append(current)
        return lines or [""]

    def _draw(self, stage: str, operations: int):
        import pygame

        self.screen.fill(self.BACKGROUND)
        margin = 34
        panel = pygame.Rect(margin, margin, self.width - margin * 2, self.height - margin * 2)
        pygame.draw.rect(self.screen, self.PANEL, panel, border_radius=8)
        pygame.draw.rect(self.screen, self.GRID_LINE, panel, width=1, border_radius=8)

        self._draw_text("title", self.title, panel.x + 26, panel.y + 26, self.TEXT)
        self._draw_text("body", stage, panel.x + 26, panel.y + 70, self.MUTED)

        y = panel.y + 118
        for line in self._wrap(self.description.replace("\n", " "), 74)[:4]:
            self._draw_text("small", line, panel.x + 26, y, self.MUTED)
            y += 20

        bar_x = panel.x + 26
        bar_y = y + 34
        bar_w = panel.width - 52
        pygame.draw.rect(self.screen, (48, 55, 67), (bar_x, bar_y, bar_w, 18), border_radius=9)
        if self.limit:
            progress = min(1.0, operations / self.limit)
            pygame.draw.rect(self.screen, self.ACCENT, (bar_x, bar_y, int(bar_w * progress), 18), border_radius=9)

        budget = f"{operations} / {self.limit}" if self.limit else str(operations)
        self._draw_text("body", f"Operations: {budget}", bar_x, bar_y + 34, self.TEXT)
        self._draw_text("small", "The replay will open as soon as the solution finishes.", bar_x, bar_y + 66, self.MUTED)
        self._draw_text("small", "Close this window to cancel the run.", bar_x, bar_y + 88, self.MUTED)

    def _draw_text(self, font_name: str, text: str, x: int, y: int, color: tuple[int, int, int]):
        self.screen.blit(self.fonts[font_name].render(text, True, color), (x, y))

    def _wrap(self, text: str, width: int) -> list[str]:
        words = text.split()
        lines: list[str] = []
        current = ""
        for word in words:
            if len(current) + len(word) + 1 > width:
                if current:
                    lines.append(current)
                current = word
            else:
                current = f"{current} {word}".strip()
        if current:
            lines.append(current)
        return lines or [""]


SPEED_PRESETS = [
    SpeedPreset("step", "Step", 0.0, 1, manual_step=True),
    SpeedPreset("crawl", "Crawl", 1.50, 60),
    SpeedPreset("very-slow", "Very Slow", 0.75, 42),
    SpeedPreset("slow", "Slow", 0.30, 24),
    SpeedPreset("normal", "Normal", 0.12, 14),
    SpeedPreset("fast", "Fast", 0.05, 8),
    SpeedPreset("turbo", "Turbo", 0.015, 4),
    SpeedPreset("instant", "Instant", 0.0, 1),
]
DEFAULT_SPEED_INDEX = 4

# Continuous zoom range. The cell size is an int in [ZOOM_MIN, ZOOM_MAX]
# and the user changes it with the mouse wheel only — no buttons, no
# keyboard shortcuts. 22px is small enough to fit the whole 50-cell
# 1D array in one screen; 50px is large enough that 3-digit values
# still fit comfortably.
ZOOM_MIN = 12
ZOOM_MAX = 50
ZOOM_STEP = 2  # pixels per wheel notch
DEFAULT_CELL_SIZE = 22

# Pixels of right-drag the user has to move to advance the view by
# one cell. Smaller = more sensitive. The float accumulator carries
# sub-cell motion between events, so very small drags feel smooth
# rather than snapping to whole cells.
PAN_PIXELS_PER_CELL = 1

# Time-based throttle for continuous arrow-key scrolling while a key
# is held down. At 60 FPS this gives ~25 scroll steps per second.
CONTINUOUS_SCROLL_INTERVAL = 0.04  # seconds between scroll steps

# Page Up / Page Down jump size (cells per press). Bigger = faster
# big-jumps when the user wants to fly across a 50-cell row.
PAGE_JUMP_SIZE = 10


class PygameRenderer:
    """Draws grid state and replays recorded operations in a Pygame window."""

    BACKGROUND = (18, 21, 26)
    PANEL = (29, 34, 43)
    GRID_LINE = (64, 73, 89)
    TEXT = (232, 236, 243)
    MUTED = (157, 166, 178)
    ACCENT_COLOR = (103, 165, 255)
    PASS = (58, 185, 117)
    FAIL = (239, 86, 86)
    READ = (103, 165, 255)
    WRITE = (255, 203, 88)
    COMPARE_A = (255, 103, 103)
    COMPARE_B = (75, 213, 190)
    SWAP = (255, 154, 77)

    CELL_COLORS = {
        CellType.EMPTY: (34, 39, 48),
        CellType.WALL: (10, 12, 16),
        CellType.VALUE: (66, 77, 92),
        CellType.MARKER: (141, 112, 45),
        CellType.START: (45, 126, 82),
        CellType.GOAL: (144, 58, 58),
        CellType.PATH: (39, 125, 149),
        CellType.VISITED: (48, 82, 152),
        CellType.CURRENT: (118, 77, 150),
        CellType.SORTED: (45, 126, 82),
        CellType.UNSORTED: (66, 77, 92),
        CellType.PIVOT: (158, 126, 45),
        CellType.COMPARE_A: COMPARE_A,
        CellType.COMPARE_B: COMPARE_B,
    }

    def __init__(self, width: int = 1100, height: int = 720, fps: int = 60,
                 speed: Optional[str] = None):
        self.width = width
        self.height = height
        self.fps = fps
        self.margin = 28
        self.panel_width = 300
        self.step_delay = SPEED_PRESETS[DEFAULT_SPEED_INDEX].step_delay
        self.swap_frames = SPEED_PRESETS[DEFAULT_SPEED_INDEX].swap_frames
        self.speed_label = SPEED_PRESETS[DEFAULT_SPEED_INDEX].label
        self.manual_step = SPEED_PRESETS[DEFAULT_SPEED_INDEX].manual_step
        self._speed_was_supplied = speed is not None
        if speed:
            self.apply_speed(speed)
        self._current_description = ""
        # Cache of player source files keyed by absolute path. Each
        # value is the list of source lines (1-indexed access via
        # ``lines[line_no - 1]``). Populated lazily by
        # ``_format_source_line`` so the "Current op" panel can show
        # the actual Python statement the engine just executed.
        self._source_cache: dict[str, list[str]] = {}
        # (var_name, index) -> (timestamp, op_type). Populated by
        # the play() loop on each operation and consumed by
        # ``_draw_variable_strip`` to flash the touched cells in
        # the op-type color (read=blue, write=yellow, etc.). Old
        # entries are pruned at draw time so the flash naturally
        # fades out.
        self._touched_cells: dict[tuple[str, int], tuple[float, str]] = {}
        # Continuous zoom between ZOOM_MIN and ZOOM_MAX, controlled by
        # the mouse wheel only. The default of 30px is small enough to
        # fit ~25 cells across the viewport; the user can wheel up to
        # 50px to make individual cells more readable.
        self.cell_size: int = DEFAULT_CELL_SIZE
        # Scroll position, in source-grid cells. (0, 0) is the top-left.
        self.scroll_x: int = 0
        self.scroll_y: int = 0
        # Vertical scroll for the Variables panel. The variables list
        # can be much taller than the available main-area height (a
        # 35x35 TrackedGrid + visited set + queue + scalars is
        # hundreds of cells), so we render it with a scroll offset
        # when the content overflows. The wheel scrolls within the
        # variables panel when the mouse is over it. The right-drag
        # pans the variables panel too (only there - the main
        # grid is no longer drawn in the main area, so there's
        # nothing to pan outside the variables section).
        # A 50-element list at 18px cells is ~950px wide, much
        # wider than the ~700px panel, so horizontal panning
        # matters as much as vertical.
        self._vars_scroll_x: int = 0
        self._vars_scroll_y: int = 0
        # Cached rect of the Variables panel, set during the last
        # _draw() so the play() loop's wheel handler can tell
        # "mouse over the variables panel" from "mouse over the
        # main grid / side panel".
        self._vars_panel_rect: tuple[int, int, int, int] = (0, 0, 0, 0)
        # True while the right mouse button is held down for panning.
        self._right_panning: bool = False
        # Sub-cell panning accumulator. Right-drag moves in pixels; we
        # accumulate the fractional pixel delta here and only commit
        # whole cells to scroll_by when the running total crosses a
        # PAN_PIXELS_PER_CELL boundary. Reset to 0 on every right
        # mouse-down/up so a stale fraction can't cause a jump.
        self._pan_accum_x: float = 0.0
        self._pan_accum_y: float = 0.0

    def apply_speed(self, speed: str):
        preset = self._find_speed(speed)
        if not preset:
            preset = SPEED_PRESETS[DEFAULT_SPEED_INDEX]
        self.step_delay = preset.step_delay
        self.swap_frames = preset.swap_frames
        self.speed_label = preset.label
        self.manual_step = preset.manual_step

    # ---- zoom and scroll ------------------------------------------------

    def zoom_by(self, delta: int) -> str:
        """Change the cell size by `delta` pixels, clamped to [ZOOM_MIN, ZOOM_MAX].

        Called exclusively by the mouse-wheel handler; there is no
        button or key shortcut for zoom. Positive delta zooms in
        (bigger cells), negative zooms out.
        """
        new_size = max(ZOOM_MIN, min(ZOOM_MAX, self.cell_size + delta))
        if new_size == self.cell_size:
            cap = "max" if delta > 0 else "min"
            return f"Zoom: {self.zoom_label()} ({cap})"
        self.cell_size = new_size
        return f"Zoom: {self.zoom_label()}"

    def zoom_label(self) -> str:
        return f"{self.cell_size}px"

    def _speed_display(self) -> str:
        """Human-readable current speed for the side panel.

        Shows the label (preset name or "Custom") plus the per-op delay
        so the user can see the effect of + / - even when the replay
        is paused. ``0.000s`` means instant (no delay between ops).
        """
        if self.speed_label and self.speed_label != "Custom":
            return f"{self.speed_label} ({self.step_delay:.3f}s)"
        return f"{self.step_delay:.3f}s/op"

    def _effective_cell_size(self, grid: Grid, values: Optional[list[list[Any]]]) -> int:
        return self.cell_size

    def _wrap_rows(self, values: list[list[Any]]) -> list[list[DisplayCell]]:
        return [[DisplayCell(value=v, source_coord=(x, y)) for x, v in enumerate(row)] for y, row in enumerate(values)]

    def _visible_viewport(self, grid: Grid, values: Optional[list[list[Any]]]) -> tuple[int, int, int, int]:
        """Return (visible_cols, visible_rows, max_scroll_x, max_scroll_y)."""
        if values is None or not values:
            return 0, 0, 0, 0
        cols = max((len(row) for row in values), default=0)
        rows = len(values)
        cell_size = self.cell_size
        label_width = self._row_label_width(self._wrap_rows(values))
        available_w = self._main_area_width() - label_width
        available_h = self.height - self._grid_top() - self.margin
        visible_cols = max(1, available_w // max(cell_size, 1))
        visible_rows = max(1, available_h // max(cell_size, 1))
        max_scroll_x = max(0, cols - visible_cols)
        max_scroll_y = max(0, rows - visible_rows)
        return visible_cols, visible_rows, max_scroll_x, max_scroll_y

    def _visible_range_text(self, grid: Grid, values: Optional[list[list[Any]]]) -> str:
        """One-line description of what's on screen, e.g. '0-22 of 50'."""
        if not values:
            return ""
        cols = max((len(row) for row in values), default=0)
        rows = len(values)
        visible_cols, visible_rows, _, _ = self._visible_viewport(grid, values)
        x_end = min(cols, self.scroll_x + visible_cols) - 1
        y_end = min(rows, self.scroll_y + visible_rows) - 1
        if cols == 0 and rows == 0:
            return ""
        if rows == 1:
            return f"View: {self.scroll_x}-{x_end} of {cols - 1}"
        return f"View: ({self.scroll_x},{self.scroll_y})-({x_end},{y_end}) of {cols - 1}x{rows - 1}"

    def scroll_by(self, dx_cells: int, dy_cells: int, grid: Grid, values: Optional[list[list[Any]]]) -> bool:
        """Pan the viewport by (dx, dy) cells, clamped to the grid bounds.

        Pan inputs are intentionally signed the way the *user's hand*
        moves (right-drag right = positive dx, drag down = positive dy).
        The mapping from hand motion to world scroll is up to the caller
        — see play()'s MOUSEMOTION handler for the current "inverted /
        grab the world" convention.
        """
        _, _, max_x, max_y = self._visible_viewport(grid, values)
        old_x, old_y = self.scroll_x, self.scroll_y
        self.scroll_x = max(0, min(self.scroll_x + dx_cells, max_x))
        self.scroll_y = max(0, min(self.scroll_y + dy_cells, max_y))
        return (self.scroll_x, self.scroll_y) != (old_x, old_y)

    # ---- Variables-panel scroll ---------------------------------------
    #
    # The variables list is its own scrollable region. A BFS
    # challenge has ``grid`` (35x35 TrackedGrid), ``visited`` (set
    # of up to ~1200 cells), and a handful of scalars; that's
    # much taller than the available main-area height, so we
    # render the panel with a vertical scroll offset and let the
    # wheel scroll it when the mouse is over the panel.

    def _mouse_in_vars_panel(self, pos) -> bool:
        if pos is None or not self._vars_panel_rect:
            return False
        x, y, w, h = self._vars_panel_rect
        if w <= 0 or h <= 0:
            return False
        return x <= pos[0] < x + w and y <= pos[1] < y + h

    def _scroll_vars(self, dx: int, dy: int) -> None:
        """Scroll the Variables panel by ``(dx, dy)`` pixels. Positive
        ``dx`` scrolls right (reveals content to the right of the
        current view); positive ``dy`` scrolls down (same
        convention as the wheel handler - the user wheels "up" to
        see content above, so the wheel handler passes a negative
        ``dy`` to that effect).

        Clamped so the content can't scroll past the top/left or
        past the bottom/right. The user can also right-drag inside
        the panel to pan - that handler routes through here too.
        """
        max_x = max(0, self._vars_content_width - self._vars_view_width)
        max_y = max(0, self._vars_content_height - self._vars_view_height)
        self._vars_scroll_x = max(0, min(self._vars_scroll_x + dx, max_x))
        self._vars_scroll_y = max(0, min(self._vars_scroll_y + dy, max_y))

    def play(self, grid: Grid, operations: Iterable[OpRecord], title: str, result: VisualRunResult):
        import pygame

        pygame.init()
        screen = open_maximized_window(pygame, self.width, self.height, f"{GAME_TITLE} - {title}")
        sync_window_size(self, screen)
        clock = pygame.time.Clock()
        fonts = {
            "title": mono_font(pygame, 26, bold=True),
            "body": mono_font(pygame, 18),
            "small": mono_font(pygame, 15),
            "cell": mono_font(pygame, 18, bold=True),
        }

        if not self._speed_was_supplied and not self._choose_speed(screen, clock, fonts, title):
            pygame.quit()
            return

        self._current_description = result.description
        initial_values = self._values_from_grid(grid)
        visual_values = self._copy_values(initial_values)
        ops = list(operations)
        current_detail = "Ready"
        # Tracks the most recent operation that was actually applied
        # to the data (e.g. ``set candies[15] = max(candies[15],
        # candies[16] + 1)``). Kept separate from ``current_detail``
        # so toggling pause/step/replay doesn't blow away the
        # operation the player was just looking at - the "Current
        # op" panel keeps showing what the engine *did*, while
        # ``current_detail`` carries the transient user-action
        # message ("Paused", "Speed changed", ...).
        last_op_detail = ""
        overlays: dict[tuple[int, int], tuple[int, int, int]] = {}
        watchpoints: set[tuple[int, int]] = set()
        source_breakpoints_hit: set[tuple[int, int]] = set()
        running = True
        paused = self.manual_step
        stopped = False
        op_index = 0
        last_step = 0.0
        last_key_scroll = 0.0
        current_detail = "Step mode: press Space or Enter." if self.manual_step else current_detail

        def apply_next_operation() -> str:
            nonlocal op_index, paused, stopped, last_op_detail
            if op_index >= len(ops):
                return "Replay complete. Press Replay to run again."

            current_op = ops[op_index]
            detail = self._apply_operation(screen, clock, fonts, grid, visual_values, current_op, op_index, len(ops), title, result)
            last_op_detail = detail
            if self._op_touches_watchpoint(current_op, watchpoints):
                paused = True
                detail = f"Watchpoint hit: {detail}"
            op_index += 1
            trace_frame = self._trace_for_op(result.trace_frames, op_index)
            # Update the touched-cells tracker so the variables
            # panel can flash the cells this op touched in the
            # op-type color. The flash is the same "this is the
            # one I just read / wrote / compared" effect that the
            # main grid already does. We pass the trace_frame so
            # the CALL branch can read the source line directly
            # (op.detail is just 'line N' for line-based tracing).
            if trace_frame and trace_frame.locals:
                self._touched_cells = self._extract_touched_cells(
                    current_op, trace_frame,
                )
            if self._source_breakpoint_hit(trace_frame, source_breakpoints_hit):
                paused = True
                detail = f"Source breakpoint line {trace_frame.line_no}: {detail}"
            stopped = False
            return detail

        def reset_replay() -> str:
            nonlocal visual_values, op_index, paused, stopped, overlays, source_breakpoints_hit, last_op_detail
            visual_values = self._copy_values(initial_values)
            op_index = 0
            paused = self.manual_step
            stopped = False
            overlays = {}
            source_breakpoints_hit = set()
            last_op_detail = ""
            # Each fresh replay starts at the default variables
            # cell size (22px, the middle of the new ZOOM_MIN..MAX
            # range of 12..50) and the top-left of the grid. The
            # 2D grid and the 1D lists both respond to wheel-zoom
            # by changing self.cell_size, so this default sets
            # the initial look. The user can zoom out to 12 to
            # see more of a 50-element list, or zoom in to 50
            # for detail.
            self.cell_size = 22
            self.scroll_x = 0
            self.scroll_y = 0
            # Reset the variables-panel scroll too - the locals
            # of the first frame are typically much smaller than
            # the mid-replay state, so starting at the top-left
            # makes sense.
            self._vars_scroll_x = 0
            self._vars_scroll_y = 0
            return "Step mode: press Space, Enter, or Right Arrow." if self.manual_step else "Replay started"

        def toggle_pause() -> str:
            nonlocal paused, stopped
            if op_index >= len(ops):
                return "Replay complete. Press Replay to run again."
            paused = not paused
            stopped = False
            if self.manual_step and not paused:
                self.manual_step = False
                self.speed_label = "Custom"
                self.step_delay = max(self.step_delay, 0.30)
            return "Paused" if paused else "Playing"

        def toggle_step_mode() -> str:
            nonlocal paused
            self.manual_step = not self.manual_step
            paused = self.manual_step
            return "Step mode: press Space, Enter, or Right Arrow." if self.manual_step else "Automatic replay resumed"

        def stop_replay() -> str:
            nonlocal paused, stopped
            paused = True
            stopped = True
            return "Stopped at current step. Press Replay to restart or Play to continue."

        def change_speed(faster: bool) -> str:
            self.manual_step = False
            self.speed_label = "Custom"
            if faster:
                self.step_delay = max(0.01, self.step_delay * 0.75)
            else:
                self.step_delay = min(5.0, max(0.05, self.step_delay * 1.25))
            return f"Speed changed: {self.step_delay:.3f}s per op"

        def handle_control_action(action: str) -> str:
            nonlocal paused
            if action == "play_pause":
                return toggle_pause()
            if action == "next":
                detail = apply_next_operation()
                paused = True
                return detail
            if action == "replay":
                return reset_replay()
            if action == "mode":
                return toggle_step_mode()
            if action == "stop":
                return stop_replay()
            if action == "slower":
                return change_speed(False)
            if action == "faster":
                return change_speed(True)
            return current_detail

        # Listen for MOUSEWHEEL across pygame versions. Pygame 2.x has
        # pygame.MOUSEWHEEL; older versions split horizontal/vertical.
        mousewheel_event = getattr(pygame, "MOUSEWHEEL", None)
        old_mousewheel = (
            getattr(pygame, "MOUSEBUTTONDOWN", None)
            if mousewheel_event is None
            else None
        )

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif is_resize_event(pygame, event):
                    screen = pygame.display.get_surface() or screen
                    sync_window_size(self, screen)
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    action = self._control_action_at_pos(event.pos, paused, stopped, op_index, len(ops))
                    if action:
                        current_detail = handle_control_action(action)
                    else:
                        coord = self._coord_at_pos(event.pos, grid, visual_values)
                        if coord:
                            if coord in watchpoints:
                                watchpoints.remove(coord)
                                current_detail = f"Removed watchpoint {coord}"
                            else:
                                watchpoints.add(coord)
                                current_detail = f"Watching {coord}; replay pauses when an operation touches it."
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    # Right-click enters "pan" mode ONLY when the
                    # click was inside the Variables panel. The
                    # main grid is no longer drawn in the main
                    # area, so right-drag outside the variables
                    # panel is a no-op - panning and scrolling live
                    # there and only there. (Old behavior was to
                    # pan the algorithm grid; the user's directive
                    # was 'I need panning and scrolling function
                    # here and only here' - meaning the variables
                    # panel.)
                    self._right_panning = self._mouse_in_vars_panel(event.pos)
                    if self._right_panning:
                        self._pan_accum_x = 0.0
                        self._pan_accum_y = 0.0
                    try:
                        pygame.mouse.set_cursor(
                            pygame.SYSTEM_CURSOR_HAND if self._right_panning
                            else pygame.SYSTEM_CURSOR_ARROW
                        )
                    except (AttributeError, pygame.error):
                        pass
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                    self._right_panning = False
                    self._pan_accum_x = 0.0
                    self._pan_accum_y = 0.0
                    try:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    except (AttributeError, pygame.error):
                        pass
                elif event.type == pygame.MOUSEMOTION and self._right_panning:
                    # Pan the variables panel (both X and Y) with
                    # the inverted / grab-the-world convention:
                    # dragging right pulls the world right
                    # (scroll_x decreases), dragging down pulls
                    # the world down (scroll_y decreases), so the
                    # cells under the cursor stay under the
                    # finger. A float accumulator carries the
                    # sub-pixel motion between events so small
                    # drags feel smooth; _scroll_vars clamps to
                    # the content bounds.
                    rel_x, rel_y = event.rel
                    self._pan_accum_x += rel_x
                    self._pan_accum_y += rel_y
                    dx_pixels = -int(self._pan_accum_x // PAN_PIXELS_PER_CELL)
                    dy_pixels = -int(self._pan_accum_y // PAN_PIXELS_PER_CELL)
                    if dx_pixels or dy_pixels:
                        self._pan_accum_x += dx_pixels * PAN_PIXELS_PER_CELL
                        self._pan_accum_y += dy_pixels * PAN_PIXELS_PER_CELL
                        self._scroll_vars(dx_pixels, dy_pixels)
                elif mousewheel_event is not None and event.type == mousewheel_event:
                    # Mouse wheel: ZOOM the variables panel cell
                    # size when the cursor is over the panel.
                    # Outside the panel the wheel does nothing -
                    # panning (right-drag) and zooming (wheel)
                    # live there and only there. (User directive:
                    # 'zooming with mouse scroll should only work
                    # in variables panel'. Earlier the wheel did
                    # vertical scrolling of the variables list;
                    # that scrolling is now handled by right-drag
                    # panning, which covers both axes.)
                    wheel_y = getattr(event, "y", 0) or 0
                    if wheel_y and self._mouse_in_vars_panel(
                        getattr(event, "pos", None) or pygame.mouse.get_pos()
                    ):
                        current_detail = self.zoom_by(wheel_y * ZOOM_STEP)
                elif old_mousewheel is not None and event.type == pygame.MOUSEBUTTONDOWN and event.button in (4, 5):
                    # Fallback for pygame 1.x: button 4 = wheel up, 5 = wheel down.
                    if self._mouse_in_vars_panel(getattr(event, "pos", None) or pygame.mouse.get_pos()):
                        # Zoom the variables panel: button 4 = bigger cells, 5 = smaller.
                        current_detail = self.zoom_by(ZOOM_STEP if event.button == 4 else -ZOOM_STEP)
                    else:
                        # Outside the panel: no-op.
                        pass
                elif event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_ESCAPE, pygame.K_q):
                        running = False
                    # Arrow keys are now reserved for scrolling in all
                    # four directions. "Next operation" stays on
                    # Space and Enter; Right is no longer overloaded.
                    elif self.manual_step and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                        current_detail = apply_next_operation()
                        paused = True
                    elif event.key in (pygame.K_SPACE, pygame.K_p):
                        current_detail = toggle_pause()
                    elif event.key == pygame.K_m:
                        current_detail = toggle_step_mode()
                    elif event.key == pygame.K_s:
                        current_detail = stop_replay()
                    elif event.key == pygame.K_r:
                        current_detail = reset_replay()
                    # Speed control via +/-. The key code varies across
                    # layouts: US keyboards send K_EQUALS for shift+= (the
                    # main-row +), numpads send K_KP_PLUS, and some
                    # non-US layouts use different scancodes. We check
                    # both key codes and fall back to the unicode
                    # character so the binding works on every layout
                    # the player might have.
                    elif (
                        event.key in (pygame.K_PLUS, pygame.K_EQUALS, pygame.K_KP_PLUS)
                        or event.unicode == "+"
                    ):
                        current_detail = change_speed(True)
                    elif (
                        event.key in (pygame.K_MINUS, pygame.K_KP_MINUS)
                        or event.unicode == "-"
                    ):
                        current_detail = change_speed(False)
                    elif event.key in (pygame.K_PAGEUP,):
                        self.scroll_by(0, -PAGE_JUMP_SIZE, grid, visual_values)
                    elif event.key in (pygame.K_PAGEDOWN,):
                        self.scroll_by(0, PAGE_JUMP_SIZE, grid, visual_values)
                    elif event.key == pygame.K_HOME:
                        self.scroll_x = 0
                        self.scroll_y = 0
                    elif event.key == pygame.K_END:
                        _, _, max_x, max_y = self._visible_viewport(grid, visual_values)
                        self.scroll_x = max_x
                        self.scroll_y = max_y
                    # Single-step arrow scroll. Holding the key for
                    # continuous scroll is handled separately below by
                    # polling pygame.key.get_pressed() each frame; this
                    # branch covers the initial key press so the user
                    # sees a scroll right away without a perceptible
                    # delay.
                    elif event.key in (pygame.K_UP, pygame.K_w):
                        self.scroll_by(0, -1, grid, visual_values)
                    elif event.key == pygame.K_DOWN:
                        self.scroll_by(0, 1, grid, visual_values)
                    elif event.key == pygame.K_LEFT:
                        self.scroll_by(-1, 0, grid, visual_values)
                    elif event.key == pygame.K_RIGHT:
                        self.scroll_by(1, 0, grid, visual_values)

            # Continuous arrow-key scroll. Pygame's KEYDOWN auto-repeat
            # is OS-dependent and feels choppy, so we poll
            # pygame.key.get_pressed() each frame and scroll on a
            # fixed time interval. This makes the scroll smooth and
            # predictable, and works on every platform the same way.
            now = time.time()
            if now - last_key_scroll >= CONTINUOUS_SCROLL_INTERVAL:
                held = pygame.key.get_pressed()
                scrolled = False
                if held[pygame.K_UP] or held[pygame.K_w]:
                    self.scroll_by(0, -1, grid, visual_values)
                    scrolled = True
                if held[pygame.K_DOWN]:
                    self.scroll_by(0, 1, grid, visual_values)
                    scrolled = True
                if held[pygame.K_LEFT]:
                    self.scroll_by(-1, 0, grid, visual_values)
                    scrolled = True
                if held[pygame.K_RIGHT]:
                    self.scroll_by(1, 0, grid, visual_values)
                    scrolled = True
                if held[pygame.K_PAGEUP]:
                    self.scroll_by(0, -PAGE_JUMP_SIZE, grid, visual_values)
                    scrolled = True
                if held[pygame.K_PAGEDOWN]:
                    self.scroll_by(0, PAGE_JUMP_SIZE, grid, visual_values)
                    scrolled = True
                if scrolled:
                    last_key_scroll = now

            if not self.manual_step and not paused and not stopped and op_index < len(ops):
                trace_frame = self._trace_for_op(result.trace_frames, op_index)
                if self._source_breakpoint_hit(trace_frame, source_breakpoints_hit):
                    paused = True
                    current_detail = f"Source breakpoint line {trace_frame.line_no}: paused before next operation"

            if not self.manual_step and not paused and not stopped and op_index < len(ops) and now - last_step >= self.step_delay:
                current_detail = apply_next_operation()
                last_step = now

            if op_index > 0 and op_index <= len(ops):
                overlays = self._overlays_for_op(ops[op_index - 1], visual_values)
            else:
                overlays = {}

            trace_frame = self._trace_for_op(result.trace_frames, op_index)
            self._draw(screen, fonts, grid, visual_values, overlays, title, result, op_index, len(ops), current_detail, paused, trace_frame=trace_frame, stopped=stopped, watchpoints=watchpoints, last_op_detail=last_op_detail)
            pygame.display.flip()
            clock.tick(self.fps)

        pygame.quit()

    def _draw(self, screen, fonts, grid, values, overlays, title, result, op_index, total_ops, detail, paused, moving=None, trace_frame=None, stopped=False, watchpoints=None, last_op_detail=""):
        import pygame

        sync_window_size(self, screen)
        screen.fill(self.BACKGROUND)
        grid_rect, cell_size, full_cols, full_rows = self._grid_rect(grid, values)
        display_rows = self._display_rows(values)
        show_row_labels = full_rows > 1

        title_surface = fonts["title"].render(title, True, self.TEXT)
        screen.blit(title_surface, (self.margin, 18))

        # ----- Three-section main area: Description / Code / Variables -----
        #
        # Each section is its own rounded panel with a labelled header.
        # The Description panel sits at the top, the Code panel sits
        # under it, and the Variables panel takes the remaining
        # vertical space at the bottom. The user wanted all three to
        # be visually distinct (so you can tell at a glance where one
        # section ends and the next begins) and more breathing room
        # between the Validated line and the variables list - this
        # is now a hard 20px gap plus the panel border.
        main_x = self.margin
        main_w = self._main_area_width()
        y = 56  # below the title bar
        bottom = self.height - self.margin
        section_gap = 20  # extra space between Validated and Variables

        desc_bottom = self._draw_description_section(
            screen, fonts, main_x, y, main_w, bottom - y,
            result.description,
        )
        if desc_bottom > 0:
            y = desc_bottom + section_gap

        if trace_frame and trace_frame.locals:
            code_h = self._code_section_height(fonts, trace_frame)
            if y + code_h <= bottom:
                self._draw_code_section(
                    screen, fonts, main_x, y, main_w, code_h, trace_frame,
                )
                y += code_h + section_gap

        if trace_frame and trace_frame.locals:
            vars_h = bottom - y
            if vars_h >= 100:
                self._draw_variables_section(
                    screen, fonts, main_x, y, main_w, vars_h,
                    trace_frame, cell_size=cell_size,
                )

        self._draw_panel(
            screen, fonts, result, op_index, total_ops, detail, paused,
            trace_frame, stopped, len(watchpoints or ()),
            view_text=self._visible_range_text(grid, values),
            last_op_detail=last_op_detail,
        )

    def _draw_panel(self, screen, fonts, result, op_index, total_ops, detail, paused, trace_frame=None, stopped=False, watchpoint_count=0, view_text="", last_op_detail=""):
        import pygame

        x = self.width - self.panel_width - self.margin
        y = self.margin
        rect = pygame.Rect(x, y, self.panel_width, self.height - self.margin * 2)
        pygame.draw.rect(screen, self.PANEL, rect, border_radius=8)

        status_color = self.PASS if result.passed else self.FAIL
        status_text = "PASSED" if result.passed else "FAILED"
        self._draw_text(screen, fonts["title"], status_text, x + 18, y + 18, status_color)

        lines = [
            f"Ops: {result.stats.total}",
            f"Compare/Swap: {result.stats.comparisons}/{result.stats.swaps}",
            f"Read/Write: {result.stats.reads}/{result.stats.writes}",
            f"Complexity: {result.actual_complexity.value}",
            f"Required: {result.required_complexity.value}",
            f"n: {result.n}  Speed: {self._speed_display()}",
            f"Zoom: {self.zoom_label()}",
        ]
        if view_text:
            lines.append(view_text)
        lines.append(f"Watchpoints: {watchpoint_count}")
        text_y = y + 68
        for line in lines:
            self._draw_text(screen, fonts["small"], line, x + 18, text_y, self.TEXT)
            text_y += 22

        bar_x = x + 18
        bar_y = text_y + 12
        bar_w = self.panel_width - 36
        pygame.draw.rect(screen, (48, 55, 67), (bar_x, bar_y, bar_w, 12), border_radius=6)
        if total_ops:
            progress = min(1.0, op_index / total_ops)
            pygame.draw.rect(screen, self.READ, (bar_x, bar_y, int(bar_w * progress), 12), border_radius=6)

        text_y = bar_y + 34
        state = "Step" if self.manual_step else ("Stopped" if stopped else ("Paused" if paused else "Playing"))
        self._draw_text(screen, fonts["body"], f"{state}: {op_index}/{total_ops}", x + 18, text_y, self.TEXT)
        buttons = self._control_buttons(paused, stopped, op_index, total_ops)
        self._draw_controls(screen, fonts, buttons)
        # A short reminder of the scroll/zoom/speed shortcuts sits right
        # under the buttons so the user can find them without reading
        # docs. Wrap to the actual panel width (the 264px content area
        # is too narrow for the whole hint in one line, so we split
        # across two lines that fit).
        text_y = max((button.rect.bottom for button in buttons), default=text_y) + 12
        hint_w = self._wrap_width(fonts)
        for line in self._wrap("Right-drag/Arrows: pan | Wheel: zoom | +/-: speed", hint_w):
            self._draw_text(screen, fonts["small"], line, x + 18, text_y, self.MUTED)
            text_y += 18
        # Skip past the hint block before laying out the rest. The
        # bottom-of-buttons reference is no longer correct because the
        # hint can wrap to a second line on narrow fonts.
        text_y += 12
        footer_top = rect.bottom - 96
        content_bottom = footer_top - 14
        previous_clip = screen.get_clip()
        screen.set_clip(pygame.Rect(x, text_y, self.panel_width, max(0, content_bottom - text_y)))

        wrap_w = self._wrap_width(fonts)
        # The "Current op", source/validated line, and variables
        # panel have all moved to the main window (which now
        # shows them with the same visuals). The side panel
        # focuses on status, controls, return value, and the
        # final Passed/Complexity messages - the data
        # visualizations live in the main window now.

        return_text = result.return_value or "<not returned>"
        return_lines = self._wrap(return_text, wrap_w)[:2]
        return_height = 24 + len(return_lines) * 18
        return_start = max(text_y, content_bottom - return_height)

        text_y = return_start
        self._draw_text(screen, fonts["body"], "Return value", x + 18, text_y, self.TEXT)
        text_y += 24
        for line in return_lines:
            if text_y + 18 > content_bottom:
                break
            self._draw_text(screen, fonts["small"], line, x + 18, text_y, self.MUTED)
            text_y += 18
        screen.set_clip(previous_clip)

        message_lines = self._wrap(result.message, wrap_w)[:4]
        for index, line in enumerate(message_lines):
            self._draw_text(screen, fonts["small"], line, x + 18, footer_top + index * 20, status_color)

    def _control_buttons(self, paused: bool, stopped: bool, op_index: int, total_ops: int) -> list[ControlButton]:
        import pygame

        panel_x = self.width - self.panel_width - self.margin
        inner_x = panel_x + 18
        inner_width = self.panel_width - 36
        start_y = self.margin + 382
        gap = 8
        row_height = 32
        primary_width = (inner_width - 2 * gap) // 3
        secondary_width = (inner_width - 3 * gap) // 4
        has_next = op_index < total_ops

        play_label = "Play" if paused or stopped else "Pause"
        mode_label = "Auto" if self.manual_step else "Manual"
        buttons: list[ControlButton] = []

        primary_specs = [
            ("play_pause", play_label, has_next, not paused and not stopped),
            ("next", "Next", has_next, False),
            ("replay", "Replay", True, False),
        ]
        for index, (action, label, enabled, active) in enumerate(primary_specs):
            button_x = inner_x + index * (primary_width + gap)
            rect = pygame.Rect(button_x, start_y, primary_width, row_height)
            buttons.append(ControlButton(action, label, rect, enabled, active))

        secondary_specs = [
            ("mode", mode_label, True, self.manual_step),
            ("stop", "Stop", has_next and not stopped, stopped),
            ("slower", "Slower", True, False),
            ("faster", "Faster", True, False),
        ]
        second_y = start_y + row_height + gap
        for index, (action, label, enabled, active) in enumerate(secondary_specs):
            button_x = inner_x + index * (secondary_width + gap)
            rect = pygame.Rect(button_x, second_y, secondary_width, row_height)
            buttons.append(ControlButton(action, label, rect, enabled, active))

        # No third row. Zoom is mouse-wheel only.

        return buttons

    def _control_action_at_pos(self, pos, paused: bool, stopped: bool, op_index: int, total_ops: int) -> str:
        for button in self._control_buttons(paused, stopped, op_index, total_ops):
            if button.enabled and button.rect.collidepoint(pos):
                return button.action
        return ""

    def _draw_controls(self, screen, fonts, buttons: list[ControlButton]):
        import pygame

        for button in buttons:
            fill = self.READ if button.active else (44, 52, 64)
            border = self.TEXT if button.active else self.GRID_LINE
            text_color = self.TEXT
            if not button.enabled:
                fill = (36, 42, 51)
                border = (48, 55, 67)
                text_color = self.MUTED
            pygame.draw.rect(screen, fill, button.rect, border_radius=6)
            pygame.draw.rect(screen, border, button.rect, width=1, border_radius=6)
            self._draw_centered_text(screen, fonts["small"], button.label, button.rect, text_color)

    def _apply_operation(self, screen, clock, fonts, grid, values, op, op_index, total_ops, title, result) -> str:
        if op.op_type == OpType.SWAP:
            coords = self._extract_coords(op.detail)
            if len(coords) >= 2:
                self._animate_swap(screen, clock, fonts, grid, values, coords[0], coords[1], title, result, op_index, total_ops, op.detail)
                self._swap_values(values, coords[0], coords[1])
                return f"swap {op.detail}"
        elif op.op_type in (OpType.WRITE, OpType.READ):
            list_action = self._apply_list_mutation(values, op.detail)
            if list_action:
                return list_action

            coord = self._extract_single_coord(op.detail)
            new_value = self._extract_written_value(op.detail)
            if coord and new_value is not None:
                x, y = coord
                self._ensure_value_cell(values, x, y)
                values[y][x] = new_value
                return f"set {op.detail}"
        return f"{op.op_type.value}: {op.detail}"

    def _apply_list_mutation(self, values, detail: str) -> str:
        if not values:
            values.append([])

        append_match = re.search(r"list\.append\((.*)\)", detail)
        if append_match:
            value = append_match.group(1).strip()
            values[0].append(value)
            return f"append {value}"

        insert_match = re.search(r"list\.insert\((-?\d+),\s*(.*)\)", detail)
        if insert_match:
            index = int(insert_match.group(1))
            value = insert_match.group(2).strip()
            index = max(0, min(index, len(values[0])))
            values[0].insert(index, value)
            return f"insert {value} at index {index}"

        pop_match = re.search(r"list\.pop\((-?\d+)\)(?:\s*->\s*(.*))?", detail)
        if pop_match:
            index = int(pop_match.group(1))
            if index < 0:
                index = len(values[0]) + index
            if 0 <= index < len(values[0]):
                value = values[0].pop(index)
                reported = pop_match.group(2).strip() if pop_match.group(2) else value
                return f"pop index {index} -> {reported}"

        return ""

    def _animate_swap(self, screen, clock, fonts, grid, values, first, second, title, result, op_index, total_ops, detail):
        grid_rect, cell_size, _, _ = self._grid_rect(grid, values)
        # Animate from the current screen positions of the two cells so
        # the swap is visible even when the user has scrolled or zoomed.
        a_screen = self._screen_rect_for_source(grid_rect, cell_size, first)
        b_screen = self._screen_rect_for_source(grid_rect, cell_size, second)
        if a_screen is None or b_screen is None:
            return
        a_value = self._value_at(values, first)
        b_value = self._value_at(values, second)
        # Hide the cells in their original positions while the floating
        # copies travel between them.
        hidden = {first: self.SWAP, second: self.SWAP}

        for frame in range(self.swap_frames + 1):
            t = frame / self.swap_frames
            moving = [
                (a_value, a_screen.topleft, b_screen.topleft, t, self.SWAP),
                (b_value, b_screen.topleft, a_screen.topleft, t, self.SWAP),
            ]
            trace_frame = self._trace_for_op(result.trace_frames, op_index)
            self._draw(screen, fonts, grid, values, hidden, title, result, op_index, total_ops, f"swap: {detail}", False, moving, trace_frame=trace_frame)
            import pygame
            pygame.display.flip()
            clock.tick(self.fps)

    def _screen_rect_for_source(self, grid_rect, cell_size, source_coord):
        """Compute the on-screen rect for a source-grid cell, honoring
        the current scroll. Returns None if the cell is outside the
        viewport (the animation just won't show for that cell)."""
        import pygame
        sx, sy = source_coord
        screen_x = grid_rect.x + (sx - self.scroll_x) * cell_size
        screen_y = grid_rect.y + (sy - self.scroll_y) * cell_size
        if not (grid_rect.x <= screen_x < grid_rect.right and grid_rect.y <= screen_y < grid_rect.bottom):
            return None
        return pygame.Rect(screen_x, screen_y, cell_size - 2, cell_size - 2)

    def _choose_speed(self, screen, clock, fonts, title: str) -> bool:
        import pygame

        selected = DEFAULT_SPEED_INDEX
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if is_resize_event(pygame, event):
                    screen = pygame.display.get_surface() or screen
                    sync_window_size(self, screen)
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_ESCAPE, pygame.K_q):
                        return False
                    if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                        self.apply_speed(SPEED_PRESETS[selected].key)
                        return True
                    if event.key in (pygame.K_RIGHT, pygame.K_DOWN, pygame.K_d, pygame.K_s):
                        selected = (selected + 1) % len(SPEED_PRESETS)
                    elif event.key in (pygame.K_LEFT, pygame.K_UP, pygame.K_a, pygame.K_w):
                        selected = (selected - 1) % len(SPEED_PRESETS)
                    elif pygame.K_1 <= event.key <= pygame.K_8:
                        selected = event.key - pygame.K_1
                        if selected < len(SPEED_PRESETS):
                            self.apply_speed(SPEED_PRESETS[selected].key)
                            return True

            screen.fill(self.BACKGROUND)
            self._draw_text(screen, fonts["title"], title, self.margin, 34, self.TEXT)
            self._draw_text(screen, fonts["body"], "Choose replay speed", self.margin, 82, self.MUTED)

            card_width = 250
            card_height = 104
            gap = 16
            columns = 4
            total_width = columns * card_width + (columns - 1) * gap
            start_x = (self.width - total_width) // 2
            start_y = 170

            for index, preset in enumerate(SPEED_PRESETS):
                column = index % columns
                row = index // columns
                x = start_x + column * (card_width + gap)
                y = start_y + row * (card_height + gap)
                rect = pygame.Rect(x, y, card_width, card_height)
                color = self.READ if index == selected else self.PANEL
                pygame.draw.rect(screen, color, rect, border_radius=8)
                pygame.draw.rect(screen, self.GRID_LINE, rect, width=2, border_radius=8)
                self._draw_text(screen, fonts["title"], str(index + 1), x + 18, y + 16, self.TEXT)
                self._draw_text(screen, fonts["body"], preset.label, x + 52, y + 22, self.TEXT)
                if preset.manual_step:
                    delay_text = "waits for each key press"
                else:
                    delay_text = "as fast as possible" if preset.step_delay == 0 else f"{preset.step_delay:.3f}s / op"
                self._draw_text(screen, fonts["small"], delay_text, x + 18, y + 60, self.TEXT)
                self._draw_text(screen, fonts["small"], f"swap frames: {preset.swap_frames}", x + 18, y + 82, self.MUTED)

            instructions = [
                "Left/Right or Up/Down: select",
                "1-8: choose immediately",
                "Enter/Space: start replay",
                "Esc/Q: cancel",
            ]
            text_y = 440
            for line in instructions:
                self._draw_text(screen, fonts["body"], line, self.margin, text_y, self.TEXT)
                text_y += 32

            pygame.display.flip()
            clock.tick(self.fps)

    def _grid_rect(self, grid, values=None):
        """Return (viewport_rect, cell_size, full_cols, full_rows).

        The viewport rect describes the slice of the screen that the grid
        currently occupies, not the full grid. Cells outside the viewport
        are not drawn (the draw step uses the viewport as a clip). The
        (full_cols, full_rows) pair lets the draw function know how big
        the source grid is when computing scroll math.
        """
        import pygame

        if values is None:
            values = self._values_from_grid(grid)
        display_rows = self._display_rows(values) if values else [[]]
        label_width = self._row_label_width(display_rows)
        full_cols = max((len(row) for row in display_rows), default=0)
        full_rows = len(display_rows)
        cell_size = self._effective_cell_size(grid, values)

        # The viewport occupies the area to the left of the side panel,
        # with the title/description bands above it. There is no need to
        # center the viewport vertically when the grid is taller than
        # the available space; the user can scroll instead.
        x = self.margin + label_width
        grid_top = self._grid_top()
        available_w = max(0, self._main_area_width() - label_width)
        available_h = max(0, self.height - grid_top - self.margin)
        viewport_w = min(available_w, cell_size * max(full_cols, 1))
        viewport_h = min(available_h, cell_size * max(full_rows, 1))
        return pygame.Rect(x, grid_top, viewport_w, viewport_h), cell_size, full_cols, full_rows

    def _main_area_width(self) -> int:
        return max(240, self.width - self.panel_width - self.margin * 3)

    def _description_lines(self, description: str) -> list[str]:
        if not description:
            return []
        width_chars = max(36, self._main_area_width() // 9)
        return self._wrap(description.replace("\n", " "), width_chars)[:3]

    def _description_height(self, description: str | None = None) -> int:
        description = self._current_description if description is None else description
        lines = self._description_lines(description)
        if not lines:
            return 0
        return 30 + len(lines) * 18 + 18

    def _grid_top(self) -> int:
        return 70 + self._description_height()

    def _draw_main_description(self, screen, fonts, description: str):
        # Kept as a thin shim so any out-of-tree callers still work;
        # the new 3-section layout uses ``_draw_description_section``
        # instead. Returns the y position after the panel (or 0 if
        # there was no description to draw).
        return self._draw_description_section(
            screen, fonts, self.margin, 56,
            self._main_area_width(), 600, description,
        )

    # --- Section panel helpers ------------------------------------------
    #
    # The main area is split into three rounded panels with a
    # labelled header each: Description, Code, Variables. Each
    # helper draws the panel background + border + title, then
    # returns the y position the next section can start at. The
    # content drawers are separate so the caller can compute the
    # section height up front (the Variables section needs to know
    # how much space the panel has so it can truncate variables that
    # don't fit).

    def _draw_description_section(
        self,
        screen,
        fonts,
        x: int,
        y: int,
        max_width: int,
        max_height: int,
        description: str,
    ) -> int:
        """Draw the Description section panel. Returns the y position
        just below the panel (0 if the description is empty).
        """
        if not description:
            return 0
        import pygame

        lines = self._description_lines(description)
        if not lines:
            return 0

        panel_pad = 12
        title_h = 28
        line_h = 18
        content_h = len(lines) * line_h
        # Top padding (under title), bottom padding (under text)
        inner_h = 6 + content_h + 6
        panel_h = title_h + inner_h
        if panel_h > max_height:
            panel_h = max_height

        panel_rect = pygame.Rect(x, y, max_width, panel_h)
        pygame.draw.rect(screen, self.PANEL, panel_rect, border_radius=8)
        pygame.draw.rect(screen, self.GRID_LINE, panel_rect, width=1, border_radius=8)

        # Title at the top of the panel.
        self._draw_text(screen, fonts["body"], "Description", x + panel_pad, y + 5, self.TEXT)
        # Horizontal separator under the title.
        sep_y = y + title_h
        pygame.draw.line(
            screen, self.GRID_LINE,
            (x + 1, sep_y), (x + max_width - 1, sep_y),
            1,
        )
        # Body text.
        content_y = sep_y + 6
        for line in lines:
            if content_y + line_h > y + panel_h:
                break
            self._draw_text(screen, fonts["small"], line, x + panel_pad, content_y, self.MUTED)
            content_y += line_h
        return y + panel_h

    def _code_section_height(self, fonts, trace_frame) -> int:
        """Height of the Code section panel. The content is fixed:
        ``Line N`` + code line + Validated line.
        """
        title_h = 28
        line_h = 18
        # 1 line for "Line N", 1 for the code, 1 for the validated.
        content_lines = 3
        inner_h = 8 + content_lines * line_h + 6
        return title_h + inner_h

    def _draw_code_section(
        self,
        screen,
        fonts,
        x: int,
        y: int,
        max_width: int,
        panel_h: int,
        trace_frame,
    ) -> None:
        """Draw the Code section panel: title, Line N, source line,
        and the Validated line.
        """
        import pygame

        panel_pad = 12
        title_h = 28

        panel_rect = pygame.Rect(x, y, max_width, panel_h)
        pygame.draw.rect(screen, self.PANEL, panel_rect, border_radius=8)
        pygame.draw.rect(screen, self.GRID_LINE, panel_rect, width=1, border_radius=8)

        # Title.
        self._draw_text(screen, fonts["body"], "Code", x + panel_pad, y + 5, self.TEXT)
        # Separator under the title.
        sep_y = y + title_h
        pygame.draw.line(
            screen, self.GRID_LINE,
            (x + 1, sep_y), (x + max_width - 1, sep_y),
            1,
        )
        # Content.
        content_y = sep_y + 8
        prefix = "Breakpoint line" if trace_frame.breakpoint else "Line"
        self._draw_text(
            screen, fonts["small"],
            f"{prefix} {trace_frame.line_no}",
            x + panel_pad, content_y, self.MUTED,
        )
        content_y += 18
        code_line, _ = self._format_source_line(trace_frame)
        if code_line:
            self._draw_text(
                screen, fonts["small"],
                f"  {code_line}", x + panel_pad, content_y, self.MUTED,
            )
            content_y += 18
        _, validated_line = self._format_source_line(trace_frame)
        if validated_line:
            self._draw_text(
                screen, fonts["small"],
                validated_line, x + panel_pad, content_y, self.ACCENT_COLOR,
            )

    def _draw_variables_section(
        self,
        screen,
        fonts,
        x: int,
        y: int,
        max_width: int,
        panel_h: int,
        trace_frame,
        cell_size: int = 18,
    ) -> None:
        """Draw the Variables section panel: title, then one entry per
        local variable rendered with the matching data-structure
        visual. Supports:

          * list / tuple / TrackedList        - row of cells, per-cell index
          * dict                              - 2-row key/value strip
          * set / TrackedSet                  - row of cells, no index
          * TrackedGrid                       - 2D grid (the actual maze)
          * TrackedQueue                      - horizontal strip w/ front→ arrow
          * TrackedStack                      - vertical strip w/ top→ arrow
          * list / set of (row, col) tuples  - 2D overlay
          * scalar                            - single cell

        The panel is scrollable: a 35x35 TrackedGrid plus a visited
        set is much taller than the available main-area height, so
        we render with a vertical offset and let the wheel scroll
        it when the mouse is over the panel. ``self._vars_scroll_y``
        is the offset, ``self._vars_content_height`` is the total
        rendered height of all variables (set by this function), and
        ``self._vars_view_height`` is the visible portion (panel
        height minus title + padding). The wheel handler clamps
        ``_vars_scroll_y`` so it can't scroll past either edge.
        """
        import pygame

        # Record the panel rect for the wheel handler. The play()
        # loop checks if the mouse is inside this rect to decide
        # whether the wheel scrolls the variables or zooms the main
        # algorithm grid.
        self._vars_panel_rect = (x, y, max_width, panel_h)

        panel_pad = 12
        title_h = 28
        content_x = x + panel_pad
        content_w = max_width - panel_pad * 2

        panel_rect = pygame.Rect(x, y, max_width, panel_h)
        pygame.draw.rect(screen, self.PANEL, panel_rect, border_radius=8)
        pygame.draw.rect(screen, self.GRID_LINE, panel_rect, width=1, border_radius=8)

        # Title.
        self._draw_text(screen, fonts["body"], "Variables", x + panel_pad, y + 5, self.TEXT)
        # Separator.
        sep_y = y + title_h
        pygame.draw.line(
            screen, self.GRID_LINE,
            (x + 1, sep_y), (x + max_width - 1, sep_y),
            1,
        )

        content_top = sep_y + 8
        content_bottom = y + panel_h - 8
        # Reserve a thin strip at the very bottom of the panel
        # for the horizontal scroll bar. The vertical bar lives
        # on the right edge.
        scrollbar_h = 6
        self._vars_view_height = max(0, content_bottom - content_top - scrollbar_h)
        self._vars_view_width = max(0, content_w)
        if self._vars_view_height <= 0:
            return

        if not trace_frame or not trace_frame.locals:
            return

        # Pre-classify each variable into a (kind, payload) pair and
        # compute its rendered height. The actual draw step is a
        # second pass so the scroll math stays simple: total
        # height -> max_scroll = max(0, total - view) -> clamp
        # _vars_scroll_y -> walk again, skipping rows outside the
        # visible window.
        items: list[tuple[str, str, Any, int]] = []
        max_content_width = 0
        between_vars = 26  # generous gap so cells don't feel cramped
        for name, value in trace_frame.locals.items():
            # Skip class / function / module objects in the locals
            # list. These are almost always function-level imports
            # the player wrote (``from code_n.tracked import
            # TrackedQueue`` makes ``TrackedQueue`` a local binding
            # for the class itself, not an instance). Drawing them
            # as scalars produced the ``<class '...'>`` text the
            # user saw in the BFS screenshot, which is just noise
            # — the class is implicit in the variables that USE it.
            if isinstance(value, (type, types.FunctionType, types.ModuleType)):
                continue
            kind, payload, h = self._classify_variable(
                value, content_w, cell_size,
            )
            # Hide empty collections. The user complained that
            # 'frontier is not there' at the start of BFS and
            # neither is 'visited' - both are initialized to
            # empty (TrackedQueue() and set()) in the canonical
            # solution, so they show up in trace_frame.locals
            # on frame 0 but contain nothing. Showing them as
            # '(empty)' is noise; the variable just appears in
            # the panel once something is enqueued / added. The
            # same rule applies to TrackedStack: an empty stack
            # doesn't render. Scalars (0, None, etc.) are
            # always shown - those are real values, not 'empty'.
            if kind == "empty":
                continue
            w = self._estimate_variable_width(
                value, content_w, cell_size,
            )
            max_content_width = max(max_content_width, w)
            total_h = h + between_vars
            items.append((name, kind, payload, total_h))

        # Total content height = sum of all variable blocks (we
        # always render every variable; the scroll is what keeps
        # the overflow out of the visible area). Subtract the
        # trailing between_vars since the last block doesn't need
        # bottom padding.
        if items:
            self._vars_content_height = sum(b[3] for b in items) - between_vars
        else:
            self._vars_content_height = 0
        self._vars_content_width = max_content_width

        # Clamp the scroll offsets now that we know the content
        # dimensions (both can grow as new variables appear
        # mid-replay).
        max_scroll_x = max(0, self._vars_content_width - self._vars_view_width)
        max_scroll_y = max(0, self._vars_content_height - self._vars_view_height)
        if self._vars_scroll_x > max_scroll_x:
            self._vars_scroll_x = max_scroll_x
        if self._vars_scroll_y > max_scroll_y:
            self._vars_scroll_y = max_scroll_y

        # Clip subsequent draws to the panel content area so a
        # variable that strays past the bottom / right doesn't
        # paint over the side panel.
        previous_clip = screen.get_clip()
        screen.set_clip(pygame.Rect(
            x + 1, content_top,
            max_width - 2, self._vars_view_height,
        ))

        # Second pass: walk the items, skipping rows that fall
        # outside the visible window after the scroll offset.
        # No horizontal separator lines between variables - they
        # were drawn at ``cur_y - between_vars // 2`` and ended
        # up touching the cells of the previous variable when
        # that variable was short (a single-cell scalar left the
        # line overlapping the cell border). The generous
        # ``between_vars`` gap alone separates the variables
        # visually.
        cur_y = content_top - self._vars_scroll_y
        cur_x = content_x - self._vars_scroll_x
        for index, (name, kind, payload, total_h) in enumerate(items):
            # Skip rows that are entirely above the visible area.
            if cur_y + total_h <= content_top:
                cur_y += total_h
                continue
            # The cell for this variable starts ``LABEL_OFFSET = 22``
            # pixels below the label (``{name}:`` line). The old
            # break only checked the label's top - so a variable
            # whose label fit but whose cell didn't (e.g. ``nc:``
            # at the very bottom of the panel) drew the label and
            # clipped the cell silently. The user couldn't scroll
            # further to see it because no scrollbar hint was
            # given either - the value just disappeared. We now
            # bail out as soon as the cell's top would land
            # below the panel.
            label_offset = 22
            if cur_y + label_offset >= content_bottom:
                break

            # Variable name on its own line.
            self._draw_text(
                screen, fonts["body"], f"{name}:", cur_x, cur_y, self.TEXT,
            )
            self._draw_variable_visual(
                screen, fonts,
                cur_x, cur_y + label_offset,
                content_w,
                kind, payload, name,
                cell_size=cell_size,
            )
            cur_y += total_h

        screen.set_clip(previous_clip)

        # Vertical scroll indicator: a small bar on the right edge
        # of the panel showing how much of the content is visible.
        # Only drawn when the content actually overflows.
        if self._vars_content_height > self._vars_view_height:
            track_x = x + max_width - 6
            track_y = content_top
            track_h = self._vars_view_height
            thumb_h = max(20, int(
                track_h * self._vars_view_height / max(1, self._vars_content_height),
            ))
            thumb_y = track_y + int(
                (track_h - thumb_h) * self._vars_scroll_y
                / max(1, self._vars_content_height - self._vars_view_height),
            )
            pygame.draw.rect(
                screen, self.GRID_LINE,
                pygame.Rect(track_x, track_y, 4, track_h),
                border_radius=2,
            )
            pygame.draw.rect(
                screen, self.READ,
                pygame.Rect(track_x, thumb_y, 4, thumb_h),
                border_radius=2,
            )

        # Horizontal scroll indicator: a small bar along the
        # bottom of the panel. Only drawn when the content
        # overflows horizontally.
        if self._vars_content_width > self._vars_view_width:
            track_x = content_x
            track_y = content_bottom - scrollbar_h + 1
            track_w = self._vars_view_width
            thumb_w = max(20, int(
                track_w * self._vars_view_width / max(1, self._vars_content_width),
            ))
            thumb_x = track_x + int(
                (track_w - thumb_w) * self._vars_scroll_x
                / max(1, self._vars_content_width - self._vars_view_width),
            )
            pygame.draw.rect(
                screen, self.GRID_LINE,
                pygame.Rect(track_x, track_y, track_w, 4),
                border_radius=2,
            )
            pygame.draw.rect(
                screen, self.READ,
                pygame.Rect(thumb_x, track_y, thumb_w, 4),
                border_radius=2,
            )

    def _estimate_variable_width(
        self, value, content_w: int, cell_size: int,
    ) -> int:
        """Rough width estimate in pixels for one variable. Used
        by ``_draw_variables_section`` to compute the horizontal
        scroll bounds. Doesn't have to be exact - overestimating
        is harmless (the user can scroll into empty space) and
        underestimating only means they can't reach the last
        few pixels.

        For collections it's ``len * (cell + gap)``. For a 2D
        list of lists we add a left margin for the row labels
        (``label_w = max(20, int(cell * 1.2))``) so the user
        can read the row index on the left of each row.
        """
        cell_gap = 1
        # 2D list of lists: width = label_w + cols * (cell + gap).
        if isinstance(value, list) and value and all(
            isinstance(item, list) for item in value
        ):
            cols = max((len(row) for row in value), default=0)
            cell_2d = min(24, max(8, content_w // max(1, cols)))
            label_w = max(20, int(cell_2d * 1.2))
            return label_w + cols * (cell_2d + cell_gap)
        # Standard collections + tracked wrappers: use __len__.
        try:
            n = len(value)
        except TypeError:
            return cell_size + cell_gap
        return n * (cell_size + cell_gap)

    def _classify_variable(self, value, content_w: int, cell_size: int) -> tuple[str, Any, int]:
        """Return (kind, payload, height_px) for a local variable.

        ``kind`` is one of: "list2d", "list", "tuple", "dict",
        "set", "scalar", "empty", "unknown". ``payload`` is
        whatever the corresponding draw helper expects.
        ``height_px`` is the vertical space the rendering will
        consume (not including the per-variable between-vars
        padding).

        All the engine's tracked wrappers (TrackedList /
        TrackedGrid) are unwrapped to their underlying Python
        types. A TrackedGrid is a list of lists, which the
        renderer detects as the "list2d" kind and draws as a
        real 2D grid (one row per inner list, one cell per
        element). TrackedQueue / TrackedStack / TrackedSet
        are gone from the engine - the player brings their
        own (collections.deque, plain list, plain set), and
        those are handled by the standard list / set paths.
        'display a 2 dimensional list as 2 dimensions ... You
        should generalize it, but somehow keep it smart.' The
        auto-sized cell keeps a 5x5 readable and a 35x35
        compact.

        The "set2d" 2D overlay for sets of ``(int, int)``
        tuples (formerly used for BFS's ``visited`` set) is
        removed. The user: 'Why visited looks like that?
        Visited does not look like a real variable.' So
        visited now renders as a plain set of 2-tuples,
        each tuple drawn as a multi-line cell (one value per
        line) - the 'single big field ()' the user asked
        for, where the cell height matches the tuple length.
        """
        try:
            from code_n.tracked import TrackedGrid, TrackedList
        except ImportError:
            TrackedGrid = TrackedList = None  # noqa

        # Unwrap all tracked wrappers to plain Python types.
        if TrackedList is not None and isinstance(value, TrackedList):
            value = list(value.raw)
        if TrackedGrid is not None and isinstance(value, TrackedGrid):
            value = value.raw  # list of lists

        # 2D list of lists - a real 2D grid. Detected by checking
        # that every element is itself a list. Mixed types
        # (e.g. ``[1, [2, 3], 4]``) fall through to the 1D
        # list path instead.
        if isinstance(value, list) and value and all(
            isinstance(item, list) for item in value
        ):
            rows = len(value)
            cols = max((len(row) for row in value), default=0)
            # Zoomable: the 2D grid's cell size follows the
            # current wheel-zoom (``self.cell_size`` is
            # passed in as ``cell_size`` here), capped so a
            # wide grid still fits the panel width. So:
            #   - wheel-zoom in (cell_size=40) for a 5x5:
            #     cell_2d = 24 (capped at the readability max)
            #   - wheel-zoom in (cell_size=40) for a 35x35:
            #     cell_2d = min(40, 700/35=20) = 20 (capped at
            #     the panel-fitting max)
            #   - wheel-zoom out (cell_size=14) for a 35x35:
            #     cell_2d = 14 (below the panel-fitting max,
            #     the user wants to see more of the grid)
            # The user asked: 'why is the 2d grid not zoomable?'.
            cell_2d = min(cell_size, max(8, content_w // max(1, cols)), 24)
            cell_gap = 1
            # The column-header row is the SAME cell size as
            # the data cells (the user: 'have the same cell
            # size as the cells themselves'). The row labels
            # to the left are ``label_w`` wide and the same
            # cell height, so they're vertically aligned with
            # the data row.
            height = cell_2d + rows * (cell_2d + cell_gap) + 4
            return "list2d", (value, cell_2d), height

        # Standard collections. Each one is drawn as a single
        # row (or two rows for dicts: keys on top, values below)
        # regardless of length. If the collection is longer
        # than the panel width, the trailing cells are clipped
        # by the panel's set_clip() rect, and the user can
        # either wheel-zoom out to shrink the cells or accept
        # the clip.
        if isinstance(value, (list, tuple)) and value:
            items = list(value)
            # Height matches the tallest cell: scalars are
            # one cell tall, tuple / list elements are N cells
            # tall (one per sub-value). The strip is drawn
            # with all cells aligned to the same y, and taller
            # cells extend further down. The column-header
            # strip on top is the SAME size as a data cell
            # (the user: 'have the same cell size as the
            # cells themselves'), so the panel reserves
            # ``cell_size`` for it. The 'no cap' policy (the
            # user complained that the previous 20-cell cap
            # was cutting the variable at the bottom) means
            # all items are shown - the user scrolls
            # vertically to see the rest.
            max_h = cell_size
            for item in items:
                if isinstance(item, (tuple, list)):
                    max_h = max(max_h, len(item) * cell_size)
            return "list", (items, cell_size), cell_size + max_h + 2
        if isinstance(value, dict) and value:
            return "dict", (list(value.items()), cell_size), 2 * (cell_size + 2)
        if isinstance(value, set) and value:
            items = list(value)
            max_h = cell_size
            for item in items:
                if isinstance(item, (tuple, list)):
                    max_h = max(max_h, len(item) * cell_size)
            return "set", (items, cell_size), cell_size + max_h + 2
        if isinstance(value, (list, tuple, dict, set)):
            # Empty collection: still allocate one row of cells so
            # the player can see the variable is present.
            return "empty", None, cell_size + 2

        # Scalar (or anything we don't recognize).
        return "scalar", value, cell_size + 2

    def _draw_variable_visual(
        self,
        screen,
        fonts,
        x: int,
        y: int,
        max_width: int,
        kind: str,
        payload,
        var_name: str,
        cell_size: int = 18,
    ) -> None:
        """Render a classified variable. The classification was done
        by ``_classify_variable``; this method just dispatches.
        TrackedGrid / TrackedQueue / TrackedStack are no longer
        special-cased here - the classifier unwraps them to
        plain lists and the standard list / dict / set renderers
        handle them. ``list2d`` is a list of lists (2D grid).
        """
        if kind == "list2d":
            data, cell_2d = payload
            self._draw_2d_list(
                screen, fonts, x, y, data, cell_2d,
                var_name=var_name,
            )
        elif kind == "list":
            items, grid_cell = payload
            self._draw_flat_strip(
                screen, fonts, x, y, items, grid_cell,
                var_name=var_name,
            )
        elif kind == "tuple":
            items, grid_cell = payload
            self._draw_flat_strip(
                screen, fonts, x, y, items, grid_cell,
                var_name=var_name,
            )
        elif kind == "dict":
            items, grid_cell = payload
            self._draw_dict_strip(
                screen, fonts, x, y, items, grid_cell,
                var_name=var_name,
            )
        elif kind == "set":
            items, grid_cell = payload
            self._draw_set_strip(
                screen, fonts, x, y, items, grid_cell,
                var_name=var_name,
            )
        else:  # "scalar" or anything else
            self._draw_scalar_cell(
                screen, fonts, x, y, cell_size, payload, var_name,
            )

    def _draw_2d_grid(
        self,
        screen,
        x: int,
        y: int,
        raw: list[list],
        cell_size: int = 12,
        label_kind: str = "walkable",
    ) -> None:
        """Render a 2D data grid (TrackedGrid raw data) as a compact
        block of cells. ``label_kind`` controls the cell palette:

          * "walkable" - 0 = dark/walkable, 1 = light/wall.
            Matches the BFS / DFS maze layout (0 = open, 1 = wall).
        """
        import pygame
        cell_gap = 1
        # 0 = walkable (use empty cell color), 1 = wall (use WALL color).
        walkable_bg = (34, 39, 48)
        wall_bg = self.WALL if hasattr(self, "WALL") else (10, 12, 16)
        for r, row in enumerate(raw):
            for c, value in enumerate(row):
                rect = pygame.Rect(
                    x + c * (cell_size + cell_gap),
                    y + r * (cell_size + cell_gap),
                    cell_size, cell_size,
                )
                bg = wall_bg if value == 1 else walkable_bg
                pygame.draw.rect(screen, bg, rect, border_radius=1)
                pygame.draw.rect(screen, self.GRID_LINE, rect, width=1, border_radius=1)
                # Show the value if there's room.
                if cell_size >= 14:
                    label = "1" if value else "0"
                    f = fonts["small"] if cell_size < 18 else fonts["cell"]
                    text_surface = f.render(label, True, self.MUTED)
                    screen.blit(text_surface, text_surface.get_rect(center=rect.center))

    def _draw_2d_overlay(
        self,
        screen,
        x: int,
        y: int,
        rows: int,
        cols: int,
        value_set,
        cell_size: int = 12,
    ) -> None:
        """Render a set / list of (row, col) tuples as a 2D grid
        where cells in the set are highlighted. ``rows`` and
        ``cols`` are the grid dimensions (inferred from the data
        by ``_classify_variable``).
        """
        import pygame
        cell_gap = 1
        empty_bg = (44, 52, 64)
        marked_bg = self.READ
        for r in range(rows):
            for c in range(cols):
                rect = pygame.Rect(
                    x + c * (cell_size + cell_gap),
                    y + r * (cell_size + cell_gap),
                    cell_size, cell_size,
                )
                bg = marked_bg if (r, c) in value_set else empty_bg
                pygame.draw.rect(screen, bg, rect, border_radius=1)
                pygame.draw.rect(screen, self.GRID_LINE, rect, width=1, border_radius=1)

    def _draw_strip_with_label(
        self,
        screen,
        fonts,
        x: int,
        y: int,
        items: list,
        cell_size: int,
        label: str = "front→",
        var_name: Optional[str] = None,
    ) -> None:
        """Draw a queue / stack as a *vertical* list of rows. Each
        element gets one row. If the element is a tuple, its
        sub-values each get their own cell in the row (so a
        BFS ``frontier`` of ``(row, col, distance)`` triples
        shows as 3 cells per row, all clearly readable). The
        label sits at the top indicating which end is the
        operational one ("front" for queue, "top" for stack -
        the next dequeue / pop is the first element).

        Layout: one element per row, growing downward. With the
        scrollable variables panel this lets the user see the
        whole queue without anything getting truncated.
        """
        import pygame
        if not items:
            self._draw_text(screen, fonts["small"], "(empty)", x, y + cell_size // 2 - 8, self.MUTED)
            return
        cell_gap = 1
        # Label at the very top of the strip pointing AT the
        # first element (which is the front of the queue or
        # the top of the stack). For "front→" (queue) the
        # first element is the next to be dequeued, so the
        # arrow points down at it. Same for "top→" (stack).
        self._draw_text(screen, fonts["small"], f"{label} ↓", x, y, self.MUTED)
        row_y = y + 20
        for index, item in enumerate(items):
            if isinstance(item, (tuple, list)):
                # Tuple / list element: each sub-value gets its
                # own cell, drawn left to right.
                for j, sub in enumerate(item):
                    cx = x + j * (cell_size + cell_gap)
                    self._draw_one_cell(
                        screen, fonts, cx, row_y, cell_size, sub,
                        touched_key=(var_name, index) if var_name else None,
                    )
            else:
                # Scalar element: single cell.
                self._draw_one_cell(
                    screen, fonts, x, row_y, cell_size, item,
                    touched_key=(var_name, index) if var_name else None,
                )
            row_y += cell_size + cell_gap + 4  # small gap between rows

    def _draw_flat_strip(
        self,
        screen,
        fonts,
        x: int,
        y: int,
        items: list,
        cell_size: int,
        var_name: Optional[str] = None,
    ) -> None:
        """Render a list / tuple as ONE row of cells with a
        column-header row above showing each element's index.

        No wrapping - a 50-element list is 50 cells in a single
        horizontal line. Cells past the panel's right edge are
        clipped by the panel's set_clip() rect; the user can
        wheel-zoom out to shrink the cell size, or just accept
        the clip. The user explicitly asked for this: "1 list
        should be just in 1 row, not wrapped".

        All cells are the same width (``cell_size``). Tuple
        and list elements get a taller cell - one cell-size
        per sub-value - so the values stack vertically. The
        row height is the tallest cell's height, and shorter
        cells just have empty space below them. This is the
        "organize the cells always to match the content size"
        the user asked for, and the "1 value per line" rendering
        for tuples.

        The column header is the SAME cell size as a data
        cell (the user: 'have the same cell size as the cells
        themselves'). So a column header for index 5 is just
        a square cell with '5' in the middle, same width and
        height as the data cell at index 5. The data cells
        start one full cell below the header row.

        No cap: every element is drawn. The user complained
        that the previous 20-element cap was 'cutting the
        variable at the bottom' - the panel scrolls
        vertically now, so the user can see the rest. For
        very long lists the user can also wheel-zoom out to
        shrink the cell size.
        """
        import pygame
        if not items:
            self._draw_text(screen, fonts["small"], "(empty)", x, y, self.MUTED)
            return
        cell_gap = 1
        # Column headers on top: the index of each element,
        # same cell size as the data cells. The user: 'have
        # the same cell size as the cells themselves'.
        for index in range(len(items)):
            self._draw_index_header_cell(
                screen, fonts,
                x + index * (cell_size + cell_gap),
                y, cell_size, str(index),
            )
        # Cells, drawn one cell-size below the header row.
        cx = x
        cell_y = y + cell_size
        for index, item in enumerate(items):
            self._draw_one_cell(
                screen, fonts, cx, cell_y, cell_size, item,
                touched_key=(var_name, index) if var_name else None,
            )
            cx += cell_size + cell_gap

    def _draw_2d_list(
        self,
        screen,
        fonts,
        x: int,
        y: int,
        data: list,
        cell_size: int,
        var_name: Optional[str] = None,
    ) -> None:
        """Render a list of lists as a real 2D grid with
        column headers on top and row labels on the left.

        Layout: cells are at ``(x + label_w + c * cell, y + header_h + r * cell)``.
        Column header ``c`` sits at ``(x + label_w + c * cell, y)``.
        Row label ``r`` sits at ``(x, y + header_h + r * cell)``.
        The corner where the row label column and the column
        header row meet is left blank.

        The user asked for this:
          - 'it is a 2d index not just an incremental number' -
            the headers show the actual (r, c) coordinates
            instead of a linear ``0, 1, 2, ...`` per-cell label.
          - 'have it on top or at the left side of the element,
            not in each cell' - headers go above the cells and
            row labels go to the left; the per-cell label in
            the top-left corner is gone.
        """
        import pygame
        if not data:
            self._draw_text(screen, fonts["small"], "(empty)", x, y, self.MUTED)
            return
        cell_gap = 1
        # Pad the row lengths so all rows align. The 2D list
        # may be ragged (e.g. ``[[1, 2, 3], [4, 5]]``); we
        # still draw a 3-wide grid with the missing cell left
        # blank rather than collapsing the whole grid.
        cols = max((len(row) for row in data), default=0)
        rows = len(data)
        # Margins for the headers / row labels.
        header_h = 14
        label_w = max(20, int(cell_size * 1.2))
        # Column headers on top, each the same cell size as the
        # data cells. The user: 'have the same cell size as
        # the cells themselves' - a column header is itself
        # a square cell, just with a number label.
        for c in range(cols):
            self._draw_index_header_cell(
                screen, fonts, x + label_w + c * (cell_size + cell_gap),
                y, cell_size, str(c),
            )
        # Cells.
        for r, row in enumerate(data):
            # Row label on the left of this row. The label is
            # ``label_w`` wide (a thin column on the left)
            # and ``cell_size`` tall (the same height as the
            # data cells in this row), so it sits flush with
            # the row.
            self._draw_index_header_cell(
                screen, fonts, x, y + cell_size + r * (cell_size + cell_gap),
                cell_size, str(r), width=label_w,
            )
            for c in range(cols):
                if c >= len(row):
                    continue  # leave the cell blank (ragged row)
                value = row[c]
                cx = x + label_w + c * (cell_size + cell_gap)
                # The data cells start one full cell below the
                # column header row, so they're not on top of
                # the header cells. (The column header and the
                # data cell are the same cell size, so this is
                # exactly one row's worth of vertical offset.)
                cy = y + cell_size + r * (cell_size + cell_gap)
                # The (r, c) tuple is the touched-cell key. The
                # cell itself doesn't show an index (per the
                # earlier directive) - the header row + column
                # carries the index.
                self._draw_one_cell(
                    screen, fonts, cx, cy, cell_size, value,
                    touched_key=(var_name, (r, c)) if var_name else None,
                )

    def _draw_index_header_cell(
        self,
        screen,
        fonts,
        x: int,
        y: int,
        cell_size: int,
        label: str,
        width: Optional[int] = None,
        height: Optional[int] = None,
    ) -> None:
        """Draw a small header cell holding a single index
        label. Used for the column-headers-on-top and
        row-labels-on-the-left of a 2D grid, and for the
        column-headers-on-top of a 1D list.

        ``width`` overrides the default square cell width
        (used for the row label column on the left of a 2D
        grid). ``height`` overrides the default square cell
        height - the column header on top of a 2D grid uses
        ``height=14`` so it doesn't overlap the cells
        (which start at ``y + 14``). Without this, a column
        header drawn as a square cell at a larger cell_size
        would extend down past the cell row and overlap the
        first row of cells.
        """
        import pygame
        w = width if width is not None else cell_size
        h = height if height is not None else cell_size
        # Outline only - no fill, so the user can still see the
        # grid behind the label cells.
        rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(screen, self.PANEL, rect, border_radius=2)
        pygame.draw.rect(screen, self.GRID_LINE, rect, width=1, border_radius=2)
        # Center the label in the cell.
        text_surface = fonts["small"].render(label, True, self.MUTED)
        text_rect = text_surface.get_rect(center=rect.center)
        screen.blit(text_surface, text_rect)

    def _draw_dict_strip(
        self,
        screen,
        fonts,
        x: int,
        y: int,
        items: list,
        cell_size: int,
        var_name: Optional[str] = None,
    ) -> None:
        """Render a dict as TWO rows of cells (keys on top, values
        on the bottom). No wrapping, no truncation - a dict
        with 50 entries is 50 columns wide. Same clipping
        behavior as ``_draw_flat_strip``.
        """
        import pygame
        if not items:
            self._draw_text(screen, fonts["small"], "(empty)", x, y, self.MUTED)
            return
        cell_gap = 1
        for index, (k, v) in enumerate(items):
            cx = x + index * (cell_size + cell_gap)
            self._draw_one_cell(screen, fonts, cx, y, cell_size, k,
                                touched_key=(var_name, k) if var_name else None)
            self._draw_one_cell(screen, fonts, cx, y + cell_size + cell_gap, cell_size, v,
                                touched_key=(var_name, k) if var_name else None)

    def _draw_set_strip(
        self,
        screen,
        fonts,
        x: int,
        y: int,
        items: list,
        cell_size: int,
        var_name: Optional[str] = None,
    ) -> None:
        """Render a set as ONE row of cells (no index labels, since
        sets are unordered). Every element is drawn - the user
        complained that the previous 20-element cap was
        'cutting the variable at the bottom'; the panel scrolls
        vertically now, so a 600-element visited set just
        needs scrolling. The user can also wheel-zoom out to
        shrink the cell size."""
        import pygame
        if not items:
            self._draw_text(screen, fonts["small"], "(empty)", x, y, self.MUTED)
            return
        cell_gap = 1
        for index, item in enumerate(items):
            cx = x + index * (cell_size + cell_gap)
            self._draw_one_cell(
                screen, fonts, cx, y, cell_size, item,
                touched_key=(var_name, item) if var_name else None,
            )

    def _draw_scalar_cell(
        self,
        screen,
        fonts,
        x: int,
        y: int,
        cell_size: int,
        value,
        var_name: Optional[str] = None,
    ) -> None:
        """Render a scalar as a single cell."""
        self._draw_one_cell(screen, fonts, x, y, cell_size, value,
                            touched_key=(var_name, None) if var_name else None)

    def _draw_one_cell(
        self,
        screen,
        fonts,
        x: int,
        y: int,
        cell_size: int,
        value,
        touched_key=None,
        cell_index: Optional[int] = None,
    ) -> None:
        """Single-cell drawer used by every variable-visual helper.
        Handles the per-cell index overlay, the touched-cell
        coloring, and the per-line content layout.

        Tuple and list values are rendered as a "single big
        field ()" - one cell, with each sub-value on its own
        line. The cell height is ``cell_size * len(value)`` (one
        cell-size per sub-value) and the cell width stays at
        ``cell_size``. The user asked for this: 'Display tuples
        in cells as 1 value per line and begin a new line for
        a new value'. The caller is responsible for the
        row-level layout (taller cells extend down from the
        top of the row).

        Scalar values are rendered as before: a single
        ``cell_size``-square cell with the value centered.
        """
        import pygame
        # Compute cell height. Tuples / lists get one row per
        # sub-value, so the cell grows taller for longer
        # collections. Scalars stay at one cell tall.
        if isinstance(value, (tuple, list)):
            cell_height = cell_size * len(value) + 2
        else:
            cell_height = cell_size

        # Background + border.
        bg = self._color_for_cell(touched_key)
        rect = pygame.Rect(x, y, cell_size, cell_height)
        pygame.draw.rect(screen, bg, rect, border_radius=3)
        pygame.draw.rect(screen, self.GRID_LINE, rect, width=1, border_radius=3)

        # Per-cell index in the top-left was removed (the
        # user: 'have it on top ... not in each cell'). The
        # column header / row label strip above and to the
        # left of the cells carries the index instead.

        # Content layout: tuple / list = one value per line,
        # centered on its own row. Scalar = centered in the
        # square cell. For multi-line cells the value sits a
        # bit lower so the per-cell index at the top doesn't
        # crowd it.
        if isinstance(value, (tuple, list)):
            for i, sub in enumerate(value):
                sub_label = str(sub)
                if len(sub_label) > 6:
                    sub_label = sub_label[:5] + "…"
                line_y = y + i * cell_size + cell_size // 2
                text_surface = fonts["small"].render(sub_label, True, self.TEXT)
                text_rect = text_surface.get_rect(
                    center=(x + cell_size // 2, line_y),
                )
                screen.blit(text_surface, text_rect)
        else:
            label = self._format_value_label(value)
            if len(label) > 6:
                label = label[:5] + "…"
            cell_font = fonts["cell"] if cell_size >= 24 else fonts["small"]
            text_surface = cell_font.render(label, True, self.TEXT)
            if cell_index is not None and cell_size >= 18:
                value_rect = text_surface.get_rect(
                    center=(rect.centerx, rect.centery + 5),
                )
                screen.blit(text_surface, value_rect)
            else:
                screen.blit(
                    text_surface, text_surface.get_rect(center=rect.center),
                )

    def _color_for_cell(self, touched_key) -> tuple:
        """Look up the touched-cell color for ``touched_key``
        (a ``(var_name, <key>)`` tuple). Returns the default
        cell background if the key isn't in the touched dict.
        """
        cell_bg = (52, 60, 74)
        if not self._touched_cells or touched_key is None:
            return cell_bg
        entry = self._touched_cells.get(touched_key)
        if entry is None:
            return cell_bg
        op_colors = {
            "READ": self.READ,
            "WRITE": self.WRITE,
            "COMPARE": self.COMPARE_A,
            "COMPARE_A": self.COMPARE_A,
            "COMPARE_B": self.COMPARE_B,
            "SWAP": self.SWAP,
        }
        return op_colors.get(entry, cell_bg)

    @staticmethod
    def _format_value_label(value) -> str:
        try:
            if isinstance(value, str):
                return value
            return str(value)
        except Exception:
            return "?"

    def _draw_index_labels(
        self,
        screen,
        font,
        x: int,
        y: int,
        cell_size: int,
        cell_gap: int,
        cols_per_row: int,
        count: int,
    ) -> None:
        """Deprecated no-op: the per-cell index inside each
        list/tuple cell replaced the old top-of-row labels.
        Kept as a shim so any stale caller doesn't break; will
        be removed in the next sweep."""
        return None

    def _cell_rect(self, grid_rect, cell_size, coord):
        import pygame

        x, y = coord
        return pygame.Rect(grid_rect.x + x * cell_size, grid_rect.y + y * cell_size, cell_size - 2, cell_size - 2)

    def _coord_at_pos(self, pos, grid, values) -> Optional[tuple[int, int]]:
        """Translate a screen pixel position to a source-grid coordinate.

        The translation uses the current scroll offset: clicking the
        top-left visible cell yields (scroll_x, scroll_y).
        """
        grid_rect, cell_size, _, _ = self._grid_rect(grid, values)
        if cell_size <= 0 or not grid_rect.collidepoint(pos):
            return None
        rel_x = (pos[0] - grid_rect.x) // cell_size
        rel_y = (pos[1] - grid_rect.y) // cell_size
        src_x = self.scroll_x + int(rel_x)
        src_y = self.scroll_y + int(rel_y)
        if values is None or src_y < 0 or src_y >= len(values):
            return None
        row = values[src_y]
        if src_x < 0 or src_x >= len(row):
            return None
        return src_x, src_y

    def _op_touches_watchpoint(self, op: OpRecord, watchpoints: set[tuple[int, int]]) -> bool:
        if not watchpoints:
            return False
        touched = set(self._extract_coords(op.detail))
        insert_match = re.search(r"list\.insert\((-?\d+),", op.detail)
        if insert_match:
            touched.add((max(0, int(insert_match.group(1))), 0))
        pop_match = re.search(r"list\.pop\((-?\d+)\)", op.detail)
        if pop_match:
            touched.add((max(0, int(pop_match.group(1))), 0))
        return bool(touched & watchpoints)

    def _touched_from_call(
        self,
        op: OpRecord,
        trace_frame,
    ) -> dict:
        """Extract touched (var_name, key) pairs for a ``CALL`` op.

        Thin wrapper around ``_walk_source_line`` that infers
        the op kind from the source line. See
        ``_walk_source_line`` for the full description of the
        AST walk.
        """
        text = self._source_line_text(trace_frame)
        op_kind = self._infer_call_kind(text) or "READ"
        return self._walk_source_line(trace_frame, op_kind)

    def _source_line_text(self, trace_frame) -> str:
        """Read the source line text from the trace frame.

        Returns the line (leading / trailing whitespace stripped)
        or ``""`` if the frame has no source file / line number /
        line content.
        """
        if not trace_frame:
            return ""
        source_file = getattr(trace_frame, "source_file", None)
        line_no = trace_frame.line_no
        if not source_file or not line_no or line_no <= 0:
            return ""
        try:
            with open(source_file, "r", encoding="utf-8", errors="replace") as f:
                lines = f.readlines()
        except OSError:
            return ""
        idx = line_no - 1
        if idx < 0 or idx >= len(lines):
            return ""
        return lines[idx].rstrip().lstrip()

    def _walk_source_line(self, trace_frame, op_kind: str) -> dict:
        """Parse the source line from ``trace_frame`` and return
        ``{(var_name, key): op_kind}`` for every cell the line
        touched. Used by BOTH the CALL op path (where the
        engine only recorded ``line N``) and the non-CALL op
        path (where the engine recorded a specific operation
        but the source line still tells us the scalars that
        line referenced - the engine doesn't track scalar
        reads / writes).

        Three kinds of references are picked up:

        1. Bare ``Name`` nodes whose value in locals is a scalar
           (int, str, bool, float, None, TrackedValue). These
           become ``(var_name, None) -> op_kind`` entries so the
           single-cell ``n: 30`` / ``i: 2`` / ``total: 48`` cells
           flash when the line references them. Walked in both
           Load and Store context (Store covers the LHS of
           ``x = 5``, so the scalar cell flashes when the engine
           writes to it).

        2. ``Subscript`` nodes in BOTH ``Load`` and ``Store``
           contexts. ``Store`` matters for dict writes
           (``d["foo"] = 5``) and list overwrites
           (``candies[i] = max(...)``) - the LHS subscript has
           ``Store`` context and the old Load-only walker missed
           it. Each subscript becomes ``(var_name, key) -> op_kind``
           where ``key`` is the integer index for lists/tuples
           and the actual key for dicts.

        3. ``Compare`` nodes with the ``In`` operator. ``x in
           my_set`` records a read against the set but the
           specific element touched is only knowable from the
           source, so we resolve ``x`` and add
           ``(set_name, x) -> op_kind``. The set renderer
           matches by element value because sets are unordered.
           ``key in my_dict`` and ``value in my_list`` are
           handled the same way.

        Returns ``{}`` if the frame has no source line (in
        that case, only the op-detail regex path can run, and
        that's the caller's responsibility).
        """
        import ast as _ast
        text = self._source_line_text(trace_frame)
        if not text:
            return {}

        safe_builtins = self._safe_builtins()
        locals_dict = trace_frame.locals or {}

        # Unwrap the engine's TrackedList to a plain list. The
        # Subscript walker only matches ``isinstance(container,
        # (list, tuple))``; without this step, every line that
        # reads or writes a TrackedList element (e.g. ``data[i]``
        # in bubble sort) produces no touched cells. The
        # renderer's _draw_variables_section does the same
        # unwrap, so the keys we put in touched_cells match the
        # keys the renderer uses when looking up the cell.
        try:
            from code_n.tracked import TrackedList as _TL
        except ImportError:
            _TL = None
        if _TL is not None:
            locals_dict = {
                _name: (list(_value) if isinstance(_value, _TL) else _value)
                for _name, _value in locals_dict.items()
            }

        stripped = text.lstrip()
        try:
            tree = _ast.parse(text, mode="exec")
        except SyntaxError:
            for kw in ("if ", "elif ", "while "):
                if stripped.startswith(kw):
                    test_str = stripped[len(kw):].rstrip().rstrip(":").rstrip()
                    try:
                        tree = _ast.parse(test_str, mode="eval")
                    except SyntaxError:
                        return {}
                    break
            else:
                try:
                    tree = _ast.parse(text, mode="eval")
                except SyntaxError:
                    return {}

        touched: dict = {}

        # 1) Bare Name references in Load OR Store context.
        for node in _ast.walk(tree):
            if isinstance(node, _ast.Name) and isinstance(node.ctx, (_ast.Load, _ast.Store)):
                if node.id in locals_dict:
                    value = locals_dict[node.id]
                    if not isinstance(value, (list, tuple, dict, set)):
                        touched[(node.id, None)] = op_kind

        # 2) Subscript references.
        for node in _ast.walk(tree):
            if not isinstance(node, _ast.Subscript):
                continue

            # NESTED subscript FIRST: ``grid[nr][nc]``. The
            # outer Subscript's value is itself a Subscript
            # (``grid[nr]``), and the unparse of that value
            # ("grid[nr]") is NOT a name in locals_dict. So the
            # normal ``var_src not in locals_dict`` check below
            # would silently drop the outer Subscript and the
            # walker would only see the inner one (recording
            # just the row index). Detect the nested case up
            # front and resolve the indices from both slices.
            if isinstance(node.value, _ast.Subscript):
                inner = node.value
                # The innermost Name is the variable (e.g. 'grid').
                try:
                    var_src = _ast.unparse(inner.value)
                except Exception:
                    continue
                if var_src not in locals_dict:
                    continue
                container = locals_dict[var_src]
                try:
                    inner_idx = eval(
                        compile(
                            _ast.Expression(inner.slice),
                            "<ast>", "eval",
                        ),
                        {"__builtins__": safe_builtins},
                        locals_dict,
                    )
                    outer_idx = eval(
                        compile(
                            _ast.Expression(node.slice),
                            "<ast>", "eval",
                        ),
                        {"__builtins__": safe_builtins},
                        locals_dict,
                    )
                except Exception:
                    continue
                if isinstance(inner_idx, int) and isinstance(outer_idx, int):
                    # For a 2D list of lists, the inner index is
                    # the row and the outer is the column. For a
                    # TrackedGrid, the same holds: ``grid[nr]``
                    # returns the row, ``[nc]`` indexes into it.
                    if isinstance(container, (list, tuple)):
                        if 0 <= inner_idx < len(container):
                            touched[(var_src, (inner_idx, outer_idx))] = op_kind
                    else:
                        # TrackedGrid / TrackedList path - the
                        # renderer uses the same ``(row, col)``
                        # key for the grid's 2D rendering.
                        try:
                            from code_n.tracked import TrackedGrid as _TG_w
                            if _TG_w is not None and isinstance(container, _TG_w):
                                if 0 <= inner_idx < container.height:
                                    touched[(var_src, (inner_idx, outer_idx))] = op_kind
                        except ImportError:
                            pass
                continue

            # Single-subscript case: ``data[i]`` or ``grid[nr]``.
            try:
                var_src = _ast.unparse(node.value)
            except Exception:
                continue
            if var_src not in locals_dict:
                continue
            container = locals_dict[var_src]
            try:
                index_src = _ast.unparse(node.slice)
                sub_tree = _ast.parse(index_src, mode="eval")
                for sub in _ast.walk(sub_tree):
                    if isinstance(sub, (_ast.Call, _ast.Attribute)):
                        raise ValueError("no calls / attrs")
                index = eval(
                    compile(sub_tree, "<ast>", "eval"),
                    {"__builtins__": safe_builtins},
                    locals_dict,
                )
            except Exception:
                continue
            if isinstance(container, (list, tuple)) and isinstance(index, int):
                if 0 <= index < len(container):
                    touched[(var_src, index)] = op_kind
            elif isinstance(container, dict):
                if index in container:
                    try:
                        hash(index)
                        touched[(var_src, index)] = op_kind
                    except TypeError:
                        pass
            else:
                # TrackedGrid ``grid[nr]`` (single index on the LHS
                # of a 2D access, or anywhere a row is read by
                # itself). The renderer's grid is keyed by
                # ``(row, col)`` tuples, so a single-index touch
                # here doesn't have a direct key - skip it. The
                # nested-subscript branch above is what lights up
                # the specific cell.
                try:
                    from code_n.tracked import TrackedGrid as _TG_w2
                    if _TG_w2 is not None and isinstance(container, _TG_w2):
                        continue
                except ImportError:
                    pass

        # 3) ``In`` comparisons.
        for node in _ast.walk(tree):
            if not isinstance(node, _ast.Compare):
                continue
            for op_node, comparator in zip(node.ops, node.comparators):
                if not isinstance(op_node, _ast.In):
                    continue
                try:
                    container_src = _ast.unparse(comparator)
                except Exception:
                    continue
                if container_src not in locals_dict:
                    continue
                container = locals_dict[container_src]
                try:
                    needle = eval(
                        compile(_ast.Expression(node.left), "<ast>", "eval"),
                        {"__builtins__": safe_builtins},
                        locals_dict,
                    )
                except Exception:
                    continue
                if isinstance(container, set):
                    for element in container:
                        if element == needle:
                            try:
                                hash(element)
                                touched[(container_src, element)] = op_kind
                            except TypeError:
                                pass
                            break
                elif isinstance(container, (list, tuple)):
                    for element_index, element in enumerate(container):
                        if element == needle:
                            touched[(container_src, element_index)] = op_kind
                            break
                elif isinstance(container, dict):
                    if needle in container:
                        try:
                            hash(needle)
                            touched[(container_src, needle)] = op_kind
                        except TypeError:
                            pass
        return touched

    @staticmethod
    def _safe_builtins() -> dict:
        """Build a dict of safe Python builtins for sandboxed eval."""
        return {
            k: getattr(__builtins__, k) if hasattr(__builtins__, k) else __builtins__[k]
            for k in (
                "abs", "all", "any", "bool", "dict", "enumerate",
                "filter", "float", "int", "len", "list", "map",
                "max", "min", "print", "range", "repr", "reversed",
                "round", "set", "sorted", "str", "sum", "tuple",
                "zip", "True", "False", "None",
            )
            if (hasattr(__builtins__, k) or
                (isinstance(__builtins__, dict) and k in __builtins__))
        }

    @staticmethod
    def _infer_call_kind(text: str) -> str | None:
        """Guess the op type (READ / WRITE / COMPARE / SWAP) from
        a source line. Used by ``_touched_from_call`` when the
        op is a CALL (line-based tracing) and the engine hasn't
        recorded the specific op type.
        """
        import ast as _ast
        # A bare if/elif/while header line (no body) fails to parse
        # in exec mode, but the keyword itself tells us this is a
        # comparison branch — the condition expression is what
        # touched the cells. Check the prefix first so we don't
        # fall through to the "exec failed → eval → no body → READ"
        # trap.
        stripped = text.lstrip()
        for kw in ("if ", "elif ", "while "):
            if stripped.startswith(kw):
                return "COMPARE"
        try:
            tree = _ast.parse(text, mode="exec")
        except SyntaxError:
            try:
                tree = _ast.parse(text, mode="eval")
            except SyntaxError:
                return None
        for stmt in getattr(tree, "body", []):
            if isinstance(stmt, (_ast.Assign, _ast.AugAssign)):
                return "WRITE"
            if isinstance(stmt, (_ast.If, _ast.While)):
                return "COMPARE"
        return "READ"

    def _source_breakpoint_hit(self, trace_frame: Optional[TraceFrame], seen: set[tuple[int, int]]) -> bool:
        if not trace_frame or not trace_frame.breakpoint:
            return False
        key = (trace_frame.line_no, trace_frame.op_index)
        if key in seen:
            return False
        seen.add(key)
        return True

    def _extract_touched_cells(
        self,
        op: OpRecord,
        trace_frame,
    ) -> dict[tuple[str, int], str]:
        """Return ``(var_name, index) -> op_type`` for the cells
        this op touches.

        For ``READ`` / ``WRITE`` / ``COMPARE`` / ``SWAP`` ops, the
        engine's op.detail hardcodes the variable name as
        ``list`` (e.g. ``list[5] = 3``). We treat ``list`` as a
        wildcard: every variable in scope with the right index
        is touched. (False positives are possible but rare since
        most challenges have one main list.)

        For ``CALL`` ops (line-based tracing, where the engine
        records one op per source line), the detail is just
        ``line N``. We read the actual source line from
        ``trace_frame.source_file`` and parse it for
        ``name[expr]`` subscripts - this gives us the real
        variable name (``ratings``, ``candies``, etc.) and
        avoids the wildcard-false-positive issue.
        """
        import re, ast as _ast
        detail = getattr(op, "detail", "") or ""
        op_type_name = getattr(op.op_type, "name", None) or str(op.op_type)
        if op_type_name == "CALL":
            return self._touched_from_call(op, trace_frame)
        locals_dict = trace_frame.locals if trace_frame else {}
        # Unwrap TrackedList (and friends) to plain lists. The
        # engine emits ops like ``list[i] = v`` for every
        # TrackedList operation, so without this step the
        # ``isinstance(value, (list, tuple))`` check below was
        # False for every list the player touched, and the
        # variables panel never colored anything for challenges
        # whose only list was the TrackedList challenge input
        # (bubble sort, selection sort, etc.). Same unwrap
        # happens in _touched_from_call and in
        # _draw_variables_section, so the keys match the
        # renderer's lookups.
        try:
            from code_n.tracked import TrackedList as _TL
        except ImportError:
            _TL = None
        if _TL is not None:
            locals_dict = {
                _name: (list(_value) if isinstance(_value, _TL) else _value)
                for _name, _value in locals_dict.items()
            }
        touched: dict[tuple[str, int], str] = {}
        safe_builtins = {
            k: getattr(__builtins__, k) if hasattr(__builtins__, k) else __builtins__[k]
            for k in ("int", "float", "len", "True", "False", "None")
            if (hasattr(__builtins__, k) or
                (isinstance(__builtins__, dict) and k in __builtins__))
        }
        # Engine's detail says e.g. ``list[5] = 3`` or
        # ``list[5] < list[6]``. We use the wildcard name
        # ``list`` so every variable in the locals dict at the
        # matching index flashes. The rendering then checks
        # against the actual variable name being drawn.
        for match in re.finditer(r'\w+\[([^\]]+)\]', detail):
            index_expr = match.group(1)
            try:
                tree = _ast.parse(index_expr, mode="eval")
                for node in _ast.walk(tree):
                    if isinstance(node, (_ast.Call, _ast.Attribute)):
                        raise ValueError("no calls / attribute access")
                index = eval(
                    compile(tree, "<ast>", "eval"),
                    {"__builtins__": safe_builtins},
                    locals_dict,
                )
            except Exception:
                continue
            if isinstance(index, int):
                # Wildcard: match every list/tuple in scope.
                for name, value in locals_dict.items():
                    if isinstance(value, (list, tuple)) and index < len(value):
                        touched[(name, index)] = op_type_name

        # Also walk the source line for SCALAR Name references.
        # The engine doesn't record scalar reads / writes at all
        # (only TrackedList / TrackedGrid / TrackedQueue / etc.
        # operations), so a line like ``if data[i] > data[i+1]:``
        # only records the two READ ops + the COMPARE op, but
        # the source line also references the scalar ``i`` which
        # never gets touched unless we walk the AST. Without this
        # pass the ``i: 2`` cell (or whatever scalar the line
        # used) stays gray on every op. The user explicitly asked
        # for scalars to blink: 'I don't see the single variables
        # blinking if they are used'.
        source_touched = self._walk_source_line(trace_frame, op_type_name)
        # source_touched wins for shared keys (e.g., the
        # Subscript walker in the source line produces a
        # var-name-specific entry, the regex produces a
        # wildcard ``list[...]`` entry - the var-name-specific
        # one is correct).
        for key, value in source_touched.items():
            touched[key] = value
        return touched

    def _format_source_line(self, trace_frame: Optional[TraceFrame]) -> tuple[str, str]:
        """Return ``(code_line, validated_line)`` for the player's source.

        The first element is the code itself, with the source's
        leading indentation stripped (so an indented ``if`` shows
        as ``if ratings[i] > ...`` rather than
        ``    if ratings[i] > ...``).

        The second element is a ``Validated:`` line that
        substitutes every Name and Subscript reference with its
        current value and shows the result of executing the
        statement. Examples::

          if ratings[i] > ratings[i - 1]:
          Validated: 6 > 2 = True

          candies[i] = candies[i - 1] + 1
          Validated: candies[16] = candies[15] + 1 = 3

        The line number is intentionally NOT shown here - the
        caller already rendered it as part of the "Line N
        variables" title, so repeating it would be redundant.

        Returns ``("", "")`` when the frame/file/line isn't
        available.
        """
        if not trace_frame or not trace_frame.source_file or trace_frame.line_no <= 0:
            return "", ""
        path = os.path.normcase(os.path.abspath(trace_frame.source_file))
        lines = self._source_cache.get(path)
        if lines is None:
            try:
                with open(trace_frame.source_file, "r", encoding="utf-8", errors="replace") as f:
                    lines = f.readlines()
            except OSError:
                lines = []
            self._source_cache[path] = lines
        if not lines:
            return "", ""
        idx = trace_frame.line_no - 1
        if idx < 0 or idx >= len(lines):
            return "", ""
        # Strip the leading whitespace the source file has - the
        # user wants to see the code, not its indentation.
        text = lines[idx].rstrip().lstrip()

        validated = self._format_validated_line(text, trace_frame.locals or {})
        return text, validated

    def _format_validated_line(self, text: str, locals_dict: dict) -> str:
        """Return the ``Validated: <substituted> = <result>`` line.

        Substitutes every Name and Subscript reference in the
        line with its current value (sandboxed eval) and shows
        the result of executing the line. Returns "" if the line
        can't be evaluated safely.

        Examples::

          "candies[i] = candies[i - 1] + 1"  -> "Validated: candies[16] = candies[15] + 1 = 3"
          "if ratings[i] > ratings[i - 1]:" -> "Validated: 6 > 2 = True"
          "i = 1"                             -> "Validated: i = 1"
        """
        import ast as _ast

        if not locals_dict or not text.strip():
            return ""

        # Helper: substitute Names in a string (preserving the rest
        # of the syntax). Used for plain expression lines and for
        # the condition of an if/while.
        def _substitute(src: str) -> str:
            try:
                tree = _ast.parse(src, mode="eval")
            except SyntaxError:
                return src
            try:
                # Walk the tree and replace Name nodes with their
                # values. For Subscript nodes, the slice (the
                # index) gets substituted; for NESTED subscripts
                # (``grid[nr][nc]``) the value is also recursed
                # into so the inner Subscript's Names (here ``nr``)
                # are substituted too. A Name value (the
                # variable itself, e.g. ``grid``) is left alone so
                # the unparse reads as ``grid[5][18]`` rather than
                # the unfriendly ``[[0,1,...],...][5][18]``.
                class _Subst(_ast.NodeTransformer):
                    def visit_Name(self, node):
                        if (isinstance(node.ctx, _ast.Load)
                                and node.id in locals_dict):
                            value = locals_dict[node.id]
                            return _ast.Constant(value=value)
                        return node

                    def visit_Subscript(self, node):
                        if node.slice is not None:
                            node.slice = self.visit(node.slice)
                        if isinstance(node.value, _ast.Subscript):
                            node.value = self.visit(node.value)
                        return node
                new_tree = _Subst().visit(tree)
                return _ast.unparse(new_tree)
            except Exception:
                return src

        # Helper: build a short "name=value, ..." hint for the
        # Names that appear as subscripts / bare references in the
        # line. Used as the leading "i=16 -> " part of the
        # Validated line. Abbreviates long values (lists, dicts).
        # ``safe_builtins`` is set up later (after the helpers it
        # needs are defined) so resolve it via a closure lookup.
        def _key_var_hint(src: str, scope: dict) -> str:
            try:
                tree = _ast.parse(src, mode="exec")
            except SyntaxError:
                try:
                    tree = _ast.parse(src, mode="eval")
                except SyntaxError:
                    return ""
            seen: set[str] = set()
            parts: list[str] = []

            def _short(value) -> str:
                try:
                    text_repr = repr(value)
                except Exception:
                    return "?"
                if len(text_repr) > 24:
                    if isinstance(value, (list, tuple, dict)):
                        return f"{type(value).__name__}({len(value)})"
                    return text_repr[:23] + "…"
                return text_repr

            class _Hint(_ast.NodeVisitor):
                def visit_Name(self, node):
                    if (isinstance(node.ctx, _ast.Load)
                            and node.id in scope
                            and node.id not in seen):
                        seen.add(node.id)
                        parts.append(f"{node.id}={_short(scope[node.id])}")
                    self.generic_visit(node)
                def visit_Subscript(self, node):
                    if isinstance(node.ctx, _ast.Load):
                        src = _ast.unparse(node)
                        if src not in seen:
                            try:
                                value = eval(
                                    compile(_ast.Expression(node), "<ast>", "eval"),
                                    {"__builtins__": safe_builtins},
                                    scope,
                                )
                                seen.add(src)
                                parts.append(f"{src}={_short(value)}")
                            except Exception:
                                pass
                    self.generic_visit(node)
            _Hint().visit(tree)
            return ", ".join(parts)

        # Helper: evaluate a string as an expression and return
        # ``str(value)`` or None on failure. The player's code
        # already had full Python builtins available when it ran,
        # so re-evaluating a single expression in the same context
        # is no less safe - we just block __import__/open/exec/etc.
        safe_builtins = {
            k: getattr(__builtins__, k) if hasattr(__builtins__, k) else __builtins__[k]
            for k in (
                "abs", "all", "any", "bool", "dict", "enumerate",
                "filter", "float", "int", "len", "list", "map",
                "max", "min", "print", "range", "repr", "reversed",
                "round", "set", "sorted", "str", "sum", "tuple",
                "zip", "True", "False", "None",
            )
            if (hasattr(__builtins__, k) or
                (isinstance(__builtins__, dict) and k in __builtins__))
        }

        def _eval_expr(src: str):
            try:
                return eval(
                    compile(_ast.parse(src, mode="eval"), "<ast>", "eval"),
                    {"__builtins__": safe_builtins},
                    locals_dict,
                )
            except Exception:
                return None

        # Single expression (no statement keywords).
        try:
            tree = _ast.parse(text, mode="eval")
            result = eval(
                compile(tree, "<ast>", "eval"),
                {"__builtins__": {}},
                locals_dict,
            )
            substituted = _ast.unparse(tree)
            return f"Validated: {substituted} = {result}"
        except Exception:
            pass

        # Try as a statement. Handle Assign / AugAssign / If / While.
        try:
            tree = _ast.parse(text, mode="exec")
        except SyntaxError:
            tree = None

        if tree is not None and tree.body:
            stmt = tree.body[0]
            if isinstance(stmt, _ast.Assign) and stmt.targets:
                target = stmt.targets[0]
                # Build the LHS: substitute Names in subscript
                # slices but keep the variable name itself.
                try:
                    import copy as _copy
                    new_target = _copy.deepcopy(target)
                    if isinstance(new_target, _ast.Subscript):

                        class _SliceSubst(_ast.NodeTransformer):
                            def visit_Name(self, node):
                                if (isinstance(node.ctx, _ast.Load)
                                        and node.id in locals_dict):
                                    return _ast.Constant(
                                        value=locals_dict[node.id])
                                return node

                            def visit_Subscript(self, node):
                                # Substitute the slice; for nested
                                # subscripts like ``grid[nr][nc]``,
                                # recurse into the inner Subscript
                                # so BOTH ``nr`` and ``nc`` get
                                # substituted. The Name value
                                # (``grid``) stays as a Name so
                                # the unparse reads naturally.
                                if node.slice is not None:
                                    node.slice = self.visit(node.slice)
                                if isinstance(node.value, _ast.Subscript):
                                    node.value = self.visit(node.value)
                                return node
                        new_target = _SliceSubst().visit(new_target)
                    lhs_str = _ast.unparse(new_target)
                except Exception:
                    lhs_str = _ast.unparse(target)
                # Substitute Names in the RHS too so builtins like
                # max() see the current value of i, etc. (Without
                # this, max(candies[i], candies[i+1]+1) fails because
                # i isn't bound in the eval namespace.) Only the
                # slice part of each Subscript gets its Names
                # substituted - the value (the list itself) stays
                # as a Name so the unparse still reads naturally
                # (``candies[16-1]`` rather than ``[2, 1, ...][16-1]``).
                rhs_text = _ast.unparse(stmt.value)
                try:
                    rhs_tree = _ast.parse(rhs_text, mode='eval')

                    class _RhsSubst(_ast.NodeTransformer):
                        def visit_Name(self, node):
                            if (isinstance(node.ctx, _ast.Load)
                                    and node.id in locals_dict):
                                return _ast.Constant(
                                    value=locals_dict[node.id])
                            return node

                        def visit_Subscript(self, node):
                            # Only substitute the index (slice), not
                            # the value (the list/dict). Otherwise
                            # the unparse reads as ``[1, 2, 3][i-1]``
                            # instead of the much friendlier
                            # ``candies[i-1]``. For NESTED
                            # subscripts (``grid[nr][nc]``), the
                            # outer value is itself a Subscript -
                            # recurse into it so the inner index
                            # (``nr``) gets substituted too.
                            if node.slice is not None:
                                node.slice = self.visit(node.slice)
                            if isinstance(node.value, _ast.Subscript):
                                node.value = self.visit(node.value)
                            return node
                    rhs_tree = _RhsSubst().visit(rhs_tree)
                    rhs_substituted = _ast.unparse(rhs_tree)
                except Exception:
                    rhs_substituted = rhs_text
                value = _eval_expr(rhs_substituted)
                if value is None:
                    return f"Validated: {lhs_str} = ?"
                return f"Validated: {lhs_str} = {rhs_substituted} = {value}"
            if isinstance(stmt, _ast.AugAssign):
                try:
                    import copy as _copy
                    new_target = _copy.deepcopy(stmt.target)
                    if isinstance(new_target, _ast.Subscript):

                        class _SliceSubst(_ast.NodeTransformer):
                            def visit_Name(self, node):
                                if (isinstance(node.ctx, _ast.Load)
                                        and node.id in locals_dict):
                                    return _ast.Constant(
                                        value=locals_dict[node.id])
                                return node
                        new_target.slice = _SliceSubst().visit(new_target.slice)
                    lhs_str = _ast.unparse(new_target)
                except Exception:
                    lhs_str = _ast.unparse(stmt.target)
                # Evaluate the original target value to compute the new one.
                old_value = _eval_expr(_ast.unparse(stmt.target))
                rhs_value = _eval_expr(_ast.unparse(stmt.value))
                if old_value is None or rhs_value is None:
                    return f"Validated: {lhs_str} {stmt.op.__class__.__name__}= ?"
                op_name = {  # map AST operator -> symbol
                    _ast.Add: "+", _ast.Sub: "-", _ast.Mult: "*",
                    _ast.Div: "/", _ast.Mod: "%", _ast.BitOr: "|",
                    _ast.BitAnd: "&", _ast.BitXor: "^",
                    _ast.LShift: "<<", _ast.RShift: ">>",
                }.get(type(stmt.op), "?")
                try:
                    new_value = eval(
                        f"old_value {op_name} rhs_value",
                        {"__builtins__": {}},
                        {"old_value": old_value, "rhs_value": rhs_value},
                    )
                except Exception:
                    new_value = "?"
                return f"Validated: {lhs_str} = {old_value} {op_name} {rhs_value} = {new_value}"
            if isinstance(stmt, _ast.Return):
                if stmt.value is None:
                    return ""
                value = _eval_expr(_ast.unparse(stmt.value))
                return f"Validated: return {value}" if value is not None else ""

        # Compound statement that didn't parse as exec (if X:, while X:).
        stripped = text.lstrip()
        for kw in ("if ", "elif ", "while "):
            if stripped.startswith(kw):
                test_str = stripped[len(kw):].rstrip().rstrip(":").rstrip()
                substituted = _substitute(test_str)
                result = _eval_expr(test_str)
                if result is None:
                    return ""
                return f"Validated: {kw.rstrip()}: {substituted} = {result}"

        # Fall back: just substitute Names in the text.
        return f"Validated: {_substitute(text)}"

    def _draw_centered_text(self, screen, font, text, rect, color):
        surface = font.render(text[:8], True, color)
        screen.blit(surface, surface.get_rect(center=rect.center))

    def _draw_grid_headers(self, screen, fonts, grid_rect, cell_size: int, display_rows: list[list[DisplayCell]], full_cols: int = 0):
        import pygame

        if not display_rows or not display_rows[0]:
            return
        axis_y = max(0, grid_rect.y - 24)
        label_height = 18
        label_bottom = axis_y + label_height
        # Headers track the scroll so the column above a cell always shows
        # that cell's source column number. A thin tick line connects the
        # label to the top of its cell so the player never has to guess
        # which number goes with which cell.
        for x, display_cell in enumerate(display_rows[0]):
            label = self._column_header_label(display_cell)
            if not label:
                continue
            screen_x = grid_rect.x + (x - self.scroll_x) * cell_size
            if screen_x + cell_size <= grid_rect.x or screen_x >= grid_rect.right:
                continue
            cell_center_x = screen_x + cell_size // 2
            label_rect = pygame.Rect(screen_x, axis_y, cell_size - 2, label_height)
            self._draw_centered_text(screen, fonts["small"], label, label_rect, self.MUTED)
            # Fine tick from the label down to the top edge of the cell.
            pygame.draw.line(
                screen, self.GRID_LINE,
                (cell_center_x, label_bottom + 1),
                (cell_center_x, grid_rect.y - 1),
                1,
            )

    def _draw_cell_contents(self, screen, fonts, rect, value_label: str, index_label: str, value_color):
        if index_label:
            index_surface = fonts["small"].render(index_label[:8], True, self.TEXT)
            screen.blit(index_surface, (rect.x + 4, rect.y + 2))
        if not value_label:
            return
        value_font = fonts["cell"] if rect.height >= 34 else fonts["small"]
        value_surface = value_font.render(value_label[:8], True, value_color)
        target = rect.copy()
        if index_label and rect.height >= 34:
            target.y += 8
            target.height = max(12, target.height - 8)
        screen.blit(value_surface, value_surface.get_rect(center=target.center))

    def _cell_index_label(self, display_cell: DisplayCell, show_row_labels: bool) -> str:
        if display_cell.source_coord is None:
            return ""
        return ""

    def _column_header_label(self, display_cell: DisplayCell) -> str:
        if display_cell.source_coord is None:
            return ""
        column, _ = display_cell.source_coord
        return f"{column}"

    def _row_header_label(self, row: list[DisplayCell], display_y: int) -> str:
        for display_cell in row:
            if display_cell.source_coord is not None:
                return f"{display_cell.source_coord[1]}"
        return ""

    def _draw_text(self, screen, font, text, x, y, color):
        screen.blit(font.render(text, True, color), (x, y))

    def _values_from_grid(self, grid: Grid) -> list[list[Any]]:
        rows: list[list[Any]] = []
        last_content_row = -1
        for y in range(grid.height):
            row: list[Any] = []
            row_has_content = False
            for x in range(grid.width):
                cell = grid.get(x, y)
                value = cell.value if cell.value is not None else cell.label
                row.append(value)
                if value not in (None, "") or cell.cell_type != CellType.EMPTY:
                    row_has_content = True
            rows.append(row)
            if row_has_content:
                last_content_row = y
        return rows[: last_content_row + 1] if last_content_row >= 0 else [[]]

    def _copy_values(self, values: list[list[Any]]) -> list[list[Any]]:
        return [row[:] for row in values]

    def _display_rows(self, values: Optional[list[list[Any]]]) -> list[list[DisplayCell]]:
        """Return the full grid wrapped in DisplayCell objects, with no
        truncation. The draw step uses scroll and zoom to decide which of
        these are actually visible."""
        if not values:
            return [[]]
        return [[DisplayCell(value=v, source_coord=(x, y)) for x, v in enumerate(row)] for y, row in enumerate(values)] or [[]]

    def _display_row(self, row: list[Any], y: int) -> list[DisplayCell]:
        return [DisplayCell(value=v, source_coord=(x, y)) for x, v in enumerate(row)]

    def _row_label_width(self, display_rows: list[list[DisplayCell]]) -> int:
        """Pixel width reserved for row index labels.

        Adapts to the number of digits in the largest row index: 1-digit
        indices need ~24px, 2-digit need ~36px, 3-digit need ~48px. The
        same convention is used for the column header strip above the
        grid (each cell is its own label), so the heights stay in sync.
        """
        if len(display_rows) <= 1:
            return 0
        max_index = len(display_rows) - 1
        digits = max(1, len(str(max_index)))
        return 16 + digits * 10

    def _ensure_value_cell(self, values: list[list[Any]], x: int, y: int):
        while len(values) <= y:
            values.append([])
        while len(values[y]) <= x:
            values[y].append("")

    def _trace_for_op(self, frames: list[TraceFrame], op_index: int) -> Optional[TraceFrame]:
        latest: Optional[TraceFrame] = None
        for frame in frames:
            if frame.op_index <= op_index:
                latest = frame
            else:
                break
        return latest

    def _overlays_for_op(self, op: OpRecord, values: list[list[Any]]) -> dict[tuple[int, int], tuple[int, int, int]]:
        """Return a dict of source_coord -> overlay color for an op.

        Keys are source-grid coordinates; the draw step translates them
        to screen pixels with the current scroll. Off-screen overlays are
        simply not drawn.
        """
        coords = self._extract_coords(op.detail)
        if op.op_type == OpType.COMPARE and len(coords) >= 2:
            return {coords[0]: self.COMPARE_A, coords[1]: self.COMPARE_B}
        if op.op_type == OpType.SWAP and len(coords) >= 2:
            return {coords[0]: self.SWAP, coords[1]: self.SWAP}
        if op.op_type == OpType.READ and coords:
            return {coords[0]: self.READ}
        if op.op_type == OpType.WRITE and coords:
            return {coords[0]: self.WRITE}
        insert_match = re.search(r"list\.insert\((-?\d+),", op.detail)
        if insert_match:
            return {(max(0, int(insert_match.group(1))), 0): self.WRITE}
        pop_match = re.search(r"list\.pop\((-?\d+)\)", op.detail)
        if pop_match:
            return {(max(0, int(pop_match.group(1))), 0): self.FAIL}
        return {}

    def _extract_coords(self, detail: str) -> list[tuple[int, int]]:
        list_coords = [(int(index), 0) for index in re.findall(r"list\[(-?\d+)\]", detail)]
        grid_coords = [(int(x), int(y)) for x, y in re.findall(r"grid\[(-?\d+),(-?\d+)\]", detail)]
        return list_coords or grid_coords

    def _extract_single_coord(self, detail: str) -> Optional[tuple[int, int]]:
        coords = self._extract_coords(detail)
        return coords[0] if coords else None

    def _extract_written_value(self, detail: str) -> Optional[str]:
        match = re.search(r"=\s*(.+)$", detail)
        if match:
            return match.group(1).strip()
        return None

    def _swap_values(self, values, first, second):
        ax, ay = first
        bx, by = second
        if 0 <= ay < len(values) and 0 <= by < len(values) and 0 <= ax < len(values[ay]) and 0 <= bx < len(values[by]):
            values[ay][ax], values[by][bx] = values[by][bx], values[ay][ax]

    def _value_at(self, values, coord):
        x, y = coord
        if 0 <= y < len(values) and 0 <= x < len(values[y]):
            return values[y][x]
        return ""

    def _wrap(self, text: str, width: int) -> list[str]:
        """Word-wrap `text` to fit `width` characters per line.

        Words that are themselves longer than `width` are broken into
        `width`-sized chunks (with an ellipsis on the first chunk of
        each word) so they can never overflow the panel. This is the
        only way a long list/dict value (e.g. ``data = [66, 64, 55, ...]``)
        stays inside the side panel.
        """
        if width <= 0:
            return [text]
        ellipsis = "..."
        # chunk_size leaves room for the ellipsis on the first chunk of
        # a long word, but stays positive even for very narrow widths.
        chunk_size = max(1, width - len(ellipsis))
        words = text.split()
        lines: list[str] = []
        current = ""
        for word in words:
            # If the word is wider than the column, emit it in pieces:
            # the first piece gets an ellipsis, subsequent pieces do
            # not (they're continuations, not a sentence ending).
            while len(word) > width:
                if current:
                    lines.append(current)
                    current = ""
                head = word[:chunk_size] + ellipsis
                lines.append(head)
                word = word[chunk_size:]
            if current and len(current) + 1 + len(word) > width:
                lines.append(current)
                current = word
            else:
                current = f"{current} {word}".strip()
        if current:
            lines.append(current)
        return lines or [""]

    def _wrap_width(self, fonts: dict) -> int:
        """Max char count that fits inside the side panel's content area.

        Measured from the actual font rather than guessed from the font
        size, so a wider/narrower glyph doesn't cause overflow. The
        result is a safe integer that leaves a small margin.
        """
        available_px = self.panel_width - 36  # 18px padding on each side
        char_px = max(1, fonts["small"].size("M")[0])
        return max(8, available_px // char_px - 2)

    def _find_speed(self, speed: str) -> Optional[SpeedPreset]:
        normalized = speed.strip().lower().replace("_", "-")
        aliases = {
            "1": "step",
            "2": "crawl",
            "3": "very-slow",
            "4": "slow",
            "5": "normal",
            "6": "fast",
            "7": "turbo",
            "8": "instant",
            "manual": "step",
            "step-by-step": "step",
            "stepping": "step",
            "very-slow": "very-slow",
            "veryslow": "very-slow",
            "extra-slow": "crawl",
            "extraslow": "crawl",
            "very-fast": "turbo",
            "veryfast": "turbo",
            "max": "instant",
        }
        normalized = aliases.get(normalized, normalized)
        for preset in SPEED_PRESETS:
            if preset.key == normalized or preset.label.lower() == normalized:
                return preset
        return None
