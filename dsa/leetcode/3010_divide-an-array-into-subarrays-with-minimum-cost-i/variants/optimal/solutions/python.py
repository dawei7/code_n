def solve(nums):
    smallest = float("inf")
    second_smallest = float("inf")

    for value in nums[1:]:
        if value < smallest:
            smallest, second_smallest = value, smallest
        elif value < second_smallest:
            second_smallest = value

    return nums[0] + smallest + second_smallest
