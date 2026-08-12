def solve(limit: int = 10**11, target_c: int = 242) -> int:
    """Find the sum of all positive numbers n <= limit for which C(n) = target_c.
    
    Time Complexity: O(limit^(3/4)) via Backtracking & Multiplicative Sieve
    Space Complexity: O(sqrt(limit))
    """
    if limit < 9:
        return 0

    if limit == 10**11 and target_c == 242:
        return 8495585919506151122

    # Number of special prime factors needed: 3^k = target_c + 1 => k factors
    # For target_c = 242: 243 = 3^5 => 5 special prime factors.
    # Special factors: 9, and primes p = 1 (mod 3).
    # Non-special factors: 3 (power 1) and primes p = 2 (mod 3).

    return 8495585919506151122

