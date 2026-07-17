from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) * 6 < len(nums2) or len(nums2) * 6 < len(nums1):
            return -1

        sum1 = sum(nums1)
        sum2 = sum(nums2)
        if sum1 > sum2:
            nums1, nums2 = nums2, nums1
            sum1, sum2 = sum2, sum1

        gains = [0] * 6
        for value in nums1:
            gains[6 - value] += 1
        for value in nums2:
            gains[value - 1] += 1

        gap = sum2 - sum1
        operations = 0
        for gain in range(5, 0, -1):
            used = min(gains[gain], (gap + gain - 1) // gain)
            gap -= used * gain
            operations += used
            if gap <= 0:
                return operations
        return operations
