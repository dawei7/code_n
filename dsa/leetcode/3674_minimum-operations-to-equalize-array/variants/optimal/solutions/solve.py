def solve(nums: list[int]) -> int:
    first = nums[0]
    for value in nums:
        if value != first:
            return 1
    return 0
