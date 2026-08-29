"""Project Euler Problem 585: Nested Square Roots.

Find F(5000000), where F(n) is the number of distinct denestable nested square roots
sqrt(x + sqrt(y) + sqrt(z)) with 0 < x <= n and y, z non-squares.
"""

from array import array
import math
from typing import Dict, List


def _totient_sieve(n: int) -> array:
    phi = array("I", [0]) * (n + 1)
    is_comp = bytearray(n + 1)
    primes: List[int] = []
    if n >= 1:
        phi[1] = 1
    for i in range(2, n + 1):
        if not is_comp[i]:
            primes.append(i)
            phi[i] = i - 1
        for p in primes:
            ip = i * p
            if ip > n:
                break
            is_comp[ip] = 1
            if i % p == 0:
                phi[ip] = phi[i] * p
                break
            phi[ip] = phi[i] * (p - 1)
    return phi


def _primitive_pair_counts(n: int) -> array:
    tot = _totient_sieve(n)
    phi = array("i", [0]) * (n + 1)
    for s in range(3, n + 1):
        phi[s] = tot[s] // 2

    lim = int(math.isqrt(n))
    gcd = math.gcd
    for a in range(2, lim + 1):
        a2 = a * a
        maxb = int(math.isqrt(n - a2))
        for b in range(1, min(a, maxb + 1)):
            if gcd(a, b) == 1:
                phi[a2 + b * b] -= 1
    return phi


def _prefix_sums_int64(vals: array) -> array:
    s_arr = array("q", [0]) * len(vals)
    acc = 0
    for i, v in enumerate(vals):
        acc += int(v)
        s_arr[i] = acc
    return s_arr


def _grouped_sum_floor(n: int, s_phi: array) -> int:
    res = 0
    i = 1
    while i <= n:
        q = n // i
        j = n // q
        res += q * (s_phi[j] - s_phi[i - 1])
        i = j + 1
    return int(res)


def _compute_c3_kernel(n: int) -> int:
    lim = int(math.isqrt(n))
    is_sf = [True] * (lim + 1)
    if lim >= 0:
        is_sf[0] = False
    r = int(math.isqrt(lim))
    for p in range(2, r + 1):
        sq = p * p
        for k in range(sq, lim + 1, sq):
            is_sf[k] = False

    gcd = math.gcd
    cnt3 = 0

    for p in range(1, lim):
        if (p + 1) * (p + 1) > n:
            break
        if not is_sf[p]:
            continue

        for q in range(1, lim + 1):
            if not is_sf[q] or gcd(p, q) != 1:
                continue
            if (p * q + 1) * (p + q) > n:
                break
            pq = p * q

            for r_val in range(1, lim + 1):
                if not is_sf[r_val] or gcd(pq, r_val) != 1:
                    continue
                if (pq + r_val) * (p * r_val + q) > n:
                    break
                pr = p * r_val
                pqr = pq * r_val

                for s in range(1, lim + 1):
                    if not is_sf[s] or gcd(pqr, s) != 1:
                        continue
                    if (pq + r_val * s) * (pr + q * s) > n:
                        break

                    u = pq
                    v = r_val * s
                    a = pr
                    b = q * s
                    if u == v or a == b:
                        continue

                    ab_sum = a + b
                    w1 = 1
                    while (u * w1 * w1 + v) * ab_sum <= n:
                        u_w1 = u * w1
                        u_w1_sq = u_w1 * w1
                        w2 = 1
                        while (u_w1_sq + v * w2 * w2) * ab_sum <= n:
                            v_w2 = v * w2
                            s1 = u_w1_sq + v_w2 * w2
                            w3 = 1
                            while s1 * (a * w3 * w3 + b) <= n:
                                a_w3 = a * w3
                                a_w3_sq = a_w3 * w3
                                w4 = 1
                                while s1 * (a_w3_sq + b * w4 * w4) <= n:
                                    b_w4 = b * w4
                                    s2 = a_w3_sq + b_w4 * w4
                                    if u_w1_sq > v_w2 * w2 and a_w3_sq > b_w4 * w4:
                                        if (
                                            gcd(u_w1, v_w2) == 1
                                            and gcd(a_w3, b_w4) == 1
                                        ):
                                            cnt3 += (n // s1) // s2
                                    w4 += 1
                                w3 += 1
                            w2 += 1
                        w1 += 1
    return cnt3


def solve(n: int = 5_000_000) -> int:
    """Compute F(n) using Dirichlet hyperbola convolution and kernel factor enumeration."""
    phi = _primitive_pair_counts(n)
    s_phi = _prefix_sums_int64(phi)

    # 1-radical term A(n)
    a_val = _grouped_sum_floor(n, s_phi)

    # 2-radical convolution C1(n)
    cache: Dict[int, int] = {}

    def p_func(m: int) -> int:
        v = cache.get(m)
        if v is None:
            v = _grouped_sum_floor(m, s_phi)
            cache[m] = v
        return v

    c1_val = 0
    i = 1
    while i <= n:
        q = n // i
        j = n // q
        sum_phi = s_phi[j] - s_phi[i - 1]
        c1_val += int(sum_phi) * p_func(q)
        i = j + 1

    # Degenerate kernel exclusion C3(n) evaluated via kernel factors
    c3_val = _compute_c3_kernel(n)

    return a_val + (c1_val - c3_val) // 2


if __name__ == "__main__":
    print(solve())
