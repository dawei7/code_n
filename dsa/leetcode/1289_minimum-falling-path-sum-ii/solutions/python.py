def solve(grid):
    n = len(grid)
    prev = grid[0][:]
    for r in range(1, n):
        first = second = float("inf")
        first_index = -1
        for c, value in enumerate(prev):
            if value < first:
                second = first
                first = value
                first_index = c
            elif value < second:
                second = value
        prev = [grid[r][c] + (second if c == first_index else first) for c in range(n)]
    return min(prev)
