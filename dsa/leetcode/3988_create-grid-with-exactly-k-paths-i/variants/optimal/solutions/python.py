def solve(m: int, n: int, k: int) -> list[str]:
    """Construct an m-by-n obstacle grid having exactly k monotone paths."""

    grid = [["#"] * n for _ in range(m)]
    blocked: set[tuple[int, int]] = set()

    if k == 1:
        height = width = 1
    elif k == 2 and m >= 2 and n >= 2:
        height, width = 2, 2
    elif k == 3 and m >= 2 and n >= 3:
        height, width = 2, 3
    elif k == 3 and m >= 3 and n >= 2:
        height, width = 3, 2
    elif k == 4 and m >= 2 and n >= 4:
        height, width = 2, 4
    elif k == 4 and m >= 4 and n >= 2:
        height, width = 4, 2
    elif k == 4 and m >= 3 and n >= 3:
        height = width = 3
        blocked = {(0, 2), (2, 0)}
    else:
        return []

    for row in range(height):
        for column in range(width):
            if (row, column) not in blocked:
                grid[row][column] = "."

    exit_row = height - 1
    exit_column = width - 1
    for column in range(exit_column, n):
        grid[exit_row][column] = "."
    for row in range(exit_row, m):
        grid[row][n - 1] = "."

    return ["".join(row) for row in grid]
