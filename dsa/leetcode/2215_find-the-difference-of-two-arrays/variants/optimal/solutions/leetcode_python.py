from typing import List


class Solution:
    def findDifference(
        self, nums1: List[int], nums2: List[int]
    ) -> List[List[int]]:
        first = set(nums1)
        second = set(nums2)
        return [list(first - second), list(second - first)]
