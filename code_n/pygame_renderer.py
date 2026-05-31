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
from .window import is_resize_event, open_maximized_window, sync_window_size


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
    value: Any
    source_coord: Optional[tuple[int, int]] = None
    ellipsis: bool = False


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
            "title": pygame.font.SysFont("consolas", 28, bold=True),
            "body": pygame.font.SysFont("consolas", 19),
            "small": pygame.font.SysFont("consolas", 15),
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
MAX_VISIBLE_ROW_ITEMS = 21


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

    def apply_speed(self, speed: str):
        preset = self._find_speed(speed)
        if not preset:
            preset = SPEED_PRESETS[DEFAULT_SPEED_INDEX]
        self.step_delay = preset.step_delay
        self.swap_frames = preset.swap_frames
        self.speed_label = preset.label
        self.manual_step = preset.manual_step

    def play(self, grid: Grid, operations: Iterable[OpRecord], title: str, result: VisualRunResult):
        import pygame

        pygame.init()
        screen = open_maximized_window(pygame, self.width, self.height, f"{GAME_TITLE} - {title}")
        sync_window_size(self, screen)
        clock = pygame.time.Clock()
        fonts = {
            "title": pygame.font.SysFont("consolas", 26, bold=True),
            "body": pygame.font.SysFont("consolas", 18),
            "small": pygame.font.SysFont("consolas", 15),
            "cell": pygame.font.SysFont("consolas", 18, bold=True),
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
        current_detail = "Step mode: press Space, Enter, or Right Arrow." if self.manual_step else current_detail

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
                    if not action and coord:
                        if coord in watchpoints:
                            watchpoints.remove(coord)
                            current_detail = f"Removed watchpoint {coord}"
                        else:
                            watchpoints.add(coord)
                            current_detail = f"Watching {coord}; replay pauses when an operation touches it."
                elif event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_ESCAPE, pygame.K_q):
                        running = False
                    elif self.manual_step and event.key in (pygame.K_SPACE, pygame.K_RIGHT, pygame.K_RETURN):
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
                    elif event.key in (pygame.K_RIGHT, pygame.K_RETURN):
                        current_detail = apply_next_operation()
                        paused = True
                    elif event.key in (pygame.K_PLUS, pygame.K_EQUALS):
                        current_detail = change_speed(True)
                    elif event.key == pygame.K_MINUS:
                        current_detail = change_speed(False)

            now = time.time()
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
        grid_rect, cell_size, display_width, display_height = self._grid_rect(grid, values)
        display_rows = self._display_rows(values)
        show_row_labels = len(display_rows) > 1

        title_surface = fonts["title"].render(title, True, self.TEXT)
        screen.blit(title_surface, (self.margin, 18))
        self._draw_main_description(screen, fonts, result.description)
        self._draw_grid_headers(screen, fonts, grid_rect, cell_size, display_rows)

        for y, row in enumerate(display_rows):
            if show_row_labels:
                label_rect = pygame.Rect(
                    grid_rect.x - self._row_label_width(display_rows),
                    grid_rect.y + y * cell_size,
                    self._row_label_width(display_rows) - 8,
                    cell_size - 2,
                )
                self._draw_centered_text(screen, fonts["small"], self._row_header_label(row, y), label_rect, self.MUTED)

            for x, display_cell in enumerate(row):
                rect = pygame.Rect(
                    grid_rect.x + x * cell_size,
                    grid_rect.y + y * cell_size,
                    cell_size - 2,
                    cell_size - 2,
                )
                source_coord = display_cell.source_coord
                cell = grid.get(*source_coord) if source_coord and grid.in_bounds(*source_coord) else None
                if display_cell.ellipsis:
                    base_color = self.PANEL
                else:
                    base_color = self.CELL_COLORS.get(cell.cell_type, self.CELL_COLORS[CellType.EMPTY]) if cell else self.CELL_COLORS[CellType.EMPTY]
                color = overlays.get((x, y), base_color) if not display_cell.ellipsis else base_color
                pygame.draw.rect(screen, color, rect, border_radius=4)
                pygame.draw.rect(screen, self.GRID_LINE, rect, width=1, border_radius=4)
                if watchpoints and source_coord in watchpoints:
                    pygame.draw.rect(screen, self.FAIL, rect.inflate(-5, -5), width=3, border_radius=4)

                text_value = display_cell.value if display_cell.value != "" else (cell.value if cell else None)
                label = str(text_value) if text_value is not None else (cell.label if cell else "")
                text_color = self.MUTED if display_cell.ellipsis else self.TEXT
                self._draw_cell_contents(screen, fonts, rect, label, self._cell_index_label(display_cell, show_row_labels), text_color)

        if moving:
            for value, start, end, t, color in moving:
                x = start[0] + (end[0] - start[0]) * t
                y = start[1] + (end[1] - start[1]) * t
                rect = pygame.Rect(x, y, cell_size - 2, cell_size - 2)
                pygame.draw.rect(screen, color, rect, border_radius=4)
                pygame.draw.rect(screen, self.TEXT, rect, width=2, border_radius=4)
                self._draw_centered_text(screen, fonts["cell"], str(value), rect, self.TEXT)

        self._draw_panel(screen, fonts, result, op_index, total_ops, detail, paused, trace_frame, stopped, len(watchpoints or ()))

    def _draw_panel(self, screen, fonts, result, op_index, total_ops, detail, paused, trace_frame=None, stopped=False, watchpoint_count=0):
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
            f"n: {result.n}  Speed: {self.speed_label}",
            f"Watchpoints: {watchpoint_count}",
        ]
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
        text_y = max((button.rect.bottom for button in buttons), default=text_y) + 24
        footer_top = rect.bottom - 96
        content_bottom = footer_top - 14
        previous_clip = screen.get_clip()
        screen.set_clip(pygame.Rect(x, text_y, self.panel_width, max(0, content_bottom - text_y)))

        self._draw_text(screen, fonts["body"], "Current op", x + 18, text_y, self.TEXT)
        text_y += 24
        for line in self._wrap(detail, 33)[:2]:
            self._draw_text(screen, fonts["small"], line, x + 18, text_y, self.MUTED)
            text_y += 20
        text_y += 12

        return_text = result.return_value or "<not returned>"
        return_lines = self._wrap(return_text, 34)[:2]
        return_height = 24 + len(return_lines) * 18
        return_start = max(text_y, content_bottom - return_height)
        variables_bottom = max(text_y, return_start - 12)

        if trace_frame and text_y + 34 < variables_bottom:
            prefix = "Breakpoint line" if trace_frame.breakpoint else "Line"
            self._draw_text(screen, fonts["body"], f"{prefix} {trace_frame.line_no} variables", x + 18, text_y, self.TEXT)
            text_y += 24
            truncated = False
            for name, value in list(trace_frame.locals.items())[:9]:
                for line in self._wrap(f"{name} = {value}", 34)[:2]:
                    if text_y + 18 > variables_bottom:
                        truncated = True
                        break
                    self._draw_text(screen, fonts["small"], line, x + 18, text_y, self.MUTED)
                    text_y += 18
                if truncated:
                    if text_y + 18 <= variables_bottom:
                        self._draw_text(screen, fonts["small"], "...", x + 18, text_y, self.MUTED)
                    break
            text_y += 12

        text_y = max(text_y, content_bottom - return_height)
        self._draw_text(screen, fonts["body"], "Return value", x + 18, text_y, self.TEXT)
        text_y += 24
        for line in return_lines:
            if text_y + 18 > content_bottom:
                break
            self._draw_text(screen, fonts["small"], line, x + 18, text_y, self.MUTED)
            text_y += 18
        screen.set_clip(previous_clip)

        message_lines = self._wrap(result.message, 33)[:4]
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
        first_display = self._display_coord_for_source(values, first)
        second_display = self._display_coord_for_source(values, second)
        if first_display is None or second_display is None:
            return
        a_rect = self._cell_rect(grid_rect, cell_size, first_display)
        b_rect = self._cell_rect(grid_rect, cell_size, second_display)
        a_value = self._value_at(values, first)
        b_value = self._value_at(values, second)
        hidden = {first_display: self.SWAP, second_display: self.SWAP}

        for frame in range(self.swap_frames + 1):
            t = frame / self.swap_frames
            moving = [
                (a_value, a_rect.topleft, b_rect.topleft, t, self.SWAP),
                (b_value, b_rect.topleft, a_rect.topleft, t, self.SWAP),
            ]
            trace_frame = self._trace_for_op(result.trace_frames, op_index)
            self._draw(screen, fonts, grid, values, hidden, title, result, op_index, total_ops, f"swap: {detail}", False, moving, trace_frame=trace_frame)
            import pygame
            pygame.display.flip()
            clock.tick(self.fps)

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
        import pygame

        available_width = self.width - self.panel_width - self.margin * 3
        grid_top = self._grid_top()
        available_height = self.height - grid_top - self.margin
        display_rows = self._display_rows(values) if values is not None else []
        label_width = self._row_label_width(display_rows)
        available_width -= label_width
        value_width = max((len(row) for row in display_rows), default=0)
        value_height = len(display_rows)
        display_width = max(value_width, 1)
        display_height = max(value_height, 1)
        cell_size = max(22, min(64, available_width // display_width, available_height // display_height))
        grid_width = cell_size * display_width
        grid_height = cell_size * display_height
        x = self.margin + label_width
        y = grid_top + max(0, (available_height - grid_height) // 2)
        return pygame.Rect(x, y, grid_width, grid_height), cell_size, display_width, display_height

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
        grid_rect, cell_size, display_width, display_height = self._grid_rect(grid, values)
        x = (pos[0] - grid_rect.x) // cell_size
        y = (pos[1] - grid_rect.y) // cell_size
        display_rows = self._display_rows(values)
        if 0 <= y < len(display_rows) and 0 <= x < len(display_rows[int(y)]):
            return display_rows[int(y)][int(x)].source_coord
        return None

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

    def _draw_grid_headers(self, screen, fonts, grid_rect, cell_size: int, display_rows: list[list[DisplayCell]]):
        import pygame

        if not display_rows or not display_rows[0]:
            return
        axis_y = max(0, grid_rect.y - 24)
        for x, display_cell in enumerate(display_rows[0]):
            label = self._column_header_label(display_cell)
            if not label:
                continue
            label_rect = pygame.Rect(
                grid_rect.x + x * cell_size,
                axis_y,
                cell_size - 2,
                18,
            )
            self._draw_centered_text(screen, fonts["small"], label, label_rect, self.MUTED)

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
        if display_cell.ellipsis:
            return ""
        if display_cell.source_coord is None:
            return ""
        return ""

    def _column_header_label(self, display_cell: DisplayCell) -> str:
        if display_cell.ellipsis:
            return "..."
        if display_cell.source_coord is None:
            return ""
        column, _ = display_cell.source_coord
        return f"{column}:"

    def _row_header_label(self, row: list[DisplayCell], display_y: int) -> str:
        for display_cell in row:
            if display_cell.ellipsis:
                continue
            if display_cell.source_coord is not None:
                return f"{display_cell.source_coord[1]}:"
        return "..."

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
        if not values:
            return [[]]
        rows: list[list[DisplayCell]] = []
        if len(values) <= MAX_VISIBLE_ROW_ITEMS:
            for y, row in enumerate(values):
                rows.append(self._display_row(row, y))
            return rows or [[]]

        for y in range(MAX_VISIBLE_ROW_ITEMS):
            rows.append(self._display_row(values[y], y))
        rows.append(self._ellipsis_row(rows[0] if rows else []))
        rows.append(self._display_row(values[-1], len(values) - 1))
        return rows or [[]]

    def _display_row(self, row: list[Any], y: int) -> list[DisplayCell]:
        if len(row) <= MAX_VISIBLE_ROW_ITEMS:
            return [DisplayCell(value=value, source_coord=(x, y)) for x, value in enumerate(row)]
        visible = [DisplayCell(value=row[x], source_coord=(x, y)) for x in range(MAX_VISIBLE_ROW_ITEMS)]
        visible.append(DisplayCell(value="...", ellipsis=True))
        visible.append(DisplayCell(value=row[-1], source_coord=(len(row) - 1, y)))
        return visible

    def _ellipsis_row(self, reference_row: list[DisplayCell]) -> list[DisplayCell]:
        width = max(1, len(reference_row))
        return [DisplayCell(value="...", ellipsis=True) for _ in range(width)]

    def _row_label_width(self, display_rows: list[list[DisplayCell]]) -> int:
        if len(display_rows) <= 1:
            return 0
        return 44

    def _display_coord_for_source(self, values: list[list[Any]], source_coord: tuple[int, int]) -> Optional[tuple[int, int]]:
        source_x, source_y = source_coord
        if source_y < 0 or source_y >= len(values):
            return None
        display_y = self._display_y_for_source(values, source_y)
        if display_y is None:
            return None
        row = values[source_y]
        if source_x < 0 or source_x >= len(row):
            return None
        if len(row) <= MAX_VISIBLE_ROW_ITEMS:
            return source_x, display_y
        if source_x < MAX_VISIBLE_ROW_ITEMS:
            return source_x, display_y
        if source_x == len(row) - 1:
            return MAX_VISIBLE_ROW_ITEMS + 1, display_y
        return None

    def _display_y_for_source(self, values: list[list[Any]], source_y: int) -> Optional[int]:
        if len(values) <= MAX_VISIBLE_ROW_ITEMS:
            return source_y
        if source_y < MAX_VISIBLE_ROW_ITEMS:
            return source_y
        if source_y == len(values) - 1:
            return MAX_VISIBLE_ROW_ITEMS + 1
        return None

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
        coords = self._extract_coords(op.detail)
        if op.op_type == OpType.COMPARE and len(coords) >= 2:
            first = self._display_coord_for_source(values, coords[0])
            second = self._display_coord_for_source(values, coords[1])
            if first is not None and second is not None:
                return {first: self.COMPARE_A, second: self.COMPARE_B}
            return {}
        if op.op_type == OpType.SWAP and len(coords) >= 2:
            first = self._display_coord_for_source(values, coords[0])
            second = self._display_coord_for_source(values, coords[1])
            if first is not None and second is not None:
                return {first: self.SWAP, second: self.SWAP}
            return {}
        if op.op_type == OpType.READ and coords:
            coord = self._display_coord_for_source(values, coords[0])
            return {coord: self.READ} if coord is not None else {}
        if op.op_type == OpType.WRITE and coords:
            coord = self._display_coord_for_source(values, coords[0])
            return {coord: self.WRITE} if coord is not None else {}
        insert_match = re.search(r"list\.insert\((-?\d+),", op.detail)
        if insert_match:
            coord = self._display_coord_for_source(values, (max(0, int(insert_match.group(1))), 0))
            return {coord: self.WRITE} if coord is not None else {}
        pop_match = re.search(r"list\.pop\((-?\d+)\)", op.detail)
        if pop_match:
            coord = self._display_coord_for_source(values, (max(0, int(pop_match.group(1))), 0))
            return {coord: self.FAIL} if coord is not None else {}
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
