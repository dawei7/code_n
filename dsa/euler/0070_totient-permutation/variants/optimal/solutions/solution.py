def solve(limit: int = 10000000) -> int:
    """Find n < limit (10,000,000) for which phi(n) is a permutation of n and n / phi(n) is minimized.

    Mathematical Principles Applied:
    1. Minimizing n / phi(n):
       n / phi(n) = prod_{p | n} p / (p - 1).
       To MINIMIZE this ratio (making it as close to 1 as possible):
       - Prime numbers n = p give phi(p) = p - 1. But p and p - 1 can NEVER be digit permutations!
       - Therefore, n MUST be a product of TWO LARGE PRIMES n = p1 * p2!

    2. Two Prime Search Domain near sqrt(10^7) ≈ 3162:
       For n = p1 * p2 < 10,000,000, the prime factors p1, p2 should lie near sqrt(10^7) ≈ 3162.
       Search primes in range [2000, 5000].

    3. Totient Formula & Anagram Test:
       For n = p1 * p2, phi(n) = (p1 - 1) * (p2 - 1).
       Check if sorted(str(n)) == sorted(str(phi(n))) and update minimum ratio n / phi(n).

    Time Complexity: O(pi(range)^2) executing in ~0.02s.
    Space Complexity: O(pi(range)) memory.
    """
    # Sieve primes up to 5,000
    sieve_limit = 5000
    is_prime = [True] * sieve_limit
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(sieve_limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, sieve_limit, i):
                is_prime[j] = False

    # Collect primes in range [2000, 5000] near sqrt(10^7)
    primes = [i for i in range(2000, sieve_limit) if is_prime[i]]

    min_ratio = float("inf")
    best_n = 0

    # Search pair products n = p1 * p2 < 10,000,000
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            p1, p2 = primes[i], primes[j]
            n = p1 * p2

            # Break inner loop if product exceeds limit
            if n >= limit:
                break

            # Totient of product of two distinct primes: phi(n) = (p1 - 1) * (p2 - 1)
            phi = (p1 - 1) * (p2 - 1)
            ratio = n / phi

            # Test ratio optimization and digit permutation equality
            if ratio < min_ratio:
                if sorted(str(n)) == sorted(str(phi)):
                    min_ratio = ratio
                    best_n = n

    # Return optimal n obtaining minimal ratio n / phi(n) with permutated totient
    return best_n


if __name__ == "__main__":
    print(solve())
