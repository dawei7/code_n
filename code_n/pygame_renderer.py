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
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(f"{GAME_TITLE} - {title}")
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
                overlays = self._overlays_for_op(ops[op_index - 1])
            else:
                overlays = {}

            trace_frame = self._trace_for_op(result.trace_frames, op_index)
            self._draw(screen, fonts, grid, visual_values, overlays, title, result, op_index, len(ops), current_detail, paused, trace_frame=trace_frame, stopped=stopped, watchpoints=watchpoints)
            pygame.display.flip()
            clock.tick(self.fps)

        pygame.quit()

    def _draw(self, screen, fonts, grid, values, overlays, title, result, op_index, total_ops, detail, paused, moving=None, trace_frame=None, stopped=False, watchpoints=None):
        import pygame

        screen.fill(self.BACKGROUND)
        grid_rect, cell_size, display_width, display_height = self._grid_rect(grid, values)

        title_surface = fonts["title"].render(title, True, self.TEXT)
        screen.blit(title_surface, (self.margin, 18))

        for y in range(display_height):
            for x in range(display_width):
                rect = pygame.Rect(
                    grid_rect.x + x * cell_size,
                    grid_rect.y + y * cell_size,
                    cell_size - 2,
                    cell_size - 2,
                )
                cell = grid.get(x, y) if grid.in_bounds(x, y) else None
                base_color = self.CELL_COLORS.get(cell.cell_type, self.CELL_COLORS[CellType.EMPTY]) if cell else self.CELL_COLORS[CellType.EMPTY]
                color = overlays.get((x, y), base_color)
                pygame.draw.rect(screen, color, rect, border_radius=4)
                pygame.draw.rect(screen, self.GRID_LINE, rect, width=1, border_radius=4)
                if watchpoints and (x, y) in watchpoints:
                    pygame.draw.rect(screen, self.FAIL, rect.inflate(-5, -5), width=3, border_radius=4)

                text_value = values[y][x] if y < len(values) and x < len(values[y]) else (cell.value if cell else None)
                label = str(text_value) if text_value is not None else (cell.label if cell else "")
                if label:
                    self._draw_centered_text(screen, fonts["cell"], label, rect, self.TEXT)

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

        if result.description:
            text_y += 4
            self._draw_text(screen, fonts["body"], "Description", x + 18, text_y, self.TEXT)
            text_y += 22
            for line in self._wrap(result.description.replace("\n", " "), 33)[:2]:
                self._draw_text(screen, fonts["small"], line, x + 18, text_y, self.MUTED)
                text_y += 18

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

        return_text = result.return_value or "<not returned>"
        return_lines = self._wrap(return_text, 34)[:2]
        return_height = 24 + len(return_lines) * 18
        return_start_limit = max(text_y + 10, content_bottom - return_height)

        if trace_frame and text_y + 34 < return_start_limit:
            text_y += 10
            prefix = "Breakpoint line" if trace_frame.breakpoint else "Line"
            self._draw_text(screen, fonts["body"], f"{prefix} {trace_frame.line_no} variables", x + 18, text_y, self.TEXT)
            text_y += 24
            truncated = False
            for name, value in list(trace_frame.locals.items())[:9]:
                for line in self._wrap(f"{name} = {value}", 34)[:2]:
                    if text_y + 18 > return_start_limit:
                        truncated = True
                        break
                    self._draw_text(screen, fonts["small"], line, x + 18, text_y, self.MUTED)
                    text_y += 18
                if truncated:
                    if text_y + 18 <= return_start_limit:
                        self._draw_text(screen, fonts["small"], "...", x + 18, text_y, self.MUTED)
                    break

        text_y = min(max(text_y + 10, return_start_limit), content_bottom - return_height)
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
        a_rect = self._cell_rect(grid_rect, cell_size, first)
        b_rect = self._cell_rect(grid_rect, cell_size, second)
        a_value = self._value_at(values, first)
        b_value = self._value_at(values, second)
        hidden = {first: self.SWAP, second: self.SWAP}

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
        available_height = self.height - self.margin * 3 - 36
        value_width = max((len(row) for row in values), default=0) if values else 0
        value_height = len(values) if values else 0
        display_width = max(grid.width, value_width, 1)
        display_height = max(grid.height, value_height, 1)
        cell_size = max(22, min(64, available_width // display_width, available_height // display_height))
        grid_width = cell_size * display_width
        grid_height = cell_size * display_height
        x = self.margin
        y = 70 + max(0, (available_height - grid_height) // 2)
        return pygame.Rect(x, y, grid_width, grid_height), cell_size, display_width, display_height

    def _cell_rect(self, grid_rect, cell_size, coord):
        import pygame

        x, y = coord
        return pygame.Rect(grid_rect.x + x * cell_size, grid_rect.y + y * cell_size, cell_size - 2, cell_size - 2)

    def _coord_at_pos(self, pos, grid, values) -> Optional[tuple[int, int]]:
        grid_rect, cell_size, display_width, display_height = self._grid_rect(grid, values)
        x = (pos[0] - grid_rect.x) // cell_size
        y = (pos[1] - grid_rect.y) // cell_size
        if 0 <= x < display_width and 0 <= y < display_height:
            return int(x), int(y)
        return None

    def _op_touches_watchpoint(self, op: OpRecord, watchpoints: set[tuple[int, int]]) -> bool:
        if not watchpoints:
            return False
        touched = set(self._extract_coords(op.detail))
        append_match = re.search(r"list\.append", op.detail)
        if append_match:
            touched.add((0, 0))
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

    def _draw_text(self, screen, font, text, x, y, color):
        screen.blit(font.render(text, True, color), (x, y))

    def _values_from_grid(self, grid: Grid) -> list[list[Any]]:
        return [[grid.get(x, y).value if grid.get(x, y).value is not None else grid.get(x, y).label for x in range(grid.width)] for y in range(grid.height)]

    def _copy_values(self, values: list[list[Any]]) -> list[list[Any]]:
        return [row[:] for row in values]

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

    def _overlays_for_op(self, op: OpRecord) -> dict[tuple[int, int], tuple[int, int, int]]:
        coords = self._extract_coords(op.detail)
        if op.op_type == OpType.COMPARE and len(coords) >= 2:
            return {coords[0]: self.COMPARE_A, coords[1]: self.COMPARE_B}
        if op.op_type == OpType.SWAP and len(coords) >= 2:
            return {coords[0]: self.SWAP, coords[1]: self.SWAP}
        if op.op_type == OpType.READ and coords:
            return {coords[0]: self.READ}
        if op.op_type == OpType.WRITE and coords:
            return {coords[0]: self.WRITE}
        append_match = re.search(r"list\.append", op.detail)
        if append_match:
            return {(0, 0): self.WRITE}
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
