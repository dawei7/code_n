def solve(nums: list[int]) -> int:
    nums.sort()
    median = nums[len(nums) // 2]
    total = 0
    for value in nums:
        total += abs(value - median)
    return total
