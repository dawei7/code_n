"""Project Euler Problem 690: Tom and Jerry.

Find T(2019) mod 1000000007, where T(n) is the number of Tom graphs (graphs where Tom can guarantee
catching Jerry in finitely many days) on n vertices.
"""

from typing import List

_MOD = 1_000_000_007


def _partitions_upto(n: int) -> List[int]:
    p = [0] * (n + 1)
    p[0] = 1
    for k in range(1, n + 1):
        for i in range(k, n + 1):
            p[i] += p[i - k]
            if p[i] >= _MOD:
                p[i] -= _MOD
    return p


def _poly_mul(a: List[int], b: List[int], n: int) -> List[int]:
    mod = _MOD
    mod2 = mod * mod
    res = [0] * (n + 1)
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        maxj = n - i
        for j in range(maxj + 1):
            v = res[i + j] + ai * b[j]
            if v >= mod2:
                v %= mod
            res[i + j] = v
    for k in range(n + 1):
        res[k] %= mod
    return res


def _inv_series(f: List[int], n: int) -> List[int]:
    mod = _MOD
    mod2 = mod * mod
    g = [0] * (n + 1)
    g0 = pow(f[0], mod - 2, mod)
    g[0] = g0
    for i in range(1, n + 1):
        s = 0
        for k in range(1, i + 1):
            s += f[k] * g[i - k]
            if s >= mod2:
                s %= mod
        g[i] = (-s * g0) % mod
    return g


def _lobster_counts_upto(n: int) -> List[int]:
    p = _partitions_upto(n)
    inv2 = (_MOD + 1) // 2

    q = [(p[i] - 1) % _MOD for i in range(n + 1)]

    num1 = _poly_mul(q, q, n)
    den1 = [0] * (n + 1)
    den1[0] = 1
    for i in range(1, n + 1):
        den1[i] = (-p[i - 1]) % _MOD
    inv_den1 = _inv_series(den1, n)
    term1 = _poly_mul(num1, inv_den1, n)

    p2 = [0] * (n + 1)
    q2 = [0] * (n + 1)
    for i in range(0, n // 2 + 1):
        p2[2 * i] = p[i]
        q2[2 * i] = (p[i] - 1) % _MOD

    one_plus = [0] * (n + 1)
    one_plus[0] = 1
    for i in range(1, n + 1):
        one_plus[i] = p[i - 1]

    num2 = _poly_mul(q2, one_plus, n)
    den2 = [0] * (n + 1)
    den2[0] = 1
    for i in range(2, n + 1):
        den2[i] = (-p2[i - 2]) % _MOD
    inv_den2 = _inv_series(den2, n)
    term2 = _poly_mul(num2, inv_den2, n)

    s = [(term1[i] + term2[i]) % _MOD for i in range(n + 1)]

    main = [0] * (n + 1)
    for i in range(0, n - 1):
        main[i + 2] = (s[i] * inv2) % _MOD

    xp = [0] * (n + 1)
    for i in range(1, n + 1):
        xp[i] = p[i - 1]

    a1 = [(i + 1) % _MOD for i in range(n + 1)]
    a2 = [1 if (i % 2 == 0) else _MOD - 1 for i in range(n + 1)]
    temp = _poly_mul(a1, a2, n)
    last = [0] * (n + 1)
    for i in range(0, n - 2):
        last[i + 3] = temp[i]

    a = [(main[i] + xp[i] - last[i]) % _MOD for i in range(n + 1)]
    return a


def solve(n: int = 2019) -> int:
    """Compute T(n) modulo 1000000007 using lobster tree generating functions and Euler multiset transform."""
    b = _lobster_counts_upto(n)
    c = [0] * (n + 1)
    for d in range(1, n + 1):
        bd = b[d]
        if bd == 0:
            continue
        addv = (d * bd) % _MOD
        for k in range(d, n + 1, d):
            c[k] += addv
            if c[k] >= _MOD:
                c[k] -= _MOD

    inv = [0] * (n + 1)
    for i in range(1, n + 1):
        inv[i] = pow(i, _MOD - 2, _MOD)

    a = [0] * (n + 1)
    a[0] = 1
    mod2 = _MOD * _MOD
    for m in range(1, n + 1):
        s = 0
        for k in range(1, m + 1):
            s += c[k] * a[m - k]
            if s >= mod2:
                s %= _MOD
        a[m] = (s % _MOD) * inv[m] % _MOD

    return a[n]


if __name__ == "__main__":
    print(solve())
