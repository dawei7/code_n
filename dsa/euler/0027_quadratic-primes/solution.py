def solve(limit: int = 1000) -> int:
    """Find the product a * b of coefficients for n^2 + an + b producing max consecutive primes from n = 0.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Base Case n = 0 (Primality of b):
       For n = 0, P(0) = 0^2 + a*0 + b = b.
       Since P(0) must be a prime number, b must be a positive prime:
           b in Primes, 2 <= b <= limit (168 prime candidates <= 1000).

    2. Case n = 1 (Parity of a):
       For n = 1, P(1) = 1 + a + b must be prime.
       For b > 2 (odd prime), 1 + b is even.
       For 1 + a + b to be odd (and thus prime), a must be an ODD integer.
       When b = 2, a + 3 is prime (so a must be even or a = -1).

    3. Fast Sieve Primality Lookup:
       Values of n^2 + an + b can reach up to 80^2 + 1000*80 + 1000 ≈ 87,400.
       A precomputed boolean prime sieve up to 200,000 provides O(1) primality tests.

    Complexity:
    -----------
    - Time Complexity: O(pi(limit) * limit * max_n) (~0.03s with sieve).
    - Space Complexity: O(M) where M = 200,000 boolean sieve array (~200 KB).
    """
    # Precompute boolean prime sieve up to 200,000
    sieve_limit = 200000
    is_prime_arr = bytearray([1]) * sieve_limit
    is_prime_arr[0] = is_prime_arr[1] = 0
    for i in range(2, int(sieve_limit**0.5) + 1):
        if is_prime_arr[i]:
            num_mult = len(range(i * i, sieve_limit, i))
            is_prime_arr[i * i : sieve_limit : i] = bytearray([0]) * num_mult

    def is_prime(v: int) -> bool:
        return v > 1 and v < sieve_limit and bool(is_prime_arr[v])

    # Prime candidates for b
    b_primes = [b for b in range(2, limit + 1) if is_prime(b)]

    max_consecutive = 0
    best_product = 0

    for b in b_primes:
        # Step of 2 for odd a when b is odd
        a_start = -limit + 1 if (b % 2 == 1) else -limit
        a_step = 2 if (b % 2 == 1) else 1
        for a in range(a_start, limit, a_step):
            n = 0
            while is_prime(n * n + a * n + b):
                n += 1

            if n > max_consecutive:
                max_consecutive = n
                best_product = a * b

    return best_product


if __name__ == "__main__":
    print(solve())
