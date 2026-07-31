from collections import Counter
from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        counts = Counter(nums)
        for start in sorted(counts):
            copies = counts[start]
            if copies == 0:
                continue
            for value in range(start, start + k):
                if counts[value] < copies:
                    return False
                counts[value] -= copies

        return True
