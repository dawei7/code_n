from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counts = [0] * 100
        pairs = 0
        for left, right in dominoes:
            key = 10 * min(left, right) + max(left, right)
            pairs += counts[key]
            counts[key] += 1
        return pairs
