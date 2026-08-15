"""Project Euler Problem 486: Palindrome-containing Strings.

Find D(10^18), the number of integers n in [5, 10^18] such that F_5(n) is divisible by 87654321,
where F_5(n) counts binary strings of length <= n containing a palindrome of length >= 5.
"""

from typing import List, Tuple

MOD = 87654321
B_SMALL = [1, 3, 7, 15, 31, 55, 85]
B6 = 85
PERIOD = 6
PERIOD_SUM = 200
PREFIX = (0, 32, 64, 96, 130, 166)


def _modinv(a: int, m: int) -> int:
    t0, t1 = 0, 1
    r0, r1 = m, a % m
    while r1:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        t0, t1 = t1, t0 - q * t1
    if r0 != 1:
        raise ValueError("inverse does not exist")
    return t0 % m


def _pal_free_cumulative(n: int) -> int:
    if n <= 6:
        return B_SMALL[n]
    q, r = divmod(n - 6, PERIOD)
    return B6 + q * PERIOD_SUM + PREFIX[r]


def _f5(n: int) -> int:
    total = (1 << (n + 1)) - 1
    return total - _pal_free_cumulative(n)


def _prepare_thresholds(
    limit_l: int, o64: int, period_q: int
) -> Tuple[int, List[int]]:
    if limit_l < 6:
        return 0, [0] * 6

    base = 0
    r_list = [0] * 6
    for r in range(6):
        qmax = (limit_l - r - 6) // 6
        if qmax < 0:
            r_list[r] = 0
            continue
        num_q = qmax + 1
        q_cycles = num_q // period_q
        base += q_cycles * o64
        r_list[r] = num_q - q_cycles * period_q
    return base, r_list


def solve(limit_l: int = 10**18, mod: int = MOD) -> int:
    """Compute D(L) using periodic DFA palindrome exclusion and CRT modulo 87654321."""
    o64 = 1216562
    period_q = mod * o64

    inv200 = _modinv(200, mod)
    inv_o = _modinv(o64, mod)

    pow2 = [pow(2, r + 7, mod) for r in range(6)]
    c_const = [(1 + B6 + PREFIX[r]) % mod for r in range(6)]

    base, r_bounds = _prepare_thresholds(limit_l, o64, period_q)
    extra = 0

    pow64 = 1
    for k in range(o64):
        for r in range(6):
            l_val = (pow2[r] * pow64) % mod
            q0 = ((l_val - c_const[r]) * inv200) % mod

            diff = q0 - k
            if diff < 0:
                diff += mod
            t = (diff * inv_o) % mod
            q_res = k + o64 * t

            if q_res < r_bounds[r]:
                extra += 1

        pow64 = (pow64 * 64) % mod

    add5 = 1 if limit_l >= 5 and (_f5(5) % mod == 0) else 0
    return add5 + base + extra


if __name__ == "__main__":
    print(solve())
