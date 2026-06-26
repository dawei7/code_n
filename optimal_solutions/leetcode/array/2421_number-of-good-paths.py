def solve(vals: list[int], edges: list[list[int]]) -> int:
    n = len(vals)
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # DSU structures
    parent = list(range(n))
    # count stores the frequency of the max value in the component
    count = [{vals[i]: 1} for i in range(n)]

    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            # Merge smaller component into larger one (or just merge)
            if len(count[root_i]) < len(count[root_j]):
                root_i, root_j = root_j, root_i
            
            parent[root_j] = root_i
            for val, freq in count[root_j].items():
                count[root_i][val] = count[root_i].get(val, 0) + freq
            count[root_j] = {} # Clear memory

    # Sort nodes by value
    nodes = sorted(range(n), key=lambda i: vals[i])
    
    ans = n  # Every single node is a good path of length 0
    
    # Process nodes in increasing order of values
    for u in nodes:
        for v in adj[u]:
            if vals[v] <= vals[u]:
                root_u = find(u)
                root_v = find(v)
                if root_u != root_v:
                    # Before merging, calculate paths formed by current value
                    # The number of new paths is (count of u in root_u) * (count of u in root_v)
                    c_u = count[root_u].get(vals[u], 0)
                    c_v = count[root_v].get(vals[u], 0)
                    ans += c_u * c_v
                    union(root_u, root_v)
                    
    return ans
