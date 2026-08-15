def solve(target: int = 500) -> int:
    """Find the first triangle number to have strictly over target divisors.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Triangular Numbers:
       The n-th triangular number is defined as:
           T_n = sum_{k=1}^n k = n * (n + 1) // 2

    2. Coprimality & Multiplicativity of Divisor Function d(m):
       Because gcd(n, n + 1) = 1, dividing the even factor by 2 preserves coprimality:
       - For even n: gcd(n // 2, n + 1) = 1 => d(T_n) = d(n // 2) * d(n + 1)
       - For odd n:  gcd(n, (n + 1) // 2) = 1 => d(T_n) = d(n) * d((n + 1) // 2)

    3. Divisor Count via Prime Factorization:
       If m = p_1^{e_1} * p_2^{e_2} * ... * p_k^{e_k}, then:
           d(m) = (e_1 + 1) * (e_2 + 1) * ... * (e_k + 1)

    Complexity:
    -----------
    - Time Complexity: O(n * sqrt(n)) where n ≈ 12,375 (terminates in ~0.04s).
    - Space Complexity: O(1) constant auxiliary memory.
    """

    def count_divisors(m: int) -> int:
        """Compute the number of divisors d(m) via trial division factorization."""
        total_divisors = 1
        d = 2
        temp = m
        while d * d <= temp:
            if temp % d == 0:
                exp = 0
                while temp % d == 0:
                    exp += 1
                    temp //= d
                total_divisors *= exp + 1
            d += 1
        if temp > 1:
            total_divisors *= 2
        return total_divisors

    n = 1
    while True:
        # Evaluate d(T_n) using coprimality split
        if n % 2 == 0:
            total_divs = count_divisors(n // 2) * count_divisors(n + 1)
        else:
            total_divs = count_divisors(n) * count_divisors((n + 1) // 2)

        if total_divs > target:
            return n * (n + 1) // 2

        n += 1


if __name__ == "__main__":
    print(solve())
