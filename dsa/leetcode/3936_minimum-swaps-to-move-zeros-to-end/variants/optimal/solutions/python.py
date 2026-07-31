def solve(nums: list[int]) -> int:
    zero_count = nums.count(0)
    suffix_start = len(nums) - zero_count
    return sum(nums[index] != 0 for index in range(suffix_start, len(nums)))
