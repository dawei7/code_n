from typing import List


class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        differences = sorted(a - b for a, b in zip(nums1, nums2))
        left = 0
        right = len(differences) - 1
        pairs = 0

        while left < right:
            if differences[left] + differences[right] > 0:
                pairs += right - left
                right -= 1
            else:
                left += 1

        return pairs
