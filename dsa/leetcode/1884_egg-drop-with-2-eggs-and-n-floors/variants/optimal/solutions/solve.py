from math import isqrt


def solve(n: int) -> int:
    moves = (isqrt(8 * n + 1) - 1) // 2
    if moves * (moves + 1) // 2 < n:
        moves += 1
    return moves
