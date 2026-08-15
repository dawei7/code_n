"""Project Euler Problem 559: Permuted Matrices.

Find Q(50000) mod 1000000123, where Q(n) = sum_{k=1..n} P(k, n, n),
and P(k, r, n) is the number of r x n matrices with given column ascent conditions.
"""

from array import array
from typing import List, Tuple

MOD = 1000000123

_BASE_BITS = 23
_BASE = 1 << _BASE_BITS
_MASK = _BASE - 1


def _conv_u64(a: List[int], b: List[int]) -> array:
    n = len(a)
    m = len(b)
    if n == 0 or m == 0:
        return array("Q")

    a_int = int.from_bytes(array("Q", a).tobytes(), "little", signed=False)
    b_int = int.from_bytes(array("Q", b).tobytes(), "little", signed=False)
    c_int = a_int * b_int

    out_len = n + m - 1
    bs = c_int.to_bytes(8 * out_len, "little", signed=False)
    res = array("Q")
    res.frombytes(bs)
    return res


def _poly_mul_naive(
    a: List[int], b: List[int], mod: int = MOD
) -> List[int]:
    n = len(a)
    m = len(b)
    res = [0] * (n + m - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                res[i + j] = (res[i + j] + ai * bj) % mod
    return res


def _poly_mul_mod(
    a: List[int], b: List[int], mod: int = MOD
) -> List[int]:
    if not a or not b:
        return []
    n = len(a)
    m = len(b)

    if n * m <= 40000 or min(n, m) <= 40:
        return _poly_mul_naive(a, b, mod)

    a0 = [x & _MASK for x in a]
    a1 = [x >> _BASE_BITS for x in a]
    b0 = [x & _MASK for x in b]
    b1 = [x >> _BASE_BITS for x in b]

    z0 = _conv_u64(a0, b0)
    z2 = _conv_u64(a1, b1)

    sa = [a0[i] + a1[i] for i in range(n)]
    sb = [b0[i] + b1[i] for i in range(m)]
    z1 = _conv_u64(sa, sb)

    out_len = n + m - 1
    res = [0] * out_len
    shift1 = _BASE_BITS
    shift2 = 2 * _BASE_BITS
    for i in range(out_len):
        cross = int(z1[i]) - int(z0[i]) - int(z2[i])
        res[i] = (
            int(z0[i]) + (cross << shift1) + (int(z2[i]) << shift2)
        ) % mod
    return res


def _poly_inv_mod(f: List[int], n: int, mod: int = MOD) -> List[int]:
    inv0 = pow(f[0], mod - 2, mod)
    g = [inv0]
    m = 1
    while m < n:
        m2 = min(2 * m, n)
        fg = _poly_mul_mod(f[:m2], g, mod)[:m2]

        for i in range(len(fg)):
            fg[i] = (-fg[i]) % mod
        fg[0] = (fg[0] + 2) % mod

        g = _poly_mul_mod(g, fg, mod)[:m2]
        m = m2
    return g


def _precompute_factorial_powers(
    n: int, r: int, mod: int = MOD
) -> Tuple[List[int], List[int]]:
    fac_pow = [1] * (n + 1)
    for i in range(1, n + 1):
        fac_pow[i] = (fac_pow[i - 1] * pow(i, r, mod)) % mod

    inv_fac_pow = [1] * (n + 1)
    inv_fac_pow[n] = pow(fac_pow[n], mod - 2, mod)
    for i in range(n - 1, -1, -1):
        inv_fac_pow[i] = (inv_fac_pow[i + 1] * pow(i + 1, r, mod)) % mod

    return fac_pow, inv_fac_pow


def _p_via_dp(
    k: int,
    r: int,
    n: int,
    fac_pow: List[int],
    inv_fac_pow: List[int],
    mod: int = MOD,
) -> int:
    q, rem = divmod(n, k)
    blocks = [k] * q + ([rem] if rem else [])
    m = len(blocks)

    f = [0] * (m + 1)
    f[0] = fac_pow[n]

    for i in range(1, m + 1):
        seg = 0
        acc = 0
        for j in range(i - 1, -1, -1):
            seg += blocks[j]
            term = f[j] * inv_fac_pow[seg] % mod
            if (i - j) & 1:
                acc += term
            else:
                acc -= term
        f[i] = acc % mod

    return f[m]


def _p_via_inverse(
    k: int,
    r: int,
    n: int,
    fac_pow: List[int],
    inv_fac_pow: List[int],
    mod: int = MOD,
) -> int:
    q, rem = divmod(n, k)

    p = [0] * (q + 1)
    p[0] = 1
    for d in range(1, q + 1):
        coeff = inv_fac_pow[d * k]
        if d & 1:
            coeff = mod - coeff
        p[d] = coeff

    s = _poly_inv_mod(p, q + 1, mod)
    g0 = fac_pow[n]
    g = [(g0 * si) % mod for si in s]

    if rem == 0:
        return g[q]

    ans = 0
    for t in range(q + 1):
        seg_len = (q - t) * k + rem
        term = g[t] * inv_fac_pow[seg_len] % mod
        if (q - t) & 1:
            ans -= term
        else:
            ans += term
    return ans % mod


def solve(n: int = 50_000, mod: int = MOD) -> int:
    """Compute Q(n) mod mod using hybrid power series inversion and block transition DP."""
    r = n
    fac_pow, inv_fac_pow = _precompute_factorial_powers(n, r, mod)
    k_inv_max = n // 200

    ans = 0
    for k in range(1, n + 1):
        q = n // k
        if k <= k_inv_max and q > 200:
            ans = (
                ans
                + _p_via_inverse(k, r, n, fac_pow, inv_fac_pow, mod)
            ) % mod
        else:
            ans = (
                ans
                + _p_via_dp(k, r, n, fac_pow, inv_fac_pow, mod)
            ) % mod
    return ans


if __name__ == "__main__":
    print(solve())
