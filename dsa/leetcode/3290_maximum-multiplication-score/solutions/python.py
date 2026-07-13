def solve(a: list[int], b: list[int]) -> int:
    # dp[k] stores the maximum score using the first k+1 elements of a
    # Initialize with a very small number to handle negative products
    inf = float('inf')
    dp = [-inf, -inf, -inf, -inf]
    
    for val in b:
        # Update dp[3]: max score using all 4 elements of a
        # It is either the previous dp[3] or the best dp[2] + a[3]*val
        dp[3] = max(dp[3], dp[2] + a[3] * val)
        
        # Update dp[2]: max score using first 3 elements of a
        dp[2] = max(dp[2], dp[1] + a[2] * val)
        
        # Update dp[1]: max score using first 2 elements of a
        dp[1] = max(dp[1], dp[0] + a[1] * val)
        
        # Update dp[0]: max score using first element of a
        dp[0] = max(dp[0], a[0] * val)
        
    return int(dp[3])
