from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        return sum(
            first % (second * k) == 0
            for first in nums1
            for second in nums2
        )
