from typing import List


class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        lower = 0
        upper = min(max(ribbons), sum(ribbons) // k)

        while lower < upper:
            length = (lower + upper + 1) // 2
            pieces = 0
            for ribbon in ribbons:
                pieces += ribbon // length
                if pieces >= k:
                    break

            if pieces >= k:
                lower = length
            else:
                upper = length - 1

        return lower
