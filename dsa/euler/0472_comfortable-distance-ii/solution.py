"""Project Euler Problem 472: Comfortable Distance II.

Find sum_{N=1..10^12} f(N) mod 10^8, where f(N) is the number of optimal initial seat choices
for N people choosing the furthest available seats without adjacency.
"""

from typing import Dict

MOD = 100_000_000


def _a_occupancy(n: int) -> int:
    if n <= 0:
        return 0
    t = n + 1
    p = 1 << (t.bit_length() - 1)
    return max(p >> 1, t - p)


def _brute_f(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2

    edge = _a_occupancy(n - 2)
    m = n - 3
    best = -1
    cnt = 0
    for x in range(m + 1):
        val = _a_occupancy(x) + _a_occupancy(m - x)
        if val > best:
            best = val
            cnt = 1
        elif val == best:
            cnt += 1

    mx = edge if edge > best else best
    ans = 0
    if edge == mx:
        ans += 2
    if best == mx:
        ans += cnt
    return ans


BASE = 64
F_BASE = [0] * (BASE + 1)
PREF_BASE = [0] * (BASE + 1)

for _i in range(1, BASE + 1):
    F_BASE[_i] = _brute_f(_i)
    PREF_BASE[_i] = PREF_BASE[_i - 1] + F_BASE[_i]


def _prefix_sum_11_block(half: int, length: int) -> int:
    if length <= 0:
        return 0
    k = half.bit_length() - 1
    if k < 3:
        s = 0
        start = 3 * half
        for n in range(start, start + length):
            s += _brute_f(n)
        return s

    m = half >> 1
    s = 4
    length -= 1
    if length == 0:
        return s

    take = min(m, length)
    s += take * (take + 1)
    length -= take
    j = take
    if length == 0:
        return s

    if j == m:
        s += 3 * m + 3
        length -= 1
        j += 1
        if length == 0:
            return s

    a1 = m + 2
    cnt = length
    s += cnt * (2 * a1 - (cnt - 1)) // 2
    return s


def solve(limit: int = 10**12, mod: int = MOD) -> int:
    """Compute sum_{1<=N<=limit} f(N) mod mod using binary block recursion and memoization."""
    memo: Dict[int, int] = {}

    def sum_upto(n: int) -> int:
        if n <= BASE:
            return PREF_BASE[n] % mod
        v = memo.get(n)
        if v is not None:
            return v

        pow2 = 1 << (n.bit_length() - 1)
        half = pow2 >> 1
        split = pow2 + half

        res = sum_upto(pow2 - 1)

        if n < split:
            u_max = n - pow2
            mapped_sum = (
                sum_upto(half + u_max) - sum_upto(half - 1)
            ) % mod
            k = half.bit_length() - 1
            if k >= 4:
                u0 = half - (half >> 2) + 1
                if u_max >= u0:
                    a = u0
                    b = u_max
                    cnt = b - a + 1
                    corr = cnt * half - (a + b) * cnt // 2
                    mapped_sum = (mapped_sum + corr) % mod
            res = (res + mapped_sum) % mod
            memo[n] = res
            return res

        sum_small_block = (sum_upto(pow2 - 1) - sum_upto(half - 1)) % mod
        k = half.bit_length() - 1
        if k >= 4:
            tail_len = (half >> 2) - 1
            corr_full = tail_len * (tail_len + 1) // 2
            sum10 = (sum_small_block + corr_full) % mod
        else:
            sum10 = 0
            for val_n in range(pow2, split):
                sum10 += _brute_f(val_n)
            sum10 %= mod

        res = (res + sum10) % mod
        len11 = n - split + 1
        res = (res + _prefix_sum_11_block(half, len11)) % mod

        memo[n] = res
        return res

    return sum_upto(limit) % mod


if __name__ == "__main__":
    print(solve())
