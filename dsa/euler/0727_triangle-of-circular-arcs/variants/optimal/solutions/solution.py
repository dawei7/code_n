"""Project Euler Problem 727: Triangle of Circular Arcs.

Find E(d) rounded to 8 decimal places, where d is the distance between the circumcentre of the
tangency triangle and the centre of the inner Soddy incircle for mutually tangent circles with
radii 1 <= ra < rb < rc <= 100 and gcd(ra, rb, rc) = 1.
"""

import math


def _distance_de(ra: int, rb: int, rc: int) -> float:
    k1 = 1.0 / ra
    k2 = 1.0 / rb
    k3 = 1.0 / rc
    k4 = k1 + k2 + k3 + 2.0 * math.sqrt(k1 * k2 + k2 * k3 + k3 * k1)
    r4 = 1.0 / k4

    d_ab = ra + rb
    ac = ra + rc
    bc = rb + rc

    xc = (ac * ac - bc * bc + d_ab * d_ab) / (2.0 * d_ab)
    yc = math.sqrt(max(0.0, ac * ac - xc * xc))

    # Tangency points
    tab_x, tab_y = float(ra), 0.0
    tac_x, tac_y = ra * xc / ac, ra * yc / ac
    tbc_x, tbc_y = d_ab + rb * (xc - d_ab) / bc, rb * yc / bc

    # Circumcenter D of tangency triangle
    det = 2.0 * (
        tab_x * (tac_y - tbc_y) + tac_x * (tbc_y - tab_y) + tbc_x * (tab_y - tac_y)
    )
    s1 = tab_x * tab_x + tab_y * tab_y
    s2 = tac_x * tac_x + tac_y * tac_y
    s3 = tbc_x * tbc_x + tbc_y * tbc_y
    dx = (s1 * (tac_y - tbc_y) + s2 * (tbc_y - tab_y) + s3 * (tab_y - tac_y)) / det
    dy = (s1 * (tbc_x - tac_x) + s2 * (tab_x - tbc_x) + s3 * (tac_x - tab_x)) / det

    # Incircle centre E (inner Soddy circle)
    ra_e = ra + r4
    rb_e = rb + r4
    xe = (ra_e * ra_e - rb_e * rb_e + d_ab * d_ab) / (2.0 * d_ab)
    ye = math.sqrt(max(0.0, ra_e * ra_e - xe * xe))

    target = rc + r4
    if abs(math.hypot(xe - xc, -ye - yc) - target) < 1e-8:
        ye = -ye

    return math.hypot(dx - xe, dy - ye)


def solve(limit: int = 100) -> str:
    """Compute E(d) over coprime triples (ra, rb, rc) with 1 <= ra < rb < rc <= limit."""
    total = 0.0
    comp = 0.0
    count = 0

    for ra in range(1, limit + 1):
        for rb in range(ra + 1, limit + 1):
            g_ab = math.gcd(ra, rb)
            for rc in range(rb + 1, limit + 1):
                if math.gcd(g_ab, rc) != 1:
                    continue
                count += 1
                d = _distance_de(ra, rb, rc)
                y = d - comp
                t = total + y
                comp = (t - total) - y
                total = t

    ans = total / count
    return f"{ans:.8f}"


if __name__ == "__main__":
    print(solve())
