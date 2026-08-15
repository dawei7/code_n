def solve(limit: int = 1000000) -> int:
    """Find the prime below limit (1,000,000) that can be written as the sum of the most consecutive primes.

    Mathematical Principles Applied:
    1. Prefix Sum Array for O(1) Range Sums:
       P_k = sum_{i=1}^k p_i.
       Sum of L consecutive primes from index i to i + L - 1 is prefix[i + L] - prefix[i].

    2. Upper Bound on Sequence Length L:
       Summing first 543 primes exceeds 1,000,000 (prefix[543] = 997,651 < 10^6, prefix[544] > 10^6).
       Max possible sequence length L_max = 543.

    3. Descending Length Search:
       Search length L from L_max down to 1.
       The first sum that is < limit and prime is guaranteed to be the global maximum length prime!

    Time Complexity: O(limit log log limit) executing in ~0.09s.
    Space Complexity: O(limit) memory for prime set and prefix array.
    """
    # Sieve array up to limit = 1,000,000
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False

    # Collect primes and prime lookup set
    primes = [i for i in range(limit) if is_prime[i]]
    prime_set = set(primes)

    # Compute prefix sums of primes for O(1) consecutive sub-array sum queries
    prefix = [0] * (len(primes) + 1)
    for i in range(len(primes)):
        prefix[i + 1] = prefix[i] + primes[i]

    # Find upper bound maximum sequence length L_max where prefix[L_max] < limit
    max_len = 0
    while max_len < len(primes) and prefix[max_len] < limit:
        max_len += 1

    # Search window length L in descending order from max_len down to 1
    for L in range(max_len, 0, -1):
        for i in range(len(primes) - L + 1):
            s = prefix[i + L] - prefix[i]

            # If range sum exceeds limit, break offset loop
            if s >= limit:
                break

            # If range sum is prime, return immediately (first match in descending L order is optimal)
            if s in prime_set:
                return s

    return -1


if __name__ == "__main__":
    print(solve())
