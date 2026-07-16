"""Optimal app-local solution for LeetCode 1559."""


def solve(grid: list[list[str]]) -> bool:
    """Detect a non-parent edge in a same-letter grid component."""
    rows = len(grid)
    columns = len(grid[0])
    seen = [[False] * columns for _ in range(rows)]

    for start_row in range(rows):
        for start_column in range(columns):
            if seen[start_row][start_column]:
                continue

            seen[start_row][start_column] = True
            stack = [(start_row, start_column, -1, -1)]
            while stack:
                row, column, parent_row, parent_column = stack.pop()
                for row_step, column_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_row = row + row_step
                    next_column = column + column_step
                    if not (0 <= next_row < rows and 0 <= next_column < columns):
                        continue
                    if grid[next_row][next_column] != grid[row][column]:
                        continue
                    if (next_row, next_column) == (parent_row, parent_column):
                        continue
                    if seen[next_row][next_column]:
                        return True
                    seen[next_row][next_column] = True
                    stack.append((next_row, next_column, row, column))

    return False
