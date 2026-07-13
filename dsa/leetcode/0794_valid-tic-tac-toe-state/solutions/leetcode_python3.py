from typing import List


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        x_count = sum(row.count("X") for row in board)
        o_count = sum(row.count("O") for row in board)
        if x_count not in (o_count, o_count + 1):
            return False

        lines = list(board)
        lines.extend(
            "".join(board[row][column] for row in range(3))
            for column in range(3)
        )
        lines.append("".join(board[index][index] for index in range(3)))
        lines.append("".join(board[index][2 - index] for index in range(3)))
        x_wins = "XXX" in lines
        o_wins = "OOO" in lines

        if x_wins and x_count != o_count + 1:
            return False
        if o_wins and x_count != o_count:
            return False
        return True
