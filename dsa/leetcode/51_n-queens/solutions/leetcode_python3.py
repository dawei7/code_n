from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board_mask = (1 << n) - 1
        positions = []
        solutions = []

        def place(columns: int, descending: int, ascending: int) -> None:
            if len(positions) == n:
                solutions.append([
                    "." * column + "Q" + "." * (n - column - 1)
                    for column in positions
                ])
                return

            free = board_mask & ~(columns | descending | ascending)
            while free:
                bit = free & -free
                free -= bit
                positions.append(bit.bit_length() - 1)
                place(
                    columns | bit,
                    ((descending | bit) << 1) & board_mask,
                    (ascending | bit) >> 1,
                )
                positions.pop()

        place(0, 0, 0)
        return solutions
