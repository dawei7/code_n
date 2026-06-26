"""Optimal solution for LeetCode 1030: Matrix Cells in Distance Order."""


def solve(rows: int, cols: int, r_center: int, c_center: int) -> list[list[int]]:
    cells = [[r, c] for r in range(rows) for c in range(cols)]
    cells.sort(key=lambda cell: abs(cell[0] - r_center) + abs(cell[1] - c_center))
    return cells
