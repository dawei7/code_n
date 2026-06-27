def solve(nums: list[int]) -> int:
    # The maximum value in nums is 300.
    # dp[v][d] stores the length of the longest subsequence ending with value v,
    # where the difference between the last two elements was d.
    # Since we need to track the "previous" difference to ensure the next one is smaller,
    # we define dp[v][d] as the max length ending at v with the *last* difference being d.
    
    MAX_VAL = 300
    # dp[last_val][diff]
    dp = [[0] * (MAX_VAL + 1) for _ in range(MAX_VAL + 1)]
    
    # Base case: any single element is a subsequence of length 1.
    # We use a separate array to track the max length ending at 'v' regardless of previous diff.
    max_len_ending_at = [1] * (MAX_VAL + 1)
    
    ans = 1
    
    for x in nums:
        # To form a new subsequence of length >= 2 ending at x:
        # We look for a previous value 'prev' and a previous difference 'd_old'
        # such that |x - prev| = d_new < d_old.
        
        # We update dp table for current x
        # We can iterate over all possible previous values 'prev'
        for prev in range(1, MAX_VAL + 1):
            d_new = abs(x - prev)
            
            # Option 1: Subsequence of length 2 (prev, x)
            # This is always possible if we have seen 'prev' before.
            if max_len_ending_at[prev] >= 1:
                dp[x][d_new] = max(dp[x][d_new], 2)
            
            # Option 2: Extend an existing subsequence ending at 'prev' with difference 'd_old'
            # where d_old > d_new
            for d_old in range(d_new + 1, MAX_VAL + 1):
                if dp[prev][d_old] > 0:
                    dp[x][d_new] = max(dp[x][d_new], dp[prev][d_old] + 1)
        
        # Update max_len_ending_at
        for d in range(MAX_VAL + 1):
            max_len_ending_at[x] = max(max_len_ending_at[x], dp[x][d])
        
        ans = max(ans, max_len_ending_at[x])
            
    return ans
