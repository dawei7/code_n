"""Project Euler Problem 579: Lattice Points in Lattice Cubes.

Find S(5000) mod 10^9, where S(n) is the sum of lattice points inside/on all
lattice cubes whose vertices lie in [0, n]^3.
"""

from math import gcd, isqrt
from typing import List, Optional, Tuple


def _power_sums(n_val: int, k_max: int) -> List[List[int]]:
    sums = [[0] * (n_val + 1) for _ in range(k_max + 1)]
    for t in range(1, n_val + 1):
        sums[0][t] = t
        p = t
        sums[1][t] = sums[1][t - 1] + p
        for k in range(2, k_max + 1):
            p *= t
            sums[k][t] = sums[k][t - 1] + p
    return sums


def solve(n: int = 5000, mod: Optional[int] = 1_000_000_000) -> int:
    """Compute S(n) mod `mod` using quaternion parameterization and Ehrhart polynomial summation."""
    k_max = 6
    sums = _power_sums(n, k_max)

    a_len = n + 1
    a2 = a_len * a_len
    a3 = a2 * a_len

    total_s = 0
    b_limit = isqrt(n)

    start_even = -b_limit if (b_limit & 1) == 0 else -b_limit + 1
    start_odd = -b_limit if (b_limit & 1) == 1 else -b_limit + 1
    even_vals = list(range(start_even, b_limit + 1, 2))
    odd_vals = list(range(start_odd, b_limit + 1, 2))

    max_a = b_limit
    a_lists = [[[[] for _ in range(max_a + 1)] for _ in range(4)] for _ in range(2)]
    for m_a in range(0, max_a + 1):
        for a in range(-m_a, m_a + 1):
            a_lists[a & 1][a & 3][m_a].append(a)

    abs_val = abs

    def gcd3(x: int, y: int, z: int) -> int:
        return gcd(gcd(abs_val(x), abs_val(y)), abs_val(z))

    cases = (
        (even_vals, 1, n - 1),
        (odd_vals, 0, n),
    )

    for bcd_vals, a_parity, s_limit in cases:
        for b in bcd_vals:
            bb = b * b
            for c in bcd_vals:
                cc = c * c
                bc2 = bb + cc
                for d in bcd_vals:
                    dd = d * d
                    s = bc2 + dd
                    if s > s_limit:
                        continue

                    rem = n - s
                    max_cand_a = isqrt(rem)

                    sum_bcd_mod4 = (b + c + d) & 3
                    a_res = (1 - sum_bcd_mod4) & 3

                    g_bcd = gcd3(b, c, d)

                    for a in a_lists[a_parity][a_res][max_cand_a]:
                        if gcd(g_bcd, abs_val(a)) != 1:
                            continue

                        aa = a * a
                        m = aa + s

                        u0 = aa + bb - cc - dd
                        u1 = 2 * (b * c - a * d)
                        u2 = 2 * (b * d + a * c)

                        v0 = 2 * (b * c + a * d)
                        v1 = aa - bb + cc - dd
                        v2 = 2 * (c * d - a * b)

                        w0 = 2 * (b * d - a * c)
                        w1 = 2 * (c * d + a * b)
                        w2 = aa - bb - cc + dd

                        sx = abs_val(u0) + abs_val(v0) + abs_val(w0)
                        sy = abs_val(u1) + abs_val(v1) + abs_val(w1)
                        sz = abs_val(u2) + abs_val(v2) + abs_val(w2)

                        t_bound = n // sx
                        ty = n // sy
                        if ty < t_bound:
                            t_bound = ty
                        tz = n // sz
                        if tz < t_bound:
                            t_bound = tz
                        if t_bound == 0:
                            continue

                        s1 = sx + sy + sz
                        s2 = sx * sy + sy * sz + sz * sx
                        s3 = sx * sy * sz

                        t0 = a3
                        t1 = -a2 * s1
                        t2 = a_len * s2
                        t3 = -s3

                        g_u = gcd(abs_val(u0), gcd(abs_val(u1), abs_val(u2)))
                        g_v = gcd(abs_val(v0), gcd(abs_val(v1), abs_val(v2)))
                        g_w = gcd(abs_val(w0), gcd(abs_val(w1), abs_val(w2)))
                        g1 = g_u + g_v + g_w

                        p1 = g1
                        p2 = m * g1
                        p3 = m * m * m

                        s0 = t_bound
                        s1p = sums[1][t_bound]
                        s2p = sums[2][t_bound]
                        s3p = sums[3][t_bound]
                        s4p = sums[4][t_bound]
                        s5p = sums[5][t_bound]
                        s6p = sums[6][t_bound]

                        if mod is None:
                            d0 = t0
                            d1 = t0 * p1 + t1
                            d2 = t0 * p2 + t1 * p1 + t2
                            d3 = t0 * p3 + t1 * p2 + t2 * p1 + t3
                            d4 = t1 * p3 + t2 * p2 + t3 * p1
                            d5 = t2 * p3 + t3 * p2
                            d6 = t3 * p3

                            total_s += (
                                d0 * s0
                                + d1 * s1p
                                + d2 * s2p
                                + d3 * s3p
                                + d4 * s4p
                                + d5 * s5p
                                + d6 * s6p
                            )
                        else:
                            big_m = mod
                            t0m = t0 % big_m
                            t1m = t1 % big_m
                            t2m = t2 % big_m
                            t3m = t3 % big_m

                            p1m = p1 % big_m
                            p2m = p2 % big_m
                            p3m = p3 % big_m

                            d0 = t0m
                            d1 = (t0m * p1m + t1m) % big_m
                            d2 = (t0m * p2m + t1m * p1m + t2m) % big_m
                            d3 = (t0m * p3m + t1m * p2m + t2m * p1m + t3m) % big_m
                            d4 = (t1m * p3m + t2m * p2m + t3m * p1m) % big_m
                            d5 = (t2m * p3m + t3m * p2m) % big_m
                            d6 = (t3m * p3m) % big_m

                            total_s = (
                                total_s
                                + d0 * (s0 % big_m)
                                + d1 * (s1p % big_m)
                                + d2 * (s2p % big_m)
                                + d3 * (s3p % big_m)
                                + d4 * (s4p % big_m)
                                + d5 * (s5p % big_m)
                                + d6 * (s6p % big_m)
                            ) % big_m

    return total_s


if __name__ == "__main__":
    print(solve())
