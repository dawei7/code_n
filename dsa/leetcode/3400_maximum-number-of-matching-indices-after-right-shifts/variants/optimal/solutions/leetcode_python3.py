from typing import List


class Solution:
    def maximumMatchingIndices(self, nums1: List[int], nums2: List[int]) -> int:
        length = len(nums1)
        best = 0

        for shift in range(length):
            matches = 0
            for index, value in enumerate(nums1):
                if value == nums2[(index + shift) % length]:
                    matches += 1
            best = max(best, matches)

        return best
