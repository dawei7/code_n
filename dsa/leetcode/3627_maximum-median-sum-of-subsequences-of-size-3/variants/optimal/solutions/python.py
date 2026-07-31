def solve(nums: list[int]) -> int:
    nums.sort()
    groups = len(nums) // 3
    return sum(nums[groups::2])

