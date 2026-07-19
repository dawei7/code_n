from collections import Counter
from typing import List


class Solution:
    def twoOutOfThree(
        self, nums1: List[int], nums2: List[int], nums3: List[int]
    ) -> List[int]:
        appearances = Counter()
        for values in (nums1, nums2, nums3):
            for value in set(values):
                appearances[value] += 1
        return [value for value, count in appearances.items() if count >= 2]
