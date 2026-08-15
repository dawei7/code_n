"""Project Euler Problem 695: Random Rectangles.

Find the expected value of the area of the second biggest of the three rectangles defined by 3 random points
in a unit square, rounded to 10 decimal places.
"""

import math
from typing import List, Tuple

_PERM_CODES = [
    (0, 1, 2),
    (2, 1, 0),
    (0, 2, 1),
    (2, 0, 1),
    (1, 2, 0),
    (1, 0, 2),
]


def _gauss_legendre_01(n: int) -> Tuple[List[float], List[float]]:
    nodes = [0.0] * n
    weights = [0.0] * n
    m = (n + 1) // 2

    for i in range(m):
        x = math.cos(math.pi * (i + 0.75) / (n + 0.5))

        for _ in range(100):
            p0, p1 = 1.0, x
            for k in range(2, n + 1):
                p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
            pn = p1
            pnm1 = p0

            dpn = n * (x * pn - pnm1) / (x * x - 1.0)
            dx = pn / dpn
            x -= dx
            if abs(dx) < 1e-16:
                break

        w = 2.0 / ((1.0 - x * x) * (dpn * dpn))
        xl = (-x + 1.0) * 0.5
        xr = (x + 1.0) * 0.5
        wl = w * 0.5
        wr = w * 0.5

        nodes[i] = xl
        nodes[n - 1 - i] = xr
        weights[i] = wl
        weights[n - 1 - i] = wr

    return nodes, weights


def _median_index(a: float, b: float, c: float) -> int:
    if (a <= b <= c) or (c <= b <= a):
        return 1
    if (b <= a <= c) or (c <= a <= b):
        return 0
    return 2


def _integral_median_linear(p: float, q: float, c: float) -> float:
    bps = [0.0, 1.0]

    if p > 0.0:
        t = c / p
        if 0.0 < t < 1.0:
            bps.append(t)

    if q > 0.0:
        t = 1.0 - c / q
        if 0.0 < t < 1.0:
            bps.append(t)

    if p + q > 0.0:
        t = q / (p + q)
        if 0.0 < t < 1.0:
            bps.append(t)

    bps = sorted(set(bps))
    total = 0.0

    for t0, t1 in zip(bps, bps[1:]):
        tm = 0.5 * (t0 + t1)
        a = p * tm
        b = q * (1.0 - tm)

        which = _median_index(a, b, c)
        if which == 0:
            total += p * (t1 * t1 - t0 * t0) * 0.5
        elif which == 1:
            total += q * (t1 - t0) - q * (t1 * t1 - t0 * t0) * 0.5
        else:
            total += c * (t1 - t0)

    return total


def solve(n_u: int = 3000) -> str:
    """Compute the expected median area of 3 random rectangles in a unit square."""
    us, ws = _gauss_legendre_01(n_u)

    acc = 0.0
    for u, w in zip(us, ws):
        ou = 1.0 - u
        perm_sum = 0.0
        for code12, code23, code13 in _PERM_CODES:
            f12 = u if code12 == 0 else (ou if code12 == 1 else 1.0)
            f23 = u if code23 == 0 else (ou if code23 == 1 else 1.0)
            f13 = u if code13 == 0 else (ou if code13 == 1 else 1.0)
            perm_sum += _integral_median_linear(f12, f23, f13)

        avg_over_t_and_perm = perm_sum / 6.0
        acc += w * avg_over_t_and_perm

    ans = 0.25 * acc
    return f"{ans:.10f}"


if __name__ == "__main__":
    print(solve())
