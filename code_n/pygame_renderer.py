"""Pygame renderer for animated algorithm visualization."""

from __future__ import annotations

import re
import time
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
ZOOM_MIN = 22
ZOOM_MAX = 50
ZOOM_STEP = 2  # pixels per wheel notch
DEFAULT_CELL_SIZE = 30

# Pixels of right-drag the user has to move to advance the view by
# one cell. Smaller = more sensitive. The float accumulator carries
# sub-cell motion between events, so very small drags feel smooth
# rather than snapping to whole cells.
PAN_PIXELS_PER_CELL = 16

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
        # Continuous zoom between ZOOM_MIN and ZOOM_MAX, controlled by
        # the mouse wheel only. The default of 30px is small enough to
        # fit ~25 cells across the viewport; the user can wheel up to
        # 50px to make individual cells more readable.
        self.cell_size: int = DEFAULT_CELL_SIZE
        # Scroll position, in source-grid cells. (0, 0) is the top-left.
        self.scroll_x: int = 0
        self.scroll_y: int = 0
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
            nonlocal op_index, paused, stopped
            if op_index >= len(ops):
                return "Replay complete. Press Replay to run again."

            detail = self._apply_operation(screen, clock, fonts, grid, visual_values, ops[op_index], op_index, len(ops), title, result)
            if self._op_touches_watchpoint(ops[op_index], watchpoints):
                paused = True
                detail = f"Watchpoint hit: {detail}"
            op_index += 1
            trace_frame = self._trace_for_op(result.trace_frames, op_index)
            if self._source_breakpoint_hit(trace_frame, source_breakpoints_hit):
                paused = True
                detail = f"Source breakpoint line {trace_frame.line_no}: {detail}"
            stopped = False
            return detail

        def reset_replay() -> str:
            nonlocal visual_values, op_index, paused, stopped, overlays, source_breakpoints_hit
            visual_values = self._copy_values(initial_values)
            op_index = 0
            paused = self.manual_step
            stopped = False
            overlays = {}
            source_breakpoints_hit = set()
            # Each fresh replay starts at the default zoom (30px per cell)
            # and the top-left of the grid.
            self.cell_size = 44
            self.scroll_x = 0
            self.scroll_y = 0
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
                    # Right-click enters "pan" mode. From now until the
                    # button is released, every mouse motion event pans
                    # the grid. The pan is bounded so dragging past the
                    # edge stops at the grid boundary; you can't scroll
                    # into the void. Reset the sub-cell accumulator on
                    # down so a stale fraction from a prior drag can't
                    # cause a sudden jump when the user starts panning
                    # again.
                    self._right_panning = True
                    self._pan_accum_x = 0.0
                    self._pan_accum_y = 0.0
                    try:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
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
                    # event.rel is (dx, dy) in pixels since the last
                    # motion event. The user wants "inverted" / natural
                    # panning: dragging right pulls the world to the
                    # right (scroll_x decreases), so the cells the
                    # finger lands on stay under the cursor. Same for
                    # the vertical axis.
                    #
                    # A float accumulator carries the sub-pixel motion
                    # between events so small drags still produce smooth
                    # movement instead of snapping to whole cells every
                    # PAN_PIXELS_PER_CELL pixels. scroll_by clamps to
                    # the grid bounds.
                    rel_x, rel_y = event.rel
                    self._pan_accum_x += rel_x
                    self._pan_accum_y += rel_y
                    dx_cells = -int(self._pan_accum_x // PAN_PIXELS_PER_CELL)
                    dy_cells = -int(self._pan_accum_y // PAN_PIXELS_PER_CELL)
                    if dx_cells or dy_cells:
                        self._pan_accum_x += dx_cells * PAN_PIXELS_PER_CELL
                        self._pan_accum_y += dy_cells * PAN_PIXELS_PER_CELL
                        self.scroll_by(dx_cells, dy_cells, grid, visual_values)
                elif mousewheel_event is not None and event.type == mousewheel_event:
                    # Mouse wheel zooms (only). Wheel up = bigger cells,
                    # wheel down = smaller. Modifiers (Shift, Ctrl) are
                    # ignored: the only way to pan is right-drag.
                    wheel_y = getattr(event, "y", 0) or 0
                    if wheel_y:
                        current_detail = self.zoom_by(wheel_y * ZOOM_STEP)
                elif old_mousewheel is not None and event.type == pygame.MOUSEBUTTONDOWN and event.button in (4, 5):
                    # Fallback for pygame 1.x: button 4 = wheel up, 5 = wheel down.
                    current_detail = self.zoom_by(ZOOM_STEP if event.button == 4 else -ZOOM_STEP)
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
            self._draw(screen, fonts, grid, visual_values, overlays, title, result, op_index, len(ops), current_detail, paused, trace_frame=trace_frame, stopped=stopped, watchpoints=watchpoints)
            pygame.display.flip()
            clock.tick(self.fps)

        pygame.quit()

    def _draw(self, screen, fonts, grid, values, overlays, title, result, op_index, total_ops, detail, paused, moving=None, trace_frame=None, stopped=False, watchpoints=None):
        import pygame

        sync_window_size(self, screen)
        screen.fill(self.BACKGROUND)
        grid_rect, cell_size, full_cols, full_rows = self._grid_rect(grid, values)
        display_rows = self._display_rows(values)
        show_row_labels = full_rows > 1

        title_surface = fonts["title"].render(title, True, self.TEXT)
        screen.blit(title_surface, (self.margin, 18))
        self._draw_main_description(screen, fonts, result.description)
        self._draw_grid_headers(screen, fonts, grid_rect, cell_size, display_rows, full_cols)

        # Iterate over every cell but draw only those that land inside
        # the viewport rect (cheap early-out). The screen position of a
        # cell is offset by (scroll_x, scroll_y) so panning is just
        # changing those two numbers.
        previous_clip = screen.get_clip()
        # The row labels sit to the LEFT of the grid, so the clip has to
        # include that column. Without this, set_clip(grid_rect) would
        # silently discard every row label and tick line.
        label_width = self._row_label_width(display_rows) if show_row_labels else 0
        cell_clip = pygame.Rect(
            grid_rect.x - label_width,
            grid_rect.y,
            grid_rect.width + label_width,
            grid_rect.height,
        )
        screen.set_clip(cell_clip)
        for sy, row in enumerate(display_rows):
            if not row:
                continue
            if show_row_labels:
                label_rect = pygame.Rect(
                    grid_rect.x - self._row_label_width(display_rows),
                    grid_rect.y + (sy - self.scroll_y) * cell_size,
                    self._row_label_width(display_rows) - 8,
                    cell_size - 2,
                )
                self._draw_centered_text(screen, fonts["small"], self._row_header_label(row, sy), label_rect, self.MUTED)
                # Fine tick from the row label across to the cell it labels.
                cell_mid_y = grid_rect.y + (sy - self.scroll_y) * cell_size + cell_size // 2
                pygame.draw.line(
                    screen, self.GRID_LINE,
                    (label_rect.right + 1, cell_mid_y),
                    (grid_rect.x - 1, cell_mid_y),
                    1,
                )

            for sx, display_cell in enumerate(row):
                screen_x = grid_rect.x + (sx - self.scroll_x) * cell_size
                screen_y = grid_rect.y + (sy - self.scroll_y) * cell_size
                # Skip cells that fall outside the viewport.
                if screen_x + cell_size <= grid_rect.x or screen_x >= grid_rect.right:
                    continue
                if screen_y + cell_size <= grid_rect.y or screen_y >= grid_rect.bottom:
                    continue
                rect = pygame.Rect(screen_x, screen_y, cell_size - 2, cell_size - 2)
                source_coord = display_cell.source_coord
                cell = grid.get(*source_coord) if source_coord and grid.in_bounds(*source_coord) else None
                base_color = self.CELL_COLORS.get(cell.cell_type, self.CELL_COLORS[CellType.EMPTY]) if cell else self.CELL_COLORS[CellType.EMPTY]
                color = overlays.get(source_coord, base_color) if source_coord else base_color
                pygame.draw.rect(screen, color, rect, border_radius=4)
                pygame.draw.rect(screen, self.GRID_LINE, rect, width=1, border_radius=4)
                if watchpoints and source_coord in watchpoints:
                    pygame.draw.rect(screen, self.FAIL, rect.inflate(-5, -5), width=3, border_radius=4)

                text_value = display_cell.value if display_cell.value != "" else (cell.value if cell else None)
                label = str(text_value) if text_value is not None else (cell.label if cell else "")
                self._draw_cell_contents(screen, fonts, rect, label, self._cell_index_label(display_cell, show_row_labels), self.TEXT)
        screen.set_clip(previous_clip)

        if moving:
            for value, start, end, t, color in moving:
                x = start[0] + (end[0] - start[0]) * t
                y = start[1] + (end[1] - start[1]) * t
                rect = pygame.Rect(x, y, cell_size - 2, cell_size - 2)
                pygame.draw.rect(screen, color, rect, border_radius=4)
                pygame.draw.rect(screen, self.TEXT, rect, width=2, border_radius=4)
                self._draw_centered_text(screen, fonts["cell"], str(value), rect, self.TEXT)

        self._draw_panel(
            screen, fonts, result, op_index, total_ops, detail, paused,
            trace_frame, stopped, len(watchpoints or ()),
            view_text=self._visible_range_text(grid, values),
        )

    def _draw_panel(self, screen, fonts, result, op_index, total_ops, detail, paused, trace_frame=None, stopped=False, watchpoint_count=0, view_text=""):
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
        self._draw_text(screen, fonts["body"], "Current op", x + 18, text_y, self.TEXT)
        text_y += 24
        for line in self._wrap(detail, wrap_w)[:2]:
            self._draw_text(screen, fonts["small"], line, x + 18, text_y, self.MUTED)
            text_y += 20
        text_y += 12

        return_text = result.return_value or "<not returned>"
        return_lines = self._wrap(return_text, wrap_w)[:2]
        return_height = 24 + len(return_lines) * 18
        return_start = max(text_y, content_bottom - return_height)
        variables_bottom = max(text_y, return_start - 12)

        if trace_frame and text_y + 34 < variables_bottom:
            prefix = "Breakpoint line" if trace_frame.breakpoint else "Line"
            self._draw_text(screen, fonts["body"], f"{prefix} {trace_frame.line_no} variables", x + 18, text_y, self.TEXT)
            text_y += 24
            panel_inner_w = self.panel_width - 36
            # Cap to the first 6 variables so the panel doesn't
            # get dominated by a single huge list. Visuals are
            # bigger per variable than text was.
            for name, value in list(trace_frame.locals.items())[:6]:
                text_y = self._draw_variable_visual(
                    screen, fonts,
                    x=x + 18,
                    y=text_y,
                    max_width=panel_inner_w,
                    max_y=variables_bottom,
                    name=name,
                    value=value,
                )
                if text_y + 4 >= variables_bottom:
                    break
            text_y += 8

        text_y = max(text_y, content_bottom - return_height)
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
        if not description:
            return
        x = self.margin
        y = 56
        width = self._main_area_width()
        self._draw_text(screen, fonts["body"], "Description", x, y, self.TEXT)
        y += 24
        previous_clip = screen.get_clip()
        import pygame
        screen.set_clip(pygame.Rect(x, y, width, self._description_height(description) - 24))
        for line in self._description_lines(description):
            self._draw_text(screen, fonts["small"], line, x, y, self.MUTED)
            y += 18
        screen.set_clip(previous_clip)

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

    def _source_breakpoint_hit(self, trace_frame: Optional[TraceFrame], seen: set[tuple[int, int]]) -> bool:
        if not trace_frame or not trace_frame.breakpoint:
            return False
        key = (trace_frame.line_no, trace_frame.op_index)
        if key in seen:
            return False
        seen.add(key)
        return True

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

    # --- Variable visual rendering. The side panel used to dump
    # truncated text for every local variable, which is hard to scan
    # and hides the actual structure. The new path renders each
    # variable as a small grid of cells, one per element, with the
    # variable name as a label above. ---

    def _draw_variable_visual(
        self,
        screen,
        fonts,
        x: int,
        y: int,
        max_width: int,
        max_y: int,
        name: str,
        value,
    ) -> int:
        """Draw a labeled visual representation of (name, value).

        Lists/tuples/TrackedList get a row of small cells, one per
        element. Dicts get a 2-row "key / value" mini-grid. Scalars
        (int, str, bool, float, None) get a single cell. Nested or
        unknown types fall back to truncated text. Returns the new
        ``y`` after drawing.
        """
        import pygame

        cell_size = 18
        cell_gap = 1
        label_h = 16
        cell_h = cell_size

        # Stop early if the label alone doesn't fit.
        if y + label_h > max_y:
            return y

        self._draw_text(screen, fonts["body"], f"{name}:", x, y, self.TEXT)
        y += label_h

        def _draw_one_cell(px: int, py: int, val) -> None:
            """Draw a single cell with the string-coerced value."""
            label = repr(val)
            if len(label) > 6:
                label = label[:5] + "…"
            cell_rect = pygame.Rect(px, py, cell_size, cell_h)
            # Cell background: slightly lighter than PANEL so the
            # visual reads as a stack of cells against the panel.
            cell_bg = (52, 60, 74)
            pygame.draw.rect(
                screen,
                cell_bg,
                cell_rect,
                border_radius=3,
            )
            pygame.draw.rect(
                screen,
                self.GRID_LINE,
                cell_rect,
                width=1,
                border_radius=3,
            )
            cell_font = fonts["small"] if cell_size < 24 else fonts["body"]
            text_surface = cell_font.render(label, True, self.TEXT)
            screen.blit(
                text_surface,
                text_surface.get_rect(center=cell_rect.center),
            )

        def _row_y_offset(row_index: int, total_rows: int) -> int:
            return y + row_index * (cell_h + 2)

        # Unwrap TrackedList (and friends) so we can iterate.
        raw = value
        try:
            from code_n.tracked import TrackedList as _TL
            if isinstance(raw, _TL):
                raw = list(raw)
        except ImportError:
            pass

        # list / tuple: 1+ rows of cells.
        if isinstance(raw, (list, tuple)) and raw:
            items = list(raw)
            cols_per_row = max(1, (max_width + cell_gap) // (cell_size + cell_gap))
            # Truncate if huge so we don't dominate the panel.
            MAX_CELLS = 80
            truncated_count = 0
            if len(items) > MAX_CELLS:
                truncated_count = len(items) - MAX_CELLS
                items = items[:MAX_CELLS]
            rows_needed = (len(items) + cols_per_row - 1) // cols_per_row
            if y + rows_needed * (cell_h + 2) > max_y:
                # Not enough room to show anything.
                return y - label_h
            for index, item in enumerate(items):
                row = index // cols_per_row
                col = index % cols_per_row
                cx = x + col * (cell_size + cell_gap)
                cy = _row_y_offset(row, rows_needed)
                _draw_one_cell(cx, cy, item)
            y += rows_needed * (cell_h + 2)
            if truncated_count:
                self._draw_text(
                    screen, fonts["small"],
                    f"... +{truncated_count} more",
                    x, y, self.MUTED,
                )
                y += 18
            return y + 4

        # dict: 2 rows (keys, values).
        if isinstance(raw, dict) and raw:
            items = list(raw.items())
            cols_per_row = max(1, (max_width + cell_gap) // (cell_size + cell_gap))
            MAX_PAIRS = 30
            truncated_count = 0
            if len(items) > MAX_PAIRS:
                truncated_count = len(items) - MAX_PAIRS
                items = items[:MAX_PAIRS]
            rows_needed = 2
            if y + rows_needed * (cell_h + 2) > max_y:
                return y - label_h
            for index, (k, v) in enumerate(items):
                col = index
                if col >= cols_per_row:
                    break
                cx = x + col * (cell_size + cell_gap)
                _draw_one_cell(cx, _row_y_offset(0, rows_needed), k)
                _draw_one_cell(cx, _row_y_offset(1, rows_needed), v)
            y += rows_needed * (cell_h + 2) + 4
            if truncated_count:
                self._draw_text(
                    screen, fonts["small"],
                    f"... +{truncated_count} more",
                    x, y, self.MUTED,
                )
                y += 18
            return y + 4

        # Scalar: 1 cell.
        if y + cell_h > max_y:
            return y - label_h
        _draw_one_cell(x, y, raw)
        return y + cell_h + 8

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
