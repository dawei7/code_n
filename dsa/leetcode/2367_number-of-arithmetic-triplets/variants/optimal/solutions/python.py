from typing import List


def solve(nums: List[int], diff: int) -> int:
    values = set(nums)
    return sum(
        value - diff in values and value - 2 * diff in values
        for value in nums
    )
