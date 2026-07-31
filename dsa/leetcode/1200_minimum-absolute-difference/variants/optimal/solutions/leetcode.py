from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        values = sorted(arr)
        best_gap = float("inf")
        pairs = []

        for left, right in zip(values, values[1:]):
            gap = right - left
            if gap < best_gap:
                best_gap = gap
                pairs = [[left, right]]
            elif gap == best_gap:
                pairs.append([left, right])
        return pairs
