"""Project Euler Problem 689: Binary Series.

Find p(0.5), the probability that sum_{i=1}^infty d_i(x) / i^2 > 0.5 for uniform x in [0, 1),
giving the answer rounded to 8 decimal places.
"""

import math
from typing import Callable, List


def _adaptive_simpson(f: Callable[[float], float], a: float, b: float, eps: float) -> float:
    fa = f(a)
    fb = f(b)
    m = (a + b) * 0.5
    fm = f(m)
    s_val = (b - a) * (fa + 4.0 * fm + fb) / 6.0

    stack = [(a, b, fa, fm, fb, s_val, eps)]
    total = 0.0
    max_iters = 2_000_000
    iters = 0

    while stack:
        ca, cb, cfa, cfm, cfb, cs, ceps = stack.pop()
        cm = (ca + cb) * 0.5
        clm = (ca + cm) * 0.5
        crm = (cm + cb) * 0.5

        cflm = f(clm)
        cfrm = f(crm)

        s_left = (cm - ca) * (cfa + 4.0 * cflm + cfm) / 6.0
        s_right = (cb - cm) * (cfm + 4.0 * cfrm + cfb) / 6.0
        s2 = s_left + s_right

        iters += 1
        if iters > max_iters:
            break

        if abs(s2 - cs) <= 15.0 * ceps:
            total += s2 + (s2 - cs) / 15.0
        else:
            half = ceps * 0.5
            stack.append((cm, cb, cfm, cfrm, cfb, s_right, half))
            stack.append((ca, cm, cfa, cflm, cfm, s_left, half))

    return total


def solve(target_a: float = 0.5) -> str:
    """Compute p(target_a) using Gil-Pelaez characteristic-function Fourier inversion."""
    mu = (math.pi * math.pi) / 12.0
    beta = mu - target_a

    n_terms = 200
    inv2_i2: List[float] = [1.0 / (2.0 * i * i) for i in range(1, n_terms + 1)]

    zeta4 = (math.pi**4) / 90.0
    partial4 = sum(1.0 / (float(i) ** 4) for i in range(1, n_terms + 1))
    tail4 = zeta4 - partial4

    cos = math.cos
    sin = math.sin
    exp = math.exp

    def prod_cos(t: float) -> float:
        p = 1.0
        for c in inv2_i2:
            p *= cos(t * c)
        tail_term = exp(- (t * t * tail4) / 8.0)
        return p * tail_term

    def integrand(t: float) -> float:
        if t < 1e-12:
            return beta
        return (sin(beta * t) / t) * prod_cos(t)

    t_cut = 1200.0
    integral = _adaptive_simpson(integrand, 0.0, t_cut, 1e-12)
    prob = 0.5 + integral / math.pi
    return f"{prob:.8f}"


if __name__ == "__main__":
    print(solve())
