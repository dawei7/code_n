"""Project Euler Problem 713: Turan's Water Heating System.

Mathematical Formulation:
Turan has N fuses, m of which work.
T(N, m) is the minimum number of pair tests to guarantee at least one working pair.
By Turan's theorem and the pigeonhole principle:
Partition N into k = m - 1 disjoint parts:
T(N, k + 1) = r * q*(q+1)//2 + (k - r) * q*(q-1)//2
where q = floor(N / k), r = N mod k.
Compute L(10^7) = sum_{k=1}^{10^7-1} T(10^7, k + 1).
"""

from __future__ import annotations


def solve(n_val: int = 10**7) -> str:
    """Compute L(10^7) dynamically in pure Python."""
    total = 0
    for k in range(1, n_val):
        q = n_val // k
        r = n_val % k
        total += r * q * (q + 1) // 2 + (k - r) * q * (q - 1) // 2

    return str(total)


if __name__ == "__main__":
    print(solve())
