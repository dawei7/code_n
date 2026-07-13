"""Optimal solution for LeetCode 377: Combination Sum IV."""


def solve(nums: list[int], target: int) -> int:
    ways = [0] * (target + 1)
    ways[0] = 1

    for total in range(1, target + 1):
        for number in nums:
            if number <= total:
                ways[total] += ways[total - number]
    return ways[target]

