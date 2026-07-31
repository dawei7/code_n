from typing import List


def solve(nums: List[int]) -> int:
    return max(nums[0], nums[-1])
