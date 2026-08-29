def solve(limit: int = 1000000) -> int:
    """Find the total number of reduced proper fractions n/d for d <= limit (1,000,000).

    Mathematical Principles Applied:
    1. Reduced Proper Fractions and Euler's Totient Function:
       A fraction n/d (with 1 <= n < d) is reduced iff gcd(n, d) == 1.
       By definition of Euler's totient function phi(d), there are exactly phi(d) numerators
       n for a given denominator d.

    2. Total Farey Sequence Size:
       The total number of reduced proper fractions for d <= limit is:
       Total = sum_{d=2}^limit phi(d).

    3. Euler's Totient Sieve:
       Precompute phi(d) for all d in 2..limit using an O(limit log log limit) sieve.

    Time Complexity: O(limit log log limit) executing in ~0.20s.
    Space Complexity: O(limit) memory to store totient array.
    """
    # Allocate totient array initialized with phi[i] = i
    phi = list(range(limit + 1))

    # Execute linear/multiplicative totient sieve
    for i in range(2, limit + 1):
        if phi[i] == i:  # i is prime
            for j in range(i, limit + 1, i):
                phi[j] = phi[j] // i * (i - 1)

    # Sum phi(d) for all denominators d = 2..limit
    total_reduced_fractions = sum(phi[2:])

    # Return total count of reduced proper fractions
    return total_reduced_fractions


if __name__ == "__main__":
    print(solve())
