def solve(edges: list[list[int]]) -> list[int]:
    node_count = len(edges)
    incoming = [0] * (node_count + 1)
    first_parent = None
    second_parent = None
    second_index = -1

    for index, edge in enumerate(edges):
        parent_node, child = edge
        if incoming[child] != 0:
            first_parent = edges[incoming[child] - 1]
            second_parent = edge
            second_index = index
        else:
            incoming[child] = index + 1

    parent = list(range(node_count + 1))
    size = [1] * (node_count + 1)

    def find(node: int) -> int:
        while node != parent[node]:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    for index, edge in enumerate(edges):
        if index == second_index:
            continue
        left_root = find(edge[0])
        right_root = find(edge[1])
        if left_root == right_root:
            return first_parent if first_parent is not None else edge
        if size[left_root] < size[right_root]:
            left_root, right_root = right_root, left_root
        parent[right_root] = left_root
        size[left_root] += size[right_root]

    return second_parent if second_parent is not None else []

