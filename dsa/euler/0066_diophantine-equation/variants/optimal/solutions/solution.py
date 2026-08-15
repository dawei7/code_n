import math


def minimal_pell_x(d: int) -> int:
    """Find the minimal integer x solving Pell's Equation x^2 - D*y^2 = 1 using continued fraction convergents.

    Mathematical Principles Applied:
    1. Pell's Equation x^2 - D*y^2 = 1:
       By Lagrange's Theorem, the fundamental (minimal) solution (x_1, y_1) to Pell's Equation
       is always a convergent p_k / q_k of the continued fraction expansion of sqrt(D).

    2. Continued Fraction Recurrence for sqrt(D):
       State variables (m_k, den_k, a_k) update via:
       m_{k+1} = den_k * a_k - m_k
       den_{k+1} = (D - m_{k+1}^2) / den_k
       a_{k+1} = floor( (a_0 + m_{k+1}) / den_{k+1} )

    3. Convergent Numerators and Denominators:
       p_k = a_k * p_{k-1} + p_{k-2}
       q_k = a_k * q_{k-1} + q_{k-2}
       Termination occurs when p^2 - D*q^2 == 1.
    """
    a0 = math.isqrt(d)

    # Perfect squares D have no non-trivial solutions
    if a0 * a0 == d:
        return 0

    m = 0
    den = 1
    a = a0

    # Initial convergents p_0 / q_0 and p_1 / q_1
    p_prev, p = 1, a0
    q_prev, q = 0, 1

    # Loop until fundamental solution p^2 - d*q^2 == 1 is reached
    while p * p - d * q * q != 1:
        m = den * a - m
        den = (d - m * m) // den
        a = (a0 + m) // den

        # Advance convergent numerators and denominators
        p_prev, p = p, a * p + p_prev
        q_prev, q = q, a * q + q_prev

    # Return minimal solution x = p
    return p


def solve(limit: int = 1000) -> int:
    """Find D <= limit (1,000) for which the minimal solution x in x^2 - D*y^2 = 1 is maximized.

    Time Complexity: O(limit * period_length) executing in ~0.015s.
    Space Complexity: O(1) constant auxiliary space.
    """
    max_x = 0
    best_d = 0

    # Scan D from 2 up to limit = 1000
    for d in range(2, limit + 1):
        x = minimal_pell_x(d)

        # Update maximum x and corresponding D value
        if x > max_x:
            max_x = x
            best_d = d

    # Return value of D obtaining largest minimal x solution
    return best_d


if __name__ == "__main__":
    print(solve())
