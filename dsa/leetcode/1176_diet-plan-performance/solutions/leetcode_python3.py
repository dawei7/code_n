from typing import List


class Solution:
    def dietPlanPerformance(
        self, calories: List[int], k: int, lower: int, upper: int
    ) -> int:
        window_sum = sum(calories[:k])
        score = 0

        if window_sum < lower:
            score -= 1
        elif window_sum > upper:
            score += 1

        for right in range(k, len(calories)):
            window_sum += calories[right] - calories[right - k]
            if window_sum < lower:
                score -= 1
            elif window_sum > upper:
                score += 1

        return score
