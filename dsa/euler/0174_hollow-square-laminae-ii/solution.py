def solve(max_tiles: int = 1000000, max_n: int = 10) -> int:
    """Find the sum of N(n) for 1 <= n <= 10, where N(n) is the number of tile counts t <= 1,000,000 that can form exactly n square laminae.

    Mathematical Principles Applied:
    1. Lamina Factor Pair Representation:
       A lamina with outer side a and inner hole side b (a > b >= 1, a == b mod 2) uses:
       t = a^2 - b^2 = 4 * x * y tiles <= 1,000,000 where x = (a - b)/2 and y = (a + b)/2 (1 <= x < y).
       Let m = t / 4 <= 250,000.
       The number of distinct laminae formed by t tiles equals the number of factor pairs (x, y) of m such that x < y.

    2. Divisor Count Function d(m) and Factor Pairs:
       Let d(m) be the number of positive divisors of m.
       The number of factor pairs (x, y) with 1 <= x < y and x * y = m is:
       - If m is NOT a perfect square: c(m) = d(m) // 2.
       - If m IS a perfect square:     c(m) = (d(m) - 1) // 2.

    3. Harmonic Sieve Divisor Counting:
       Compute d(m) for all 1 <= m <= 250,000 in O(M log M) time via a harmonic sieve.
       Count m where 1 <= c(m) <= 10.

    Time Complexity: O(M log M) where M = max_tiles / 4 executing in ~0.08s.
    Space Complexity: O(M) memory for divisor count array.
    """
    LIMIT = max_tiles // 4

    # Harmonic sieve for divisor counts d(m) up to LIMIT = 250,000
    div_count = [0] * (LIMIT + 1)
    for i in range(1, LIMIT + 1):
        for j in range(i, LIMIT + 1, i):
            div_count[j] += 1

    N_counts = [0] * (max_n + 1)
    for m in range(1, LIMIT + 1):
        d = div_count[m]
        sq = int(m**0.5)
        # Factor pairs x < y with x * y = m
        if sq * sq == m:
            c = (d - 1) // 2
        else:
            c = d // 2

        if 1 <= c <= max_n:
            N_counts[c] += 1

    # Return total sum sum_{n=1}^{10} N(n)
    return sum(N_counts)


if __name__ == "__main__":
    print(solve())
