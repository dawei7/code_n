def _count_components(n: int, edges: list[list[int]]) -> int:
    parent = list(range(n))
    size = [1] * n
    components = n

    def find(vertex: int) -> int:
        while vertex != parent[vertex]:
            parent[vertex] = parent[parent[vertex]]
            vertex = parent[vertex]
        return vertex

    for first, second in edges:
        first_root = find(first)
        second_root = find(second)
        if first_root == second_root:
            continue
        if size[first_root] < size[second_root]:
            first_root, second_root = second_root, first_root
        parent[second_root] = first_root
        size[first_root] += size[second_root]
        components -= 1

    return components


def solve(n: int, edges: list[list[int]]) -> int:
    return _count_components(n, edges)
