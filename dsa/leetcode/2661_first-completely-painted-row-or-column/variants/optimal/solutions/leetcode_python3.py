from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows = len(mat)
        columns = len(mat[0])
        position = [(-1, -1)] * (rows * columns + 1)

        for row in range(rows):
            for column in range(columns):
                position[mat[row][column]] = (row, column)

        painted_in_row = [0] * rows
        painted_in_column = [0] * columns

        for index, value in enumerate(arr):
            row, column = position[value]
            painted_in_row[row] += 1
            painted_in_column[column] += 1
            if painted_in_row[row] == columns or painted_in_column[column] == rows:
                return index

        return -1
