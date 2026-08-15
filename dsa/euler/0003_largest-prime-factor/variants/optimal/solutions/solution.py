def solve(n: int = 600851475143) -> int:
    """Find the largest prime factor of n using wheel trial division.

    Mathematical Principles Applied:
    1. Fundamental Theorem of Arithmetic:
       Every integer n > 1 can be uniquely factorized into prime powers:
       n = p_1^{e_1} * p_2^{e_2} * ... * p_k^{e_k}

    2. Square Root Bound:
       If a composite integer n has a non-trivial factor, at least one prime factor
       must be <= sqrt(n). If no factor <= sqrt(n) exists, n itself is prime.

    3. Consecutive Division (Reduction):
       Whenever a divisor d divides n, we repeatedly divide n by d until d no longer
       divides n. This removes all multiples of d from n, ensuring that subsequent
       divisors found are strictly prime numbers.

    4. Odd Step Wheel Optimization:
       We handle d = 2 separately, then increment d by 2 (d = 3, 5, 7, 9, ...)
       skipping all even candidate divisors.

    Time Complexity: O(sqrt(p_max)) where p_max is the largest prime factor.
    Space Complexity: O(1) constant auxiliary space.
    """
    # Track the largest prime factor encountered
    max_factor = 1

    # Candidate divisor starting at 2
    d = 2

    # Loop while d * d <= n (since composite numbers must have a prime factor <= sqrt(n))
    while d * d <= n:
        # If d divides n, d is guaranteed to be prime (earlier composite multiples were removed)
        if n % d == 0:
            max_factor = d
            # Repeatedly divide n by d to fully remove factor d
            while n % d == 0:
                n //= d

        # Step optimization: increment by 1 if d == 2, otherwise by 2 to skip even numbers
        d += 1 if d == 2 else 2

    # If n > 1 after trial division, the remaining value of n is itself prime and is the largest factor
    if n > 1:
        max_factor = n

    # Return the largest prime factor
    return max_factor


if __name__ == "__main__":
    print(solve())
