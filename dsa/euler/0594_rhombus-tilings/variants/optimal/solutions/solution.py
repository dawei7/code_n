"""Project Euler Problem 594: Rhombus Tilings.

Find t(O_{4,2}), where t(O_{a,b}) is the number of tilings of the equiangular
convex octagon with alternating side lengths a and b using unit squares and 45-degree rhombi.
"""

from typing import Dict, Iterator, List, Tuple

_BINOM_CACHE: Dict[Tuple[int, int], int] = {}


def _binom(n: int, k: int) -> int:
    if n < 0 or k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)
    key = (n, k)
    if key in _BINOM_CACHE:
        return _BINOM_CACHE[key]

    res = 1
    for i in range(1, k + 1):
        res = res * (n - k + i) // i
    _BINOM_CACHE[key] = res
    return res


def _det_bareiss(mat: List[List[int]]) -> int:
    n = len(mat)
    if n == 0:
        return 1
    if n == 1:
        return mat[0][0]

    a = [row[:] for row in mat]
    sign = 1
    prev = 1

    for k in range(n - 1):
        if a[k][k] == 0:
            swap = None
            for i in range(k + 1, n):
                if a[i][k] != 0:
                    swap = i
                    break
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            sign = -sign

        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * pivot - a[i][k] * a[k][j]) // prev
        prev = pivot
        for i in range(k + 1, n):
            a[i][k] = 0

    return sign * a[n - 1][n - 1]


def _gen_monotone_matrices(
    rows: int, cols: int, max_value: int
) -> Iterator[Tuple[Tuple[int, ...], ...]]:
    m = [[0] * cols for _ in range(rows)]

    def rec(pos: int) -> Iterator[Tuple[Tuple[int, ...], ...]]:
        if pos == rows * cols:
            yield tuple(tuple(r) for r in m)
            return
        i, j = divmod(pos, cols)
        lo = 0
        if i > 0:
            lo = max(lo, m[i - 1][j])
        if j > 0:
            lo = max(lo, m[i][j - 1])
        for v in range(lo, max_value + 1):
            m[i][j] = v
            yield from rec(pos + 1)

    yield from rec(0)


def solve(a: int = 4, b: int = 2) -> int:
    """Count tilings t(O_{a,b}) using Lindstrom-Gessel-Viennot determinantal sums."""
    c, d = a, b
    x_list = list(_gen_monotone_matrices(b, d, a))
    y_list = []
    for y_rev in _gen_monotone_matrices(b, d, c):
        y = tuple(
            tuple(y_rev[b - 1 - i][j] for j in range(d)) for i in range(b)
        )
        y_list.append(y)

    total = 0

    for x in x_list:
        x_full = [[0] * (d + 2) for _ in range(b + 2)]
        for k in range(1, b + 1):
            for l in range(1, d + 1):
                x_full[k][l] = x[k - 1][l - 1]
        for k in range(1, b + 1):
            x_full[k][0] = 0
            x_full[k][d + 1] = a
        for l in range(0, d + 2):
            x_full[0][l] = 0
            x_full[b + 1][l] = a

        for y in y_list:
            y_full = [[0] * (d + 2) for _ in range(b + 2)]
            for k in range(1, b + 1):
                for l in range(1, d + 1):
                    y_full[k][l] = y[k - 1][l - 1]
            for k in range(1, b + 1):
                y_full[k][0] = 0
                y_full[k][d + 1] = c
            for l in range(0, d + 2):
                y_full[0][l] = c
                y_full[b + 1][l] = 0

            prod = 1

            for u in range(1, d + 2):
                m_mat = []
                for i in range(1, b + 1):
                    row = []
                    for j in range(1, b + 1):
                        val_a = (x_full[j][u] - x_full[i][u - 1]) + (
                            y_full[j][u] - y_full[i][u - 1]
                        )
                        val_b = (x_full[j][u] - x_full[i][u - 1]) + (j - i)
                        row.append(_binom(val_a, val_b))
                    m_mat.append(row)
                det_m = _det_bareiss(m_mat)
                prod *= det_m
                if prod == 0:
                    break
            if prod == 0:
                continue

            for v in range(1, b + 2):
                p_mat = []
                for i in range(1, d + 1):
                    row = []
                    for j in range(1, d + 1):
                        val_a = (x_full[v][j] - x_full[v - 1][i]) + (
                            y_full[v - 1][i] - y_full[v][j]
                        )
                        val_b = (x_full[v][j] - x_full[v - 1][i]) + (j - i)
                        row.append(_binom(val_a, val_b))
                    p_mat.append(row)
                det_p = _det_bareiss(p_mat)
                prod *= det_p
                if prod == 0:
                    break

            total += prod

    return total


if __name__ == "__main__":
    print(solve())
