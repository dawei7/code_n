"""Optimal solution for LeetCode 1040: Moving Stones Until Consecutive II."""


def solve(stones: list[int]) -> list[int]:
    stones.sort()
    n = len(stones)
    max_moves = max(
        stones[-1] - stones[1] + 1 - (n - 1),
        stones[-2] - stones[0] + 1 - (n - 1),
    )

    min_moves = n
    left = 0
    for right, stone in enumerate(stones):
        while stone - stones[left] + 1 > n:
            left += 1
        already = right - left + 1
        if already == n - 1 and stone - stones[left] + 1 == n - 1:
            min_moves = min(min_moves, 2)
        else:
            min_moves = min(min_moves, n - already)
    return [min_moves, max_moves]
