from typing import List


class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        score1 = 0
        score2 = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                score1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                score2 += nums2[j]
                j += 1
            else:
                best = max(score1, score2) + nums1[i]
                score1 = best
                score2 = best
                i += 1
                j += 1

        score1 += sum(nums1[i:])
        score2 += sum(nums2[j:])
        return max(score1, score2) % 1_000_000_007
