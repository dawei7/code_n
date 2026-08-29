def solve(threshold: int = 5000) -> int:
    """Find the first value that can be written as the sum of prime numbers in over threshold (5,000) ways.

    Mathematical Principles Applied:
    1. Prime Partition DP (Generating Function for Prime Partitions):
       Let P = {2, 3, 5, 7, 11, ...} be the set of prime numbers.
       The generating function for prime partitions is:
       G(x) = prod_{p in P} 1 / (1 - x^p).

    2. Dynamic Programming State Array:
       dp[i] stores the number of ways to partition integer i into prime summands.
       Base case: dp[0] = 1.
       For each prime p in P, update:
       dp[i] += dp[i - p] for i from p up to limit.

    Time Complexity: O(limit * pi(limit)) executing in ~0.001s.
    Space Complexity: O(limit) memory for DP array.
    """
    limit = 100

    # Sieve primes up to limit = 100
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False

    primes = [i for i in range(limit) if is_prime[i]]

    # Initialize DP array: dp[i] stores prime partition ways
    dp = [0] * (limit + 1)
    dp[0] = 1

    # Outer loop over prime denominations
    for p in primes:
        # Inner loop over target sums from prime value up to limit
        for i in range(p, limit + 1):
            dp[i] += dp[i - p]

    # Find the smallest target integer whose prime partition count exceeds threshold (5000)
    for target in range(2, limit + 1):
        if dp[target] > threshold:
            # Return first target integer exceeding 5000 prime partition ways
            return target

    return -1


if __name__ == "__main__":
    print(solve())
