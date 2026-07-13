def solve(nums):
    total = 0
    lowest = 0
    for num in nums:
        total += num
        lowest = min(lowest, total)
    return 1 - lowest
