"""Project Euler Problem 416: A Frog's Trip.

Find the last 9 digits of F(10, 10^12), where F(m, n) is the number of ways a frog
can make m round trips on a row of n squares visiting at least n-1 squares.
"""

from typing import List, Tuple

MOD = 10**9


def _build_transitions(
    k: int, mod: int
) -> Tuple[List[List[Tuple[int, int, bool]]], int]:
    idx = {}
    states: List[Tuple[int, int]] = []
    for a in range(k + 1):
        for c in range(k - a + 1):
            idx[(a, c)] = len(states)
            states.append((a, c))

    comb = [[0] * (k + 1) for _ in range(k + 1)]
    for n in range(k + 1):
        comb[n][0] = comb[n][n] = 1
        for r in range(1, n):
            comb[n][r] = comb[n - 1][r - 1] + comb[n - 1][r]

    transitions: List[List[Tuple[int, int, bool]]] = [
        [] for _ in range(len(states))
    ]
    for i, (a, c) in enumerate(states):
        b = k - a - c
        for a0 in range(a + 1):
            for a1 in range(a - a0 + 1):
                a2 = a - a0 - a1
                coeff = comb[a][a0] * comb[a - a0][a1]
                a_new = a0 + b
                c_new = a2
                j = idx[(a_new, c_new)]
                transitions[i].append((j, coeff % mod, a_new == 0))
    target = idx[(k, 0)]
    return transitions, target


def _matmul(
    a: List[List[int]], b: List[List[int]], mod: int
) -> List[List[int]]:
    n = len(a)
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        ai = a[i]
        ri = res[i]
        for k in range(n):
            aik = ai[k]
            if aik == 0:
                continue
            bk = b[k]
            for j in range(n):
                ri[j] = (ri[j] + aik * bk[j]) % mod
    return res


def _matadd(
    a: List[List[int]], b: List[List[int]], mod: int
) -> List[List[int]]:
    n = len(a)
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        ai = a[i]
        bi = b[i]
        ri = res[i]
        for j in range(n):
            ri[j] = (ai[j] + bi[j]) % mod
    return res


def _matvec(v: List[int], a: List[List[int]], mod: int) -> List[int]:
    n = len(v)
    res = [0] * n
    for i in range(n):
        vi = v[i]
        if vi == 0:
            continue
        ai = a[i]
        for j in range(n):
            res[j] = (res[j] + vi * ai[j]) % mod
    return res


def solve(m_val: int = 10, n_val: int = 10**12, mod: int = MOD) -> str:
    """Compute F(m_val, n_val) mod mod using dual-component block matrix exponentiation."""
    if n_val <= 1:
        return f"{1 % mod:09d}"

    k = 2 * m_val
    transitions, target = _build_transitions(k, mod)
    size = len(transitions)

    # A: no-miss transitions, B: miss transitions
    a_mat = [[0] * size for _ in range(size)]
    b_mat = [[0] * size for _ in range(size)]
    for s in range(size):
        for j, c, is_zero in transitions[s]:
            if is_zero:
                b_mat[s][j] = (b_mat[s][j] + c) % mod
            else:
                a_mat[s][j] = (a_mat[s][j] + c) % mod

    exp = n_val - 1
    res_a = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    res_b = [[0] * size for _ in range(size)]
    base_a = a_mat
    base_b = b_mat

    while exp > 0:
        if exp & 1:
            ra = _matmul(res_a, base_a, mod)
            rb = _matadd(
                _matmul(res_b, base_a, mod),
                _matmul(res_a, base_b, mod),
                mod,
            )
            res_a, res_b = ra, rb
        ba = _matmul(base_a, base_a, mod)
        bb = _matadd(
            _matmul(base_b, base_a, mod),
            _matmul(base_a, base_b, mod),
            mod,
        )
        base_a, base_b = ba, bb
        exp >>= 1

    start = [0] * size
    start[target] = 1
    v_a = _matvec(start, res_a, mod)
    v_b = _matvec(start, res_b, mod)
    ans = (v_a[target] + v_b[target]) % mod
    return f"{ans:09d}"


if __name__ == "__main__":
    print(solve())
