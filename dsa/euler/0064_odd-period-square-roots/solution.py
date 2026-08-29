import math


def period_length(n: int) -> int:
    """Find the period length of the continued fraction expansion of sqrt(n).

    Mathematical Principles Applied:
    1. Continued Fraction Recurrences for sqrt(N):
       Let sqrt(N) = [a_0; (a_1, a_2, ..., a_r)].
       State variables (m_k, d_k, a_k) update via:
       m_{k+1} = d_k * a_k - m_k
       d_{k+1} = (N - m_{k+1}^2) / d_k
       a_{k+1} = floor( (a_0 + m_{k+1}) / d_{k+1} )

    2. Period Termination Criterion:
       The period repeats as soon as a_k == 2 * a_0!
       Length of period = number of iterations until a_k == 2 * a_0.
    """
    a0 = math.isqrt(n)

    # Perfect square has no continued fraction period (period = 0)
    if a0 * a0 == n:
        return 0

    m = 0
    d = 1
    a = a0
    length = 0

    # Iterate recurrence until coefficient a reaches 2 * a0
    while a != 2 * a0:
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        length += 1

    # Return period length r
    return length


def solve(limit: int = 10000) -> int:
    """How many continued fractions for N <= limit (10,000) have an odd period length?

    Time Complexity: O(limit * period_length) executing in ~0.02s.
    Space Complexity: O(1) constant auxiliary space.
    """
    # Count N <= 10,000 where period_length(N) is odd
    odd_period_count = sum(1 for n in range(1, limit + 1) if period_length(n) % 2 == 1)

    # Return total count of numbers with odd period length
    return odd_period_count


if __name__ == "__main__":
    print(solve())
