from collections import Counter
from typing import List


def solve(nums: List[int]) -> int:
    operations = 0
    for frequency in Counter(nums).values():
        if frequency == 1:
            return -1
        operations += (frequency + 2) // 3
    return operations
