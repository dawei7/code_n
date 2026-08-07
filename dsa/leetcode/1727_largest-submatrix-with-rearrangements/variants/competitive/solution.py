from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        columns = len(matrix[0])
        heights = [0] * columns
        order = list(range(columns))
        best = 0

        for row in matrix:
            positive = []
            zero = []

            for column in order:
                if row[column] == 1:
                    heights[column] += 1
                    positive.append(column)
                else:
                    heights[column] = 0
                    zero.append(column)

            order = positive + zero
            for width, column in enumerate(positive, 1):
                best = max(best, width * heights[column])

        return best
