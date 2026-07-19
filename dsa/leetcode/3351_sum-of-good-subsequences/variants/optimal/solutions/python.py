def solve(nums: list[int]) -> int:
    MOD = 10**9 + 7
    
    # count[x] stores the number of good subsequences ending with value x
    # total_sum[x] stores the sum of all good subsequences ending with value x
    count = {}
    total_sum = {}
    
    for x in nums:
        # A new subsequence can start with x itself
        c_x = 1
        s_x = x
        
        # Extend existing subsequences ending in x-1
        if (x - 1) in count:
            c_x = (c_x + count[x - 1]) % MOD
            s_x = (s_x + total_sum[x - 1] + count[x - 1] * x) % MOD
            
        # Extend existing subsequences ending in x+1
        if (x + 1) in count:
            c_x = (c_x + count[x + 1]) % MOD
            s_x = (s_x + total_sum[x + 1] + count[x + 1] * x) % MOD
            
        # Update the DP tables
        count[x] = (count.get(x, 0) + c_x) % MOD
        total_sum[x] = (total_sum.get(x, 0) + s_x) % MOD
        
    return sum(total_sum.values()) % MOD
