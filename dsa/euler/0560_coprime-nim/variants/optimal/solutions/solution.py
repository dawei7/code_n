"""Project Euler Problem 560: Coprime Nim.

Find L(10^7, 10^7) mod 10^9+7, where L(n, k) is the number of losing starting positions
with k piles of sizes between 1 and n - 1 in Coprime Nim.
"""

from array import array
from math import isqrt
from typing import List

MOD = 1_000_000_007


def _fwht_xor_inplace(a: List[int], mod: int = MOD) -> None:
    n = len(a)
    h = 1
    while h < n:
        step = h << 1
        for i in range(0, n, step):
            j = i
            end = i + h
            while j < end:
                x = a[j]
                y = a[j + h]
                s = x + y
                if s >= mod:
                    s -= mod
                d = x - y
                if d < 0:
                    d += mod
                a[j] = s
                a[j + h] = d
                j += 1
        h = step


def solve(n: int = 10_000_000, k: int = 10_000_000, mod: int = MOD) -> int:
    """Compute L(n, k) mod mod using Sprague-Grundy prime index reduction and FWHT."""
    if n <= 1:
        return 0
    limit_n = n - 1

    even_count = limit_n // 2
    odd_len = (limit_n + 1) // 2
    spf = array("I", [0]) * odd_len
    counts = array("I", [0])

    lim = isqrt(limit_n)
    i_end = (lim - 1) // 2

    for i in range(1, i_end + 1):
        if spf[i] == 0:
            p = 2 * i + 1
            spf[i] = p
            counts.append(1)

            start = (p * p - 1) // 2
            step = p
            for j in range(start, odd_len, step):
                if spf[j] == 0:
                    spf[j] = p
                    counts[-1] += 1

    for i in range(1, odd_len):
        if spf[i] == 0:
            counts.append(1)
            spf[i] = 2 * i + 1

    p_count = len(counts)
    m = 1 << ((p_count + 1).bit_length())

    a = [0] * m
    a[0] = even_count % mod
    a[1] = 1
    for idx in range(2, p_count + 1):
        a[idx] = counts[idx - 1] % mod

    _fwht_xor_inplace(a, mod)

    total = 0
    for v in a:
        total = (total + pow(v, k, mod)) % mod

    total = (total * pow(m, mod - 2, mod)) % mod
    return total


if __name__ == "__main__":
    print(solve())
