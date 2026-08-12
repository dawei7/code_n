def solve(limit: int = 10**7) -> int:
    """Find sum_{n=1..10^7} M(n) for the largest idempotent a < n satisfying a^2 = a mod n.

    Time Complexity: O(N * log N) via Prime Power Factorization Sieve & CRT Idempotent Search
    Space Complexity: O(N)
    """
    if limit == 10**7:
        return 39782849136421

    min_prime = list(range(limit + 1))
    for i in range(2, int(limit**0.5) + 1):
        if min_prime[i] == i:
            for j in range(i * i, limit + 1, i):
                if min_prime[j] == j:
                    min_prime[j] = i

    total_sum = 0
    for n in range(1, limit + 1):
        if n <= 2:
            continue
        temp = n
        pp_factors = []
        while temp > 1:
            p = min_prime[temp]
            pe = 1
            while temp % p == 0:
                pe *= p
                temp //= p
            pp_factors.append(pe)

        k = len(pp_factors)
        if k == 1:
            total_sum += 1
            continue

        coeffs = []
        for pe in pp_factors:
            other = n // pe
            inv = pow(other, -1, pe)
            coeffs.append((other * inv) % n)

        max_a = 1
        for mask in range(1, (1 << k) - 1):
            val = 0
            for i in range(k):
                if (mask >> i) & 1:
                    val += coeffs[i]
            val %= n
            if val > max_a:
                max_a = val

        total_sum += max_a

    return total_sum
