def solve(limit: int = 1000000) -> int:
    """Find the value of n <= limit (1,000,000) for which n / phi(n) is maximized.

    Mathematical Principles Applied:
    1. Euler's Totient Product Formula:
       phi(n) = n * prod_{p | n} (1 - 1/p) = n * prod_{p | n} (p - 1)/p.
       Therefore, the ratio n / phi(n) equals:
       n / phi(n) = prod_{p | n} p / (p - 1).

    2. Maximizing n / phi(n):
       To maximize the product prod_{p | n} p / (p - 1), we MUST include as many distinct SMALL prime factors as possible!
       For each prime p, the ratio p / (p - 1) > 1, and smaller primes p yield strictly larger ratios (e.g. 2/1 > 3/2 > 5/4 > 7/6).

    3. Primorial Product n_max:
       The optimal n <= limit is the product of consecutive primes starting from 2:
       n = 2 * 3 * 5 * 7 * 11 * 13 * 17 = 510,510 <= 1,000,000.
       Multiplying by the next prime 19 exceeds 1,000,000 (510510 * 19 = 9,699,690 > 10^6).

    Time Complexity: O(1) constant time execution in ~0.0000s.
    Space Complexity: O(1) constant auxiliary space.
    """
    # Consecutive prime factors starting from 2
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    n = 1
    # Multiply consecutive primes while product n <= limit
    for p in primes:
        if n * p > limit:
            break
        n *= p

    # Return primorial number n obtaining maximum n / phi(n)
    return n


if __name__ == "__main__":
    print(solve())
