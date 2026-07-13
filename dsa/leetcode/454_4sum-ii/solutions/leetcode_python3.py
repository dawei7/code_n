from collections import Counter
from typing import List


class Solution:
    def fourSumCount(
        self,
        nums1: List[int],
        nums2: List[int],
        nums3: List[int],
        nums4: List[int],
    ) -> int:
        first_sums = Counter(a + b for a in nums1 for b in nums2)
        total = 0
        for c in nums3:
            for d in nums4:
                total += first_sums.get(-(c + d), 0)
        return total
