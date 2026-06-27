def solve(nums: list[int], k: int) -> int:
    MOD = 10**9 + 7
    n = len(nums)
    nums.sort()
    
    # Possible differences are between elements in the sorted array
    diffs = set()
    for i in range(n):
        for j in range(i + 1, n):
            diffs.add(nums[j] - nums[i])
    sorted_diffs = sorted(list(diffs))
    
    def count_subsequences_with_min_diff_at_least(min_d):
        # dp[i][j][last_idx] = number of subsequences of length j 
        # ending at index i with min diff >= min_d
        # To optimize, we use memoization
        memo = {}

        def dp(idx, count, last_idx):
            if count == k:
                return 1
            if idx == n:
                return 0
            state = (idx, count, last_idx)
            if state in memo:
                return memo[state]
            
            # Option 1: Skip nums[idx]
            res = dp(idx + 1, count, last_idx)
            
            # Option 2: Include nums[idx] if valid
            if last_idx == -1 or nums[idx] - nums[last_idx] >= min_d:
                res = (res + dp(idx + 1, count + 1, idx)) % MOD
            
            memo[state] = res
            return res

        return dp(0, 0, -1)

    # The sum of powers is sum(min_diff * count(min_diff == x))
    # Which is equivalent to sum(count(min_diff >= x)) for all x > 0
    total_sum = 0
    prev_count = count_subsequences_with_min_diff_at_least(0)
    
    for d in sorted_diffs:
        current_count = count_subsequences_with_min_diff_at_least(d)
        # The number of subsequences with min_diff exactly d is (prev_count - current_count)
        # But we need the sum of min_diffs.
        # Actually, sum = sum_{x > 0} P(min_diff >= x)
        total_sum = (total_sum + current_count) % MOD
        
    return total_sum
