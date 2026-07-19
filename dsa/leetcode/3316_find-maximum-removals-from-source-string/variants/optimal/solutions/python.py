def solve(source: str, pattern: str, targetIndices: list[int]) -> int:
    n = len(source)
    m = len(pattern)
    
    # Create a set for O(1) lookup of removable indices
    removable = [False] * n
    for idx in targetIndices:
        removable[idx] = True
        
    # dp[i][j] = max removals using first i chars of source to match first j of pattern
    # Initialize with -1 to represent unreachable states
    dp = [[-1] * (m + 1) for _ in range(n + 1)]
    
    # Base case: 0 chars of pattern matched using 0 chars of source
    dp[0][0] = 0
    
    for i in range(n):
        for j in range(m + 1):
            if dp[i][j] == -1:
                continue
            
            # Option 1: Remove source[i] if it is in targetIndices
            if removable[i]:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + 1)
            else:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
                
            # Option 2: Keep source[i] if it matches pattern[j]
            if j < m and source[i] == pattern[j]:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])
                
    return dp[n][m]
