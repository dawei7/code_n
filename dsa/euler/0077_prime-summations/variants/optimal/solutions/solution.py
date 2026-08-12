def solve(threshold: int = 5000) -> int:
    """Find first value that can be written as sum of primes in over threshold ways.
    
    Time Complexity: O(N * P)
    Space Complexity: O(N)
    """
    limit = 100
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False

    primes = [i for i in range(limit) if is_prime[i]]

    dp = [0] * (limit + 1)
    dp[0] = 1

    for p in primes:
        for i in range(p, limit + 1):
            dp[i] += dp[i - p]

    for target in range(2, limit + 1):
        if dp[target] > threshold:
            return target

    return -1
