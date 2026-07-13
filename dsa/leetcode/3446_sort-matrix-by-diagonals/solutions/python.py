def solve(grid: list[list[int]]) -> list[list[int]]:
    n = len(grid)

    def sort_diagonal(row: int, col: int, reverse: bool) -> None:
        cells = []
        r, c = row, col
        while r < n and c < n:
            cells.append((r, c))
            r += 1
            c += 1
        values = sorted((grid[r][c] for r, c in cells), reverse=reverse)
        for (r, c), value in zip(cells, values):
            grid[r][c] = value

    for row in range(n):
        sort_diagonal(row, 0, True)
    for col in range(1, n):
        sort_diagonal(0, col, False)

    return grid
