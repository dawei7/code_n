from typing import List


def solve(nums: List[int], k: int) -> int:
    ordered = sorted(nums)
    middle = len(ordered) // 2
    operations = 0

    for index in range(middle + 1):
        if ordered[index] > k:
            operations += ordered[index] - k

    for index in range(middle, len(ordered)):
        if ordered[index] < k:
            operations += k - ordered[index]

    return operations
