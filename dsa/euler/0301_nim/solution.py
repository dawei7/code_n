"""Project Euler 301: Nim

Find the number of positive integers n <= 2^30 for which X(n, 2n, 3n) = 0.
"""

from __future__ import annotations


def solve(power: int = 30) -> str:
    """Calculates the number of positive integers n <= 2^power such that n ^ (2n) ^ (3n) == 0.

    Since 3n = n + 2n, the condition n ^ (2n) ^ (3n) == 0 holds if and only if
    n + 2n = n ^ (2n), which means there are no carry bits in the binary addition n + 2n.
    Equivalently, n & (2n) == 0, which means the binary representation of n contains no consecutive 1s.

    The number of k-bit strings with no consecutive 1s is given by the Fibonacci number F_{k+2}.
    For 1 <= n <= 2^power, the count is exactly F_{power + 2}.
    """
    # Compute Fibonacci numbers iteratively: F_1 = 1, F_2 = 1, F_3 = 2, ...
    a, b = 1, 1
    for _ in range(power):
        a, b = b, a + b

    # b is F_{power + 2}
    return str(b)


if __name__ == "__main__":
    print(solve())
