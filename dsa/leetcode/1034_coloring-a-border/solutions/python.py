"""Optimal app-local solution for LeetCode 1034."""


def solve(grid, row, col, color):
    rows, cols = len(grid), len(grid[0])
    original = grid[row][col]
    seen = {(row, col)}
    stack = [(row, col)]
    border = []

    while stack:
        current_row, current_col = stack.pop()
        is_border = current_row in (0, rows - 1) or current_col in (0, cols - 1)
        for row_step, col_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_row = current_row + row_step
            next_col = current_col + col_step
            if not (0 <= next_row < rows and 0 <= next_col < cols):
                is_border = True
            elif grid[next_row][next_col] != original:
                is_border = True
            elif (next_row, next_col) not in seen:
                seen.add((next_row, next_col))
                stack.append((next_row, next_col))
        if is_border:
            border.append((current_row, current_col))

    for border_row, border_col in border:
        grid[border_row][border_col] = color
    return grid
