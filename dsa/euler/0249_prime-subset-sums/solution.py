def solve(limit: int = 5000, mod: int = 10**16) -> int:
    """Find the number of subsets of primes < limit whose element sum is a prime number, modulo 10^16.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Prime Subset Generating Function:
       Let S = {p_1, p_2, ..., p_k} be the set of all primes less than limit.
       The generating function for subset sums is:
           G(x) = prod_{p in S} (1 + x^p).
       The coefficient of x^s in G(x) gives the number of subsets of S summing to s.

    2. Dynamic Programming Knapsack Progression:
       Starting from dp[0] = 1, for each prime p in S:
           dp[s + p] = (dp[s + p] + dp[s]) mod 10^16  (for s descending from curr_max to 0).

    3. Prime Sum Accumulation:
       We sieve all primes up to the maximum possible sum S_max = sum(S) = 1,548,136.
       The final answer is:
           Answer = sum_{q prime, q <= S_max} dp[q] mod 10^16.

    Complexity:
    -----------
    - Time Complexity: O(|S| * sum(S)) where |S| = 669 primes.
    - Space Complexity: O(sum(S)) array of size ~1.55 MB.
    """
    if limit <= 2:
        return 0

    def get_primes(n: int) -> list[int]:
        sieve = bytearray([1]) * (n + 1)
        sieve[0] = sieve[1] = 0
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                sieve[i * i : n + 1 : i] = bytearray(
                    len(range(i * i, n + 1, i))
                )
        return [i for i, v in enumerate(sieve) if v]

    primes_in_set = get_primes(limit - 1)
    if not primes_in_set:
        return 0

    max_sum = sum(primes_in_set)

    sieve_sum = bytearray([1]) * (max_sum + 1)
    sieve_sum[0] = sieve_sum[1] = 0
    for i in range(2, int(max_sum**0.5) + 1):
        if sieve_sum[i]:
            sieve_sum[i * i : max_sum + 1 : i] = bytearray(
                len(range(i * i, max_sum + 1, i))
            )

    dp = [0] * (max_sum + 1)
    dp[0] = 1
    curr_max = 0

    for p in primes_in_set:
        for s in range(curr_max, -1, -1):
            v = dp[s]
            if v:
                sp = s + p
                nv = dp[sp] + v
                dp[sp] = nv if nv < mod else (nv % mod)
        curr_max += p

    ans = 0
    for s in range(2, max_sum + 1):
        if sieve_sum[s] and dp[s]:
            ans = (ans + dp[s]) % mod

    return ans


if __name__ == "__main__":
    print(solve())
