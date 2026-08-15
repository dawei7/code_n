"""Project Euler Problem 372: Pencils of Rays.

Find the number of lattice points (x, y) with M < x <= N, M < y <= N
such that floor(y^2 / x^2) is odd, for M = 2*10^6 and N = 10^9.
"""

from decimal import Decimal, getcontext
from math import isqrt
from typing import List


def solve(min_val: int = 2000000, max_val: int = 1000000000) -> int:
    """Count lattice points satisfying floor(y^2 / x^2) is odd via Beatty sequence summation."""
    getcontext().prec = 60

    def sum_floor_alpha_x(alpha_dec: Decimal, n_val: int) -> int:
        """Compute sum_{x=1..n_val} floor(alpha * x) in O(log n_val) steps."""
        if n_val <= 0:
            return 0
        k_int = int(alpha_dec)
        res = k_int * n_val * (n_val + 1) // 2
        rem_alpha = alpha_dec - k_int
        if rem_alpha < Decimal("1e-35"):
            return res
        m_val = int(rem_alpha * n_val)
        if m_val == 0:
            return res
        return res + n_val * m_val - sum_floor_alpha_x(1 / rem_alpha, m_val)

    def sum_floor_range(alpha_dec: Decimal, x1: int, x2: int) -> int:
        if x1 > x2:
            return 0
        return sum_floor_alpha_x(alpha_dec, x2) - sum_floor_alpha_x(
            alpha_dec, x1 - 1
        )

    max_ratio = max_val / (min_val + 1)
    max_k = int(max_ratio * max_ratio) + 2

    total_lattice_points = 0

    # Iterate over odd integers k
    for k in range(1, max_k + 1, 2):
        sq_k = isqrt(k)
        is_sq_k = sq_k * sq_k == k

        sq_k1 = isqrt(k + 1)
        is_sq_k1 = sq_k1 * sq_k1 == k + 1

        alpha_dec = Decimal(k).sqrt()
        beta_dec = Decimal(k + 1).sqrt()

        c_alpha = 0 if is_sq_k else 1
        c_beta = 1 if is_sq_k1 else 0

        x_min = max(min_val + 1, int(Decimal(min_val) / beta_dec) + 1)
        x_max = min(max_val, int(Decimal(max_val) / alpha_dec))
        if x_min > x_max:
            continue

        p1 = int(Decimal(min_val + 1 - c_alpha) / alpha_dec)
        p2 = int(Decimal(max_val + c_beta) / beta_dec)

        cuts: List[int] = sorted(
            list(
                set(
                    [
                        x_min - 1,
                        x_max,
                        min(max(x_min - 1, p1), x_max),
                        min(max(x_min - 1, p2), x_max),
                    ]
                )
            )
        )

        for i in range(len(cuts) - 1):
            x1 = cuts[i] + 1
            x2 = cuts[i + 1]
            if x1 > x2:
                continue

            num_x = x2 - x1 + 1

            if x2 <= p2:
                sum_ymax = sum_floor_range(beta_dec, x1, x2) - c_beta * num_x
            else:
                sum_ymax = max_val * num_x

            if x2 <= p1:
                sum_ymin = (min_val + 1) * num_x
            else:
                sum_ymin = sum_floor_range(alpha_dec, x1, x2) + c_alpha * num_x

            diff = sum_ymax - sum_ymin + num_x
            if diff > 0:
                total_lattice_points += diff

    return total_lattice_points


if __name__ == "__main__":
    print(solve())
