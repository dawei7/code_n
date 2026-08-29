"""Project Euler Problem 669: The King's Banquet.

Find the knight sitting in the 10^16-th chair from the king's left for n = 99194853094755497.
"""

from typing import List


def _get_fib_sequence(limit: int) -> List[int]:
    fibs = [1, 2]
    while fibs[-1] < limit:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


def _knight_at_index_from_right(pos: int, limit: int) -> int:
    fibs = _get_fib_sequence(limit * 2)
    y = limit  # F_k
    idx_y = fibs.index(y)
    z = fibs[idx_y - 1]  # F_{k-1}

    mult = pos // 2
    temp = (y - z * mult) % y
    if pos % 2 == 0:
        temp = (-temp) % y
        if temp == 0:
            temp = y
    else:
        if temp == 0:
            temp = y
    return temp


def solve(n: int = 99_194_853_094_755_497, k_chair: int = 10_000_000_000_000_000) -> int:
    """Compute the knight in the k-th chair from the king's left using the modular Fibonacci reflection group."""
    fibs = [1, 2]
    while fibs[-1] < n * 2:
        fibs.append(fibs[-1] + fibs[-2])

    pos_from_right = n + 1 - k_chair
    ans = _knight_at_index_from_right(pos_from_right, n)
    return ans


if __name__ == "__main__":
    print(solve())
