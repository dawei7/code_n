def solve(grid: list[list[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    flips = 0

    for r in range(m // 2):
        for c in range(n // 2):
            ones = (
                grid[r][c]
                + grid[r][n - 1 - c]
                + grid[m - 1 - r][c]
                + grid[m - 1 - r][n - 1 - c]
            )
            flips += min(ones, 4 - ones)

    mismatched_middle_pairs = 0
    middle_pair_ones = 0

    if m % 2:
        r = m // 2
        for c in range(n // 2):
            left = grid[r][c]
            right = grid[r][n - 1 - c]
            if left != right:
                mismatched_middle_pairs += 1
            elif left == 1:
                middle_pair_ones += 2

    if n % 2:
        c = n // 2
        for r in range(m // 2):
            top = grid[r][c]
            bottom = grid[m - 1 - r][c]
            if top != bottom:
                mismatched_middle_pairs += 1
            elif top == 1:
                middle_pair_ones += 2

    flips += mismatched_middle_pairs

    if m % 2 and n % 2 and grid[m // 2][n // 2] == 1:
        flips += 1

    if mismatched_middle_pairs == 0 and middle_pair_ones % 4 == 2:
        flips += 2

    return flips
