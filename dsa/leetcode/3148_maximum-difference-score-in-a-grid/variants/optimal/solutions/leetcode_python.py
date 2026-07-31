from typing import List


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        columns = len(grid[0])
        prefix_minimum = [10**18] * columns
        answer = -(10**18)

        for row in grid:
            left_minimum = 10**18
            for column, value in enumerate(row):
                previous_minimum = min(left_minimum, prefix_minimum[column])
                answer = max(answer, value - previous_minimum)

                current_minimum = min(value, previous_minimum)
                prefix_minimum[column] = current_minimum
                left_minimum = current_minimum

        return answer
