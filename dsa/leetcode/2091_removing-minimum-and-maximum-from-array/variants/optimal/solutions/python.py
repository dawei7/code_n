def solve(nums: list[int]) -> int:
    minimum_index = 0
    maximum_index = 0

    for index in range(1, len(nums)):
        if nums[index] < nums[minimum_index]:
            minimum_index = index
        if nums[index] > nums[maximum_index]:
            maximum_index = index

    left, right = sorted((minimum_index, maximum_index))
    return min(
        right + 1,
        len(nums) - left,
        left + 1 + len(nums) - right,
    )
