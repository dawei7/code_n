from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            return 0 if nums1 == nums2 else -1

        balance = 0
        operations = 0

        for current, target in zip(nums1, nums2):
            difference = current - target
            if difference % k:
                return -1

            units = difference // k
            balance += units
            if units > 0:
                operations += units

        return operations if balance == 0 else -1
