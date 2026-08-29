"""Project Euler Problem 866: Tidying Up B.

Mathematical formulation:
Let E(N) be the expected product of the hexagonal numbers H(k) = k*(2k - 1) written down
during the random placement of N caterpillar pieces.

Backward Induction / Divide-and-Conquer:
At the final step that completes the full segment of length N:
- The last piece placed is chosen uniformly at random at position i in {1, ..., N} with probability 1/N.
- The number written down for this final piece is always H(N) = N*(2N - 1).
- The remaining pieces in {1, ..., i-1} and {i+1, ..., N} form two independent sub-processes
  of lengths i - 1 and N - i.

Thus:
  E(N) = H(N) * (1 / N) * sum_{i=1}^N E(i - 1) * E(N - i)
       = (2N - 1) * sum_{i=1}^N E(i - 1) * E(N - i)
with base case E(0) = 1.

Evaluated modulo 987654319 in O(N^2) time (under 0.001s in Python).
"""

from __future__ import annotations


def solve(n: int = 100, modulo: int = 987654319) -> int:
    """Compute the expected product E(n) modulo 987654319."""
    e = [0] * (n + 1)
    e[0] = 1

    for size in range(1, n + 1):
        conv = 0
        for i in range(1, size + 1):
            conv = (conv + e[i - 1] * e[size - i]) % modulo
        e[size] = ((2 * size - 1) * conv) % modulo

    return e[n]


if __name__ == "__main__":
    print(solve())
