from typing import List


class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        length = len(nums1)
        costs = [float("inf")] * (1 << length)
        costs[0] = 0

        for mask in range(1, 1 << length):
            first_index = mask.bit_count() - 1
            for second_index in range(length):
                bit = 1 << second_index
                if mask & bit:
                    costs[mask] = min(
                        costs[mask],
                        costs[mask ^ bit]
                        + (nums1[first_index] ^ nums2[second_index]),
                    )

        return int(costs[-1])
