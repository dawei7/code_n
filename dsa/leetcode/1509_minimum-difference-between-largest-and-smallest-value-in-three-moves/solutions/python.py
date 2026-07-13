def solve(nums):
    if len(nums) <= 4:
        return 0
    nums = sorted(nums)
    return min(nums[-4 + i] - nums[i] for i in range(4))
