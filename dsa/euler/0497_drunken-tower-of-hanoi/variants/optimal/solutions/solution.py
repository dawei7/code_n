"""Project Euler Problem 497: Drunken Tower of Hanoi.

Find the last 9 digits of sum_{1 <= n <= 10000} E(n, 10^n, 3^n, 6^n, 9^n),
where E(n, k, a, b, c) is the expected number of squares Bob travels during a game of Tower of Hanoi.
"""

from typing import List, Optional

MOD = 1_000_000_000
EDGES = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
EDGE_IDX = {e: i for i, e in enumerate(EDGES)}


def _expected_steps_reflecting(i: int, j: int, k: int) -> int:
    if i == j:
        return 0
    if i < j:
        return (j - i) * (j + i - 2)
    return (i - j) * (2 * k - i - j)


def _init_counts(mod: Optional[int]) -> List[List[List[List[int]]]]:
    dp = [[[[0] * 6 for _ in range(3)] for _ in range(3)] for _ in range(3)]
    for fr in range(3):
        for to in range(3):
            if fr == to:
                continue
            for st in range(3):
                vec = [0] * 6
                if st != fr:
                    vec[EDGE_IDX[(st, fr)]] += 1
                vec[EDGE_IDX[(fr, to)]] += 1
                if mod is not None:
                    vec = [x % mod for x in vec]
                dp[fr][to][st] = vec
    return dp


def _step_counts(
    dp: List[List[List[List[int]]]], mod: Optional[int]
) -> List[List[List[List[int]]]]:
    new_dp = [
        [[[0] * 6 for _ in range(3)] for _ in range(3)] for _ in range(3)
    ]
    for fr in range(3):
        for to in range(3):
            if fr == to:
                continue
            aux = 3 - fr - to
            for st in range(3):
                v1 = dp[fr][aux][st]
                v2 = dp[aux][to][to]
                vec = [v1[i] + v2[i] for i in range(6)]
                vec[EDGE_IDX[(aux, fr)]] += 1
                vec[EDGE_IDX[(fr, to)]] += 1
                if mod is not None:
                    vec = [x % mod for x in vec]
                new_dp[fr][to][st] = vec
    return new_dp


def expected_distance(n: int, k: int, a: int, b: int, c: int) -> int:
    """Exact expected distance for small test cases."""
    pos = {0: a, 1: b, 2: c}
    d_map = {
        (u, v): _expected_steps_reflecting(pos[u], pos[v], k)
        for u in range(3)
        for v in range(3)
        if u != v
    }

    dp = _init_counts(mod=None)
    for _ in range(2, n + 1):
        dp = _step_counts(dp, mod=None)

    counts = dp[0][2][1]
    return sum(counts[idx] * d_map[(u, v)] for idx, (u, v) in enumerate(EDGES))


def solve(limit: int = 10_000, mod: int = MOD) -> int:
    """Compute the last 9 digits of sum_{n=1..limit} E(n, 10^n, 3^n, 6^n, 9^n)."""
    dp = _init_counts(mod=mod)
    a = b = c = k = 1
    total = 0

    for n in range(1, limit + 1):
        a = (a * 3) % mod
        b = (b * 6) % mod
        c = (c * 9) % mod
        k = (k * 10) % mod

        if n > 1:
            dp = _step_counts(dp, mod=mod)

        d01 = ((b - a) % mod) * ((b + a - 2) % mod) % mod
        d02 = ((c - a) % mod) * ((c + a - 2) % mod) % mod
        d10 = ((b - a) % mod) * ((2 * k - b - a) % mod) % mod
        d12 = ((c - b) % mod) * ((c + b - 2) % mod) % mod
        d20 = ((c - a) % mod) * ((2 * k - c - a) % mod) % mod
        d21 = ((c - b) % mod) * ((2 * k - c - b) % mod) % mod

        dist_vec = [d01, d02, d10, d12, d20, d21]
        counts = dp[0][2][1]

        en = sum(counts[i] * dist_vec[i] for i in range(6)) % mod
        total = (total + en) % mod

    return total


if __name__ == "__main__":
    print(solve())
