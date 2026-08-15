"""Project Euler Problem 654: Neighbourly Constraints.

Find T(5000, 10^12) mod 1000000007, where T(n, m) is the number of m-tuples of positive integers
such that the sum of any two neighbouring elements is <= n.
"""

import math
from typing import Dict, List

_MOD = 1_000_000_007
_B = 1 << 15
_MASK = _B - 1
_BMOD = _B % _MOD
_B2MOD = (_B * _B) % _MOD


def _iround(x: float) -> int:
    return int(x + 0.5) if x >= 0.0 else -int(-x + 0.5)


class _FFTPlan:
    __slots__ = ("n", "rev", "roots_fwd", "roots_inv")

    def __init__(self, n: int):
        self.n = n
        lg = n.bit_length() - 1
        rev = [0] * n
        for i in range(1, n):
            rev[i] = (rev[i >> 1] >> 1) | ((i & 1) << (lg - 1))
        self.rev = rev

        roots_fwd: Dict[int, List[complex]] = {}
        roots_inv: Dict[int, List[complex]] = {}
        two_pi = 2.0 * math.pi
        length = 2
        while length <= n:
            half = length >> 1
            ang = two_pi / length
            rl = [
                complex(math.cos(ang * k), math.sin(ang * k))
                for k in range(half)
            ]
            roots_fwd[length] = rl
            roots_inv[length] = [z.conjugate() for z in rl]
            length <<= 1
        self.roots_fwd = roots_fwd
        self.roots_inv = roots_inv

    def fft(self, a: List[complex], invert: bool) -> None:
        n = self.n
        rev = self.rev
        for i in range(n):
            j = rev[i]
            if i < j:
                a[i], a[j] = a[j], a[i]

        roots = self.roots_inv if invert else self.roots_fwd
        length = 2
        while length <= n:
            half = length >> 1
            root_list = roots[length]
            for base in range(0, n, length):
                for k in range(half):
                    u = a[base + k]
                    v = a[base + k + half] * root_list[k]
                    a[base + k] = u + v
                    a[base + k + half] = u - v
            length <<= 1

        if invert:
            inv_n = 1.0 / n
            for i in range(n):
                a[i] *= inv_n


_plan_cache: Dict[int, _FFTPlan] = {}


def _get_plan(n: int) -> _FFTPlan:
    plan = _plan_cache.get(n)
    if plan is None:
        plan = _FFTPlan(n)
        _plan_cache[n] = plan
    return plan


def _convolve_mod(
    a: List[int], b: List[int], mod: int = _MOD
) -> List[int]:
    la, lb = len(a), len(b)
    if la == 0 or lb == 0:
        return []
    need = la + lb - 1
    n = 1 << ((need - 1).bit_length())
    plan = _get_plan(n)

    fa = [0j] * n
    fb = [0j] * n
    for i, x in enumerate(a):
        fa[i] = complex(x & _MASK, x >> 15)
    for i, x in enumerate(b):
        fb[i] = complex(x & _MASK, x >> 15)

    plan.fft(fa, False)
    plan.fft(fb, False)

    p = [fa[i] * fb[i] for i in range(n)]
    q = [0j] * n
    nmask = n - 1
    half = 0.5
    halfj = -0.5j
    for i in range(n):
        j = (-i) & nmask
        ai = fa[i]
        aj = fa[j].conjugate()
        bi = fb[i]
        bj = fb[j].conjugate()

        f0a = (ai + aj) * half
        f1a = (ai - aj) * halfj
        f0b = (bi + bj) * half
        f1b = (bi - bj) * halfj

        sa = f0a + f1a
        sb = f0b + f1b
        q[i] = sa * sb

    plan.fft(p, True)
    plan.fft(q, True)

    res = [0] * need
    for i in range(need):
        r = _iround(p[i].real)
        mid = _iround(p[i].imag)
        s = _iround(q[i].real)

        c00_plus_c11 = s - mid
        c00 = (c00_plus_c11 + r) // 2
        c11 = c00_plus_c11 - c00

        res[i] = (
            c00 % mod + (mid % mod) * _BMOD + (c11 % mod) * _B2MOD
        ) % mod
    return res


def _berlekamp_massey(seq: List[int], mod: int = _MOD) -> List[int]:
    c = [1]
    bp = [1]
    length_l = 0
    m = 1
    b = 1

    for n_idx, sn in enumerate(seq):
        d = sn
        for i in range(1, length_l + 1):
            d = (d + c[i] * seq[n_idx - i]) % mod

        if d == 0:
            m += 1
            continue

        coef = d * pow(b, mod - 2, mod) % mod
        t_copy = c.copy()

        need_len = len(bp) + m
        if len(c) < need_len:
            c += [0] * (need_len - len(c))
        for i in range(len(bp)):
            c[i + m] = (c[i + m] - coef * bp[i]) % mod

        if 2 * length_l <= n_idx:
            length_l = n_idx + 1 - length_l
            bp = t_copy
            b = d
            m = 1
        else:
            m += 1

    return [(mod - c[i]) % mod for i in range(1, length_l + 1)]


def _bostan_mori(
    p_poly: List[int], q_poly: List[int], n_pow: int, mod: int = _MOD
) -> int:
    while n_pow:
        qm = q_poly[:]
        for i in range(1, len(qm), 2):
            qi = qm[i]
            if qi:
                qm[i] = mod - qi

        u_poly = _convolve_mod(p_poly, qm, mod)
        v_poly = _convolve_mod(q_poly, qm, mod)

        p_poly = u_poly[1::2] if (n_pow & 1) else u_poly[0::2]
        q_poly = v_poly[0::2]
        n_pow >>= 1

        while p_poly and p_poly[-1] == 0:
            p_poly.pop()
        while q_poly and q_poly[-1] == 0:
            q_poly.pop()

    return (p_poly[0] * pow(q_poly[0], mod - 2, mod)) % mod


def solve(n: int = 5000, m: int = 10**12) -> int:
    """Compute T(n, m) mod 1000000007 using prefix DP, Berlekamp-Massey, and Bostan-Mori polynomial division."""
    dim = n - 1
    if m <= 1:
        return dim % _MOD

    if m <= 20000 or dim <= 400:
        dp = [1] * dim
        prefix = [0] * (dim + 1)
        for _ in range(1, m):
            s = 0
            prefix[0] = 0
            for i, x in enumerate(dp):
                s += x
                if s >= _MOD:
                    s -= _MOD
                prefix[i + 1] = s
            dp = prefix[:0:-1]

        total = sum(dp) % _MOD
        return total

    terms_needed = 2 * dim
    dp = [1] * dim
    prefix = [0] * (dim + 1)
    seq = [0] * terms_needed
    for t in range(terms_needed):
        s = 0
        prefix[0] = 0
        for i, x in enumerate(dp):
            s += x
            if s >= _MOD:
                s -= _MOD
            prefix[i + 1] = s
        seq[t] = s
        dp = prefix[:0:-1]

    rec = _berlekamp_massey(seq, _MOD)
    l_deg = len(rec)
    init = seq[:l_deg]

    p_init = [0] * l_deg
    for i in range(l_deg):
        v = init[i]
        for j in range(1, i + 1):
            v = (v - rec[j - 1] * init[i - j]) % _MOD
        p_init[i] = v

    q_poly = [1] + [(_MOD - c) % _MOD for c in rec]
    ans = _bostan_mori(p_init, q_poly, m - 1, _MOD)
    return ans


if __name__ == "__main__":
    print(solve())
