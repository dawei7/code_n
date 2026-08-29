"""Project Euler Problem 532: Nanobots on Geodesics.

Find the total length of all lines drawn by nanobots on a unit sphere when using
just enough bots so that the line each bot draws is longer than 1000.
"""

from __future__ import annotations

import math
from typing import Callable, Dict

RADIUS_SMALL_CIRCLE = 0.999
Y_MAX = 0.5 * math.log(
    (1.0 + RADIUS_SMALL_CIRCLE) / (1.0 - RADIUS_SMALL_CIRCLE)
)


def _adaptive_simpson(
    f: Callable[[float], float],
    a: float,
    b: float,
    eps: float,
    fa: float | None = None,
    fb: float | None = None,
    fm: float | None = None,
    depth: int = 0,
    max_depth: int = 30,
) -> float:
    m = (a + b) * 0.5
    if fa is None:
        fa = f(a)
    if fb is None:
        fb = f(b)
    if fm is None:
        fm = f(m)

    s_coarse = (b - a) * (fa + 4.0 * fm + fb) / 6.0

    lm = (a + m) * 0.5
    rm = (m + b) * 0.5
    flm = f(lm)
    frm = f(rm)

    s_left = (m - a) * (fa + 4.0 * flm + fm) / 6.0
    s_right = (b - m) * (fm + 4.0 * frm + fb) / 6.0
    s_fine = s_left + s_right

    if depth >= max_depth or abs(s_fine - s_coarse) <= 15.0 * eps:
        return s_fine + (s_fine - s_coarse) / 15.0

    return _adaptive_simpson(
        f, a, m, eps * 0.5, fa, fm, flm, depth + 1, max_depth
    ) + _adaptive_simpson(
        f, m, b, eps * 0.5, fm, fb, frm, depth + 1, max_depth
    )


def length_per_bot(n: int, cache: Dict[int, float]) -> float:
    """Compute arc-length drawn by each bot for n bots on the sphere."""
    if n in cache:
        return cache[n]
    if n < 3:
        raise ValueError("n must be at least 3")

    alpha = math.pi / n
    s = math.sin(alpha)
    u = s * s

    def integrand(y: float) -> float:
        t = math.tanh(y)
        return math.sqrt(1.0 - u * t * t)

    integral_val = _adaptive_simpson(integrand, 0.0, Y_MAX, 1e-12)
    length = integral_val / s
    cache[n] = length
    return length


def solve(target_length: float = 1000.0) -> str:
    """Find minimal n such that length_per_bot(n) > target_length, and return total length."""
    cache: Dict[int, float] = {}

    hi = 3
    while length_per_bot(hi, cache) <= target_length:
        hi *= 2
    lo = hi // 2

    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if length_per_bot(mid, cache) > target_length:
            hi = mid
        else:
            lo = mid

    min_n = hi
    total = min_n * length_per_bot(min_n, cache)
    return f"{total:.2f}"


if __name__ == "__main__":
    print(solve())
