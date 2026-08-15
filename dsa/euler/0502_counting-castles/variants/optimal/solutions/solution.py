"""Project Euler Problem 502: Counting Castles.

Find (F(10^12, 100) + F(10000, 10000) + F(100, 10^12)) mod 1_000_000_007,
where F(w, h) is the number of valid castles with width w and height h.
"""

from typing import List, Tuple

MOD = 1_000_000_007
INV2 = (MOD + 1) // 2

P1, G1 = 998244353, 3
P2, G2 = 1004535809, 3
P3, G3 = 469762049, 3

INV_P1_MOD_P2 = pow(P1 % P2, P2 - 2, P2)
P12 = P1 * P2
INV_P12_MOD_P3 = pow(P12 % P3, P3 - 2, P3)


def _ntt(a: List[int], invert: bool, mod: int, root: int) -> None:
    n = len(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            a[i], a[j] = a[j], a[i]

    length = 2
    while length <= n:
        wlen = pow(root, (mod - 1) // length, mod)
        if invert:
            wlen = pow(wlen, mod - 2, mod)
        half = length >> 1
        for i in range(0, n, length):
            w = 1
            for j_idx in range(i, i + half):
                u = a[j_idx]
                v = (a[j_idx + half] * w) % mod
                a[j_idx] = (u + v) % mod
                a[j_idx + half] = (u - v) % mod
                w = (w * wlen) % mod
        length <<= 1

    if invert:
        n_inv = pow(n, mod - 2, mod)
        for i in range(n):
            a[i] = (a[i] * n_inv) % mod


def _convolve_mod(a: List[int], b: List[int]) -> List[int]:
    if not a or not b:
        return []
    n1, n2 = len(a), len(b)
    n = 1
    while n < n1 + n2 - 1:
        n <<= 1

    fa1 = [0] * n
    fb1 = [0] * n
    fa2 = [0] * n
    fb2 = [0] * n
    fa3 = [0] * n
    fb3 = [0] * n

    for i, x in enumerate(a):
        fa1[i] = x % P1
        fa2[i] = x % P2
        fa3[i] = x % P3
    for i, x in enumerate(b):
        fb1[i] = x % P1
        fb2[i] = x % P2
        fb3[i] = x % P3

    _ntt(fa1, False, P1, G1)
    _ntt(fb1, False, P1, G1)
    _ntt(fa2, False, P2, G2)
    _ntt(fb2, False, P2, G2)
    _ntt(fa3, False, P3, G3)
    _ntt(fb3, False, P3, G3)

    for i in range(n):
        fa1[i] = fa1[i] * fb1[i] % P1
        fa2[i] = fa2[i] * fb2[i] % P2
        fa3[i] = fa3[i] * fb3[i] % P3

    _ntt(fa1, True, P1, G1)
    _ntt(fa2, True, P2, G2)
    _ntt(fa3, True, P3, G3)

    m = n1 + n2 - 1
    res = [0] * m
    for i in range(m):
        r1, r2, r3 = fa1[i], fa2[i], fa3[i]
        t2 = ((r2 - r1) % P2 * INV_P1_MOD_P2) % P2
        x12 = r1 + P1 * t2
        t3 = ((r3 - (x12 % P3)) % P3 * INV_P12_MOD_P3) % P3
        res[i] = (x12 + P12 * t3) % MOD

    return res


def _poly_mul_trunc(a: List[int], b: List[int], n: int) -> List[int]:
    res = _convolve_mod(a, b)
    if len(res) < n:
        res += [0] * (n - len(res))
    return res[:n]


def _inv_series(q: List[int], n: int) -> List[int]:
    invq = [pow(q[0], MOD - 2, MOD)]
    m = 1
    while m < n:
        m2 = min(2 * m, n)
        t = _poly_mul_trunc(q[:m2], invq, m2)
        t[0] = (2 - t[0]) % MOD
        for i in range(1, m2):
            t[i] = (-t[i]) % MOD
        invq = _poly_mul_trunc(invq, t, m2)
        m = m2
    return invq[:n]


def _build_pq_mod(h: int, y: int, deg_limit: int) -> Tuple[List[int], List[int]]:
    if h <= 0:
        return [0], [1]

    y_mod = 1 if y == 1 else MOD - 1
    P = [0, y_mod]
    Q = [1, MOD - 1]

    if h == 1:
        return P[: deg_limit + 1], Q[: deg_limit + 1]

    for _ in range(2, h + 1):
        old_len = len(P)
        new_len = min(old_len + 1, deg_limit + 1)
        newP = [0] * new_len
        newQ = [0] * new_len
        newQ[0] = 1

        if y == 1:
            for i in range(1, new_len):
                s = (P[i - 1] + Q[i - 1]) % MOD
                p_i = P[i] if i < old_len else 0
                newP[i] = (p_i + s) % MOD
                q_i = Q[i] if i < old_len else 0
                newQ[i] = (q_i - s) % MOD
        else:
            for i in range(1, new_len):
                s = (P[i - 1] + Q[i - 1]) % MOD
                p_i = P[i] if i < old_len else 0
                v = (p_i + s) % MOD
                newP[i] = 0 if v == 0 else MOD - v
                q_i = Q[i] if i < old_len else 0
                newQ[i] = (q_i - s) % MOD

        P, Q = newP, newQ

    return P, Q


def _series_coeff_mod(P: List[int], Q: List[int], w: int) -> int:
    n = w + 1
    if w < 2048:
        f = [0] * n
        for i in range(n):
            val = P[i] if i < len(P) else 0
            for j in range(1, min(i + 1, len(Q))):
                val -= Q[j] * f[i - j]
            f[i] = val % MOD
        return f[w]
    invQ = _inv_series(Q[:n], n)
    prod = _poly_mul_trunc(P[:n], invQ, n)
    return prod[w]


def _kitamasa(init: List[int], coef: List[int], k: int) -> int:
    d = len(coef)
    if k < d:
        return init[k]

    def mul_reduce(a: List[int], b: List[int]) -> List[int]:
        tmp = [0] * (2 * d - 1)
        for i in range(d):
            ai = a[i]
            if ai:
                for j in range(d):
                    tmp[i + j] = (tmp[i + j] + ai * b[j]) % MOD
        for i in range(2 * d - 2, d - 1, -1):
            t = tmp[i]
            if t:
                for j in range(d):
                    tmp[i - 1 - j] = (tmp[i - 1 - j] + t * coef[j]) % MOD
        return tmp[:d]

    res = [0] * d
    res[0] = 1
    base = [0] * d
    if d > 1:
        base[1] = 1
    else:
        base[0] = coef[0]

    p = k
    while p > 0:
        if p & 1:
            res = mul_reduce(res, base)
        base = mul_reduce(base, base)
        p >>= 1

    return sum(res[i] * init[i] for i in range(d)) % MOD


def _coeff_large_w_small_h(w: int, h: int, y: int) -> int:
    if h <= 0:
        return 0
    P, Q = _build_pq_mod(h, y, h)
    d = len(Q) - 1
    coef = [(-Q[i]) % MOD for i in range(1, d + 1)]
    init = [0] * d
    for i in range(d):
        val = P[i] if i < len(P) else 0
        for j in range(1, min(i + 1, len(Q))):
            val -= Q[j] * init[i - j]
        init[i] = val % MOD
    return _kitamasa(init, coef, w)


def _poly_mul_small(a: List[int], b: List[int], limit: int) -> List[int]:
    res = [0] * limit
    for i, ai in enumerate(a):
        if not ai:
            continue
        for j in range(min(len(b), limit - i)):
            res[i + j] = (res[i + j] + ai * b[j]) % MOD
    return res


def _mat_mul(a: List[List[List[int]]], b: List[List[List[int]]], limit: int) -> List[List[List[int]]]:
    res = [[[0] * limit, [0] * limit], [[0] * limit, [0] * limit]]
    for r in range(2):
        for c in range(2):
            for k in range(2):
                p = _poly_mul_small(a[r][k], b[k][c], limit)
                res[r][c] = [(res[r][c][i] + p[i]) % MOD for i in range(limit)]
    return res


def _mat_pow(M: List[List[List[int]]], e: int, limit: int) -> List[List[List[int]]]:
    I = [
        [[1] + [0] * (limit - 1), [0] * limit],
        [[0] * limit, [1] + [0] * (limit - 1)],
    ]
    while e > 0:
        if e & 1:
            I = _mat_mul(I, M, limit)
        M = _mat_mul(M, M, limit)
        e >>= 1
    return I


def _coeff_large_h_small_w(w: int, h: int, y: int) -> int:
    if h <= 0:
        return 0
    limit = w + 1
    y_mod = 1 if y == 1 else MOD - 1
    P = [0] * limit
    Q = [0] * limit
    if w >= 1:
        P[1] = y_mod
        Q[1] = MOD - 1
    Q[0] = 1
    if h == 1:
        return _series_coeff_mod(P, Q, w)

    one = [1] + [0] * (limit - 1)
    xpoly = [0, 1] + [0] * (limit - 2) if limit >= 2 else [0]
    one_plus_x = one[:]
    if limit >= 2:
        one_plus_x[1] = (one_plus_x[1] + 1) % MOD

    y_one_plus_x = [(c * y_mod) % MOD for c in one_plus_x]
    y_x = [(c * y_mod) % MOD for c in xpoly]
    minus_x = [0] * limit
    if limit >= 2:
        minus_x[1] = MOD - 1
    one_minus_x = one[:]
    if limit >= 2:
        one_minus_x[1] = (one_minus_x[1] - 1) % MOD

    A = [[y_one_plus_x, y_x], [minus_x, one_minus_x]]
    Mp = _mat_pow(A, h - 1, limit)
    Pn = [
        (_poly_mul_small(Mp[0][0], P, limit)[i] + _poly_mul_small(Mp[0][1], Q, limit)[i]) % MOD
        for i in range(limit)
    ]
    Qn = [
        (_poly_mul_small(Mp[1][0], P, limit)[i] + _poly_mul_small(Mp[1][1], Q, limit)[i]) % MOD
        for i in range(limit)
    ]
    return _series_coeff_mod(Pn, Qn, w)


def _coeff_c_mod(w: int, h: int, y: int) -> int:
    if h <= 0:
        return 0
    if w <= 200 and h > 2000:
        return _coeff_large_h_small_w(w, h, y)
    if h <= 200 and w > 2000:
        return _coeff_large_w_small_h(w, h, y)
    P, Q = _build_pq_mod(h, y, w)
    return _series_coeff_mod(P, Q, w)


def _f_mod(w: int, h: int) -> int:
    def e_leq(ww: int, hh: int) -> int:
        if hh <= 0:
            return 0
        t = _coeff_c_mod(ww, hh, 1)
        s = _coeff_c_mod(ww, hh, -1)
        return ((t + s) * INV2) % MOD

    return (e_leq(w, h) - e_leq(w, h - 1)) % MOD


def solve() -> int:
    """Compute (F(10^12, 100) + F(10000, 10000) + F(100, 10^12)) mod 10^9+7."""
    cases = [(10**12, 100), (10000, 10000), (100, 10**12)]
    total = 0
    for w, h in cases:
        total = (total + _f_mod(w, h)) % MOD
    return total


if __name__ == "__main__":
    print(solve())
