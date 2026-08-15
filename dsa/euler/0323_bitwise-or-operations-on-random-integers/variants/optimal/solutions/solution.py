"""Project Euler 323: Bitwise-OR Operations on Random Integers

Find the expected value of the number of steps N until x_i = 2^32 - 1,
rounded to 10 decimal places.
"""

from __future__ import annotations


def solve(bits: int = 32, max_steps: int = 100) -> str:
    """Calculates the expected value of N using bit independence and the tail-sum formula:

    E[N] = sum_{i=0}^infty (1 - P(N <= i)) = sum_{i=0}^infty (1 - (1 - 2^(-i))^bits).
    """
    expected_n = 0.0

    for i in range(max_steps):
        # Probability that all bits are set to 1 by step i
        if i == 0:
            prob_all_ones = 0.0
        else:
            prob_single_bit_one = 1.0 - 2.0 ** (-i)
            prob_all_ones = prob_single_bit_one**bits

        # Tail probability P(N > i)
        prob_not_yet = 1.0 - prob_all_ones
        expected_n += prob_not_yet

    return f"{expected_n:.10f}"


if __name__ == "__main__":
    print(solve())
