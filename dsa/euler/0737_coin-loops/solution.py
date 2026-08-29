"""Project Euler Problem 737: Coin Loops.

Find the number of coins needed to loop 2020 times around the vertical line.
"""

from array import array
import math
from typing import List, Tuple

_EULER_GAMMA = 0.5772156649015328606065120900824024310421


def _harmonic_asymp(x: float) -> float:
    inv = 1.0 / x
    inv2 = inv * inv
    inv4 = inv2 * inv2
    inv6 = inv4 * inv2
    inv8 = inv4 * inv4
    return (
        math.log(x)
        + _EULER_GAMMA
        + 0.5 * inv
        - (1.0 / 12.0) * inv2
        + (1.0 / 120.0) * inv4
        - (1.0 / 252.0) * inv6
        + (1.0 / 240.0) * inv8
    )


def _gauss_legendre(n: int) -> Tuple[List[float], List[float]]:
    x = [0.0] * n
    w = [0.0] * n
    m = (n + 1) // 2
    for i in range(1, m + 1):
        z = math.cos(math.pi * (i - 0.25) / (n + 0.5))
        for _ in range(50):
            p1 = 1.0
            p2 = 0.0
            for j in range(1, n + 1):
                p3 = p2
                p2 = p1
                p1 = ((2.0 * j - 1.0) * z * p2 - (j - 1.0) * p3) / j
            pp = n * (z * p1 - p2) / (z * z - 1.0)
            z1 = z
            z = z1 - p1 / pp
            if abs(z - z1) < 1e-15:
                break
        p1 = 1.0
        p2 = 0.0
        for j in range(1, n + 1):
            p3 = p2
            p2 = p1
            p1 = ((2.0 * j - 1.0) * z * p2 - (j - 1.0) * p3) / j
        pp = n * (z * p1 - p2) / (z * z - 1.0)
        wi = 2.0 / ((1.0 - z * z) * pp * pp)
        x[i - 1] = -z
        x[n - i] = z
        w[i - 1] = wi
        w[n - i] = wi
    return x, w


def _beta_from_t(t: float, ht: float) -> float:
    r = math.sqrt(ht / t)
    q = math.sqrt(1.0 - 0.25 * r * r) / (r * (t + 0.5))
    return math.atan(q)


def _beta_real(m: float) -> float:
    t = m - 1.0
    return _beta_from_t(t, _harmonic_asymp(t))


def _alpha_from_t(t: float, ht: float) -> float:
    r = math.sqrt(ht / t)
    return math.acos(0.5 * r)


def _integral_beta_log(
    a: float, b: float, gl_x: List[float], gl_w: List[float], seg_u: float = 0.5
) -> float:
    if b <= a:
        return 0.0
    ua = math.log(a)
    ub = math.log(b)
    steps = max(1, int(math.ceil((ub - ua) / seg_u)))
    du = (ub - ua) / steps
    total = 0.0
    for i in range(steps):
        u0 = ua + i * du
        u1 = ua + (i + 1) * du
        mid = 0.5 * (u0 + u1)
        half = 0.5 * (u1 - u0)
        s = 0.0
        for xi, wi in zip(gl_x, gl_w):
            u = mid + half * xi
            m = math.exp(u)
            s += wi * _beta_real(m) * m
        total += s * half
    return total


def solve(loops: int = 2020) -> int:
    """Find the number of coins needed to loop given number of times using Gauss-Legendre quadrature integration."""
    m_bound = 500_000
    gl_x, gl_w = _gauss_legendre(16)

    h_arr = array("d", [0.0]) * (m_bound + 1)
    pref_beta = array("d", [0.0]) * (m_bound + 1)

    h_cur = 0.0
    for t in range(1, m_bound + 1):
        h_cur += 1.0 / t
        h_arr[t] = h_cur

    s_cur = 0.0
    for m in range(2, m_bound + 1):
        t = m - 1
        s_cur += _beta_from_t(float(t), h_arr[t])
        pref_beta[m] = s_cur

    def rotation_sum(n: int) -> float:
        if n < 2:
            return 0.0
        if n <= m_bound + 1:
            t = n - 1
            alpha = _alpha_from_t(float(t), h_arr[t])
            return alpha + pref_beta[n - 1]
        t = n - 1
        alpha = _alpha_from_t(float(t), _harmonic_asymp(float(t)))
        ia = float(m_bound + 1)
        ib = float(n - 1)
        integ = _integral_beta_log(ia, ib, gl_x, gl_w)
        fa = _beta_real(ia)
        fb = _beta_real(ib)
        tail = integ + 0.5 * (fa + fb)
        return alpha + pref_beta[m_bound] + tail

    target = 2.0 * math.pi * loops
    lo = 1
    hi = max(2, loops * 5)
    while rotation_sum(hi) <= target:
        hi *= 2

    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if rotation_sum(mid) > target:
            hi = mid
        else:
            lo = mid

    return hi


if __name__ == "__main__":
    print(solve())
