def solve(edges: list[list[int]]) -> list[int]:
    parent = list(range(len(edges) + 1))
    size = [1] * (len(edges) + 1)

    def find(node: int) -> int:
        while node != parent[node]:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    for left, right in edges:
        left_root = find(left)
        right_root = find(right)
        if left_root == right_root:
            return [left, right]

        if size[left_root] < size[right_root]:
            left_root, right_root = right_root, left_root
        parent[right_root] = left_root
        size[left_root] += size[right_root]

    return []

