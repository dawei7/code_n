"""Project Euler Problem 459: Flipping Game.

Find W(10^6), the number of winning first moves for the first player
on an N x N board of white disks with square width and triangular height flips.
"""

from math import isqrt
from typing import Dict, List, Tuple

M = 1024
FERMAT: List[int] = [1 << (1 << n) for n in range(7)]


def _fermat_index(x: int) -> int:
    i = 0
    while i + 1 < len(FERMAT) and FERMAT[i + 1] <= x:
        i += 1
    return i


_nim_mul_cache: Dict[Tuple[int, int], int] = {}


def _nim_mul(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    if a == 1:
        return b
    if b == 1:
        return a
    if a < b:
        a, b = b, a
    key = (a, b)
    r = _nim_mul_cache.get(key)
    if r is not None:
        return r

    m = _fermat_index(a)
    n = _fermat_index(b)

    if m != n:
        if m > n:
            fm = FERMAT[m]
            shift = 1 << m
            a1, a2 = divmod(a, fm)
            r = (_nim_mul(a1, b) << shift) ^ _nim_mul(a2, b)
        else:
            fn = FERMAT[n]
            shift = 1 << n
            b1, b2 = divmod(b, fn)
            r = (_nim_mul(a, b1) << shift) ^ _nim_mul(a, b2)
    else:
        fn = FERMAT[n]
        shift = 1 << n
        a1, a2 = divmod(a, fn)
        b1, b2 = divmod(b, fn)

        p1 = _nim_mul(a1, b1)
        p2 = _nim_mul(a2, b2)
        p3 = _nim_mul(a1 ^ a2, b1 ^ b2)
        p4 = _nim_mul(p1, fn >> 1)
        p5 = p3 ^ p2

        r = (p5 << shift) ^ p2 ^ p4

    _nim_mul_cache[key] = r
    return r


def _nim_pow(a: int, e: int) -> int:
    res = 1
    base = a
    exp = e
    while exp:
        if exp & 1:
            res = _nim_mul(res, base)
        exp >>= 1
        if exp:
            base = _nim_mul(base, base)
    return res


def _nim_inv_2_16(a: int) -> int:
    if a == 0:
        raise ZeroDivisionError(
            "0 has no multiplicative inverse in nimbers"
        )
    return _nim_pow(a, 65534)


def _make_squares_upto(n: int) -> List[int]:
    r = isqrt(n)
    return [k * k for k in range(1, r + 1)]


def _make_triangles_upto(n: int) -> List[int]:
    out = []
    k = 1
    while True:
        t = k * (k + 1) // 2
        if t > n:
            break
        out.append(t)
        k += 1
    return out


def _compute_1d_prefix_and_freq(
    n: int, lengths: List[int]
) -> Tuple[List[int], List[int]]:
    c_arr = [0] * (n + 1)
    freq = [0] * M

    mark = [0] * M
    cnt = [0] * M
    touched = [0] * M

    m = 0
    l_list = lengths
    l_len = len(l_list)

    for x in range(1, n + 1):
        while m < l_len and l_list[m] <= x:
            m += 1

        cx_prev = c_arr[x - 1]
        tlen = 0

        for j in range(m):
            v = cx_prev ^ c_arr[x - l_list[j]]
            if mark[v] != x:
                mark[v] = x
                cnt[v] = 1
                touched[tlen] = v
                tlen += 1
            else:
                cnt[v] += 1

        t = 0
        while mark[t] == x:
            t += 1

        cx = cx_prev ^ t
        c_arr[x] = cx

        for i in range(tlen):
            v = touched[i]
            freq[v ^ t] += cnt[v]

    return c_arr, freq


def solve(n: int = 1_000_000) -> int:
    """Compute W(n) using Pearson's Tartan theorem and 2D Nim-multiplication."""
    squares = _make_squares_upto(n)
    triangles = _make_triangles_upto(n)

    c_sq, freq_sq = _compute_1d_prefix_and_freq(n, squares)
    c_tr, freq_tr = _compute_1d_prefix_and_freq(n, triangles)

    board = _nim_mul(c_sq[n], c_tr[n])
    total = 0
    sum_sq = sum(freq_sq)
    sum_tr = sum(freq_tr)

    if board == 0:
        a0 = freq_sq[0]
        b0 = freq_tr[0]
        return a0 * sum_tr + (sum_sq - a0) * b0

    inv_cache: Dict[int, int] = {}
    for a in range(1, M):
        fa = freq_sq[a]
        if fa == 0:
            continue
        inva = inv_cache.get(a)
        if inva is None:
            inva = _nim_inv_2_16(a)
            inv_cache[a] = inva
        b = _nim_mul(board, inva)
        if b < M:
            total += fa * freq_tr[b]

    return total


if __name__ == "__main__":
    print(solve())
