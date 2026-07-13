def solve(nums):
    base = sum(abs(nums[i] - nums[i - 1]) for i in range(1, len(nums)))
    gain = 0
    low = float("inf")
    high = float("-inf")
    for i in range(1, len(nums)):
        a, b = nums[i - 1], nums[i]
        gain = max(gain, abs(nums[0] - b) - abs(a - b))
        gain = max(gain, abs(nums[-1] - a) - abs(a - b))
        low = min(low, max(a, b))
        high = max(high, min(a, b))
    gain = max(gain, 2 * (high - low))
    return base + gain
