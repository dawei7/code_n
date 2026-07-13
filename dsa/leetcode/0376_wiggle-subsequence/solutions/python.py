"""Optimal solution for LeetCode 376: Wiggle Subsequence."""


def solve(nums: list[int]) -> int:
    if not nums:
        return 0

    up = 1
    down = 1
    for index in range(1, len(nums)):
        if nums[index] > nums[index - 1]:
            up = down + 1
        elif nums[index] < nums[index - 1]:
            down = up + 1
    return max(up, down)

