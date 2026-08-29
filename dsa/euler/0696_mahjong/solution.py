"""Project Euler Problem 696: Mahjong.

Find w(10^8, 10^8, 30) mod 1000000007, the number of distinct winning Mahjong hands
of t Triples and one Pair across s suits with numbers 1..n.
"""

from collections import deque
from typing import Dict, FrozenSet, List, Set, Tuple

_MOD = 1_000_000_007


def _precompute_fact(kmax: int) -> Tuple[List[int], List[int]]:
    fact = [1] * (kmax + 1)
    invfact = [1] * (kmax + 1)
    for i in range(1, kmax + 1):
        fact[i] = fact[i - 1] * i % _MOD
    invfact[kmax] = pow(fact[kmax], _MOD - 2, _MOD)
    for i in range(kmax, 0, -1):
        invfact[i - 1] = invfact[i] * i % _MOD
    return fact, invfact


def _nck_small(n: int, k: int, invfact: List[int]) -> int:
    if k < 0 or n < k:
        return 0
    if k == 0:
        return 1
    num = 1
    for i in range(k):
        num = (num * ((n - i) % _MOD)) % _MOD
    return (num * invfact[k]) % _MOD


def _nfa_next(a: int, b: int, p: int, c: int) -> Tuple[Tuple[int, int, int], ...]:
    if a + b > c:
        return ()
    r = c - (a + b)
    out: List[Tuple[int, int, int]] = []
    z_choices = (0, 1) if p == 0 else (0,)
    for z in z_choices:
        if 2 * z > r:
            continue
        r2 = r - 2 * z
        for y in (0, 1):
            if 3 * y > r2:
                continue
            x = r2 - 3 * y
            if 0 <= x <= 4:
                out.append((x, a, p | z))
    if len(out) <= 1:
        return tuple(out)
    return tuple(sorted(set(out)))


def _build_dfa():
    nfa_states = [(a, b, p) for a in range(5) for b in range(5) for p in (0, 1)]
    nfa_index = {st: i for i, st in enumerate(nfa_states)}
    nfa_trans = [[None] * 5 for _ in range(len(nfa_states))]
    for st in nfa_states:
        i = nfa_index[st]
        a, b, p = st
        for c in range(5):
            nxt = _nfa_next(a, b, p, c)
            nfa_trans[i][c] = tuple(nfa_index[s] for s in nxt)

    init = frozenset([nfa_index[(0, 0, 0)]])
    q = deque([init])
    dfa_index: Dict[FrozenSet[int], int] = {init: 0}
    dfa_states = []
    dfa_trans = []
    while q:
        s_set = q.popleft()
        dfa_states.append(s_set)
        row = []
        for c in range(5):
            nxt = set()
            for si in s_set:
                nxt.update(nfa_trans[si][c])
            f_nxt = frozenset(nxt)
            if f_nxt not in dfa_index:
                dfa_index[f_nxt] = len(dfa_index)
                q.append(f_nxt)
            row.append(dfa_index[f_nxt])
        dfa_trans.append(row)

    b0 = dfa_index[frozenset([nfa_index[(0, 0, 0)]])]
    b1 = dfa_index[frozenset([nfa_index[(0, 0, 1)]])]
    empty_state = dfa_index[frozenset()]
    return dfa_states, dfa_trans, b0, b1, empty_state


_DFA_STATES, _DFA_TRANS, _BOUNDARY0, _BOUNDARY1, _DEAD = _build_dfa()


def _build_block_tables(max_len: int, max_tiles: int):
    d = len(_DFA_STATES)
    dp = [[0] * (max_tiles + 1) for _ in range(d)]
    dp[_BOUNDARY0][0] = 1

    h_table = [[0] * (max_tiles + 1) for _ in range(max_len + 1)]
    j_table = [[0] * (max_tiles + 1) for _ in range(max_len + 1)]

    for length in range(1, max_len + 1):
        new_dp = [[0] * (max_tiles + 1) for _ in range(d)]
        for st in range(d):
            if st == _DEAD:
                continue
            row_dp = dp[st]
            trans_st = _DFA_TRANS[st]
            for c in range(1, 5):
                nxt_st = trans_st[c]
                if nxt_st == _DEAD:
                    continue
                nxt_row = new_dp[nxt_st]
                for t in range(max_tiles - c + 1):
                    v = row_dp[t]
                    if v:
                        nxt_row[t + c] = (nxt_row[t + c] + v) % _MOD

        dp = new_dp
        for st in range(d):
            nxt0 = _DFA_TRANS[st][0]
            if nxt0 == _BOUNDARY0:
                for t in range(max_tiles + 1):
                    v = dp[st][t]
                    if v:
                        h_table[length][t] = (h_table[length][t] + v) % _MOD
            elif nxt0 == _BOUNDARY1:
                for t in range(max_tiles + 1):
                    v = dp[st][t]
                    if v:
                        j_table[length][t] = (j_table[length][t] + v) % _MOD

    return h_table, j_table


def _per_suit_a_b(n: int, t_triples: int) -> Tuple[List[int], List[int]]:
    max_k = t_triples
    max_t = 3 * max_k + 2
    max_len = max_t

    h_table, j_table = _build_block_tables(max_len, max_t)

    gh = [[0] * (max_k + 1) for _ in range(max_len + 1)]
    gj = [[0] * (max_k + 1) for _ in range(max_len + 1)]
    for l_val in range(1, max_len + 1):
        for k in range(max_k + 1):
            if 3 * k <= max_t:
                gh[l_val][k] = h_table[l_val][3 * k]
            if 3 * k + 2 <= max_t:
                gj[l_val][k] = j_table[l_val][3 * k + 2]

    fact, invfact = _precompute_fact(2 * max_k + 5)

    u_dp = [[[0] * (max_k + 1) for _ in range(max_len + 1)] for _ in range(max_k + 2)]
    u_dp[0][0][0] = 1

    for m in range(max_k):
        for l_sum in range(max_len + 1):
            for k in range(max_k + 1):
                ways = u_dp[m][l_sum][k]
                if not ways:
                    continue
                for l_b in range(1, max_len - l_sum + 1):
                    gh_row = gh[l_b]
                    for k_b in range(max_k - k + 1):
                        val = gh_row[k_b]
                        if val:
                            nxt = (ways * val) % _MOD
                            u_dp[m + 1][l_sum + l_b][k + k_b] = (
                                u_dp[m + 1][l_sum + l_b][k + k_b] + nxt
                            ) % _MOD

    a_poly = [0] * (max_k + 1)
    for k in range(max_k + 1):
        tot = 0
        if k == 0:
            tot = 1
        for m in range(1, max_k + 1):
            for l_sum in range(m, max_len + 1):
                ways = u_dp[m][l_sum][k]
                if not ways:
                    continue
                comb_val = _nck_small(n - l_sum + 1, m, invfact)
                tot = (tot + ways * comb_val) % _MOD
        a_poly[k] = tot

    v_dp = [[[0] * (max_k + 1) for _ in range(max_len + 1)] for _ in range(max_k + 3)]
    for m in range(max_k + 1):
        for l_sum in range(max_len + 1):
            for k in range(max_k + 1):
                ways = u_dp[m][l_sum][k]
                if not ways:
                    continue
                for l_b in range(1, max_len - l_sum + 1):
                    gj_row = gj[l_b]
                    for k_b in range(max_k - k + 1):
                        val = gj_row[k_b]
                        if val:
                            nxt = (ways * val) % _MOD
                            v_dp[m + 1][l_sum + l_b][k + k_b] = (
                                v_dp[m + 1][l_sum + l_b][k + k_b] + nxt
                            ) % _MOD

    w_dp = [[[0] * (max_k + 1) for _ in range(max_len + 1)] for _ in range(max_k + 3)]
    for m1 in range(1, max_k + 2):
        for l1 in range(max_len + 1):
            for k1 in range(max_k + 1):
                v1 = v_dp[m1][l1][k1]
                if not v1:
                    continue
                for m2 in range(max_k - m1 + 2):
                    for l2 in range(max_len - l1 + 1):
                        for k2 in range(max_k - k1 + 1):
                            v2 = u_dp[m2][l2][k2]
                            if v2:
                                nxt = (v1 * v2) % _MOD
                                w_dp[m1 + m2][l1 + l2][k1 + k2] = (
                                    w_dp[m1 + m2][l1 + l2][k1 + k2] + nxt
                                ) % _MOD

    b_poly = [0] * (max_k + 1)
    for k in range(max_k + 1):
        tot = 0
        for m in range(1, max_k + 2):
            for l_sum in range(m, max_len + 1):
                ways = w_dp[m][l_sum][k]
                if not ways:
                    continue
                comb_val = _nck_small(n - l_sum + 1, m, invfact)
                tot = (tot + ways * comb_val) % _MOD
        b_poly[k] = tot

    return a_poly, b_poly


def _poly_mul(a: List[int], b: List[int], deg: int) -> List[int]:
    res = [0] * (deg + 1)
    for i, ai in enumerate(a):
        if not ai:
            continue
        for j, bj in enumerate(b):
            if not bj or i + j > deg:
                continue
            res[i + j] = (res[i + j] + ai * bj) % _MOD
    return res


def _poly_pow(base: List[int], exp: int, deg: int) -> List[int]:
    res = [0] * (deg + 1)
    res[0] = 1
    b = base[:]
    e = exp
    while e > 0:
        if e & 1:
            res = _poly_mul(res, b, deg)
        e >>= 1
        if e:
            b = _poly_mul(b, b, deg)
    return res


def solve(n: int = 100_000_000, s: int = 100_000_000, t: int = 30) -> int:
    """Compute w(n, s, t) modulo 1000000007 using Mahjong DFA block decomposition and polynomial powers."""
    a_poly, b_poly = _per_suit_a_b(n, t)

    if s <= 1:
        a_pow = [1] + [0] * t
    else:
        a_pow = _poly_pow(a_poly, s - 1, t)

    total = 0
    for k in range(t + 1):
        total = (total + b_poly[k] * a_pow[t - k]) % _MOD

    ans = (total * (s % _MOD)) % _MOD
    return ans


if __name__ == "__main__":
    print(solve())
