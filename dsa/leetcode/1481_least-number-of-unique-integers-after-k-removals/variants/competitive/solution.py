from collections import Counter
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        frequencies = sorted(Counter(arr).values())
        remaining = len(frequencies)

        for frequency in frequencies:
            if frequency > k:
                break
            k -= frequency
            remaining -= 1

        return remaining
