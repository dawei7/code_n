def solve(nums: list[int]) -> int:
    best = nums[0]
    high = nums[0]
    low = nums[0]
    for value in nums[1:]:
        if value < 0:
            high, low = low, high
        high = max(value, high * value)
        low = min(value, low * value)
        best = max(best, high)
    return best
