from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        column_count = len(points[0])
        previous = points[0][:]

        for row in points[1:]:
            left = [0] * column_count
            right = [0] * column_count

            left[0] = previous[0]
            for column in range(1, column_count):
                left[column] = max(previous[column], left[column - 1] - 1)

            right[-1] = previous[-1]
            for column in range(column_count - 2, -1, -1):
                right[column] = max(previous[column], right[column + 1] - 1)

            previous = [
                row[column] + max(left[column], right[column])
                for column in range(column_count)
            ]

        return max(previous)
