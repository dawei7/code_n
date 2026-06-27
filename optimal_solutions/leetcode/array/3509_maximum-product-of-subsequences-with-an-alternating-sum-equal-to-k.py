def solve(nums, k):
    MOD = 10**9 + 7
    n = len(nums)
    
    # dp[sum][parity] stores the maximum product found so far.
    # Since we need the maximum product, we store the actual value.
    # To handle large products, we use a dictionary or array.
    # Given the constraints, we use a DP table: dp[current_sum][parity]
    # parity 0: next element added is subtracted (even index in subsequence)
    # parity 1: next element added is added (odd index in subsequence)
    
    # Using a dictionary to store {sum: max_product} for each parity
    # dp[parity][sum] = max_product
    dp = [{}, {}]
    dp[0][0] = 1
    
    for x in nums:
        new_dp = [dp[0].copy(), dp[1].copy()]
        
        # Case 1: Add x as an even-indexed element (subtract)
        # Current parity is 0, becomes 1
        for s, prod in dp[0].items():
            new_s = s - x
            new_prod = prod * x
            if new_s not in new_dp[1] or new_prod > new_dp[1][new_s]:
                new_dp[1][new_s] = new_prod
                
        # Case 2: Add x as an odd-indexed element (add)
        # Current parity is 1, becomes 0
        for s, prod in dp[1].items():
            new_s = s + x
            new_prod = prod * x
            if new_s not in new_dp[0] or new_prod > new_dp[0][new_s]:
                new_dp[0][new_s] = new_prod
        
        dp = new_dp

    # The problem asks for alternating sum = k.
    # An alternating sum is (a1 - a0 + a3 - a2 + ...).
    # This is equivalent to sum of elements at odd indices - sum of elements at even indices.
    # Our DP state parity 0 means we just finished an odd-indexed element (or started).
    # The result is in dp[0][k] if we consider the sequence length.
    
    res = dp[0].get(k, -1)
    return res % MOD if res != -1 else -1
