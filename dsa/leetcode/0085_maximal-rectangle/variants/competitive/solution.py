from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        heights = [0] * len(matrix[0])
        best = 0
        for row in matrix:
            for column, value in enumerate(row):
                heights[column] = heights[column] + 1 if value == "1" else 0

            stack = []
            for index, height in enumerate(heights + [0]):
                start = index
                while stack and stack[-1][1] > height:
                    start, previous_height = stack.pop()
                    best = max(best, previous_height * (index - start))
                stack.append((start, height))
        return best
