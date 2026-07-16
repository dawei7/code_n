from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        even = 1
        odd = 0
        parity = 0

        for value in arr:
            parity ^= value & 1
            if parity:
                odd += 1
            else:
                even += 1

        return even * odd % 1_000_000_007
