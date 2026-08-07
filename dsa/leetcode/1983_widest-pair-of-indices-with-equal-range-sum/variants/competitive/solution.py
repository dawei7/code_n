from typing import List


class Solution:
    def widestPairOfIndices(self, nums1: List[int], nums2: List[int]) -> int:
        earliest = {0: -1}
        difference = 0
        widest = 0

        for index, (left, right) in enumerate(zip(nums1, nums2)):
            difference += left - right
            if difference in earliest:
                widest = max(widest, index - earliest[difference])
            else:
                earliest[difference] = index

        return widest
