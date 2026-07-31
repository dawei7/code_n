def solve(nums: list[int]) -> int:
    if nums[0] >= nums[1]:
        largest, second_largest = nums[0], nums[1]
    else:
        largest, second_largest = nums[1], nums[0]
    smallest = min(nums[0], nums[1])

    for value in nums[2:]:
        smallest = min(smallest, value)
        if value >= largest:
            largest, second_largest = value, largest
        elif value > second_largest:
            second_largest = value

    return largest + second_largest - smallest
