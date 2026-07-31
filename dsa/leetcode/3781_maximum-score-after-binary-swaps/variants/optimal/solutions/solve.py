from heapq import heappop, heappush
from typing import List


def solve(nums: List[int], s: str) -> int:
    available = []
    score = 0
    for value, bit in zip(nums, s):
        heappush(available, -value)
        if bit == "1":
            score -= heappop(available)
    return score
