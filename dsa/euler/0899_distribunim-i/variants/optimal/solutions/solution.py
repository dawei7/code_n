"""Project Euler Problem 899: DistribuNim I.

Mathematical formulation:
Two piles of stones (a, b). A move takes u + v = min(a, b) stones with u < a, v < b.
The first player unable to move loses.
L(n) is the number of losing positions (a, b) in [1, n]^2.

Bit-Length & Trailing Ones Invariant:
A position (a, b) is a losing (P-)position if and only if:
  b = 2^{len(a)} - 1 (mod 2^{len(a)})  or  a = 2^{len(b)} - 1 (mod 2^{len(b)}).

Disjoint Bit-Block Counting:
Letting k = len(a), we partition pairs into:
1. len(a) < len(b): 2 * count(a in [2^{k-1}, 2^k-1]) * count(b in [2^k, N] with b = 2^k - 1 mod 2^k).
2. len(a) == len(b) == k: 2 * count(k) - 1 if 2^k - 1 <= N.

Evaluates L(7^{17}) = 10784223938983273 in under 0.001s in pure Python.
"""

from __future__ import annotations


def solve(base: int = 7, exp: int = 17) -> int:
    """Compute L(base^exp)."""
    n = base**exp
    max_k = n.bit_length()
    total = 0

    # Case 1: len(a) < len(b)
    for k in range(1, max_k + 1):
        min_a = 1 << (k - 1)
        max_a = min(n, (1 << k) - 1)
        if min_a > max_a:
            continue
        count_a = max_a - min_a + 1

        mod = 1 << k
        rem = mod - 1
        if n >= mod + rem:
            count_b = (n - (mod + rem)) // mod + 1
        else:
            count_b = 0
        total += 2 * count_a * count_b

    # Case 2: len(a) == len(b) == k
    for k in range(1, max_k + 1):
        min_a = 1 << (k - 1)
        max_a = min(n, (1 << k) - 1)
        if min_a > max_a:
            continue
        count_k = max_a - min_a + 1

        if (1 << k) - 1 <= n:
            total += 2 * count_k - 1

    return total


if __name__ == "__main__":
    print(solve())
