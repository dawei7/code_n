from bisect import bisect_left
from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        tails = [[] for _ in range(30)]
        answer = 0

        for value in nums:
            remaining_bits = value
            while remaining_bits:
                lowest_bit = remaining_bits & -remaining_bits
                bit = lowest_bit.bit_length() - 1
                bit_tails = tails[bit]
                position = bisect_left(bit_tails, value)

                if position == len(bit_tails):
                    bit_tails.append(value)
                else:
                    bit_tails[position] = value

                answer = max(answer, position + 1)
                remaining_bits -= lowest_bit

        return answer
