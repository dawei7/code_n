from typing import List


def solve(nums: List[int], k: int) -> int:
    return sum(value for index, value in enumerate(nums) if index.bit_count() == k)
