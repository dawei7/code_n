from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        bits = max(nums).bit_length()
        size = 1 << bits
        best_submask = [0] * size
        for value in nums:
            best_submask[value] = value

        for bit in range(bits):
            half = 1 << bit
            block = half << 1
            for start in range(0, size, block):
                for offset in range(half):
                    lower = start + offset
                    upper = lower + half
                    if best_submask[lower] > best_submask[upper]:
                        best_submask[upper] = best_submask[lower]

        full_mask = size - 1
        return max(
            value * best_submask[full_mask ^ value]
            for value in nums
        )
