"""Project Euler Problem 550: Divisor Game.

Find f(10^7, 10^12) mod 987654321, where f(n, k) is the number of winning positions
for the first player in a k-pile divisor game with pile sizes between 2 and n.
"""

from array import array
from typing import List, Tuple

MOD = 987654321


def _fwht_xor(a: List[int], mod: int = MOD) -> None:
    n = len(a)
    h = 1
    while h < n:
        step = h << 1
        for i in range(0, n, step):
            j_end = i + h
            for j in range(i, j_end):
                x = a[j]
                y = a[j + h]
                a[j] = (x + y) % mod
                a[j + h] = (x - y) % mod
        h = step


def _compute_h_sequence(tmax: int) -> List[int]:
    if tmax <= 0:
        return [0] * (tmax + 1)

    h = [0] * (tmax + 1)
    h[1] = 0
    prev = [0]

    for t in range(2, tmax + 1):
        reachable = set()
        for a in prev:
            for b in prev:
                reachable.add(a ^ b)
        mex = 0
        while mex in reachable:
            mex += 1
        h[t] = mex
        prev.append(mex)

    return h


def _omega_counts_up_to(n: int) -> Tuple[List[int], int]:
    spf = array("I", [0]) * (n + 1)
    omega = bytearray(n + 1)
    primes: List[int] = []

    counts = [0] * 32
    max_om = 0

    spf_local = spf
    omega_local = omega
    primes_append = primes.append
    counts_local = counts

    for i in range(2, n + 1):
        si = spf_local[i]
        if si == 0:
            spf_local[i] = i
            primes_append(i)
            omega_local[i] = 1
            si = i
            oi = 1
        else:
            oi = omega_local[i]

        counts_local[oi] += 1
        if oi > max_om:
            max_om = oi

        for p in primes:
            ip = i * p
            if ip > n:
                break
            spf_local[ip] = p
            omega_local[ip] = oi + 1
            if p == si:
                break

    return counts_local, max_om


def solve(n: int = 10_000_000, k: int = 10**12, mod: int = MOD) -> int:
    """Compute f(n, k) mod mod using Sprague-Grundy prime factor count reduction and FWHT."""
    omega_counts, max_om = _omega_counts_up_to(n)
    h = _compute_h_sequence(max_om)

    max_g = 0
    for t in range(1, max_om + 1):
        if h[t] > max_g:
            max_g = h[t]

    size = 1 << (max_g.bit_length())
    vec = [0] * size
    for t in range(1, max_om + 1):
        vec[h[t]] += omega_counts[t]
    vec = [v % mod for v in vec]

    _fwht_xor(vec, mod)

    s = 0
    for v in vec:
        s = (s + pow(v, k, mod)) % mod

    inv_size = pow(size, -1, mod)
    losing = s * inv_size % mod
    total = pow(n - 1, k, mod)
    return (total - losing) % mod


if __name__ == "__main__":
    print(solve())
