"""Project Euler Problem 411: Uphill Paths.

Find sum_{k=1..30} S(k^5), where S(n) is the maximum number of stations on an uphill path
through distinct stations (2^i mod n, 3^i mod n) for 0 <= i <= 2n.
"""

from array import array
from bisect import bisect_right
from math import gcd
from typing import Dict


def _factor(n: int) -> Dict[int, int]:
    factors: Dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def _phi(n: int) -> int:
    factors = _factor(n)
    res = n
    for p in factors:
        res //= p
        res *= p - 1
    return res


def _multiplicative_order(a: int, n: int) -> int:
    if n == 1:
        return 1
    if gcd(a, n) != 1:
        raise ValueError("a and n must be coprime")
    ph = _phi(n)
    factors = _factor(ph)
    order = ph
    for p, exp in factors.items():
        for _ in range(exp):
            if order % p == 0 and pow(a, order // p, n) == 1:
                order //= p
            else:
                break
    return order


def _compute_s(n: int) -> int:
    n2 = n
    v2 = 0
    while n2 % 2 == 0:
        n2 //= 2
        v2 += 1

    n3 = n
    v3 = 0
    while n3 % 3 == 0:
        n3 //= 3
        v3 += 1

    preperiod = max(v2, v3)
    ord2 = 1 if n2 == 1 else _multiplicative_order(2, n2)
    ord3 = 1 if n3 == 1 else _multiplicative_order(3, n3)
    period = ord2 // gcd(ord2, ord3) * ord3
    total = preperiod + period

    # Counting sort array by x-coordinate
    counts = array("I", [0]) * (n + 1)
    x = 1 % n
    for _ in range(total):
        counts[x] += 1
        x = (x * 2) % n

    running = 0
    for i in range(n):
        c = counts[i]
        counts[i] = running
        running += c
    counts[n] = running

    pos = counts[:-1]
    ys = array("I", [0]) * total

    x = 1 % n
    y = 1 % n
    for _ in range(total):
        idx = pos[x]
        ys[idx] = y
        pos[x] = idx + 1
        x = (x * 2) % n
        y = (y * 3) % n

    # Longest non-decreasing subsequence over 2D sorted points
    tails: list[int] = []
    for x_val in range(n):
        start = counts[x_val]
        end = counts[x_val + 1]
        if start == end:
            continue
        if end - start == 1:
            y_val = ys[start]
            idx_pos = bisect_right(tails, y_val)
            if idx_pos == len(tails):
                tails.append(y_val)
            else:
                tails[idx_pos] = y_val
        else:
            segment = list(ys[start:end])
            segment.sort()
            for y_val in segment:
                idx_pos = bisect_right(tails, y_val)
                if idx_pos == len(tails):
                    tails.append(y_val)
                else:
                    tails[idx_pos] = y_val

    return len(tails)


def solve(k_limit: int = 30) -> int:
    """Compute sum_{k=1..k_limit} S(k^5)."""
    total = 0
    for k in range(1, k_limit + 1):
        total += _compute_s(k**5)
    return total


if __name__ == "__main__":
    print(solve())
