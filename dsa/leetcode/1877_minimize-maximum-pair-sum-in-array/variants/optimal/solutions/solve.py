def solve(nums: list[int]) -> int:
    nums.sort()
    return max(nums[index] + nums[-index - 1] for index in range(len(nums) // 2))
