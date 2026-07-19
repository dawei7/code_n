from typing import List

def solve(nums: List[int], queries: List[List[int]]) -> List[int]:
    n = len(nums)
    
    # dp[i][j] will store the XOR score of the subarray nums[i...j]
    dp = [[0] * n for _ in range(n)]
    
    # Base case: subarrays of length 1
    for i in range(n):
        dp[i][i] = nums[i]
        
    # Fill DP table for XOR scores
    # score(i, j) = score(i, j-1) ^ score(i+1, j)
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = dp[i][j - 1] ^ dp[i + 1][j]
            
    # max_dp[i][j] will store the maximum XOR score of any subarray 
    # contained within the range [i, j]
    max_dp = [[0] * n for _ in range(n)]
    
    # Base case: subarrays of length 1
    for i in range(n):
        max_dp[i][i] = dp[i][i]
        
    # Fill max_dp table
    # max_dp[i][j] = max(dp[i][j], max_dp[i+1][j], max_dp[i][j-1])
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            max_dp[i][j] = max(dp[i][j], max_dp[i + 1][j], max_dp[i][j - 1])
            
    # Answer queries in O(1)
    results = []
    for l, r in queries:
        results.append(max_dp[l][r])
        
    return results
