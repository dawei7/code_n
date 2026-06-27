import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

def solve(parent, s):
    n = len(parent)
    adj = [[] for _ in range(n)]
    for i in range(1, n):
        adj[parent[i]].append(i)
    
    # Sort children to ensure consistent DFS order
    for i in range(n):
        adj[i].sort()
        
    tin = [0] * n
    tout = [0] * n
    timer = 0
    dfs_order = []
    
    def dfs(u):
        nonlocal timer
        tin[u] = timer
        timer += 1
        dfs_order.append(s[u])
        for v in adj[u]:
            dfs(v)
        tout[u] = timer - 1
        
    dfs(0)
    
    # Rolling Hash parameters
    P = 131
    MOD = (1 << 61) - 1
    
    pow_p = [1] * (n + 1)
    for i in range(1, n + 1):
        pow_p[i] = (pow_p[i - 1] * P) % MOD
        
    pref = [0] * (n + 1)
    suff = [0] * (n + 1)
    
    for i in range(n):
        val = ord(dfs_order[i]) - ord('a') + 1
        pref[i + 1] = (pref[i] * P + val) % MOD
        
    for i in range(n - 1, -1, -1):
        val = ord(dfs_order[i]) - ord('a') + 1
        suff[i] = (suff[i + 1] * P + val) % MOD
        
    def get_hash_pref(l, r):
        return (pref[r + 1] - pref[l] * pow_p[r - l + 1]) % MOD
        
    def get_hash_suff(l, r):
        return (suff[l] - suff[r + 1] * pow_p[r - l + 1]) % MOD
        
    res = [False] * n
    for i in range(n):
        l, r = tin[i], tout[i]
        if get_hash_pref(l, r) == get_hash_suff(l, r):
            res[i] = True
            
    return res
