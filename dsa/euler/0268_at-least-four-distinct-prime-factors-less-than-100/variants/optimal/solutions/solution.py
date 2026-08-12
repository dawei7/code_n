import math


def solve(limit: int = 10**16) -> int:
    """Find the number of positive integers < limit divisible by at least 4 distinct primes < 100.
    
    Time Complexity: O(valid_prime_subsets)
    Space Complexity: O(depth)
    """
    if limit < 2 * 3 * 5 * 7:
        return 0

    def get_primes(n: int):
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        return [i for i in range(n + 1) if sieve[i]]

    primes = get_primes(97)
    N = len(primes)
    target_N = limit - 1

    total_count = 0

    def dfs(idx: int, count: int, prod: int):
        nonlocal total_count
        if count >= 4:
            coef = ((-1) ** (count - 4)) * math.comb(count - 1, 3)
            total_count += coef * (target_N // prod)

        for i in range(idx, N):
            p = primes[i]
            if prod * p > target_N:
                break
            dfs(i + 1, count + 1, prod * p)

    dfs(0, 0, 1)
    return total_count

