def solve(limit: int = 1000000) -> int:
    """Find the numerator of the reduced proper fraction immediately to the left of 3/7 for d <= limit (1,000,000).

    Mathematical Principles Applied:
    1. Farey Sequence Properties & Diophantine Approximations:
       For a given denominator d <= 1,000,000, the largest numerator n < (3/7)*d is:
       n = floor( (3*d - 1) / 7 ).

    2. Maximizing n / d:
       The fraction closest to 3/7 occurs when d is as close to limit as possible
       such that (3d - 1) mod 7 is maximized.
       Scanning d in descending order from limit down to limit - 7 evaluates the maximal proper fraction.

    Time Complexity: O(1) over 7 denominator steps (executes in ~0.0000s).
    Space Complexity: O(1) constant auxiliary space.
    """
    target_num, target_den = 3, 7
    best_num, best_den = 0, 1

    # Scan the 7 largest denominators <= limit
    for d in range(limit, limit - 7, -1):
        # Calculate maximal integer numerator n strictly less than (3/7)*d
        n = (target_num * d - 1) // target_den

        # Compare fractions via cross-multiplication: n/d > best_num/best_den <=> n * best_den > best_num * d
        if n * best_den > best_num * d:
            best_num, best_den = n, d

    # Return numerator of the fraction immediately to the left of 3/7
    return best_num


if __name__ == "__main__":
    print(solve())
