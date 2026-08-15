"""Project Euler Problem 509: Divisor Nim.

Find S(123456787654321) mod 1234567890, where S(n) is the number of winning positions
for the next player in 3-pile Divisor Nim with pile sizes 1 <= a, b, c <= n.
"""

from typing import List

MOD = 1234567890


def solve(n: int = 123456787654321, mod: int = MOD) -> int:
    """Compute number of winning triples in 3-pile Divisor Nim using Sprague-Grundy theorem."""
    max_k = n.bit_length()
    counts: List[int] = [0] * max_k

    for k in range(max_k):
        counts[k] = (n // (1 << k)) - (n // (1 << (k + 1)))

    total = pow(n % mod, 3, mod)
    losing = 0

    for i in range(max_k):
        ci = counts[i] % mod
        if not ci:
            continue
        for j in range(max_k):
            cj = counts[j] % mod
            if not cj:
                continue
            k = i ^ j
            if k < max_k:
                ck = counts[k] % mod
                losing = (losing + ci * cj % mod * ck) % mod

    return (total - losing) % mod


if __name__ == "__main__":
    print(solve())
