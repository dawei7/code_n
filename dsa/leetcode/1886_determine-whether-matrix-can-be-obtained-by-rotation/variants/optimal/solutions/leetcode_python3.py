from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        size = len(mat)
        possible = 0b1111

        for row in range(size):
            for column in range(size):
                value = target[row][column]
                if mat[row][column] != value:
                    possible &= ~0b0001
                if mat[size - 1 - column][row] != value:
                    possible &= ~0b0010
                if mat[size - 1 - row][size - 1 - column] != value:
                    possible &= ~0b0100
                if mat[column][size - 1 - row] != value:
                    possible &= ~0b1000
                if possible == 0:
                    return False

        return True
