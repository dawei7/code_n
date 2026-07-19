from typing import List


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        occupied = {tuple(queen) for queen in queens}
        answer = []
        directions = (
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1),
        )
        for row_change, column_change in directions:
            row, column = king[0] + row_change, king[1] + column_change
            while 0 <= row < 8 and 0 <= column < 8:
                if (row, column) in occupied:
                    answer.append([row, column])
                    break
                row += row_change
                column += column_change
        return answer
