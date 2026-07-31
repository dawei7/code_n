from collections import defaultdict
from typing import List


def solve(nums: List[int]) -> int:
    frequencies: dict[int, int] = defaultdict(int)
    bad_pairs = 0
    for index, value in enumerate(nums):
        key = value - index
        bad_pairs += index - frequencies[key]
        frequencies[key] += 1
    return bad_pairs
