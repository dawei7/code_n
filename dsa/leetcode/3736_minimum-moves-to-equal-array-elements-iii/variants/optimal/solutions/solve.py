def solve(nums: list[int]) -> int:
    maximum = max(nums)
    return maximum * len(nums) - sum(nums)
