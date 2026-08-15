"""Project Euler Problem 645: Every Day Is a Holiday.

Find E(10000) rounded to 4 digits after the decimal point, where E(D) is the expected
number of emperors to reign before all D days of the year are holidays.
"""

import math
from typing import List, Tuple

_GL_N = 64


def _gauss_legendre_nodes_weights(n: int) -> Tuple[List[float], List[float]]:
    nodes = [0.0] * n
    weights = [0.0] * n
    m = (n + 1) // 2

    for i in range(m):
        z = math.cos(math.pi * (i + 0.75) / (n + 0.5))
        pp = 0.0
        for _ in range(30):
            p1, p2 = 1.0, 0.0
            for j in range(1, n + 1):
                p3, p2, p1 = p2, p1, ((2 * j - 1) * z * p1 - (j - 1) * p2) / j
            pp = n * (z * p1 - p2) / (z * z - 1.0)
            z1 = z
            z = z1 - p1 / pp
            if abs(z - z1) < 1e-15:
                break
        nodes[i] = -z
        nodes[n - 1 - i] = z
        w = 2.0 / ((1.0 - z * z) * (pp * pp))
        weights[i] = weights[n - 1 - i] = w

    return nodes, weights


_GL_X, _GL_W = _gauss_legendre_nodes_weights(_GL_N)


def _q_no_adjacent_cycle(d_days: int, p: float) -> float:
    if p <= 0.0:
        return 1.0
    if p >= 1.0:
        return 0.0

    a = 1.0 - p
    disc = math.sqrt(a * (1.0 + 3.0 * p))
    lam1 = (a + disc) * 0.5
    lam2 = (a - disc) * 0.5

    def pow_int(x: float) -> float:
        if x == 0.0:
            return 0.0
        ax = abs(x)
        ln = math.log1p(ax - 1.0) if ax > 0.9 else math.log(ax)
        val = math.exp(d_days * ln)
        if x < 0.0 and (d_days & 1):
            val = -val
        return val

    return pow_int(lam1) + pow_int(lam2)


def solve(d_days: int = 10000) -> str:
    """Compute E(D) using Poissonization, transfer matrix spectral trace, and Gauss-Legendre quadrature."""
    t_max = 25.0
    segments = 10
    step = t_max / segments
    total = 0.0

    for i in range(segments):
        a = i * step
        b = (i + 1) * step
        mid = (a + b) * 0.5
        half = (b - a) * 0.5
        s = 0.0
        for x, w in zip(_GL_X, _GL_W):
            t = mid + half * x
            prob_unpicked = math.exp(-t)
            integrand = 1.0 - _q_no_adjacent_cycle(d_days, prob_unpicked)
            s += w * integrand
        total += half * s

    ans = d_days * total
    return f"{ans:.4f}"


if __name__ == "__main__":
    print(solve())
