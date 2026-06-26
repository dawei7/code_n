"""Optimal solution for LeetCode 1005: Maximize Sum Of Array After K Negations."""


def solve(nums: list[int], k: int) -> int:
    nums.sort()
    for i, value in enumerate(nums):
        if k == 0 or value >= 0:
            break
        nums[i] = -value
        k -= 1

    total = sum(nums)
    if k % 2 == 1:
        total -= 2 * min(nums)
    return total
