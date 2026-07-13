def solve(nums: list[int], k: int) -> int:
    MOD = 10**9 + 7
    n = len(nums)
    total_sum = sum(nums)
    
    # If the total sum is less than 2*k, no partition can satisfy the condition
    if total_sum < 2 * k:
        return 0
    
    # dp[i] will store the number of subsets that sum up to i
    dp = [0] * k
    dp[0] = 1
    
    for x in nums:
        for j in range(k - 1, x - 1, -1):
            dp[j] = (dp[j] + dp[j - x]) % MOD
            
    # The number of subsets with sum < k
    bad_subsets_count = sum(dp) % MOD
    
    # Total ways to form subsets is 2^n.
    # A partition is invalid if one subset has sum < k.
    # Since total_sum >= 2*k, it's impossible for both subsets to be < k.
    # Thus, we subtract 2 * bad_subsets_count from 2^n.
    # We also exclude the empty set and the full set cases if necessary,
    # but the problem implies non-empty subsets.
    
    total_ways = pow(2, n, MOD)
    # Subtract the cases where one subset is < k (multiplied by 2 for both sides)
    ans = (total_ways - 2 * bad_subsets_count) % MOD
    
    return ans
