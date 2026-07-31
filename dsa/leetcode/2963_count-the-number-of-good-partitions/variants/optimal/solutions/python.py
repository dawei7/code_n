from typing import List


def solve(nums: List[int]) -> int:
    last = {value: index for index, value in enumerate(nums)}
    components = 0
    rightmost = 0

    for index, value in enumerate(nums):
        rightmost = max(rightmost, last[value])
        if index == rightmost:
            components += 1

    return pow(2, components - 1, 1_000_000_007)
