"""Project Euler Problem 629: Scatterstone Nim.

Find g(200) mod 1000000007, where g(n) is the sum of winning positions f(n, k)
for Alice over all 2 <= k <= n in Scatterstone Nim.
"""

from typing import List

_MOD = 1_000_000_007


def _partition_numbers(n_max: int) -> List[int]:
    p = [0] * (n_max + 1)
    p[0] = 1
    for part in range(1, n_max + 1):
        for s in range(part, n_max + 1):
            p[s] += p[s - part]
            if p[s] >= _MOD:
                p[s] -= _MOD
    return p


def _grundy_k2(n_max: int) -> List[int]:
    g = [0] * (n_max + 1)
    for s in range(2, n_max + 1):
        g[s] = 1 if (s % 2 == 0) else 0
    return g


def _grundy_k3(n_max: int) -> List[int]:
    g = [0] * (n_max + 1)
    for n in range(2, n_max + 1):
        seen = [False] * 256
        for a in range(1, n // 2 + 1):
            seen[g[a] ^ g[n - a]] = True

        for a in range(1, n // 3 + 1):
            max_b = (n - a) // 2
            for b in range(a, max_b + 1):
                c = n - a - b
                if b <= c:
                    seen[g[a] ^ g[b] ^ g[c]] = True

        mex = 0
        while mex < len(seen) and seen[mex]:
            mex += 1
        g[n] = mex
    return g


def _grundy_k4plus(n_max: int) -> List[int]:
    return [max(0, s - 1) for s in range(n_max + 1)]


def _count_losing_partitions(n: int, grundy: List[int]) -> int:
    max_g = max(grundy[1 : n + 1])
    width = 1
    while width < max_g + 1:
        width <<= 1
    if width < 2:
        width = 2

    dp = [[0] * width for _ in range(n + 1)]
    dp[0][0] = 1

    for size in range(1, n + 1):
        g = grundy[size]
        pair = 2 * size

        if pair <= n:
            for s in range(pair, n + 1):
                src = dp[s - pair]
                dst = dp[s]
                for x, val in enumerate(src):
                    if val:
                        nv = dst[x] + val
                        if nv >= _MOD:
                            nv -= _MOD
                        dst[x] = nv

        for s in range(n, size - 1, -1):
            src = dp[s - size]
            dst = dp[s]
            if g == 0:
                for x, val in enumerate(src):
                    if val:
                        nv = dst[x] + val
                        if nv >= _MOD:
                            nv -= _MOD
                        dst[x] = nv
            else:
                for x, val in enumerate(src):
                    if val:
                        j = x ^ g
                        nv = dst[j] + val
                        if nv >= _MOD:
                            nv -= _MOD
                        dst[j] = nv

    return dp[n][0]


def solve(n: int = 200) -> int:
    """Compute g(n) modulo 1000000007 by classifying Sprague-Grundy values across split bounds."""
    if n < 2:
        return 0

    partitions = _partition_numbers(n)
    g2 = _grundy_k2(n)
    g3 = _grundy_k3(n)
    g4 = _grundy_k4plus(n)

    f2 = (partitions[n] - _count_losing_partitions(n, g2)) % _MOD
    f3 = (partitions[n] - _count_losing_partitions(n, g3)) % _MOD
    f4 = (partitions[n] - _count_losing_partitions(n, g4)) % _MOD

    total = 0
    for k in range(2, n + 1):
        if k == 2:
            val = f2
        elif k == 3:
            val = f3
        else:
            val = f4
        total = (total + val) % _MOD

    return total


if __name__ == "__main__":
    print(solve())
