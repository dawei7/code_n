from collections import defaultdict
from typing import List


def solve(nums: List[int], k: int) -> int:
    counts = defaultdict(int)
    left = 0
    best = 0

    for right, value in enumerate(nums):
        counts[value] += 1
        while counts[value] > k:
            counts[nums[left]] -= 1
            left += 1
        best = max(best, right - left + 1)

    return best
