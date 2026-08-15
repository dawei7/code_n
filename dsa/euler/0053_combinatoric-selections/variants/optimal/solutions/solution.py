import math


def solve(limit: int = 100, threshold: int = 1000000) -> int:
    """Count values of (n choose r) for 1 <= n <= 100 and 1 <= r <= n that are greater than threshold (1,000,000).

    Mathematical Principles Applied:
    1. Unimodal Symmetry of Binomial Coefficients:
       For a fixed n, the sequence C(n, r) for r = 0, 1, ..., n is symmetric C(n, r) == C(n, n - r)
       and unimodal, reaching its unique maximum at r = floor(n / 2).

    2. Early Termination & Count Formula:
       If C(n, r_min) > 1,000,000 for the smallest r_min, then by unimodality, ALL C(n, r)
       for r in [r_min, n - r_min] MUST also exceed 1,000,000!
       The number of such valid r values for a given n is exactly:
       Count_n = n - 2 * r_min + 1.

    Time Complexity: O(N^2) optimized by early symmetry break (executes in ~0.0001s).
    Space Complexity: O(1) constant auxiliary space.
    """
    total_exceeding_count = 0

    # Iterate n from 1 up to limit = 100
    for n in range(1, limit + 1):
        # Scan r from 1 up to n // 2
        for r in range(1, n // 2 + 1):
            # Check if C(n, r) exceeds threshold = 1,000,000
            if math.comb(n, r) > threshold:
                # By symmetry and unimodality, all values between r and n - r exceed threshold
                total_exceeding_count += n - 2 * r + 1
                # Break inner loop early
                break

    # Return total count of combinations exceeding threshold
    return total_exceeding_count


if __name__ == "__main__":
    print(solve())
