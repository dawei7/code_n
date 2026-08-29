"""Project Euler Problem 449: Chocolate Covered Candy.

Find the volume of chocolate in mm^3 required to cover an ellipsoid of revolution
b^2 x^2 + b^2 y^2 + a^2 z^2 = a^2 b^2 with a uniform layer 1 mm thick,
where a = 3 mm and b = 1 mm, rounded to 8 decimal places.
"""

from math import atan, atanh, pi, sqrt


def solve(
    a: float = 3.0, b: float = 1.0, t: float = 1.0, n_layers: int = 1000
) -> str:
    """Compute the parallel outer volume V(t) - V_0 via differential geometry and layer quadrature."""
    if abs(a - b) < 1e-14:
        s_area = 4.0 * pi * a * a
        m_curv = 4.0 * pi * a
    elif a > b:
        # Oblate spheroid
        e = sqrt(1.0 - (b * b) / (a * a))
        s_area = 2.0 * pi * a * a * (1.0 + (b * b / (a * a)) * (atanh(e) / e))
        m_curv = 2.0 * pi * b + (2.0 * pi * a / e) * atan((a * e) / b)
    else:
        # Prolate spheroid
        e = sqrt(1.0 - (a * a) / (b * b))
        s_area = 2.0 * pi * a * a * (1.0 + (b / a) * (atanh(e) / e))
        m_curv = 2.0 * pi * b + (2.0 * pi * a * a / (b * e)) * atanh(e)

    # Integrate layer surface area S(r) = S + 2*M*r + 4*pi*r^2 across r in [0, t]
    dr = t / n_layers
    vol = 0.0
    for i in range(n_layers + 1):
        r = i * dr
        area_r = s_area + 2.0 * m_curv * r + 4.0 * pi * r * r
        weight = (
            1 if (i == 0 or i == n_layers) else (4 if (i & 1) == 1 else 2)
        )
        vol += weight * area_r
    vol *= dr / 3.0

    return f"{vol:.8f}"


if __name__ == "__main__":
    print(solve())
