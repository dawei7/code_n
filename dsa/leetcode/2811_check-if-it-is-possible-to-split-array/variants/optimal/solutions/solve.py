def solve(nums: list[int], m: int) -> bool:
    return len(nums) <= 2 or any(left + right >= m for left, right in zip(nums, nums[1:]))
