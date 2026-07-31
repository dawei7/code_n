from collections import Counter
from typing import List


class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        modulus = 1_000_000_007
        totals = Counter(nums)
        powers = {}

        for value, total in totals.items():
            row = [1] * (total + 1)
            for exponent in range(1, total + 1):
                row[exponent] = row[exponent - 1] * value % modulus
            powers[value] = row

        counts = Counter()
        score = 0
        answer = 0

        for index, value in enumerate(nums):
            old_count = counts[value]
            if old_count:
                score -= powers[value][old_count]
            counts[value] = old_count + 1
            score += powers[value][old_count + 1]

            if index >= k:
                outgoing = nums[index - k]
                old_count = counts[outgoing]
                score -= powers[outgoing][old_count]
                counts[outgoing] = old_count - 1
                if old_count > 1:
                    score += powers[outgoing][old_count - 1]

            score %= modulus
            if index >= k - 1:
                answer = max(answer, score)

        return answer
