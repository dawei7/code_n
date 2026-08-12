def solve(k: int = 10**9, target_count: int = 40) -> int:
    """Find sum of the first 40 prime factors of R(10^9).
    
    Time Complexity: O(Limit * log K)
    Space Complexity: O(Limit)
    """
    limit = 200000
    is_p = [True] * limit
    is_p[0] = is_p[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_p[i]:
            for j in range(i * i, limit, i):
                is_p[j] = False

    primes = [i for i in range(limit) if is_p[i]]

    prime_factors = []
    for p in primes:
        if p in (2, 5):
            continue

        mod = 9 * p if p == 3 else p
        if pow(10, k, mod) == 1:
            prime_factors.append(p)
            if len(prime_factors) == target_count:
                break

    return sum(prime_factors)
