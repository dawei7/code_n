from typing import List


class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        side = len(board)
        origin = board[0][0]
        for row in range(side):
            for column in range(side):
                if origin ^ board[row][0] ^ board[0][column] ^ board[row][column]:
                    return -1

        def minimum_swaps(labels: List[int]) -> int:
            ones = sum(labels)
            if abs(side - 2 * ones) > 1:
                return -1

            mismatch_zero = sum(
                value != index % 2 for index, value in enumerate(labels)
            )
            if side % 2 == 0:
                mismatches = min(mismatch_zero, side - mismatch_zero)
            elif mismatch_zero % 2 == 0:
                mismatches = mismatch_zero
            else:
                mismatches = side - mismatch_zero
            return mismatches // 2

        row_swaps = minimum_swaps([board[row][0] for row in range(side)])
        column_swaps = minimum_swaps(board[0])
        if row_swaps == -1 or column_swaps == -1:
            return -1
        return row_swaps + column_swaps
