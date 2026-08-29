"""Project Euler Problem 464: Mobius Function and Intervals.

Find C(20_000_000), the number of integer pairs (a, b) such that 1 <= a <= b <= n,
99 * N(a, b) <= 100 * P(a, b) and 99 * P(a, b) <= 100 * N(a, b).
"""

from collections import Counter
from typing import Dict, List, Tuple


def solve(n: int = 20_000_000) -> int:
    """Compute C(n) using 2D prefix coordinate reduction and Fenwick tree sweep."""
    mu = bytearray(n + 1)
    is_comp = bytearray(n + 1)
    primes: List[int] = []
    mu[1] = 1

    for i in range(2, n + 1):
        if not is_comp[i]:
            primes.append(i)
            mu[i] = 2
        for p in primes:
            ip = i * p
            if ip > n:
                break
            is_comp[ip] = 1
            if i % p == 0:
                break
            mu[ip] = 2 if mu[i] == 1 else (1 if mu[i] == 2 else 0)

    u = 0
    v = 0
    p_cnt = 0
    n_cnt = 0

    counts: Dict[Tuple[int, int], int] = Counter()
    counts[(0, 0)] = 1

    for i in range(1, n + 1):
        m = mu[i]
        if m == 1:
            p_cnt += 1
        elif m == 2:
            n_cnt += 1
        u = 100 * p_cnt - 99 * n_cnt
        v = 100 * n_cnt - 99 * p_cnt
        counts[(u, v)] += 1

    unique_pts = sorted(counts.keys())
    unique_v = sorted(set(pt[1] for pt in unique_pts))
    v_map = {val: idx + 1 for idx, val in enumerate(unique_v)}

    bit_size = len(unique_v) + 2
    bit = [0] * bit_size

    def add(idx: int, val: int) -> None:
        while idx < bit_size:
            bit[idx] += val
            idx += idx & -idx

    def query(idx: int) -> int:
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= idx & -idx
        return s

    ans = 0
    for pt in unique_pts:
        cnt = counts[pt]
        vr = v_map[pt[1]]
        smaller = query(vr)
        ans += smaller * cnt
        ans += cnt * (cnt - 1) // 2
        add(vr, cnt)

    return ans


if __name__ == "__main__":
    print(solve())
