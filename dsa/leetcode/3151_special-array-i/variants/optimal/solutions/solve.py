from typing import List


def solve(nums: List[int]) -> bool:
    for i in range(1, len(nums)):
        if nums[i] % 2 == nums[i - 1] % 2:
            return False
    return True
