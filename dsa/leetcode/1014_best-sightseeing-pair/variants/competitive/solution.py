from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best_left = values[0]
        answer = 0

        for index in range(1, len(values)):
            answer = max(answer, best_left + values[index] - index)
            best_left = max(best_left, values[index] + index)

        return answer
