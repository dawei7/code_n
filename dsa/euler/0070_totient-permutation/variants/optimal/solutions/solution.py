def solve(limit: int = 10000000) -> int:
    """Find n < limit for which phi(n) is a permutation of n and n/phi(n) is minimized.
    
    Time Complexity: O(P^2)
    Space Complexity: O(P)
    """
    # Primes near sqrt(10^7) ~ 3162
    sieve_limit = 5000
    is_prime = [True] * sieve_limit
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(sieve_limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, sieve_limit, i):
                is_prime[j] = False

    primes = [i for i in range(2000, sieve_limit) if is_prime[i]]

    min_ratio = float('inf')
    best_n = 0

    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            p1, p2 = primes[i], primes[j]
            n = p1 * p2
            if n >= limit:
                break
            phi = (p1 - 1) * (p2 - 1)
            ratio = n / phi

            if ratio < min_ratio:
                if sorted(str(n)) == sorted(str(phi)):
                    min_ratio = ratio
                    best_n = n

    return best_n
