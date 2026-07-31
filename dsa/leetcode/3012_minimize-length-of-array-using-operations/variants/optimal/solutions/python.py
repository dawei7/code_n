def solve(nums):
    minimum = min(nums)
    minimum_count = nums.count(minimum)

    if any(value % minimum != 0 for value in nums):
        return 1

    return (minimum_count + 1) // 2
