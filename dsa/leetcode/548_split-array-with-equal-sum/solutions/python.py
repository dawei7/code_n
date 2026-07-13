"""Quadratic prefix-sum split search for LeetCode 548."""


def solve(nums: list[int]) -> bool:
    length = len(nums)
    prefix = [0] * (length + 1)

    for index, value in enumerate(nums):
        prefix[index + 1] = prefix[index] + value

    for middle in range(3, length - 3):
        left_sums = set()

        for left in range(1, middle - 1):
            first = prefix[left]
            second = prefix[middle] - prefix[left + 1]
            if first == second:
                left_sums.add(first)

        for right in range(middle + 2, length - 1):
            third = prefix[right] - prefix[middle + 1]
            fourth = prefix[length] - prefix[right + 1]
            if third == fourth and third in left_sums:
                return True

    return False

