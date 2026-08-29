"""Project Euler Problem 620: Planetary Gears.

Find G(500), where G(n) is the sum over s+p+q <= n (p < q, s, p >= 5)
of the number of valid gear arrangements g(s+p+q, s, p, q).
"""

import math

_PI = math.pi
_TWO_PI = 2.0 * _PI
_EPS = 1e-12


def _arrangements_for_spq(s: int, p: int, q: int) -> int:
    a = s + q
    b = s + p
    c_len = (p + q) - _TWO_PI

    a2 = a * a
    b2 = b * b
    c2 = c_len * c_len

    cos_alpha = (a2 + b2 - c2) / (2.0 * a * b)
    if cos_alpha > 1.0:
        cos_alpha = 1.0
    elif cos_alpha < -1.0:
        cos_alpha = -1.0
    alpha = math.acos(cos_alpha)

    cos_beta = (a2 + c2 - b2) / (2.0 * a * c_len)
    if cos_beta > 1.0:
        cos_beta = 1.0
    elif cos_beta < -1.0:
        cos_beta = -1.0
    beta = math.acos(cos_beta)

    t = (alpha * b + beta * ((p + q) + 2 * s)) / _PI
    return int(t + _EPS)


def solve(n: int = 500) -> int:
    """Compute G(n) by summing discrete phase meshing arrangements across all valid (s, p, q)."""
    total = 0
    for s in range(5, n - 9):
        rem = n - s
        p_max = (rem - 1) // 2
        for p in range(5, p_max + 1):
            q_max = rem - p
            for q in range(p + 1, q_max + 1):
                total += _arrangements_for_spq(s, p, q)
    return total


if __name__ == "__main__":
    print(solve())
