"""Project Euler Problem 363: Bézier Curves.

Find by how many percent the length of the cubic Bézier curve approximating a quarter circle
differs from the length of the quarter circle (rounded to 10 decimal places).
"""

from decimal import Decimal, getcontext
from math import cos, pi as math_pi


def solve(precision_digits: int = 10) -> str:
    """Compute the difference percentage between cubic Bézier curve length and quarter circle."""
    getcontext().prec = 60

    # Compute pi using Gauss-Legendre (Brent-Salamin) iteration
    a = Decimal(1)
    b = Decimal(1) / Decimal(2).sqrt()
    t_val = Decimal(1) / Decimal(4)
    p = Decimal(1)

    for _ in range(7):
        a_next = (a + b) / Decimal(2)
        b_next = (a * b).sqrt()
        t_val = t_val - p * (a - a_next) * (a - a_next)
        p = Decimal(2) * p
        a, b = a_next, b_next

    pi = (a + b) * (a + b) / (Decimal(4) * t_val)

    # Exact parameter v satisfying enclosed Area(v) = pi / 4
    # Area(v) = (10 + 12v - 3v^2) / 20 = pi / 4 => 3v^2 - 12v + (5*pi - 10) = 0
    v = Decimal(2) - ((Decimal(22) - Decimal(5) * pi) / Decimal(3)).sqrt()

    # Gauss-Legendre quadrature nodes and weights for n=64
    def legendre_quadrature(n: int = 64):
        nodes = []
        weights = []
        for i in range(1, n + 1):
            x = Decimal(str(cos(math_pi * (i - 0.25) / (n + 0.5))))
            for _ in range(30):
                p0 = Decimal(1)
                p1 = x
                for k in range(1, n):
                    p2 = (
                        Decimal(2 * k + 1) * x * p1 - Decimal(k) * p0
                    ) / Decimal(k + 1)
                    p0 = p1
                    p1 = p2
                dp = Decimal(n) * (x * p1 - p0) / (x * x - Decimal(1))
                x_next = x - p1 / dp
                if abs(x_next - x) < Decimal("1e-45"):
                    x = x_next
                    break
                x = x_next
            w = Decimal(2) / ((Decimal(1) - x * x) * (dp * dp))
            nodes.append(x)
            weights.append(w)
        return nodes, weights

    nodes, weights = legendre_quadrature(64)

    # Parametric velocity magnitude sqrt(x'(t)^2 + y'(t)^2)
    def speed(t: Decimal) -> Decimal:
        dx = (
            Decimal(3)
            * t
            * ((Decimal(2) - Decimal(3) * v) * t + Decimal(2) * v - Decimal(2))
        )
        t_opp = Decimal(1) - t
        dy = (
            -Decimal(3)
            * t_opp
            * (
                (Decimal(2) - Decimal(3) * v) * t_opp
                + Decimal(2) * v
                - Decimal(2)
            )
        )
        return (dx * dx + dy * dy).sqrt()

    # Arc length L = int_0^1 speed(t) dt
    arc_length = Decimal(0)
    for x, w in zip(nodes, weights):
        t = (x + Decimal(1)) / Decimal(2)
        arc_length += w * speed(t)
    arc_length /= Decimal(2)

    # Difference percentage 100 * (L - pi/2) / (pi/2)
    quarter_circle = pi / Decimal(2)
    diff_pct = Decimal(100) * (arc_length - quarter_circle) / quarter_circle

    return f"{diff_pct:.{precision_digits}f}"


if __name__ == "__main__":
    print(solve())
