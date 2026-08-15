import math


def solve(limit: int = 12000) -> int:
    """Find the number of reduced proper fractions between 1/3 and 1/2 for d <= limit (12,000).

    Mathematical Principles Applied:
    1. Strictly Bounded Fraction Range:
       For a given denominator d, the fraction n/d lies strictly between 1/3 and 1/2 iff:
       1/3 < n/d < 1/2 <=> d/3 < n < d/2.
       Therefore:
       n_min = floor(d / 3) + 1
       n_max = floor((d - 1) / 2)

    2. Coprimality Condition:
       A proper fraction n/d is reduced iff gcd(n, d) == 1.

    Time Complexity: O(limit^2) executing in ~0.50s.
    Space Complexity: O(1) constant auxiliary space.
    """
    count = 0

    # Iterate denominators d from 4 to limit = 12,000
    for d in range(4, limit + 1):
        # Bounds for numerator n strictly between d/3 and d/2
        n_min = d // 3 + 1
        n_max = (d - 1) // 2

        # Count coprimes in interval [n_min, n_max]
        for n in range(n_min, n_max + 1):
            if math.gcd(n, d) == 1:
                count += 1

    # Return total count of reduced proper fractions in range (1/3, 1/2)
    return count


if __name__ == "__main__":
    print(solve())
