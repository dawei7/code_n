"""Project Euler Problem 677: Coloured Graphs.

Find g(10000) mod 1000000007, where g(n) is the number of unlabelled coloured trees with n nodes
such that red nodes have degree <= 4, blue and yellow nodes have degree <= 3, and no yellow-yellow edge exists.
"""

from typing import List

_MOD = 1_000_000_007
_INV2 = (_MOD + 1) // 2
_INV6 = pow(6, _MOD - 2, _MOD)
_INV24 = pow(24, _MOD - 2, _MOD)


def _coeff_square(seq: List[int], d: int) -> int:
    """Coefficient of x^d in (seq(x))^2."""
    if d < 2:
        return 0
    half = d // 2
    s = 0
    if d & 1:
        for i in range(1, half + 1):
            s += 2 * seq[i] * seq[d - i]
    else:
        mid = seq[half]
        s = mid * mid
        for i in range(1, half):
            s += 2 * seq[i] * seq[d - i]
    return s % _MOD


def _f3_nony_at_degree(
    d: int, n: int, b: List[int], sq_b: List[int], py: List[int]
) -> int:
    f2n = py[n]
    if d < 3:
        return f2n

    s = 0
    for i in range(1, d):
        s += b[i] * sq_b[d - i]
    cube = s % _MOD

    s = 0
    for j in range(1, d // 2 + 1):
        i = d - 2 * j
        if i <= 0:
            break
        s += b[i] * b[j]
    prod = s % _MOD

    b3 = b[d // 3] if d % 3 == 0 else 0
    set3_nony = (cube + 3 * prod + 2 * b3) % _MOD * _INV6 % _MOD
    return (f2n + set3_nony) % _MOD


def _set4_total_at_degree(d: int, a: List[int], sq_a: List[int]) -> int:
    if d < 4:
        return 0

    s = 0
    for i in range(1, d):
        s += sq_a[i] * sq_a[d - i]
    a1_4 = s % _MOD

    s = 0
    for j in range(1, d // 2 + 1):
        i = d - 2 * j
        if i <= 0:
            break
        s += sq_a[i] * a[j]
    a1_2_a2 = s % _MOD

    a2_2 = sq_a[d // 2] if d % 2 == 0 else 0

    s = 0
    for j in range(1, d // 3 + 1):
        i = d - 3 * j
        if i <= 0:
            break
        s += a[i] * a[j]
    a1_a3 = s % _MOD

    a4 = a[d // 4] if d % 4 == 0 else 0

    term = (a1_4 + 6 * a1_2_a2 + 3 * a2_2 + 8 * a1_a3 + 6 * a4) % _MOD
    return (term * _INV24) % _MOD


def solve(n: int = 10_000) -> int:
    """Compute g(n) modulo 1000000007 using generating functions and Otter's dissimilarity theorem."""
    pr = [0] * (n + 1)
    pb = [0] * (n + 1)
    py = [0] * (n + 1)

    a = [0] * (n + 1)
    b = [0] * (n + 1)

    sq_a = [0] * (n + 1)
    sq_b = [0] * (n + 1)

    for k in range(1, n + 1):
        d = k - 1

        if d < 2:
            sqa = 0
            sqb = 0
        else:
            half = d // 2
            s = 0
            if d & 1:
                for i in range(1, half + 1):
                    s += 2 * a[i] * a[d - i]
            else:
                mid = a[half]
                s = mid * mid
                for i in range(1, half):
                    s += 2 * a[i] * a[d - i]
            sqa = s % _MOD

            s = 0
            if d & 1:
                for i in range(1, half + 1):
                    s += 2 * b[i] * b[d - i]
            else:
                mid = b[half]
                s = mid * mid
                for i in range(1, half):
                    s += 2 * b[i] * b[d - i]
            sqb = s % _MOD

        sq_a[d] = sqa
        sq_b[d] = sqb

        if d < 3:
            cube = 0
        else:
            s = 0
            for i in range(1, d):
                s += a[i] * sq_a[d - i]
            cube = s % _MOD

        if d < 3:
            prod = 0
        else:
            s = 0
            for j in range(1, d // 2 + 1):
                i = d - 2 * j
                if i <= 0:
                    break
                s += a[i] * a[j]
            prod = s % _MOD

        f2 = a[d] + (1 if d == 0 else 0)
        tmp = sqa + (a[d // 2] if (d & 1) == 0 else 0)
        f2 = (f2 + (tmp % _MOD) * _INV2) % _MOD

        f2n = b[d] + (1 if d == 0 else 0)
        tmp = sqb + (b[d // 2] if (d & 1) == 0 else 0)
        f2n = (f2n + (tmp % _MOD) * _INV2) % _MOD

        a3 = a[d // 3] if d % 3 == 0 else 0
        set3_total = (cube + 3 * prod + 2 * a3) % _MOD * _INV6 % _MOD
        f3 = (f2 + set3_total) % _MOD

        pr[k] = f3
        pb[k] = f2
        py[k] = f2n

        a[k] = (pr[k] + pb[k] + py[k]) % _MOD
        b[k] = (pr[k] + pb[k]) % _MOD

    sq_a[n] = _coeff_square(a, n)

    d = n - 1
    f3_total = pr[n]
    f4_total = (f3_total + _set4_total_at_degree(d, a, sq_a)) % _MOD
    f3_nony = _f3_nony_at_degree(d, n, b, sq_b, py)
    v_nodes = (f4_total + f3_total + f3_nony) % _MOD

    sq_a_n = sq_a[n] if sq_a[n] else _coeff_square(a, n)
    sq_py_n = _coeff_square(py, n)

    a2_n = a[n // 2] if (n & 1) == 0 else 0
    py2_n = py[n // 2] if (n & 1) == 0 else 0

    d_edges = (sq_a_n - sq_py_n) % _MOD
    e_edges = ((sq_a_n + a2_n - sq_py_n - py2_n) % _MOD) * _INV2 % _MOD

    ans = (v_nodes + e_edges - d_edges) % _MOD
    return ans


if __name__ == "__main__":
    print(solve())
