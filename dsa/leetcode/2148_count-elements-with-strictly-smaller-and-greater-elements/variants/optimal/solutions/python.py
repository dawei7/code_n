def solve(nums: list[int]) -> int:
    minimum = min(nums)
    maximum = max(nums)
    return sum(minimum < value < maximum for value in nums)
