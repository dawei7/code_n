"""Project Euler Problem 616: Creative Numbers.

Find the sum of all creative numbers less than or equal to 10^12.
"""

from math import isqrt
from typing import List, Set


def _sieve_primes(n: int) -> List[int]:
    if n < 2:
        return []
    bs = bytearray(b"\x01") * (n + 1)
    bs[0:2] = b"\x00\x00"
    for p in range(2, int(n**0.5) + 1):
        if bs[p]:
            bs[p * p : n + 1 : p] = b"\x00" * (((n - p * p) // p) + 1)
    return [i for i in range(n + 1) if bs[i]]


def solve(limit: int = 10**12) -> int:
    """Sum all creative integers up to limit = 10^12."""
    perfect_powers: Set[int] = set()
    for exp in range(2, 41):
        base = int(limit ** (1.0 / exp))
        while (base + 1) ** exp <= limit:
            base += 1
        while base**exp > limit:
            base -= 1

        for a in range(2, base + 1):
            perfect_powers.add(a**exp)

    prime_powers: Set[int] = set()
    primes_base = _sieve_primes(isqrt(limit))
    prime_exps = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    for q in prime_exps:
        maxb = int(limit ** (1.0 / q))
        while (maxb + 1) ** q <= limit:
            maxb += 1
        while maxb**q > limit:
            maxb -= 1

        for p in primes_base:
            if p > maxb:
                break
            prime_powers.add(p**q)

    # Creative numbers are all perfect powers except p^q (p, q prime) and 16
    sum_pp = sum(perfect_powers)
    sum_pq = sum(prime_powers)
    ans = sum_pp - sum_pq
    if 16 <= limit:
        ans -= 16

    return ans


if __name__ == "__main__":
    print(solve())
