def solve(nums: list[int]) -> int:
    smallest = nums[0]
    largest = -101
    second_largest = -101

    for value in nums:
        smallest = min(smallest, value)
        if value >= largest:
            second_largest = largest
            largest = value
        elif value > second_largest:
            second_largest = value

    return largest + second_largest - smallest
