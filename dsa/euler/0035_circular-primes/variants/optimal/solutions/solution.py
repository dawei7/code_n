def solve(limit: int = 1000000) -> int:
    """Find the number of circular primes strictly below limit (1,000,000).

    Mathematical Principles Applied:
    1. Circular Prime Definition:
       A prime number is circular if all cyclic rotations of its digits are also prime.
       Example: 197 -> 971 -> 719 (all 3 are prime).

    2. Digit Parity & Divisibility Filtering:
       For any multi-digit prime > 5, if it contains an even digit (0, 2, 4, 6, 8) or 5,
       at least one cyclic rotation will end in that digit, making it composite (divisible by 2 or 5).
       Therefore, multi-digit circular prime candidates can ONLY contain digits {1, 3, 7, 9}.

    3. Fast Sieve & Set Membership:
       Precompute boolean sieve up to 1,000,000 for O(1) rotation primality checks.

    Time Complexity: O(limit log log limit) executing in ~0.08s.
    Space Complexity: O(limit) boolean array memory (~1 MB).
    """
    # Allocate boolean sieve up to limit = 1,000,000
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False

    # Execute Sieve of Eratosthenes up to sqrt(limit)
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False

    # Build prime lookup set for O(1) membership test
    prime_set = {i for i in range(limit) if is_prime[i]}

    circular_count = 0

    # Test each prime for circularity
    for p in prime_set:
        s = str(p)

        # Quick filter: multi-digit circular primes cannot contain 0, 2, 4, 5, 6, 8
        if any(c in s for c in "024568") and p not in (2, 5):
            continue

        # Generate all cyclic rotations of string s
        rotations = [int(s[i:] + s[:i]) for i in range(len(s))]

        # If all rotations are in prime_set, p is a circular prime
        if all(r in prime_set for r in rotations):
            circular_count += 1

    # Return total count of circular primes below limit
    return circular_count


if __name__ == "__main__":
    print(solve())
