def solve(nums):
    largest = 0
    second_largest = 0

    for value in nums:
        if value > largest:
            largest, second_largest = value, largest
        elif value > second_largest:
            second_largest = value

    return (largest - 1) * (second_largest - 1)
