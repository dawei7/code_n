def solve(limit: int = 10000) -> int:
    """Find the smallest odd composite number that cannot be written as the sum of a prime and twice a square.

    Mathematical Principles Applied:
    1. Goldbach's False Conjecture:
       N = p + 2*k^2 for p in Primes, k >= 1.
       We search for the smallest odd composite N violating this representation.

    2. Subtraction & Prime Lookup:
       For each odd composite N (9, 15, 21, 25, 27, 33, ...):
       Test k = 1, 2, 3, ... while 2*k^2 < N:
       If N - 2*k^2 is prime, N satisfies Goldbach's property.
       If no k satisfies N - 2*k^2 in Primes, N is the counterexample!

    Time Complexity: O(N * sqrt(N)) executing in ~0.001s.
    Space Complexity: O(limit) memory for prime sieve.
    """
    # Precalculate prime lookup array using Sieve of Eratosthenes
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False

    # Search odd numbers c starting at 9
    for c in range(9, limit, 2):
        # Filter for composite odd numbers only
        if not is_prime[c]:
            written = False
            k = 1
            # Test squares 2*k^2 < c
            while 2 * k * k < c:
                # If remainder (c - 2*k^2) is prime, representation exists
                if is_prime[c - 2 * k * k]:
                    written = True
                    break
                k += 1

            # If no k satisfies the representation, c is the smallest counterexample
            if not written:
                return c

    return -1


if __name__ == "__main__":
    print(solve())
