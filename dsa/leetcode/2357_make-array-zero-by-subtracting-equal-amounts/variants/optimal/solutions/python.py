from typing import List


def solve(nums: List[int]) -> int:
    return len({value for value in nums if value > 0})
