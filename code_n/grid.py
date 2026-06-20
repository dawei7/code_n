"""2D Grid Engine - The core world representation.

The grid is a 2D array where each cell can hold values, colors, and state.
Players interact with the grid through the API to solve algorithm challenges.
"""

from dataclasses import dataclass
from enum import IntEnum
from typing import Any


class CellType(IntEnum):
    EMPTY = 0
    WALL = 1
    VALUE = 2
    MARKER = 3
    START = 4
    GOAL = 5
    PATH = 6
    VISITED = 7
    CURRENT = 8
    SORTED = 9
    UNSORTED = 10
    PIVOT = 11
    COMPARE_A = 12
    COMPARE_B = 13


# ANSI color codes for terminal rendering
CELL_COLORS = {
    CellType.EMPTY: "\033[90m",       # Dark gray
    CellType.WALL: "\033[97;40m",     # White on black
    CellType.VALUE: "\033[37m",       # White
    CellType.MARKER: "\033[93m",      # Yellow
    CellType.START: "\033[92m",       # Green
    CellType.GOAL: "\033[91m",        # Red
    CellType.PATH: "\033[96m",        # Cyan
    CellType.VISITED: "\033[94m",     # Blue
    CellType.CURRENT: "\033[95m",     # Magenta
    CellType.SORTED: "\033[92m",      # Green
    CellType.UNSORTED: "\033[37m",    # White
    CellType.PIVOT: "\033[93m",       # Yellow
    CellType.COMPARE_A: "\033[91m",   # Red
    CellType.COMPARE_B: "\033[96m",   # Cyan
}

RESET = "\033[0m"


@dataclass
class Cell:
    cell_type: CellType = CellType.EMPTY
    value: Any = None
    label: str = ""

    def __repr__(self):
        if self.value is not None:
            return f"Cell({self.cell_type.name}, {self.value})"
        return f"Cell({self.cell_type.name})"


class Grid:
    """2D grid world for algorithm visualization."""

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self._cells: list[list[Cell]] = [
            [Cell() for _ in range(width)] for _ in range(height)
        ]

    def get(self, x: int, y: int) -> Cell:
        if not self.in_bounds(x, y):
            raise IndexError(f"Position ({x}, {y}) out of bounds ({self.width}x{self.height})")
        return self._cells[y][x]

    def set(self, x: int, y: int, cell_type: CellType = CellType.VALUE,
            value: Any = None, label: str = ""):
        if not self.in_bounds(x, y):
            raise IndexError(f"Position ({x}, {y}) out of bounds ({self.width}x{self.height})")
        self._cells[y][x] = Cell(cell_type, value, label)

    def set_value(self, x: int, y: int, value: Any):
        if not self.in_bounds(x, y):
            raise IndexError(f"Position ({x}, {y}) out of bounds ({self.width}x{self.height})")
        self._cells[y][x].value = value

    def set_type(self, x: int, y: int, cell_type: CellType):
        if not self.in_bounds(x, y):
            raise IndexError(f"Position ({x}, {y}) out of bounds ({self.width}x{self.height})")
        self._cells[y][x].cell_type = cell_type

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def clear(self):
        for y in range(self.height):
            for x in range(self.width):
                self._cells[y][x] = Cell()

    def fill_row(self, y: int, values: list[Any], cell_type: CellType = CellType.VALUE):
        for x, val in enumerate(values):
            if x < self.width:
                self._cells[y][x] = Cell(cell_type, val)

    def get_row_values(self, y: int) -> list[Any]:
        return [self._cells[y][x].value for x in range(self.width)]

    def get_col_values(self, x: int) -> list[Any]:
        return [self._cells[y][x].value for y in range(self.height)]

    def swap_cells(self, x1: int, y1: int, x2: int, y2: int):
        self._cells[y1][x1], self._cells[y2][x2] = (
            self._cells[y2][x2], self._cells[y1][x1]
        )

    def find_cells(self, cell_type: CellType) -> list[tuple[int, int]]:
        result = []
        for y in range(self.height):
            for x in range(self.width):
                if self._cells[y][x].cell_type == cell_type:
                    result.append((x, y))
        return result

    def to_value_array(self) -> list[list[Any]]:
        """Export grid as a 2D array of values."""
        return [
            [self._cells[y][x].value for x in range(self.width)]
            for y in range(self.height)
        ]

    def from_value_array(self, arr: list[list[Any]], cell_type: CellType = CellType.VALUE):
        """Import a 2D array of values into the grid."""
        for y, row in enumerate(arr):
            for x, val in enumerate(row):
                if self.in_bounds(x, y):
                    self._cells[y][x] = Cell(cell_type, val)
