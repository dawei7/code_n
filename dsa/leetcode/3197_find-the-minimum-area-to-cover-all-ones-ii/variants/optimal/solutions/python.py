from functools import lru_cache


def solve(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])

    row_prefix = [[0] * (n + 1) for _ in range(m)]
    col_prefix = [[0] * (m + 1) for _ in range(n)]
    for r in range(m):
        for c in range(n):
            row_prefix[r][c + 1] = row_prefix[r][c] + grid[r][c]
    for c in range(n):
        for r in range(m):
            col_prefix[c][r + 1] = col_prefix[c][r] + grid[r][c]

    @lru_cache(maxsize=None)
    def area(r1: int, r2: int, c1: int, c2: int) -> int:
        if r1 > r2 or c1 > c2:
            return 0

        top = bottom = left = right = -1
        for r in range(r1, r2 + 1):
            if row_prefix[r][c2 + 1] - row_prefix[r][c1]:
                top = r
                break
        if top == -1:
            return 0
        for r in range(r2, r1 - 1, -1):
            if row_prefix[r][c2 + 1] - row_prefix[r][c1]:
                bottom = r
                break
        for c in range(c1, c2 + 1):
            if col_prefix[c][r2 + 1] - col_prefix[c][r1]:
                left = c
                break
        for c in range(c2, c1 - 1, -1):
            if col_prefix[c][r2 + 1] - col_prefix[c][r1]:
                right = c
                break
        return (bottom - top + 1) * (right - left + 1)

    answer = float("inf")

    for first in range(m - 2):
        for second in range(first + 1, m - 1):
            answer = min(
                answer,
                area(0, first, 0, n - 1)
                + area(first + 1, second, 0, n - 1)
                + area(second + 1, m - 1, 0, n - 1),
            )

    for first in range(n - 2):
        for second in range(first + 1, n - 1):
            answer = min(
                answer,
                area(0, m - 1, 0, first)
                + area(0, m - 1, first + 1, second)
                + area(0, m - 1, second + 1, n - 1),
            )

    for row_cut in range(m - 1):
        for col_cut in range(n - 1):
            answer = min(
                answer,
                area(0, row_cut, 0, col_cut)
                + area(0, row_cut, col_cut + 1, n - 1)
                + area(row_cut + 1, m - 1, 0, n - 1),
                area(0, row_cut, 0, n - 1)
                + area(row_cut + 1, m - 1, 0, col_cut)
                + area(row_cut + 1, m - 1, col_cut + 1, n - 1),
                area(0, m - 1, 0, col_cut)
                + area(0, row_cut, col_cut + 1, n - 1)
                + area(row_cut + 1, m - 1, col_cut + 1, n - 1),
                area(0, row_cut, 0, col_cut)
                + area(row_cut + 1, m - 1, 0, col_cut)
                + area(0, m - 1, col_cut + 1, n - 1),
            )

    return int(answer)
