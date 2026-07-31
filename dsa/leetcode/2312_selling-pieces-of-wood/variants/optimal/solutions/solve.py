from typing import List


def solve(m: int, n: int, prices: List[List[int]]) -> int:
    best = [[0] * (n + 1) for _ in range(m + 1)]
    for height, width, price in prices:
        best[height][width] = price

    for height in range(1, m + 1):
        for width in range(1, n + 1):
            value = best[height][width]
            for cut in range(1, height // 2 + 1):
                value = max(
                    value,
                    best[cut][width] + best[height - cut][width],
                )
            for cut in range(1, width // 2 + 1):
                value = max(
                    value,
                    best[height][cut] + best[height][width - cut],
                )
            best[height][width] = value

    return best[m][n]
