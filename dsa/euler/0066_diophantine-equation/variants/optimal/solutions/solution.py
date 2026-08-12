import math


def minimal_pell_x(d: int) -> int:
    """Find minimal integer x solving Pell's Equation x^2 - d*y^2 = 1 via continued fraction convergents."""
    a0 = math.isqrt(d)
    if a0 * a0 == d:
        return 0

    m, m_prev = 0, 0
    den, den_prev = 1, 1
    a = a0

    p_prev, p = 1, a0
    q_prev, q = 0, 1

    while p * p - d * q * q != 1:
        m = den * a - m
        den = (d - m * m) // den
        a = (a0 + m) // den

        p_prev, p = p, a * p + p_prev
        q_prev, q = q, a * q + q_prev

    return p


def solve(limit: int = 1000) -> int:
    """Find D <= limit in minimal solutions of x^2 - D*y^2 = 1 for which largest x is obtained.
    
    Time Complexity: O(limit * P)
    Space Complexity: O(1)
    """
    max_x = 0
    best_d = 0

    for d in range(2, limit + 1):
        x = minimal_pell_x(d)
        if x > max_x:
            max_x = x
            best_d = d

    return best_d
