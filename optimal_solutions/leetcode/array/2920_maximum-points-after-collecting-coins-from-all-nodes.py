import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

def solve(edges, coins, k):
    n = len(coins)
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Memoization table: (node, halving_count)
    # halving_count is capped at 13 because 10^9 // 2^14 is 0
    memo = {}

    def dfs(u, p, halving_count):
        # Cap halving_count at 13
        state = (u, halving_count)
        if state in memo:
            return memo[state]
        
        # Strategy 1: Take all coins, then halve descendants
        # Current value is coins[u] // (2^halving_count)
        val1 = (coins[u] >> halving_count) - k
        for v in adj[u]:
            if v != p:
                val1 += dfs(v, u, min(halving_count + 1, 13))
        
        # Strategy 2: Take half coins, no halving effect on descendants
        # Current value is (coins[u] // 2) // (2^halving_count)
        val2 = (coins[u] >> (halving_count + 1))
        for v in adj[u]:
            if v != p:
                val2 += dfs(v, u, min(halving_count, 13))
        
        res = max(val1, val2)
        memo[state] = res
        return res

    return dfs(0, -1, 0)
