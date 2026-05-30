"""Terminal-based 2D renderer with ANSI colors.

Renders the grid state to the terminal with color-coded cells,
supports animation/replay of grid history, and displays stats.
"""

import os
import sys
import time
from typing import Optional

from .grid import Grid, Cell, CellType, CELL_COLORS, RESET
from .counter import OperationCounter, OpStats, ComplexityClass


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def move_cursor_home():
    sys.stdout.write("\033[H")
    sys.stdout.flush()


class Renderer:
    """Renders the grid and stats to the terminal."""

    def __init__(self, cell_width: int = 4):
        self.cell_width = cell_width
        self._frame_delay = 0.3

    @property
    def frame_delay(self) -> float:
        return self._frame_delay

    @frame_delay.setter
    def frame_delay(self, value: float):
        self._frame_delay = max(0.01, value)

    def render_cell(self, cell: Cell) -> str:
        color = CELL_COLORS.get(cell.cell_type, "")
        if cell.value is not None:
            text = str(cell.value)
        elif cell.label:
            text = cell.label
        elif cell.cell_type == CellType.WALL:
            text = "█" * self.cell_width
            return f"{color}{text}{RESET}"
        elif cell.cell_type == CellType.EMPTY:
            text = "·"
        else:
            text = cell.cell_type.name[0]

        padded = text.center(self.cell_width)
        return f"{color}{padded}{RESET}"

    def render_grid(self, grid: Grid, title: str = "") -> str:
        lines = []
        if title:
            lines.append(f"\033[1m{title}\033[0m")
            lines.append("")

        # Top border
        border = "┌" + "─" * (grid.width * self.cell_width + grid.width - 1) + "┐"
        lines.append(border)

        for y in range(grid.height):
            row_parts = []
            for x in range(grid.width):
                cell = grid.get(x, y)
                row_parts.append(self.render_cell(cell))
            lines.append("│" + "│".join(row_parts) + "│")

        # Bottom border
        border = "└" + "─" * (grid.width * self.cell_width + grid.width - 1) + "┘"
        lines.append(border)

        return "\n".join(lines)

    def render_stats(self, stats: OpStats, n: int,
                     complexity: ComplexityClass,
                     threshold: Optional[ComplexityClass] = None) -> str:
        lines = [
            "",
            "\033[1m── Statistics ──\033[0m",
            f"  Input size (n):  {n}",
            f"  Total operations: {stats.total}",
            f"    Comparisons:    {stats.comparisons}",
            f"    Swaps:          {stats.swaps}",
            f"    Reads:          {stats.reads}",
            f"    Writes:         {stats.writes}",
            f"    Calls:          {stats.calls}",
            f"  Complexity:       {complexity.value}",
        ]
        if threshold:
            passed = stats.total <= _threshold_limit(n, threshold)
            status = "\033[92mPASS\033[0m" if passed else "\033[91mFAIL\033[0m"
            lines.append(f"  Required:         {threshold.value}  [{status}]")
        return "\n".join(lines)

    def render_frame(self, grid: Grid, title: str = "",
                     stats: Optional[OpStats] = None,
                     n: int = 0,
                     complexity: Optional[ComplexityClass] = None,
                     threshold: Optional[ComplexityClass] = None):
        """Render a single frame to terminal."""
        move_cursor_home()
        output = self.render_grid(grid, title)
        if stats and complexity:
            output += self.render_stats(stats, n, complexity, threshold)
        print(output)

    def play_history(self, grid: Grid, title: str = ""):
        """Animate the grid history."""
        clear_screen()
        for i, frame_cells in enumerate(grid.history):
            # Temporarily set grid cells to this frame
            original = grid._cells
            grid._cells = frame_cells
            frame_title = f"{title} [Frame {i + 1}/{grid.frame_count}]"
            move_cursor_home()
            print(self.render_grid(grid, frame_title))
            grid._cells = original
            time.sleep(self._frame_delay)

        # Show final state
        move_cursor_home()
        print(self.render_grid(grid, f"{title} [Final]"))

    def display(self, grid: Grid, title: str = "",
                counter: Optional[OperationCounter] = None,
                n: int = 0,
                threshold: Optional[ComplexityClass] = None):
        """Full display: grid + stats."""
        clear_screen()
        output = self.render_grid(grid, title)
        if counter:
            stats = counter.stats
            complexity = counter.classify(n)
            output += self.render_stats(stats, n, complexity, threshold)
        print(output)


def _threshold_limit(n: int, max_class: ComplexityClass) -> int:
    import math
    limits = {
        ComplexityClass.O_1: 10,
        ComplexityClass.O_LOG_N: int(math.log2(max(n, 2)) * 3) + 10,
        ComplexityClass.O_N: n * 3 + 10,
        ComplexityClass.O_N_LOG_N: int(n * math.log2(max(n, 2)) * 2) + 10,
        ComplexityClass.O_N2: n * n * 2 + 10,
        ComplexityClass.O_N3: n * n * n * 2 + 10,
        ComplexityClass.O_2N: 2 ** min(n, 25) + 10,
    }
    return limits.get(max_class, 999999)
