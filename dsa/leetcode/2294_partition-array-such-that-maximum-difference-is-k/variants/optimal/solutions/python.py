from typing import List


def solve(nums: List[int], k: int) -> int:
    ordered = sorted(nums)
    groups = 0
    index = 0

    while index < len(ordered):
        groups += 1
        limit = ordered[index] + k
        index += 1
        while index < len(ordered) and ordered[index] <= limit:
            index += 1

    return groups
