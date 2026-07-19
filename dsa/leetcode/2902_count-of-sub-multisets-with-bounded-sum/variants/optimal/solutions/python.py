from collections import Counter

def solve(nums: list[int], l: int, r: int) -> int:
    MOD = 10**9 + 7

    # Count frequencies of each number
    counts = Counter(nums)

    # dp[i] stores the number of ways to get sum i
    dp = [0] * (r + 1)
    dp[0] = 1

    # Current maximum possible sum reachable so far
    current_max = 0

    for val, count in counts.items():
        if val == 0:
            # Zeros can be included in any sub-multiset
            # If there are 'z' zeros, each existing sub-multiset can be
            # combined with any subset of zeros (2^z ways)
            for i in range(r + 1):
                dp[i] = (dp[i] * (count + 1)) % MOD
            continue

        new_dp = list(dp)
        # Sliding window sum to update DP table
        # For a value 'val' with 'count' occurrences:
        # dp[i] = sum(dp[i - k * val]) for 0 <= k <= count
        for i in range(val, r + 1):
            new_dp[i] = (new_dp[i] + new_dp[i - val]) % MOD
            if i >= (count + 1) * val:
                new_dp[i] = (new_dp[i] - dp[i - (count + 1) * val] + MOD) % MOD
        dp = new_dp

    # The result is the sum of ways to get sums from l to r
    return sum(dp[l : r + 1]) % MOD
