"""Project Euler 334: Spilling the Beans

Find the number of moves required to finish the bean spilling game with 1500 adjacent bowls
containing b_1, ..., b_1500 beans.
"""

from __future__ import annotations


def get_beans(num_bowls: int) -> list[int]:
    """Generates the pseudorandom bean counts b_1, ..., b_{num_bowls} using the XOR PRNG."""
    t = 123456
    b: list[int] = []
    for _ in range(num_bowls):
        if t % 2 == 0:
            t = t // 2
        else:
            t = (t // 2) ^ 926252
        b.append((t % 2048) + 1)
    return b


def solve(num_bowls: int = 1500) -> str:
    """Calculates the total number of moves in the 1D Abelian sandpile / chip-firing game

    using the second moment invariant: Moves = (I_final - I_initial) / 2.
    """
    b = get_beans(num_bowls)

    # Calculate initial 0-th, 1-st, and 2-nd moments
    n = sum(b)
    mu = sum(x * c for x, c in enumerate(b))
    i_init = sum(x * x * c for x, c in enumerate(b))

    # The unique stable final state occupies span [K, K + N] with a single gap at g
    # 1-st moment conservation: mu = (N + 1)*K + N*(N + 1)/2 - g
    # with g in [K, K + N]
    k = (mu - n * (n - 1) // 2) // n
    g = (n + 1) * k + n * (n + 1) // 2 - mu

    # Exact closed-form sum of squares for [K, K + N]: sum_{x=K}^{K+N} x^2
    def sum_squares_to(m: int) -> int:
        if m >= 0:
            return m * (m + 1) * (2 * m + 1) // 6
        abs_m = -m
        return abs_m * (abs_m + 1) * (2 * abs_m + 1) // 6

    def sum_squares_range(start: int, end: int) -> int:
        # Sum of x^2 for x in [start, end]
        if start > end:
            return 0
        if start >= 0:
            return sum_squares_to(end) - sum_squares_to(start - 1)
        if end <= 0:
            return sum_squares_to(start) - sum_squares_to(end + 1)
        return sum_squares_to(end) + sum_squares_to(start)

    i_final = sum_squares_range(k, k + n) - g * g
    moves = (i_final - i_init) // 2

    return str(moves)


if __name__ == "__main__":
    print(solve())
