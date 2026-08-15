"""Project Euler Problem 525: Rolling Ellipse.

Find C(1, 4) + C(3, 4) rounded to 8 decimal places, where C(a, b) is the length
of the path traced by the center of an ellipse E(a, b) rolling without slipping
for one complete turn.
"""

import math


def _center_arc_length(a: float, b: float, n_steps: int = 500000) -> float:
    """Compute arc length of ellipse center path using instantaneous center of rotation integration."""
    h = (math.pi / 2.0) / n_steps
    a2 = a * a
    b2 = b * b
    ab = a * b

    def integrand(theta: float) -> float:
        s = math.sin(theta)
        c = math.cos(theta)
        s2 = s * s
        c2 = c * c
        dist_to_center = math.sqrt(a2 * c2 + b2 * s2)
        dphi_dtheta = ab / (a2 * s2 + b2 * c2)
        return dist_to_center * dphi_dtheta

    total = integrand(0.0) + integrand(math.pi / 2.0)
    for i in range(1, n_steps):
        theta = i * h
        weight = 4.0 if i % 2 == 1 else 2.0
        total += weight * integrand(theta)

    quarter_arc = total * h / 3.0
    return 4.0 * quarter_arc


def solve(pairs=((1, 4), (3, 4))) -> str:
    """Compute sum of center curve lengths for given ellipse semiaxis pairs."""
    total_length = 0.0
    for a, b in pairs:
        total_length += _center_arc_length(float(a), float(b))

    return f"{total_length:.8f}"


if __name__ == "__main__":
    print(solve())
