"""Optimal app-local solution for LeetCode 905."""


def solve(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        while left < right and nums[left] % 2 == 0:
            left += 1
        while left < right and nums[right] % 2 == 1:
            right -= 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    return nums
