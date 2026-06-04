"""Terminal-based 2D renderer with ANSI colors.

Renders the grid state to the terminal with color-coded cells
and displays stats after a run.
"""

import os
import sys
from typing import Optional

from .grid import Grid, Cell, CellType, CELL_COLORS, RESET
from .counter import OperationCounter, OpStats, ComplexityClass, limit_for


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
            # Use the same limit table as the engine so the on-screen
            # PASS/FAIL matches the actual pass/fail result.
            budget = limit_for(n, threshold)
            passed = stats.total <= budget
            status = "\033[92mPASS\033[0m" if passed else "\033[91mFAIL\033[0m"
            lines.append(f"  Required:         {threshold.value}  [{status}]")
            lines.append(f"  Budget:           {budget} ops")
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
