"""Optimal solution for LeetCode 1034: Coloring A Border."""


def solve(grid: list[list[int]], row: int, col: int, color: int) -> list[list[int]]:
    rows, cols = len(grid), len(grid[0])
    original = grid[row][col]
    seen: set[tuple[int, int]] = set()
    border: list[tuple[int, int]] = []

    def dfs(r: int, c: int) -> None:
        seen.add((r, c))
        is_border = r in (0, rows - 1) or c in (0, cols - 1)
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] != original:
                is_border = True
            elif (nr, nc) not in seen:
                dfs(nr, nc)
        if is_border:
            border.append((r, c))

    dfs(row, col)
    for r, c in border:
        grid[r][c] = color
    return grid
