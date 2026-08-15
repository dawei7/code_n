"""Project Euler Problem 670: Colouring a Strip.

Find F(10^16) mod 1000004321, where F(n) is the number of valid 4-coloured tilings of a 2xn grid
with 1x1, 1x2, 1x3, and 2x1 tiles with no 4 corners meeting at a single interior point.
"""

from typing import Dict, List, Tuple

_MOD = 1_000_004_321
_COLORS = 4
_NONE = 4


def _transitions(state: Tuple[int, ...]) -> Dict[Tuple[int, ...], int]:
    v_prev, in_t, cont_t, val_t, in_b, cont_b, val_b = state
    out: Dict[Tuple[int, ...], int] = {}

    def add(
        v_cur: int,
        t_state: Tuple[int, int, int],
        b_state: Tuple[int, int, int],
        ways: int,
    ) -> None:
        if v_prev == 0 and v_cur == 0 and in_t == 0 and in_b == 0:
            return
        nt_in, nt_cont, nt_val = t_state
        nb_in, nb_cont, nb_val = b_state
        ns = (v_cur, nt_in, nt_cont, nt_val, nb_in, nb_cont, nb_val)
        out[ns] = (out.get(ns, 0) + ways) % _MOD

    c_t = val_t if in_t else -1
    c_b = val_b if in_b else -1

    def next_from_incoming(
        _incoming: int, cont: int, colour: int
    ) -> Tuple[int, int, int]:
        if cont:
            return (1, 0, colour)
        return (0, 0, colour)

    next_t = next_from_incoming(in_t, cont_t, val_t) if in_t else None
    next_b = next_from_incoming(in_b, cont_b, val_b) if in_b else None

    left_t = val_t
    left_b = val_b

    # Case 1: both cells already occupied
    if in_t and in_b:
        if c_t != c_b:
            add(0, next_t, next_b, 1)
        return out

    # Case 2: top occupied, bottom free
    if in_t and not in_b:
        for length in (1, 2, 3):
            for col in range(_COLORS):
                if left_b != _NONE and col == left_b:
                    continue
                if col == c_t:
                    continue
                if length == 1:
                    b_state = (0, 0, col)
                elif length == 2:
                    b_state = (1, 0, col)
                else:
                    b_state = (1, 1, col)
                add(0, next_t, b_state, 1)
        return out

    # Case 3: bottom occupied, top free
    if not in_t and in_b:
        for length in (1, 2, 3):
            for col in range(_COLORS):
                if left_t != _NONE and col == left_t:
                    continue
                if col == c_b:
                    continue
                if length == 1:
                    t_state = (0, 0, col)
                elif length == 2:
                    t_state = (1, 0, col)
                else:
                    t_state = (1, 1, col)
                add(0, t_state, next_b, 1)
        return out

    # Case 4: both cells free
    # Option A: vertical domino (2x1)
    for col in range(_COLORS):
        if left_t != _NONE and col == left_t:
            continue
        if left_b != _NONE and col == left_b:
            continue
        add(1, (0, 0, col), (0, 0, col), 1)

    # Option B: two horizontal tiles
    for lt in (1, 2, 3):
        for lb in (1, 2, 3):
            for ct in range(_COLORS):
                if left_t != _NONE and ct == left_t:
                    continue
                for cb in range(_COLORS):
                    if left_b != _NONE and cb == left_b:
                        continue
                    if ct == cb:
                        continue

                    if lt == 1:
                        t_state = (0, 0, ct)
                    elif lt == 2:
                        t_state = (1, 0, ct)
                    else:
                        t_state = (1, 1, ct)

                    if lb == 1:
                        b_state = (0, 0, cb)
                    elif lb == 2:
                        b_state = (1, 0, cb)
                    else:
                        b_state = (1, 1, cb)

                    add(0, t_state, b_state, 1)

    return out


def _build_automaton() -> (
    Tuple[List[Tuple[int, ...]], List[List[Tuple[int, int]]]]
):
    init = (1, 0, 0, _NONE, 0, 0, _NONE)
    states: List[Tuple[int, ...]] = [init]
    index = {init: 0}
    adj: List[List[Tuple[int, int]]] = []

    q = [init]
    qi = 0
    while qi < len(q):
        s = q[qi]
        qi += 1
        trans = _transitions(s)
        row: List[Tuple[int, int]] = []
        for ns, w in trans.items():
            if ns not in index:
                index[ns] = len(states)
                states.append(ns)
                q.append(ns)
            row.append((index[ns], w))
        adj.append(row)

    return states, adj


def _mat_mul(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    dim = len(a)
    c = [[0] * dim for _ in range(dim)]
    rng = range(dim)
    for i in rng:
        ai = a[i]
        ci = c[i]
        for k in rng:
            val_a = ai[k]
            if val_a:
                bk = b[k]
                for j in rng:
                    ci[j] += val_a * bk[j]
        for j in rng:
            ci[j] %= _MOD
    return c


def solve(n: int = 10_000_000_000_000_000) -> int:
    """Compute F(n) modulo 1000004321 using column transfer automaton and fast matrix exponentiation."""
    states, adj = _build_automaton()
    dim = len(states)

    if n <= 10:
        vec = [0] * dim
        vec[0] = 1
        for _ in range(n):
            nxt = [0] * dim
            for i, val in enumerate(vec):
                if val == 0:
                    continue
                for j, w in adj[i]:
                    nxt[j] = (nxt[j] + val * w) % _MOD
            vec = nxt
        ans = 0
        for i, s in enumerate(states):
            _, in_t, _, _, in_b, _, _ = s
            if in_t == 0 and in_b == 0:
                ans = (ans + vec[i]) % _MOD
        return ans

    t_mat = [[0] * dim for _ in range(dim)]
    for i in range(dim):
        for j, w in adj[i]:
            t_mat[i][j] = w

    # Binary exponentiation on vector
    vec = [0] * dim
    vec[0] = 1

    cur_mat = t_mat
    power = n
    while power > 0:
        if power & 1:
            nxt_vec = [0] * dim
            for i, vi in enumerate(vec):
                if vi:
                    row_i = cur_mat[i]
                    for j, aij in enumerate(row_i):
                        if aij:
                            nxt_vec[j] = (nxt_vec[j] + vi * aij) % _MOD
            vec = nxt_vec
        power >>= 1
        if power > 0:
            cur_mat = _mat_mul(cur_mat, cur_mat)

    ans = 0
    for i, s in enumerate(states):
        _, in_t, _, _, in_b, _, _ = s
        if in_t == 0 and in_b == 0:
            ans = (ans + vec[i]) % _MOD
    return ans


if __name__ == "__main__":
    print(solve())
