"""Project Euler Problem 619: Square Subsets.

Find C(1000000, 1234567) mod 1000000007, where C(a, b) is the number of non-empty
subsets of {a, ..., b} whose product is a perfect square.
"""

from typing import Dict, List, Set

_MOD = 1_000_000_007


def _sieve_spf(limit: int) -> List[int]:
    spf = list(range(limit + 1))
    for i in range(2, int(limit**0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, limit + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


def solve(a: int = 1_000_000, b: int = 1_234_567) -> int:
    """Compute C(a, b) mod 1000000007 via GF(2) linear basis / Gaussian elimination."""
    spf = _sieve_spf(b)
    basis: Dict[int, Set[int]] = {}
    rank = 0
    num_vectors = b - a + 1

    for x in range(a, b + 1):
        temp = x
        sqfree_primes: List[int] = []
        while temp > 1:
            p = spf[temp]
            cnt = 0
            while temp % p == 0:
                temp //= p
                cnt ^= 1
            if cnt:
                sqfree_primes.append(p)

        vec = set(sqfree_primes)
        while vec:
            pivot = max(vec)
            if pivot not in basis:
                basis[pivot] = vec
                rank += 1
                break
            vec ^= basis[pivot]

    nullity = num_vectors - rank
    ans = (pow(2, nullity, _MOD) - 1) % _MOD
    return ans


if __name__ == "__main__":
    print(solve())
