from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        values1 = set(nums1)
        values2 = set(nums2)
        return [
            sum(value in values2 for value in nums1),
            sum(value in values1 for value in nums2),
        ]
