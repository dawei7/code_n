"""Project Euler Problem 725: Digit Sum Numbers.

Find S(2020) mod 10^16, where S(n) is the sum of all DS-numbers of n digits or less,
and a DS-number has one digit equal to the sum of all its other digits.
"""

import math
from typing import List, Tuple

_MOD = 10**16


def _partition(goal: int) -> List[List[Tuple[int, ...]]]:
    part: List[List[Tuple[int, ...]]] = [[] for _ in range(goal + 1)]
    part[0] = [()]
    for opt in range(1, goal + 1):
        for i in range(len(part) - opt):
            for y in part[i]:
                part[i + opt].append((opt,) + y)
    return part


def _combs(x: Tuple[int, ...], n: int) -> int:
    d = [x.count(i) for i in range(10)]
    d[0] = n - sum(d)
    t = math.factorial(n) // math.factorial(d[0])
    for v in range(1, 10):
        t //= math.factorial(d[v])
    return t


def solve(n: int = 2020, mod: int = _MOD) -> int:
    """Compute S(n) modulo 10^16 using integer partitions of maximal digits and multinomial coefficient sums."""
    part = _partition(9)
    total = 0
    rep = (10**n - 1) // 9

    for k in range(1, 10):
        for p in part[k]:
            full_p = p + (k,)
            if len(full_p) - 1 < n:
                t = _combs(full_p, n)
                v = (rep * 2 * k * t) // n
                total = (total + v) % mod

    return total


if __name__ == "__main__":
    print(solve())
