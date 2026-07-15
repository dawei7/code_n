"""Optimal app-local solution for LeetCode 1319."""


def solve(n, connections):
    if len(connections) < n - 1:
        return -1

    parent = list(range(n))
    size = [1] * n
    components = n

    def find(node):
        while node != parent[node]:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    for left, right in connections:
        left_root = find(left)
        right_root = find(right)
        if left_root == right_root:
            continue
        if size[left_root] < size[right_root]:
            left_root, right_root = right_root, left_root
        parent[right_root] = left_root
        size[left_root] += size[right_root]
        components -= 1

    return components - 1
