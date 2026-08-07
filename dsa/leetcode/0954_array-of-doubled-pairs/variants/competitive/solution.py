from collections import Counter
from typing import List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        for value in sorted(counts, key=abs):
            available = counts[value]
            if available == 0:
                continue
            if value == 0:
                if available % 2:
                    return False
                counts[value] = 0
                continue
            if counts[2 * value] < available:
                return False
            counts[2 * value] -= available
        return True
