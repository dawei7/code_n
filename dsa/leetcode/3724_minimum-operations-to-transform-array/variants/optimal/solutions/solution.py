from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        operations = 1
        appended_target = nums2[-1]
        extra = float("inf")

        for current, target in zip(nums1, nums2):
            operations += abs(current - target)
            low = min(current, target)
            high = max(current, target)

            if low <= appended_target <= high:
                extra = 0
            else:
                extra = min(
                    extra,
                    abs(appended_target - low),
                    abs(appended_target - high),
                )

        return operations + extra
