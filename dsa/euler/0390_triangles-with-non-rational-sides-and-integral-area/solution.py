"""Project Euler Problem 390: Triangles with Non Rational Sides and Integral Area.

Find S(10^10), the sum of the areas of all triangles with sides sqrt(1+b^2), sqrt(1+c^2), sqrt(b^2+c^2)
having integral area <= 10^10.
"""

from typing import List, Tuple


def solve(limit: int = 10**10) -> int:
    """Compute S(limit) using symmetric branching tree of generalized Pell equations."""
    # Find upper bound on p: 8p^3 + p <= limit
    p_max = int((limit / 8.0) ** (1 / 3.0)) + 2
    while 8 * p_max**3 + p_max > limit:
        p_max -= 1

    total_area = 0
    # Stack stores (p, q, A)
    stack: List[Tuple[int, int, int]] = [
        (p, 0, p) for p in range(1, p_max + 1)
    ]

    while stack:
        p, q, a_curr = stack.pop()

        a_coeff = 8 * p * p + 1
        b_coeff = 4 * p
        c_coeff = 4 * p * (4 * p * p + 1)

        # Pell transformation step
        q_new = a_coeff * q + b_coeff * a_curr
        a_new = c_coeff * q + a_coeff * a_curr

        if a_new > limit:
            continue

        total_area += a_new

        # Branch along the same p sequence and symmetric coordinates
        stack.append((p, q_new, a_new))
        stack.append((q_new, p, a_new))
        stack.append((q_new, -p, a_new))

    return total_area


if __name__ == "__main__":
    print(solve())
