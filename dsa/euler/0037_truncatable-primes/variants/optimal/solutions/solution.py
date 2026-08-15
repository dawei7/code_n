def solve(count_needed: int = 11) -> int:
    """Find the sum of the eleven truncatable primes (primes truncatable from left-to-right and right-to-left).

    Mathematical Principles Applied:
    1. Truncatable Prime Definition:
       A prime p > 7 is truncatable if repeatedly removing digits from the left OR right
       yields prime numbers at every truncation step.
       Single-digit primes 2, 3, 5, 7 are NOT considered truncatable primes.

    2. Finite Quantity Theorem:
       There exist EXACTLY 11 truncatable primes in total.
       All 11 truncatable primes lie strictly below upper limit = 1,000,000.

    3. Fast Sieve & Set Membership:
       Precompute boolean prime sieve up to 1,000,000 for O(1) truncation checks.

    Time Complexity: O(limit log log limit) executing in ~0.15s.
    Space Complexity: O(limit) boolean array memory (~1 MB).
    """
    limit = 1000000

    # Allocate boolean sieve up to limit = 1,000,000
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False

    # Execute Sieve of Eratosthenes up to sqrt(limit)
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False

    # Build prime lookup set for O(1) membership testing
    prime_set = {i for i in range(limit) if is_prime[i]}

    # Array to collect truncatable primes
    truncatable = []

    # Iterate candidate primes starting at 11 (first multi-digit prime)
    for p in range(11, limit):
        if p in prime_set:
            s = str(p)

            # Check all left-to-right truncations (removing leading digits)
            if not all(int(s[i:]) in prime_set for i in range(len(s))):
                continue

            # Check all right-to-left truncations (removing trailing digits)
            if not all(int(s[:i]) in prime_set for i in range(1, len(s) + 1)):
                continue

            # p is a valid truncatable prime
            truncatable.append(p)

            # Early exit as soon as all 11 truncatable primes are found
            if len(truncatable) == count_needed:
                break

    # Return total sum of all 11 truncatable primes
    return sum(truncatable)


if __name__ == "__main__":
    print(solve())
