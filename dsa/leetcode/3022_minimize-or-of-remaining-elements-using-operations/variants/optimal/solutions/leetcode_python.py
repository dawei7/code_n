from typing import List


class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        answer = 0
        zero_mask = 0
        all_bits = (1 << 30) - 1

        for bit in range(29, -1, -1):
            zero_mask |= 1 << bit
            operations = 0
            segment_and = all_bits

            for value in nums:
                segment_and &= value
                if segment_and & zero_mask:
                    operations += 1
                else:
                    segment_and = all_bits

            if operations > k:
                answer |= 1 << bit
                zero_mask ^= 1 << bit

        return answer
