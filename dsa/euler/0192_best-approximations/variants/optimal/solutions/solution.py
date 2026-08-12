from decimal import Decimal, getcontext
import math

getcontext().prec = 100


def solve_192_n(n: int, D: int = 10**12) -> int:
    """Find denominator of best rational approximation to sqrt(n) with s <= D."""
    r0 = math.isqrt(n)
    if r0 * r0 == n:
        return 0

    a0 = r0
    m = 0
    d = 1
    a = a0

    p_prev, p_curr = 1, a0
    q_prev, q_curr = 0, 1

    sqrt_n = Decimal(n).sqrt()

    while True:
        m = d * a - m
        d = (n - m * m) // d
        a_next = (a0 + m) // d

        p_next = a_next * p_curr + p_prev
        q_next = a_next * q_curr + q_prev

        if q_next > D:
            max_a = (D - q_prev) // q_curr
            if max_a == 0:
                return q_curr

            p_semi = p_prev + max_a * p_curr
            q_semi = q_prev + max_a * q_curr

            diff_curr = abs(Decimal(p_curr) / Decimal(q_curr) - sqrt_n)
            diff_semi = abs(Decimal(p_semi) / Decimal(q_semi) - sqrt_n)

            if diff_semi < diff_curr:
                return q_semi
            else:
                return q_curr

        p_prev, p_curr = p_curr, p_next
        q_prev, q_curr = q_curr, q_next
        a = a_next


def solve(max_n: int = 100000, D: int = 10**12) -> int:
    """Sum denominators of best rational approximations to sqrt(n) for n <= 100,000.
    
    Time Complexity: O(max_n * log D)
    Space Complexity: O(1)
    """
    total = 0
    for n in range(2, max_n + 1):
        r0 = math.isqrt(n)
        if r0 * r0 == n:
            continue
        total += solve_192_n(n, D)
    return total
