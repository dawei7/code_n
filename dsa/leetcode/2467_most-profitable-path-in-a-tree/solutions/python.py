import collections

def solve(edges, bob, amount):
    n = len(amount)
    adj = collections.defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Find Bob's path to root (0)
    bob_time = {bob: 0}
    parent = {0: -1}
    stack = [0]
    
    # Build parent pointers to trace Bob's path
    q = collections.deque([0])
    visited = {0}
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                parent[v] = u
                q.append(v)
    
    curr = bob
    time = 0
    while curr != 0:
        curr = parent[curr]
        time += 1
        bob_time[curr] = time
        
    # Alice's DFS
    max_profit = float('-inf')
    
    def dfs(u, p, time, current_income):
        nonlocal max_profit
        
        # Calculate income at current node
        if u not in bob_time or time < bob_time[u]:
            current_income += amount[u]
        elif time == bob_time[u]:
            current_income += amount[u] // 2
            
        # Check if leaf
        is_leaf = True
        for v in adj[u]:
            if v != p:
                is_leaf = False
                dfs(v, u, time + 1, current_income)
        
        if is_leaf:
            max_profit = max(max_profit, current_income)
            
    dfs(0, -1, 0, 0)
    return max_profit
