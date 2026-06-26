import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

def solve(n: int, edges: list[list[int]], price: list[int]) -> int:
    if n == 1:
        return 0
    
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # dp[u][0]: max path sum starting at u going down into subtree
    # dp[u][1]: max path sum starting at u going down into subtree, excluding price[u]
    dp = [[0, 0] for _ in range(n)]
    ans = 0
    
    def dfs(u, p):
        nonlocal ans
        dp[u][0] = price[u]
        dp[u][1] = 0
        
        max1, max2 = 0, 0 # max1: max path sum, max2: max path sum excluding root
        
        for v in adj[u]:
            if v == p:
                continue
            dfs(v, u)
            
            # The path can be:
            # 1. Path ending at u (price[u] + dp[v][0])
            # 2. Path ending at u (price[u] + dp[v][1])
            # We update global answer
            ans = max(ans, dp[u][0] + dp[v][1], dp[u][1] + dp[v][0])
            
            dp[u][0] = max(dp[u][0], price[u] + dp[v][0])
            dp[u][1] = max(dp[u][1], price[u] + dp[v][1], dp[v][0])
            
    dfs(0, -1)
    return ans
