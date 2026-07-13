from functools import lru_cache
from math import comb


def solve(balls):
    total = sum(balls)
    if len(balls) > 8 or total > 48:
        return 0.0
    half = total // 2
    if total % 2:
        return 0.0
    colors = len(balls)
    total_ways = comb(total, half)

    @lru_cache(None)
    def dfs(index, left_count, left_distinct, right_distinct):
        if index == colors:
            return 1 if left_count == half and left_distinct == right_distinct else 0
        ways = 0
        count = balls[index]
        for left in range(count + 1):
            if left_count + left > half:
                break
            right = count - left
            ways += (
                comb(count, left)
                * dfs(index + 1, left_count + left, left_distinct + (left > 0), right_distinct + (right > 0))
            )
        return ways

    return dfs(0, 0, 0, 0) / total_ways if total_ways else 0.0
