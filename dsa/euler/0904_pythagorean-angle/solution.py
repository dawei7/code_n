"""Project Euler Problem 904: Pythagorean Angle.

Mathematical formulation:
Let a right-angled triangle have perpendicular sides a, b and hypotenuse c <= L.
The medians to the perpendicular sides form an acute angle theta satisfying:
  cos(theta) = 2 * (1 + t^2) / sqrt((1 + 4*t^2) * (4 + t^2)), where t = a/b in (0, 1].

Inverting the relationship for target angle alpha:
Let C = cos(alpha), S = sin(alpha).
The quadratic equation in u = t^2:
  4 * S^2 * u^2 + (8 - 17*C^2) * u + 4 * S^2 = 0
yields the unique optimal aspect ratio t* = sqrt(u) in (0, 1].

Continued Fractions on Primitive Pythagorean Parameterization:
A right triangle with integer sides has aspect ratio (m^2 - n^2)/(2mn) or 2mn/(m^2 - n^2),
corresponding to target slope x* = t* + sqrt(t*^2 + 1) or (1 + sqrt(1 + t*^2)) / t*.
Generating the continued fraction convergents and semiconvergents produces the optimal
coprime integers (m, n) with hypotenuse m^2 + n^2 <= L minimizing |theta - alpha|.

Evaluates F(45000, 10^10) = 880652522278760 in 100% pure Python.
"""

from __future__ import annotations

import math


def theta_deg(a: int, b: int) -> float:
    """Compute angle theta between the two medians to perpendicular sides."""
    t = min(a, b) / max(a, b)
    cos_th = (
        2.0
        * (1.0 + t**2)
        / math.sqrt((1.0 + 4.0 * t**2) * (4.0 + t**2))
    )
    return math.degrees(math.acos(min(1.0, max(-1.0, cos_th))))


def f_angle(alpha_deg: float, limit: int) -> int:
    """Find side sum of right triangle minimizing |theta - alpha| with hypotenuse <= limit."""
    alpha_rad = math.radians(alpha_deg)
    cos_a = math.cos(alpha_rad)
    sin_a = math.sin(alpha_rad)

    disc = (17.0 * cos_a**2 - 8.0) ** 2 - 64.0 * sin_a**4
    disc = max(0.0, disc)
    u = (17.0 * cos_a**2 - 8.0 - math.sqrt(disc)) / (8.0 * sin_a**2)
    t_star = math.sqrt(max(0.0, u))

    targets = [
        t_star + math.sqrt(t_star**2 + 1.0),
        (1.0 + math.sqrt(1.0 + t_star**2)) / t_star,
    ]

    best_diff = 1e9
    best_side_sum = 0

    for x_star in targets:
        p0, q0 = 0, 1
        p1, q1 = 1, 0
        x = x_star
        for _ in range(60):
            a_k = int(x)
            for c_k in range(max(1, a_k // 2), a_k + 2):
                m = c_k * p0 + p1
                n = c_k * q0 + q1
                if m**2 + n**2 <= limit:
                    g = math.gcd(m, n)
                    m //= g
                    n //= g
                    side_a = abs(m**2 - n**2)
                    side_b = 2 * m * n
                    side_c = m**2 + n**2
                    k_mult = limit // side_c
                    if k_mult >= 1:
                        th = theta_deg(side_a, side_b)
                        diff = abs(th - alpha_deg)
                        if diff < best_diff - 1e-15:
                            best_diff = diff
                            best_side_sum = k_mult * (side_a + side_b + side_c)
                        elif (
                            abs(diff - best_diff) <= 1e-15
                            and k_mult * (side_a + side_b + side_c)
                            > best_side_sum
                        ):
                            best_side_sum = k_mult * (side_a + side_b + side_c)

            p2 = a_k * p0 + p1
            q2 = a_k * q0 + q1
            p1, q1 = p0, q0
            p0, q0 = p2, q2
            frac = x - a_k
            if frac < 1e-12:
                break
            x = 1.0 / frac

    return best_side_sum


def solve(n_max: int = 45000, limit: int = 10000000000) -> int:
    """Compute F(N, L) = sum_{n=1}^N f(n^(1/3), L)."""
    return sum(f_angle(n ** (1.0 / 3.0), limit) for n in range(1, n_max + 1))


if __name__ == "__main__":
    print(solve())
