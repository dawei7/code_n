from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        answer = []

        for diagonal_index in range(rows + cols - 1):
            row = max(0, diagonal_index - cols + 1)
            col = diagonal_index - row
            diagonal = []
            while row < rows and col >= 0:
                diagonal.append(mat[row][col])
                row += 1
                col -= 1
            if diagonal_index % 2 == 0:
                diagonal.reverse()
            answer.extend(diagonal)
        return answer
