class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        larger, smaller = sorted((abs(x), abs(y)), reverse=True)
        if (larger, smaller) == (1, 0):
            return 3
        if (larger, smaller) == (2, 2):
            return 4

        moves = max((larger + 1) // 2, (larger + smaller + 2) // 3)
        moves += (moves + larger + smaller) % 2
        return moves
