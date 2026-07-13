from bisect import bisect_left
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        ordered = sorted(envelopes, key=lambda envelope: (envelope[0], -envelope[1]))
        tails = []
        for _, height in ordered:
            position = bisect_left(tails, height)
            if position == len(tails):
                tails.append(height)
            else:
                tails[position] = height
        return len(tails)
