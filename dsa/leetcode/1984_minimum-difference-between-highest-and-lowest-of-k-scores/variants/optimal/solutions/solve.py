def solve(nums: list[int], k: int) -> int:
    nums.sort()
    return min(nums[index + k - 1] - nums[index] for index in range(len(nums) - k + 1))
