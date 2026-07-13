from typing import List


def solve(nums: List[int]) -> List[int]:
    even_count = sum(1 for value in nums if value % 2 == 0)
    return [0] * even_count + [1] * (len(nums) - even_count)
