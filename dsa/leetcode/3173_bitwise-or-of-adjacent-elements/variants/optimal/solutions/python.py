def solve(nums: list[int]) -> list[int]:
    return [left | right for left, right in zip(nums, nums[1:])]
