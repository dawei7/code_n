def solve(nums: list[int]) -> int:
    positives = {value for value in nums if value > 0}
    if positives:
        return sum(positives)
    return max(nums)
