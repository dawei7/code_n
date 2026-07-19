from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        suffix_lengths = [0] * (len(nums2) + 1)
        best = 0

        for value in nums1:
            for index in range(len(nums2) - 1, -1, -1):
                if value == nums2[index]:
                    suffix_lengths[index + 1] = suffix_lengths[index] + 1
                    best = max(best, suffix_lengths[index + 1])
                else:
                    suffix_lengths[index + 1] = 0

        return best
