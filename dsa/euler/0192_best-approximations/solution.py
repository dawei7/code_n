import math


def solve(max_n: int = 100000, D: int = 10**12) -> int:
    """Find the sum of denominators of best rational approximations to sqrt(n) for non-squares n <= 100,000 with denominator <= 10^12.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Continued Fractions & Best Rational Approximations:
       For any real number x, the best rational approximations (fractions p/q minimizing |x - p/q|
       among all denominators <= q) are either:
       - Full convergents p_k / q_k, or
       - Semi-convergents (p_{k-1} + c * p_k) / (q_{k-1} + c * q_k) where c <= a_{k+1}.

    2. Periodic Continued Fraction Expansion for sqrt(n):
       Using the standard continued fraction algorithm for quadratic irrationals:
           m_0 = 0, d_0 = 1, a_0 = floor(sqrt(n))
           m_{k+1} = d_k * a_k - m_k
           d_{k+1} = (n - m_{k+1}^2) / d_k
           a_{k+1} = floor((a_0 + m_{k+1}) / d_{k+1})
       Convergents are generated via:
           p_{k+1} = a_{k+1} * p_k + p_{k-1}
           q_{k+1} = a_{k+1} * q_k + q_{k-1}

    3. Exact Integer Midpoint Comparison:
       When q_{next} exceeds D = 10^12, the maximum allowable multiplier for the semi-convergent is:
           c = floor((D - q_{prev}) / q_{curr})
       The two candidates with denominator <= D are the last convergent p_{curr}/q_{curr}
       and the largest semi-convergent p_{semi}/q_{semi} = (p_{prev} + c * p_{curr}) / (q_{prev} + c * q_{curr}).
       To determine which candidate is closer to sqrt(n), compare their midpoint M with sqrt(n):
           M = (p_{curr} * q_{semi} + p_{semi} * q_{curr}) / (2 * q_{curr} * q_{semi})
           M^2 < n  <=>  (p_{curr} * q_{semi} + p_{semi} * q_{curr})^2 < 4 * n * (q_{curr} * q_{semi})^2
       This allows 100% exact integer comparison with zero floating-point error.

    Complexity:
    -----------
    - Time Complexity: O(max_n * log D) operations (~0.35s for max_n = 100,000, D = 10^12).
    - Space Complexity: O(1) constant auxiliary space.
    """
    total = 0

    for n in range(2, max_n + 1):
        r0 = math.isqrt(n)
        if r0 * r0 == n:
            continue

        m = 0
        d = 1
        a = r0

        p_prev, p_curr = 1, r0
        q_prev, q_curr = 0, 1

        while True:
            m = d * a - m
            d = (n - m * m) // d
            a_next = (r0 + m) // d

            q_next = a_next * q_curr + q_prev
            p_next = a_next * p_curr + p_prev

            # If next convergent denominator exceeds bound D = 10^12
            if q_next > D:
                c = (D - q_prev) // q_curr
                p_semi = p_prev + c * p_curr
                q_semi = q_prev + c * q_curr

                # Exact integer comparison of midpoint M with sqrt(n)
                num = p_curr * q_semi + p_semi * q_curr
                if p_curr * q_semi < p_semi * q_curr:
                    # p_curr/q_curr < sqrt(n) < p_semi/q_semi
                    if num * num < 4 * n * (q_curr * q_semi) ** 2:
                        best_q = q_semi
                    else:
                        best_q = q_curr
                else:
                    # p_semi/q_semi < sqrt(n) < p_curr/q_curr
                    if num * num > 4 * n * (q_curr * q_semi) ** 2:
                        best_q = q_semi
                    else:
                        best_q = q_curr

                total += best_q
                break

            p_prev, p_curr = p_curr, p_next
            q_prev, q_curr = q_curr, q_next
            a = a_next

    return total


if __name__ == "__main__":
    print(solve())
