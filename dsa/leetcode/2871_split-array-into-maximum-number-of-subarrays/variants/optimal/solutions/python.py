from typing import List


def solve(nums: List[int]) -> int:
    segments = 0
    running_and = -1

    for value in nums:
        running_and &= value
        if running_and == 0:
            segments += 1
            running_and = -1

    return max(segments, 1)
