def is_prime(n: int) -> bool:
    """Fast wheel primality test for cuban prime candidates."""
    if n < 2:
        return False
    if n in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29):
        return True
    if any(n % p == 0 for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)):
        return False
    d = 5
    while d * d <= n:
        if n % d == 0 or n % (d + 2) == 0:
            return False
        d += 6
    return True


def solve(limit: int = 1000000) -> int:
    """Find the number of primes p < limit (1,000,000) for which there exists an integer n such that n^3 + n^2 * p is a perfect cube.

    Mathematical Principles Applied:
    1. Algebraic Reduction to Cuban Primes:
       Let n^3 + n^2 * p = m^3 for integers n, m.
       n^2 * (n + p) = m^3.
       Since p is prime and gcd(n, n+p) divides p:
       n MUST be a perfect cube n = k^3, and (n + p) = (k + 1)^3.

    2. Difference of Consecutive Cubes Formula:
       p = (k + 1)^3 - k^3 = 3*k^2 + 3*k + 1.
       Primes of the form p = 3*k^2 + 3*k + 1 are known as Cuban Primes!

    3. Search Space Bound:
       Since p = 3*k^2 + 3*k + 1 < 1,000,000:
       k <= sqrt(1,000,000 / 3) approx 577.
       We only need to test primality of 3*k^2 + 3*k + 1 for k = 1 to 577.

    Time Complexity: O(sqrt(limit)) executing in ~0.0001s.
    Space Complexity: O(1) constant auxiliary space.
    """
    count = 0
    k = 1

    # Loop integer k upwards until p = 3*k^2 + 3*k + 1 >= 1,000,000
    while True:
        p = 3 * k * k + 3 * k + 1
        if p >= limit:
            break

        # Check if cuban prime candidate p is prime
        if is_prime(p):
            count += 1

        k += 1

    # Return total count of qualifying primes p < 1,000,000
    return count


if __name__ == "__main__":
    print(solve())
