def solve(grid: list[list[int]]) -> bool:
    n = len(grid)
    positions = [None] * (n * n)

    for row in range(n):
        for col in range(n):
            positions[grid[row][col]] = (row, col)

    if positions[0] != (0, 0):
        return False

    for previous, current in zip(positions, positions[1:]):
        row_change = abs(previous[0] - current[0])
        col_change = abs(previous[1] - current[1])
        if sorted((row_change, col_change)) != [1, 2]:
            return False

    return True
