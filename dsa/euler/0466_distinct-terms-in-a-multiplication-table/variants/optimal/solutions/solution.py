"""Project Euler Problem 466: Distinct Terms in a Multiplication Table.

Find P(64, 10^16), the number of distinct terms in an m x n multiplication table.
"""

from functools import lru_cache
from math import gcd
from typing import Dict, Iterable, List, Tuple


def _lcm(a: int, b: int) -> int:
    return (a // gcd(a, b)) * b


def _minimal_under_divisibility(
    nums: Iterable[int],
) -> Tuple[int, ...]:
    uniq = sorted(set(x for x in nums if x > 1))
    kept: List[int] = []
    for x in uniq:
        redundant = False
        for y in kept:
            if x % y == 0:
                redundant = True
                break
        if not redundant:
            kept.append(x)
    return tuple(kept)


def _forbidden_set(d: int, m: int) -> Tuple[int, ...]:
    return _minimal_under_divisibility(
        e // gcd(e, d) for e in range(d + 1, m + 1)
    )


def _count_divisible_by_any(n: int, divisors: Tuple[int, ...]) -> int:
    if not divisors:
        return 0
    divs = tuple(x for x in divisors if x <= n)
    if not divs:
        return 0

    @lru_cache(maxsize=None)
    def ie(start: int, cur_lcm: int) -> int:
        total = 0
        for i in range(start, len(divs)):
            nl = _lcm(cur_lcm, divs[i])
            if nl > n:
                continue
            total += (n // nl) - ie(i + 1, nl)
        return total

    return ie(0, 1)


def solve(m: int = 64, n: int = 10**16) -> int:
    """Compute P(m, n) by partitioning on the maximal bounded divisor and inclusion-exclusion."""
    if m <= 0 or n <= 0:
        return 0

    total = 0
    cache: Dict[Tuple[int, ...], int] = {}

    for d in range(1, m + 1):
        fs = _forbidden_set(d, m)
        bad = cache.get(fs)
        if bad is None:
            bad = _count_divisible_by_any(n, fs)
            cache[fs] = bad
        total += n - bad

    return total


if __name__ == "__main__":
    print(solve())
