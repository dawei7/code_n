def solve(nums: list[int]) -> list[int]:
    odd_count = sum(value & 1 for value in nums)
    return [0] * (len(nums) - odd_count) + [1] * odd_count
