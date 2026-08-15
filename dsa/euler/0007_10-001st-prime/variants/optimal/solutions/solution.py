def solve(n: int = 10001) -> int:
    """Find the nth prime number using a Sieve of Eratosthenes.

    Mathematical Principles Applied:
    1. Prime Number Theorem (PNT) & Upper Bound Estimation:
       By Dusart's inequality for p_n (the n-th prime):
       p_n < n * (ln n + ln ln n) for n >= 6.
       For n = 10,001, p_10001 < 10001 * (9.2104 + 2.2203) ≈ 114,318.
       Setting limit = 120,000 strictly guarantees that p_10001 <= limit.

    2. Sieve of Eratosthenes:
       Construct a boolean array up to limit = 120,000.
       Iterate through primes starting from 2, marking multiples i*i, i*(i+1), ... as composite.
       Count encountered prime numbers until the n-th prime is reached.

    Time Complexity: O(L log log L) where L = 120,000 (executes in ~0.013s).
    Space Complexity: O(L) bit/boolean array auxiliary space.
    """
    # Upper bound estimate for the 10,001st prime number
    limit = 120000

    # Allocate boolean sieve array (True = prime candidate, False = composite)
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False

    # Track count of prime numbers encountered so far
    count = 0

    # Execute Sieve of Eratosthenes while counting primes
    for i in range(2, limit):
        if is_prime[i]:
            count += 1

            # If this is the n-th prime, return it immediately
            if count == n:
                return i

            # Mark all multiples starting from i * i as composite (False)
            for j in range(i * i, limit, i):
                is_prime[j] = False

    # Return -1 if limit was insufficient (not reached for valid bounds)
    return -1


if __name__ == "__main__":
    print(solve())
