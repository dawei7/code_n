def solve(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    horizontal = [[0] * (cols + 1) for _ in range(rows + 1)]
    vertical = [[0] * (cols + 1) for _ in range(rows + 1)]

    best = 0
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if grid[r - 1][c - 1] == 1:
                horizontal[r][c] = horizontal[r][c - 1] + 1
                vertical[r][c] = vertical[r - 1][c] + 1
                side = min(horizontal[r][c], vertical[r][c])
                while side > best:
                    if horizontal[r - side + 1][c] >= side and vertical[r][c - side + 1] >= side:
                        best = side
                        break
                    side -= 1
    return best * best
