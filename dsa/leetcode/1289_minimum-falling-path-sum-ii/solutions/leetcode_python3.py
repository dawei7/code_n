from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        length = len(grid)
        previous = grid[0][:]

        for row in range(1, length):
            smallest = second_smallest = float("inf")
            smallest_column = -1
            for column, value in enumerate(previous):
                if value < smallest:
                    second_smallest = smallest
                    smallest = value
                    smallest_column = column
                elif value < second_smallest:
                    second_smallest = value

            previous = [
                grid[row][column]
                + (second_smallest if column == smallest_column else smallest)
                for column in range(length)
            ]

        return min(previous)
