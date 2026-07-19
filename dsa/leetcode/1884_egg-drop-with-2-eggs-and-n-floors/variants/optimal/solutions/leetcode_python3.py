from math import isqrt


class Solution:
    def twoEggDrop(self, n: int) -> int:
        moves = (isqrt(8 * n + 1) - 1) // 2
        if moves * (moves + 1) // 2 < n:
            moves += 1
        return moves
