def solve(nums: list[int]) -> int:
    maximum = max(nums)
    return sum(maximum - value for value in nums)
