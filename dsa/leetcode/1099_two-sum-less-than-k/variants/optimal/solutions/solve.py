"""Optimal app-local solution for LeetCode 1099."""


def solve(nums: list[int], k: int) -> int:
    values = sorted(nums)
    left = 0
    right = len(values) - 1
    best = -1

    while left < right:
        pair_sum = values[left] + values[right]
        if pair_sum < k:
            best = max(best, pair_sum)
            left += 1
        else:
            right -= 1
    return best
