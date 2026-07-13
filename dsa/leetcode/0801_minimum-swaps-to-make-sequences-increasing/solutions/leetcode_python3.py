from typing import List


class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        keep = 0
        swap = 1

        for index in range(1, len(nums1)):
            next_keep = float("inf")
            next_swap = float("inf")

            if nums1[index] > nums1[index - 1] and nums2[index] > nums2[index - 1]:
                next_keep = keep
                next_swap = swap + 1

            if nums1[index] > nums2[index - 1] and nums2[index] > nums1[index - 1]:
                next_keep = min(next_keep, swap)
                next_swap = min(next_swap, keep + 1)

            keep, swap = next_keep, next_swap

        return int(min(keep, swap))
