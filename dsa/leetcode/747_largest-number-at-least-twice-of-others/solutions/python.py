def solve(nums: list[int]) -> int:
    largest = -1
    second_largest = -1
    largest_index = -1

    for index, value in enumerate(nums):
        if value > largest:
            second_largest = largest
            largest = value
            largest_index = index
        elif value > second_largest:
            second_largest = value

    return largest_index if largest >= 2 * second_largest else -1
