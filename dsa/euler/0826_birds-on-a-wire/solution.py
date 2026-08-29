def solve(limit: int = 1000000) -> str:
    """Find average of F(n) for odd primes n < 10^6.

    Linear prime sieve and Dirichlet order statistic expectation loop.

    Time Complexity: O(limit)
    Space Complexity: O(limit)
    """
    # Linear prime sieve for odd primes < limit
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False

    odd_primes = [p for p in range(3, limit) if is_prime[p]]

    # Dirichlet order statistic expected painted length F(p) for each odd prime
    total_F = 0.0
    for p in odd_primes:
        # F(p) = (7p + 15) / (18(p + 1))
        fp = (7 * p + 15) / (18 * (p + 1))
        total_F += fp

    # Pure dynamic prime average calculation
    avg = total_F / len(odd_primes)
    return f"{avg:.10f}"


if __name__ == "__main__":
    print(solve())
