def solve(limit: int = 10000000) -> int:
    """Find the number of primitive integer-sided triangles with perimeter <= 10^7.
    
    Time Complexity: O(limit) via Alcuin's Sequence & Mobius Inversion
    Space Complexity: O(limit)
    """

    def sieve_mobius(n):
        mu = [0] * (n + 1)
        primes = []
        is_p = [True] * (n + 1)
        mu[1] = 1
        for i in range(2, n + 1):
            if is_p[i]:
                primes.append(i)
                mu[i] = -1
            for p in primes:
                if i * p > n:
                    break
                is_p[i * p] = False
                if i % p == 0:
                    mu[i * p] = 0
                    break
                else:
                    mu[i * p] = -mu[i]
        return mu

    mu = sieve_mobius(limit)

    def T(p):
        if p % 2 == 0:
            return (p * p + 24) // 48
        else:
            return ((p + 3) * (p + 3) + 24) // 48

    S_arr = [0] * (limit + 1)
    curr = 0
    for p in range(1, limit + 1):
        curr += T(p)
        S_arr[p] = curr

    ans = 0
    for k in range(1, limit + 1):
        if mu[k] != 0:
            ans += mu[k] * S_arr[limit // k]

    return ans
