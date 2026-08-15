"""Project Euler Problem 544: Chromatic Conundrum.

Find S(9, 10, 1112131415) mod 10^9+7, where F(r, c, n) is the chromatic polynomial
of the r x c grid graph, and S(r, c, n) = sum_{k=1..n} F(r, c, k).
"""

from typing import Dict, List, Optional, Tuple

MOD = 1_000_000_007
EMPTY = -1


def _poly_eval(coeffs: List[int], x: int, mod: int = MOD) -> int:
    x %= mod
    res = 0
    p = 1
    for a in coeffs:
        res = (res + a * p) % mod
        p = (p * x) % mod
    return res


def _lagrange_eval_0_to_n(values: List[int], x: int, mod: int = MOD) -> int:
    n = len(values) - 1
    if 0 <= x <= n:
        return values[x] % mod

    x %= mod
    fac = [1] * (n + 1)
    for i in range(1, n + 1):
        fac[i] = (fac[i - 1] * i) % mod
    invfac = [1] * (n + 1)
    invfac[n] = pow(fac[n], mod - 2, mod)
    for i in range(n, 0, -1):
        invfac[i - 1] = (invfac[i] * i) % mod

    pre = [1] * (n + 2)
    for i in range(n + 1):
        pre[i + 1] = (pre[i] * (x - i)) % mod
    suf = [1] * (n + 2)
    for i in range(n, -1, -1):
        suf[i] = (suf[i + 1] * (x - i)) % mod

    ans = 0
    for i in range(n + 1):
        num = (pre[i] * suf[i + 1]) % mod
        den = (invfac[i] * invfac[n - i]) % mod
        if (n - i) & 1:
            den = (-den) % mod
        ans = (ans + values[i] * num % mod * den) % mod
    return ans


def _chromatic_poly_grid(r: int, c: int, mod: int = MOD) -> List[int]:
    canon_cache: Dict[Tuple[int, ...], Tuple[int, ...]] = {}

    def canon(state: Tuple[int, ...]) -> Tuple[int, ...]:
        res = canon_cache.get(state)
        if res is not None:
            return res
        mp = [-1] * (r + 1)
        nxt = 0
        out = [0] * r
        for idx, x in enumerate(state):
            if x == EMPTY:
                out[idx] = EMPTY
            else:
                y = mp[x]
                if y == -1:
                    y = nxt
                    mp[x] = y
                    nxt += 1
                out[idx] = y
        res = tuple(out)
        canon_cache[state] = res
        return res

    trans_cache: Dict[
        Tuple[Tuple[int, ...], int], Tuple[int, List[Tuple[int, ...]]]
    ] = {}

    def trans(
        st: Tuple[int, ...], i: int
    ) -> Tuple[int, List[Tuple[int, ...]]]:
        key = (st, i)
        res = trans_cache.get(key)
        if res is not None:
            return res
        mx = max(st)
        m = 0 if mx == EMPTY else mx + 1
        base = list(st)
        nexts: List[Optional[Tuple[int, ...]]] = [None] * (m + 1)
        for lab in range(m + 1):
            base[i] = lab
            nexts[lab] = canon(tuple(base))
        base[i] = st[i]
        res = (m, [n for n in nexts if n is not None])
        trans_cache[key] = res
        return res

    forget_cache: Dict[Tuple[Tuple[int, ...], int], Tuple[int, ...]] = {}

    def forget(st: Tuple[int, ...], i: int) -> Tuple[int, ...]:
        key = (st, i)
        res = forget_cache.get(key)
        if res is not None:
            return res
        base = list(st)
        base[i] = EMPTY
        res = canon(tuple(base))
        forget_cache[key] = res
        return res

    def add_poly(tgt: List[int], poly: List[int]) -> None:
        if len(tgt) < len(poly):
            tgt.extend([0] * (len(poly) - len(tgt)))
        for j, v in enumerate(poly):
            x = tgt[j] + v
            if x >= mod:
                x -= mod
            tgt[j] = x

    def add_q_minus_m_mul(tgt: List[int], poly: List[int], m: int) -> None:
        need = len(poly) + 1
        if len(tgt) < need:
            tgt.extend([0] * (need - len(tgt)))
        mm = m % mod
        for j, v in enumerate(poly):
            tgt[j] = (tgt[j] - (mm * v) % mod) % mod
            x = tgt[j + 1] + v
            if x >= mod:
                x -= mod
            tgt[j + 1] = x

    start = tuple([EMPTY] * r)
    dp: Dict[Tuple[int, ...], List[int]] = {start: [1]}

    for col in range(c):
        for row in range(r):
            i = row
            has_up = row > 0
            has_left = col > 0
            ndp: Dict[Tuple[int, ...], List[int]] = {}
            for st, poly in dp.items():
                m, nexts = trans(st, i)
                up = st[i - 1] if has_up else -2
                left = st[i] if has_left else -2

                for lab in range(m):
                    if lab == up or lab == left:
                        continue
                    ns = nexts[lab]
                    tgt = ndp.get(ns)
                    if tgt is None:
                        tgt = []
                        ndp[ns] = tgt
                    add_poly(tgt, poly)

                ns = nexts[m]
                tgt = ndp.get(ns)
                if tgt is None:
                    tgt = []
                    ndp[ns] = tgt
                add_q_minus_m_mul(tgt, poly, m)

            dp = ndp

    for i in range(r):
        ndp = {}
        for st, poly in dp.items():
            ns = forget(st, i)
            tgt = ndp.get(ns)
            if tgt is None:
                tgt = []
                ndp[ns] = tgt
            add_poly(tgt, poly)
        dp = ndp

    return dp[start]


def solve(r: int = 9, c: int = 10, n: int = 1112131415) -> int:
    """Compute S(r, c, n) mod MOD via frontier transfer matrix DP and O(V) Lagrange polynomial interpolation."""
    p = _chromatic_poly_grid(r, c)
    deg = r * c
    m = deg + 1
    prefix = [0] * (m + 1)
    acc = 0
    for k in range(1, m + 1):
        acc = (acc + _poly_eval(p, k)) % MOD
        prefix[k] = acc

    return _lagrange_eval_0_to_n(prefix, n)


if __name__ == "__main__":
    print(solve())
