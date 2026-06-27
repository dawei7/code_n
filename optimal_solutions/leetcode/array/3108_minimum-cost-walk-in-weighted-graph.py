def solve(n: int, edges: list[list[int]], query: list[list[int]]) -> list[int]:
    parent = list(range(n))
    # Initialize AND values with all bits set (using -1 as a mask of all 1s)
    and_val = [-1] * n

    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j, weight):
        root_i = find(i)
        root_j = find(j)
        
        # Update the AND value of the component
        new_and = and_val[root_i] & and_val[root_j] & weight
        
        if root_i != root_j:
            parent[root_i] = root_j
            and_val[root_j] = new_and
        else:
            and_val[root_i] = new_and

    for u, v, w in edges:
        union(u, v, w)

    results = []
    for start, end in query:
        if start == end:
            results.append(0)
            continue
            
        root_s = find(start)
        root_e = find(end)
        
        if root_s != root_e:
            results.append(-1)
        else:
            results.append(and_val[root_s])
            
    return results
