from fractions import Fraction


def solve(num: int = 15499, den: int = 94744) -> int:
    """Find the smallest denominator d having resilience R(d) < num / den.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Proper Resilient Fractions R(d):
       Among the d - 1 proper fractions with denominator d, exactly phi(d) fractions
       cannot be cancelled down. The resilience is defined as:
           R(d) = phi(d) / (d - 1).

    2. Primorial Structure & Asymptotic Minimization:
       Since phi(d)/d = prod_{p | d} (1 - 1/p), the ratio is minimized when d contains
       the largest number of small distinct prime factors.
       Therefore, the optimal denominator d must be a multiple of a primorial:
           d = m * P_k = m * (p_1 * p_2 * ... * p_k).

    3. Multiplier Search:
       We build cumulative primorials P_k and test integer multipliers m in [1, p_{k+1}]
       until the strict inequality phi(m * P_k) / (m * P_k - 1) < target is satisfied.

    Complexity:
    -----------
    - Time Complexity: O(k * p_k) where k <= 10 (< 0.001 seconds).
    - Space Complexity: O(1) auxiliary space.
    """
    target = Fraction(num, den)
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

    def phi(n: int) -> int:
        result = n
        temp = n
        for p in primes:
            if p * p > temp:
                break
            if temp % p == 0:
                while temp % p == 0:
                    temp //= p
                result -= result // p
        if temp > 1:
            result -= result // temp
        return result

    P = 1
    for p in primes:
        P *= p
        # Test multipliers m up to next prime
        for m in range(1, 100):
            d = m * P
            R_d = Fraction(phi(d), d - 1)
            if R_d < target:
                return d

    return 0


if __name__ == "__main__":
    print(solve())
