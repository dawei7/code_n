"""Optimal solution for LeetCode 361: Bomb Enemy."""


def solve(grid: list[list[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    column_hits = [0] * cols
    best = 0
    row_hits = 0

    for row in range(rows):
        for col in range(cols):
            if col == 0 or grid[row][col - 1] == "W":
                row_hits = 0
                scan_col = col
                while scan_col < cols and grid[row][scan_col] != "W":
                    row_hits += grid[row][scan_col] == "E"
                    scan_col += 1

            if row == 0 or grid[row - 1][col] == "W":
                column_hits[col] = 0
                scan_row = row
                while scan_row < rows and grid[scan_row][col] != "W":
                    column_hits[col] += grid[scan_row][col] == "E"
                    scan_row += 1

            if grid[row][col] == "0":
                best = max(best, row_hits + column_hits[col])

    return best

