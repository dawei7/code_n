def solve(
    n: int,
    edgeList: list[list[int]],
    queries: list[list[int]],
) -> list[bool]:
    parent = list(range(n))
    size = [1] * n

    def find(node: int) -> int:
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    def union(first: int, second: int) -> None:
        first_root = find(first)
        second_root = find(second)
        if first_root == second_root:
            return
        if size[first_root] < size[second_root]:
            first_root, second_root = second_root, first_root
        parent[second_root] = first_root
        size[first_root] += size[second_root]

    edges = sorted(edgeList, key=lambda edge: edge[2])
    ordered_queries = sorted(
        (limit, first, second, index)
        for index, (first, second, limit) in enumerate(queries)
    )
    answers = [False] * len(queries)
    edge_index = 0

    for limit, first, second, query_index in ordered_queries:
        while edge_index < len(edges) and edges[edge_index][2] < limit:
            union(edges[edge_index][0], edges[edge_index][1])
            edge_index += 1
        answers[query_index] = find(first) == find(second)

    return answers
