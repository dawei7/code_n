def solve(n: int, edges: list[list[int]], query: list[list[int]]) -> list[int]:
    parent = list(range(n))
    size = [1] * n

    def find(node: int) -> int:
        while node != parent[node]:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    for u, v, _ in edges:
        root_u = find(u)
        root_v = find(v)
        if root_u == root_v:
            continue
        if size[root_u] < size[root_v]:
            root_u, root_v = root_v, root_u
        parent[root_v] = root_u
        size[root_u] += size[root_v]

    component_cost = [-1] * n
    for u, _, weight in edges:
        component_cost[find(u)] &= weight

    answer = []
    for start, target in query:
        root = find(start)
        answer.append(component_cost[root] if root == find(target) else -1)
    return answer
