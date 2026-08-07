from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        present = [False] * 10
        for digit in nums1:
            present[digit] = True

        common = 10
        for digit in nums2:
            if present[digit]:
                common = min(common, digit)
        if common < 10:
            return common

        first = min(nums1)
        second = min(nums2)
        return min(10 * first + second, 10 * second + first)
