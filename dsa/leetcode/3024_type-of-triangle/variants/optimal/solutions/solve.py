"""Optimal solution for LeetCode 3024: Type of Triangle."""


def solve(nums: list[int]) -> str:
    nums.sort()

    if nums[0] + nums[1] <= nums[2]:
        return "none"
    if nums[0] == nums[2]:
        return "equilateral"
    if nums[0] == nums[1] or nums[1] == nums[2]:
        return "isosceles"
    return "scalene"
