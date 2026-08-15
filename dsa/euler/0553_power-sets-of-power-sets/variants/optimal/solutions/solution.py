"""Project Euler Problem 553: Power Sets of Power Sets.

Find C(10^4, 10) mod 10^9+7, where C(n, k) is the number of non-empty hypergraphs
on {1..n} having exactly k connected components.
"""

from typing import Dict, List, Optional, Tuple

MOD = 1_000_000_007

_NTT_MODS = (
    (998244353, 3),
    (1004535809, 3),
    (469762049, 3),
)

_ntt_cache: Dict[
    Tuple[int, int], Tuple[List[int], List[int], List[int]]
] = {}


def _prepare_ntt(
    mod: int, root: int, n: int
) -> Tuple[List[int], List[int], List[int]]:
    key = (mod, n)
    cached = _ntt_cache.get(key)
    if cached is not None:
        return cached

    logn = n.bit_length() - 1
    rev = [0] * n
    for i in range(1, n):
        rev[i] = (rev[i >> 1] >> 1) | ((i & 1) << (logn - 1))

    roots_fwd = []
    roots_inv = []
    length = 2
    while length <= n:
        wlen = pow(root, (mod - 1) // length, mod)
        roots_fwd.append(wlen)
        roots_inv.append(pow(wlen, mod - 2, mod))
        length <<= 1

    cached = (rev, roots_fwd, roots_inv)
    _ntt_cache[key] = cached
    return cached


def _ntt_inplace(a: List[int], invert: bool, mod: int, root: int) -> None:
    n = len(a)
    rev, roots_fwd, roots_inv = _prepare_ntt(mod, root, n)

    for i in range(n):
        j = rev[i]
        if i < j:
            a[i], a[j] = a[j], a[i]

    length = 2
    stage = 0
    while length <= n:
        wlen = roots_inv[stage] if invert else roots_fwd[stage]
        half = length >> 1

        for i in range(0, n, length):
            w = 1
            for j in range(i, i + half):
                u = a[j]
                v = (a[j + half] * w) % mod

                x = u + v
                if x >= mod:
                    x -= mod
                a[j] = x

                y = u - v
                if y < 0:
                    y += mod
                a[j + half] = y

                w = (w * wlen) % mod

        stage += 1
        length <<= 1

    if invert:
        inv_n = pow(n, mod - 2, mod)
        for i in range(n):
            a[i] = (a[i] * inv_n) % mod


def _convolution_ntt_mod(
    a: List[int], b: List[int], mod: int, root: int
) -> List[int]:
    if not a or not b:
        return []

    need = len(a) + len(b) - 1
    n = 1
    while n < need:
        n <<= 1

    fa = [0] * n
    fb = [0] * n
    for i, x in enumerate(a):
        fa[i] = x % mod
    for i, x in enumerate(b):
        fb[i] = x % mod

    _ntt_inplace(fa, False, mod, root)
    _ntt_inplace(fb, False, mod, root)

    for i in range(n):
        fa[i] = (fa[i] * fb[i]) % mod

    _ntt_inplace(fa, True, mod, root)
    return fa[:need]


_m1, _m2, _m3 = (_NTT_MODS[0][0], _NTT_MODS[1][0], _NTT_MODS[2][0])
_inv_m1_mod_m2 = pow(_m1, _m2 - 2, _m2)
_m1m2 = _m1 * _m2
_inv_m1m2_mod_m3 = pow(_m1m2 % _m3, _m3 - 2, _m3)


def _convolution_mod(
    a: List[int],
    b: List[int],
    limit: Optional[int] = None,
    naive_threshold: int = 20000,
) -> List[int]:
    if not a or not b:
        return []
    need = len(a) + len(b) - 1
    if limit is not None and limit < need:
        need = limit

    if len(a) * len(b) <= naive_threshold:
        res = [0] * need
        for i, ai in enumerate(a):
            if ai == 0:
                continue
            maxj = min(len(b), need - i)
            for j in range(maxj):
                res[i + j] = (res[i + j] + ai * b[j]) % MOD
        return res

    r1 = _convolution_ntt_mod(a, b, _NTT_MODS[0][0], _NTT_MODS[0][1])
    r2 = _convolution_ntt_mod(a, b, _NTT_MODS[1][0], _NTT_MODS[1][1])
    r3 = _convolution_ntt_mod(a, b, _NTT_MODS[2][0], _NTT_MODS[2][1])

    res_len = min(need, len(r1))
    res = [0] * res_len

    for i in range(res_len):
        x1 = r1[i]
        t1 = ((r2[i] - x1) * _inv_m1_mod_m2) % _m2
        x12 = x1 + _m1 * t1
        t2 = ((r3[i] - (x12 % _m3)) * _inv_m1m2_mod_m3) % _m3
        x = x12 + _m1m2 * t2
        res[i] = x % MOD

    return res


def _poly_inv(f: List[int], deg: int) -> List[int]:
    if deg <= 0:
        return []
    f0 = f[0] % MOD
    g = [pow(f0, MOD - 2, MOD)]
    m = 1
    while m < deg:
        m2 = min(2 * m, deg)
        f_cut = f[:m2]
        t = _convolution_mod(f_cut, g, limit=m2)
        t[0] = (2 - t[0]) % MOD
        for i in range(1, len(t)):
            t[i] = (-t[i]) % MOD
        g = _convolution_mod(g, t, limit=m2)
        m = m2
    return g[:deg]


def _poly_log(f: List[int], deg: int, inv_int: List[int]) -> List[int]:
    if deg <= 0:
        return []
    df = [(i * f[i]) % MOD for i in range(1, min(len(f), deg))]
    invf = _poly_inv(f[:deg], deg)
    prod = _convolution_mod(df, invf, limit=deg - 1)
    res = [0] * deg
    for i in range(1, deg):
        res[i] = prod[i - 1] * inv_int[i] % MOD
    return res


def _poly_pow(a: List[int], exp: int, deg: int) -> List[int]:
    res = [0] * deg
    res[0] = 1
    base = a[:deg]
    e = exp
    while e > 0:
        if e & 1:
            res = _convolution_mod(res, base, limit=deg)
        e >>= 1
        if e:
            base = _convolution_mod(base, base, limit=deg)
    return res


def solve(n: int = 10_000, k: int = 10) -> int:
    """Compute C(n, k) mod 10^9+7 using EGF log/power transformations via 3-NTT CRT."""
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = (fact[i - 1] * i) % MOD

    inv_fact = [1] * (n + 1)
    inv_fact[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n, 0, -1):
        inv_fact[i - 1] = (inv_fact[i] * i) % MOD

    inv_int = [0] * (n + 1)
    if n >= 1:
        inv_int[1] = 1
        for i in range(2, n + 1):
            inv_int[i] = MOD - (MOD // i) * inv_int[MOD % i] % MOD

    modm1 = MOD - 1
    exp2 = [1] * (n + 1)
    for i in range(1, n + 1):
        exp2[i] = (exp2[i - 1] * 2) % modm1

    a0 = [0] * (n + 1)
    for i in range(n + 1):
        a0[i] = pow(2, (exp2[i] - 1) % modm1, MOD)

    p = [(a0[i] * inv_fact[i]) % MOD for i in range(n + 1)]
    q = [
        inv_fact[i] if (i & 1) == 0 else (MOD - inv_fact[i])
        for i in range(n + 1)
    ]
    h = _convolution_mod(p, q, limit=n + 1)
    h[0] = 1

    a_series = _poly_log(h, n + 1, inv_int)

    deg = n + 1
    ak = _poly_pow(a_series[:deg], k, deg)
    expx = inv_fact[:deg]
    prod = _convolution_mod(ak, expx, limit=deg)

    return fact[n] * prod[n] % MOD * inv_fact[k] % MOD


if __name__ == "__main__":
    print(solve())
