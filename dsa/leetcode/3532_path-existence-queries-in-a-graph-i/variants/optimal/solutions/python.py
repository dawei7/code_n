def solve(n: int, edges: list[list[int]], queries: list[list[int]]) -> list[bool]:
    parent = list(range(n))
    
    def find(i: int) -> int:
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]
    
    def union(i: int, j: int) -> None:
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j
            
    for u, v in edges:
        union(u, v)
        
    results = []
    for u, v in queries:
        results.append(find(u) == find(v))
        
    return results
