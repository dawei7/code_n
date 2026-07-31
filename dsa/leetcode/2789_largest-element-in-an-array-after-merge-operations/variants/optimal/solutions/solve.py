def solve(nums: list[int]) -> int:
    merged = nums[-1]

    for index in range(len(nums) - 2, -1, -1):
        if nums[index] <= merged:
            merged += nums[index]
        else:
            merged = nums[index]

    return merged
