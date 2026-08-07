from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zeros1 = nums1.count(0)
        zeros2 = nums2.count(0)
        minimum1 = sum(nums1) + zeros1
        minimum2 = sum(nums2) + zeros2

        if minimum1 < minimum2 and zeros1 == 0:
            return -1
        if minimum2 < minimum1 and zeros2 == 0:
            return -1
        return max(minimum1, minimum2)
