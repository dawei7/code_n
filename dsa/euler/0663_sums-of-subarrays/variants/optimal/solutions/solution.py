"""Project Euler Problem 663: Sums of Subarrays.

Find S(10000003, 10200000) - S(10000003, 10000000), where S(n, l) is the sum over i=1..l
of the maximum contiguous subarray sum M_n(i) of an array updated by tribonacci steps.
"""

from array import array
from typing import Tuple

_NEG_INF = -(10**18)


def _max_subarray_kadane(arr: list) -> int:
    cur = best = arr[0]
    for x in arr[1:]:
        s = cur + x
        cur = x if s < x else s
        best = best if best > cur else cur
    return best


def _block_summary(a_arr: array, start: int, end: int) -> Tuple[int, int, int, int]:
    r = 0
    max_pref = _NEG_INF
    min_pref_best = 0
    best = _NEG_INF
    min_pref_suff = 0
    last = end - 1

    for k in range(start, end):
        r += a_arr[k]
        if r > max_pref:
            max_pref = r
        cand = r - min_pref_best
        if cand > best:
            best = cand
        if r < min_pref_best:
            min_pref_best = r
        if k != last and r < min_pref_suff:
            min_pref_suff = r

    total = r
    max_suff = total - min_pref_suff
    return total, max_pref, max_suff, best


def _build_block_tree(a_arr: array, n: int, b_size: int):
    m = (n + b_size - 1) // b_size
    size = 1
    while size < m:
        size <<= 1

    total = array("q", [0]) * (2 * size)
    pref = array("q", [_NEG_INF]) * (2 * size)
    suff = array("q", [_NEG_INF]) * (2 * size)
    best = array("q", [_NEG_INF]) * (2 * size)

    for b in range(m):
        s = b * b_size
        e = min(n, s + b_size)
        ts, tp, tu, tb = _block_summary(a_arr, s, e)
        pos = size + b
        total[pos] = ts
        pref[pos] = tp
        suff[pos] = tu
        best[pos] = tb

    for pos in range(size - 1, 0, -1):
        l = pos * 2
        r = l + 1
        total[pos] = total[l] + total[r]
        v1 = pref[l]
        v2 = total[l] + pref[r]
        pref[pos] = v1 if v1 >= v2 else v2
        v1 = suff[r]
        v2 = total[r] + suff[l]
        suff[pos] = v1 if v1 >= v2 else v2
        v = best[l]
        br = best[r]
        if br > v:
            v = br
        cross = suff[l] + pref[r]
        if cross > v:
            v = cross
        best[pos] = v

    return m, size, total, pref, suff, best


def _update_block(tree, a_arr: array, n: int, b_size: int, b: int) -> None:
    _, size, total, pref, suff, best = tree
    s = b * b_size
    e = min(n, s + b_size)
    ts, tp, tu, tb = _block_summary(a_arr, s, e)

    pos = size + b
    total[pos] = ts
    pref[pos] = tp
    suff[pos] = tu
    best[pos] = tb

    pos //= 2
    while pos:
        l = pos * 2
        r = l + 1
        total[pos] = total[l] + total[r]
        v1 = pref[l]
        v2 = total[l] + pref[r]
        pref[pos] = v1 if v1 >= v2 else v2
        v1 = suff[r]
        v2 = total[r] + suff[l]
        suff[pos] = v1 if v1 >= v2 else v2
        v = best[l]
        br = best[r]
        if br > v:
            v = br
        cross = suff[l] + pref[r]
        if cross > v:
            v = cross
        best[pos] = v
        pos //= 2


def solve(
    n: int = 10_000_003, start: int = 10_000_000, end: int = 10_200_000
) -> int:
    """Compute S(n, end) - S(n, start) using delayed segment tree construction over blocked array updates."""
    if n <= 200 and end <= 1000:
        a_arr = [0] * n
        u0, u1, u2 = 0, 0, 1 % n
        total_ans = 0
        for step in range(1, end + 1):
            idx = u0
            delta = (u1 << 1) - n + 1
            a_arr[idx] += delta
            if step > start:
                total_ans += _max_subarray_kadane(a_arr)

            t3 = u0 + u1 + u2
            if t3 >= n:
                t3 -= n
            if t3 >= n:
                t3 -= n
            t4 = u1 + u2 + t3
            if t4 >= n:
                t4 -= n
            if t4 >= n:
                t4 -= n
            u0, u1, u2 = u2, t3, t4
        return total_ans

    b_size = 256
    a_arr = array("q", [0]) * n
    u0, u1, u2 = 0, 0, 1 % n
    tree = None
    ans = 0

    for i in range(1, end + 1):
        idx = u0
        delta = (u1 << 1) - n + 1
        a_arr[idx] += delta

        if i == start:
            tree = _build_block_tree(a_arr, n, b_size)
        elif i > start:
            _update_block(tree, a_arr, n, b_size, idx // b_size)
            ans += tree[5][1]

        t3 = u0 + u1 + u2
        if t3 >= n:
            t3 -= n
        if t3 >= n:
            t3 -= n
        t4 = u1 + u2 + t3
        if t4 >= n:
            t4 -= n
        if t4 >= n:
            t4 -= n
        u0, u1, u2 = u2, t3, t4

    return ans


if __name__ == "__main__":
    print(solve())
