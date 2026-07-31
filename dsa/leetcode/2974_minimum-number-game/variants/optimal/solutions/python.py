from typing import List


def solve(nums: List[int]) -> List[int]:
    ordered = sorted(nums)
    for index in range(0, len(ordered), 2):
        ordered[index], ordered[index + 1] = ordered[index + 1], ordered[index]
    return ordered
