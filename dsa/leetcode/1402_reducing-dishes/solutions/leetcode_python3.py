from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        suffix_sum = 0
        coefficient = 0
        for value in sorted(satisfaction, reverse=True):
            if suffix_sum + value <= 0:
                break
            suffix_sum += value
            coefficient += suffix_sum
        return coefficient
