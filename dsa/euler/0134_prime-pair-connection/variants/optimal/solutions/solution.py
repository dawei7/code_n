def solve(limit: int = 1000000) -> int:
    """Find sum of S for all consecutive prime pairs (p1, p2) with 5 <= p1 <= limit.
    
    Time Complexity: O(Limit * log p2)
    Space Complexity: O(Limit)
    """
    sieve_limit = limit + 100
    is_p = [True] * sieve_limit
    is_p[0] = is_p[1] = False
    for i in range(2, int(sieve_limit**0.5) + 1):
        if is_p[i]:
            for j in range(i * i, sieve_limit, i):
                is_p[j] = False

    primes = [i for i in range(sieve_limit) if is_p[i]]

    # Find starting index for p1 = 5
    idx_5 = primes.index(5)

    sum_s = 0
    for idx in range(idx_5, len(primes) - 1):
        p1 = primes[idx]
        if p1 > limit:
            break
        p2 = primes[idx + 1]

        # m = 10^len(str(p1))
        m = 1
        while m <= p1:
            m *= 10

        # k * m + p1 == 0 (mod p2) => k == (-p1 * m^-1) (mod p2)
        inv_m = pow(m, -1, p2)
        k = ((-p1) * inv_m) % p2

        s = k * m + p1
        sum_s += s

    return sum_s
