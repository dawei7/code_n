"""Project Euler Problem 529: 10-substrings.

Find T(10^18) mod 1_000_000_007, where T(n) is the number of 10-substring-friendly
numbers from 1 to 10^n.
"""

from typing import Callable, Dict, List, Optional, Tuple

MOD = 1_000_000_007
N = 10**18


def _next_state(
    digs: Tuple[int, ...], sum_digs: int, uncovered: int, d: int
) -> Optional[Tuple[Tuple[int, ...], int]]:
    new_digs = digs + (d,)
    new_uncovered = uncovered + 1
    new_sum = sum_digs + d

    while new_sum > 10:
        if len(new_digs) == new_uncovered:
            return None
        new_sum -= new_digs[0]
        new_digs = new_digs[1:]

    if new_sum == 10:
        new_uncovered = 0
    return new_digs, new_uncovered


def _build_dfa() -> Tuple[List[List[int]], List[int]]:
    start: Tuple[Tuple[int, ...], int] = ((), 0)
    state_id: Dict[Tuple[Tuple[int, ...], int], int] = {start: 0}
    states: List[Tuple[Tuple[int, ...], int]] = [start]
    trans: List[List[int]] = []

    q = 0
    while q < len(states):
        digs, uncovered = states[q]
        sum_digs = sum(digs)
        row = [-1] * 9
        for di, digit in enumerate(range(1, 10)):
            nxt = _next_state(digs, sum_digs, uncovered, digit)
            if nxt is None:
                continue
            if nxt not in state_id:
                state_id[nxt] = len(states)
                states.append(nxt)
            row[di] = state_id[nxt]
        trans.append(row)
        q += 1

    accept_ids: List[int] = []
    outs: List[List[int]] = []
    for sid, (digs, uncovered) in enumerate(states):
        if digs and uncovered == 0:
            accept_ids.append(sid)
        out = []
        for j in trans[sid]:
            if j != -1:
                out.append(j)
        outs.append(out)

    return outs, accept_ids


def _generate_e_terms(
    outs: List[List[int]], accept_ids: List[int], num_terms: int
) -> List[int]:
    s_size = len(outs)
    dp = [0] * s_size
    dp[0] = 1

    seq = [0] * num_terms
    for t in range(1, num_terms):
        ndp = [0] * s_size
        for i, v in enumerate(dp):
            if v:
                for j in outs[i]:
                    x = ndp[j] + v
                    if x >= MOD:
                        x -= MOD
                    ndp[j] = x
        dp = ndp

        total = 0
        for i in accept_ids:
            total += dp[i]
            if total >= MOD:
                total -= MOD
        seq[t] = total
    return seq


def _berlekamp_massey(seq: List[int]) -> List[int]:
    c_poly = [1]
    b_poly = [1]
    l_deg = 0
    m = 1
    b_val = 1

    for n in range(len(seq)):
        d = seq[n]
        for i in range(1, l_deg + 1):
            d = (d + c_poly[i] * seq[n - i]) % MOD
        if d == 0:
            m += 1
            continue

        coef = d * pow(b_val, MOD - 2, MOD) % MOD
        t_poly = c_poly[:]
        need = max(l_deg + m, len(b_poly) - 1 + m)
        if len(c_poly) < need + 1:
            c_poly.extend([0] * (need + 1 - len(c_poly)))
        for i in range(len(b_poly)):
            c_poly[i + m] = (c_poly[i + m] - coef * b_poly[i]) % MOD
        if 2 * l_deg <= n:
            l2 = n + 1 - l_deg
            b_poly = t_poly
            l_deg = l2
            b_val = d
            m = 1
        else:
            m += 1

    return [(-c_poly[i]) % MOD for i in range(1, l_deg + 1)]


BASE_BITS = 72
BASE_MASK = (1 << BASE_BITS) - 1


def _pack(coeffs: List[int]) -> int:
    x = 0
    for c in reversed(coeffs):
        x = (x << BASE_BITS) + c
    return x


def _unpack(x: int, n: int) -> List[int]:
    out = [0] * n
    for i in range(n):
        out[i] = x & BASE_MASK
        x >>= BASE_BITS
    return out


def _conv(a: List[int], b: List[int]) -> List[int]:
    return _unpack(_pack(a) * _pack(b), len(a) + len(b) - 1)


def _conv_with_const(a: List[int], packed_b: int, len_b: int) -> List[int]:
    return _unpack(_pack(a) * packed_b, len(a) + len_b - 1)


def _poly_inv_mod_xk(f: List[int], k: int) -> List[int]:
    inv0 = pow(f[0], MOD - 2, MOD)
    g = [inv0]
    m = 1
    while m < k:
        m2 = min(2 * m, k)
        t = _conv(f[:m2], g)[:m2]
        for i in range(m2):
            t[i] %= MOD
        t[0] = (2 - t[0]) % MOD
        for i in range(1, m2):
            t[i] = (-t[i]) % MOD
        g = _conv(g, t)[:m2]
        for i in range(m2):
            g[i] %= MOD
        m = m2
    return g


def _prepare_ring(
    rec: List[int],
) -> Tuple[int, Callable[[List[int], int], List[int]]]:
    l_len = len(rec)
    k_len = l_len - 1

    c_mod = [0] * (l_len + 1)
    c_mod[l_len] = 1
    for i, c in enumerate(rec):
        c_mod[l_len - 1 - i] = (-c) % MOD

    cr = list(reversed(c_mod))
    inv_cr = _poly_inv_mod_xk(cr, k_len)

    packed_inv_cr = _pack(inv_cr)
    packed_c = _pack(c_mod)
    len_inv_cr = len(inv_cr)
    len_c = len(c_mod)

    def poly_mod(p_poly: List[int]) -> List[int]:
        pr = p_poly[::-1]
        q_rev = _conv_with_const(pr[:k_len], packed_inv_cr, len_inv_cr)[
            :k_len
        ]
        for i in range(k_len):
            q_rev[i] %= MOD
        q = q_rev[::-1]

        qc = _conv_with_const(q, packed_c, len_c)
        r = [0] * l_len
        for i in range(l_len):
            r[i] = (p_poly[i] - qc[i]) % MOD
        return r

    def poly_mul_mod(a: List[int], b: List[int]) -> List[int]:
        p_poly = _conv(a, b)
        for i in range(2 * l_len - 1):
            p_poly[i] %= MOD
        return poly_mod(p_poly)

    def poly_pow(base: List[int], exp: int) -> List[int]:
        res = [0] * l_len
        res[0] = 1
        b_cur = base
        e_cur = exp
        while e_cur > 0:
            if e_cur & 1:
                res = poly_mul_mod(res, b_cur)
            e_cur >>= 1
            if e_cur > 0:
                b_cur = poly_mul_mod(b_cur, b_cur)
        return res

    return l_len, poly_pow


def solve(n: int = N) -> int:
    """Compute T(n) mod MOD via DFA generation, Berlekamp-Massey, and polynomial exponentiation."""
    outs, accept_ids = _build_dfa()
    s_size = len(outs)
    e_terms = _generate_e_terms(outs, accept_ids, 2 * s_size + 5)

    rec = _berlekamp_massey(e_terms)
    l_len, poly_pow = _prepare_ring(rec)
    e_init = e_terms[:l_len]

    base = [0] * l_len
    base[0] = 1
    if l_len > 1:
        base[1] = 1
    r_poly = poly_pow(base, n)

    ans = 0
    for i in range(l_len):
        ans = (ans + r_poly[i] * e_init[i]) % MOD
    return ans


if __name__ == "__main__":
    print(solve())
