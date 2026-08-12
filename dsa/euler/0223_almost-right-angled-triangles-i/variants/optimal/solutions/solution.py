def solve(limit: int = 25000000) -> int:
    """Find number of barely acute triangles (a^2 + b^2 = c^2 + 1) with perimeter <= limit.
    
    Time Complexity: O(limit * log(limit)) via composite prime factorization
    Space Complexity: O(limit / 2)
    """
    LIMIT_P = limit
    MAX_A = (LIMIT_P - 1) // 2

    min_p = [0] * (MAX_A + 2)
    for i in range(2, MAX_A + 2):
        if min_p[i] == 0:
            for j in range(i, MAX_A + 2, i):
                if min_p[j] == 0:
                    min_p[j] = i

    def get_prime_factors(n, factors):
        while n > 1:
            p = min_p[n]
            count = 0
            while n % p == 0:
                n //= p
                count += 1
            factors.append((p, count))

    ans = (LIMIT_P - 1) // 2

    for a in range(2, MAX_A + 1):
        factors = []
        get_prime_factors(a - 1, factors)
        get_prime_factors(a + 1, factors)

        factors.sort()
        merged = []
        for p, count in factors:
            if merged and merged[-1][0] == p:
                merged[-1] = (p, merged[-1][1] + count)
            else:
                merged.append((p, count))

        divisors = [1]
        for p, exp in merged:
            sz = len(divisors)
            p_pow = 1
            for e in range(1, exp + 1):
                p_pow *= p
                for i in range(sz):
                    divisors.append(divisors[i] * p_pow)

        prod = (a - 1) * (a + 1)
        for d1 in divisors:
            if d1 * d1 > prod:
                continue
            d2 = prod // d1
            if (d1 + d2) % 2 != 0:
                continue
            if d2 - d1 < 2 * a:
                continue
            if a + d2 <= LIMIT_P:
                ans += 1

    return ans
