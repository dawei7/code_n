"""Project Euler Problem 438: Integer Part of Polynomial Equation's Solutions.

Find sum S(t) for n = 7, where S(t) = sum_i |a_i| over all integer tuples (a_1, ..., a_n)
such that all roots x_1 < ... < x_n of x^n + a_1 x^(n-1) + ... + a_n = 0 satisfy floor(x_i) = i.
"""

from math import comb
from typing import List, Tuple


def _sum_abs_range(lo: int, hi: int) -> int:
    if lo > hi:
        return 0
    if hi < 0:
        cnt = hi - lo + 1
        return -(lo + hi) * cnt // 2
    if lo > 0:
        cnt = hi - lo + 1
        return (lo + hi) * cnt // 2
    neg = (-lo) * ((-lo) + 1) // 2
    pos = hi * (hi + 1) // 2
    return neg + pos


def _precompute_p_and_a0(
    n: int,
) -> Tuple[List[List[List[List[int]]]], List[List[int]]]:
    maxdeg = n
    max_base = 2 * n + 1
    pow_shift = {}
    for base in range(1, max_base + 1):
        for p in range(0, n + 1):
            coeffs = [0] * (maxdeg + 1)
            for e in range(p + 1):
                coeffs[e] = comb(p, e) * (base ** (p - e)) * ((-1) ** e)
            pow_shift[(base, p)] = coeffs

    t_dict = {}
    for k in range(1, n + 1):
        r = n - k
        cjs = [((-1) ** (r - j)) * comb(r, j) for j in range(r + 1)]
        for m in range(1, k + 2):
            for i in range(0, k + 1):
                p = n - i
                acc = [0] * (maxdeg + 1)
                for j, cj in enumerate(cjs):
                    if cj == 0:
                        continue
                    poly = pow_shift[(m + j, p)]
                    for d in range(maxdeg + 1):
                        acc[d] += cj * poly[d]
                t_dict[(k, m, i)] = acc

    p_mat = [
        [[None for _ in range(n + 1)] for _ in range(k + 2)]
        for k in range(n + 1)
    ]
    a0_mat = [[0] * (k + 2) for k in range(n + 1)]
    for k in range(1, n + 1):
        r = n - k
        fact = 1
        for t in range(2, r + 1):
            fact *= t
        for m in range(1, k + 2):
            s = 1 if ((k + 1 - m) & 1) == 0 else -1
            for i in range(0, k + 1):
                poly = t_dict[(k, m, i)]
                if s == 1:
                    p_mat[k][m][i] = poly
                else:
                    p_mat[k][m][i] = [-x for x in poly]
            a0_mat[k][m] = s * fact
    return p_mat, a0_mat


def _first_nonzero_sign(poly: List[int], start: int = 1) -> int:
    for i in range(start, len(poly)):
        v = poly[i]
        if v != 0:
            return 1 if v > 0 else -1
    return 0


def solve(n: int = 7) -> int:
    """Compute sum S(t) over valid polynomial coefficient tuples using forward difference polytope search."""
    if n == 1:
        return 1

    p_mat, a0_mat = _precompute_p_and_a0(n)
    b_mat = [[None] * (k + 2) for k in range(n + 1)]
    for k in range(1, n + 1):
        for m in range(1, k + 2):
            b_mat[k][m] = p_mat[k][m][0].copy()

    def bound_from_ineq(a0_val: int, bpoly: List[int]) -> Tuple[int, int]:
        b0 = bpoly[0]
        if a0_val > 0:
            num = -b0
            den = a0_val
            if num % den:
                return 1, num // den + 1
            x0 = num // den
            s = _first_nonzero_sign(bpoly, 1)
            return 1, (x0 if s > 0 else x0 + 1)
        else:
            den = -a0_val
            num = b0
            if num % den:
                return 0, num // den
            x0 = num // den
            s = _first_nonzero_sign(bpoly, 1)
            return 0, (x0 if s > 0 else x0 - 1)

    count = 0
    total = 0

    def dfs(k: int, prefix_abs: int) -> None:
        nonlocal count, total
        lb = -10**30
        ub = 10**30
        a0_k = a0_mat[k]
        b_k = b_mat[k]
        for m in range(1, k + 2):
            is_lb, bnd = bound_from_ineq(a0_k[m], b_k[m])
            if is_lb:
                if bnd > lb:
                    lb = bnd
            else:
                if bnd < ub:
                    ub = bnd
        if lb > ub:
            return

        if k == n:
            cnt = ub - lb + 1
            count += cnt
            total += cnt * prefix_abs + _sum_abs_range(lb, ub)
            return

        kp_range = list(range(k + 1, n + 1))
        p_kp_m_k = [
            [p_mat[kp][m][k] for m in range(1, kp + 2)] for kp in kp_range
        ]
        b_kp_m = [b_mat[kp] for kp in kp_range]
        len_kp = len(kp_range)
        n_plus_1 = n + 1

        for ak in range(lb, ub + 1):
            if ak != 0:
                for idx in range(len_kp):
                    bkp = b_kp_m[idx]
                    pkp = p_kp_m_k[idx]
                    for m in range(len(pkp)):
                        poly = pkp[m]
                        bb = bkp[m + 1]
                        for d in range(n_plus_1):
                            bb[d] += ak * poly[d]

            dfs(k + 1, prefix_abs + abs(ak))

            if ak != 0:
                for idx in range(len_kp):
                    bkp = b_kp_m[idx]
                    pkp = p_kp_m_k[idx]
                    for m in range(len(pkp)):
                        poly = pkp[m]
                        bb = bkp[m + 1]
                        for d in range(n_plus_1):
                            bb[d] -= ak * poly[d]

    dfs(1, 0)
    return total


if __name__ == "__main__":
    print(solve())
