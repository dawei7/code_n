import collections

def solve(n: int, edges: list[list[int]], price: list[int], trips: list[list[int]]) -> int:
    adj = collections.defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    freq = [0] * n
    
    def get_path(curr, target, parent, path):
        path.append(curr)
        if curr == target:
            return True
        for neighbor in adj[curr]:
            if neighbor != parent:
                if get_path(neighbor, target, curr, path):
                    return True
        path.pop()
        return False
    
    for start, end in trips:
        path = []
        get_path(start, end, -1, path)
        for node in path:
            freq[node] += 1
            
    # dp[u][0]: min cost for subtree u, u is NOT halved
    # dp[u][1]: min cost for subtree u, u IS halved
    memo = {}
    
    def dfs(u, p):
        cost0 = price[u] * freq[u]
        cost1 = (price[u] // 2) * freq[u]
        
        for v in adj[u]:
            if v == p:
                continue
            c0, c1 = dfs(v, u)
            cost0 += min(c0, c1)
            cost1 += c0
            
        return cost0, cost1
    
    res0, res1 = dfs(0, -1)
    return min(res0, res1)
