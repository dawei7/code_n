"""Leaf-trimming tree centers for LeetCode 310."""

from collections import deque


def _centers(n: int, edges: list[list[int]]) -> list[int]:
    if n <= 2:
        return list(range(n))

    adjacency = [set() for _ in range(n)]
    for left, right in edges:
        adjacency[left].add(right)
        adjacency[right].add(left)

    leaves = deque(node for node in range(n) if len(adjacency[node]) == 1)
    remaining = n
    while remaining > 2:
        layer_size = len(leaves)
        remaining -= layer_size
        for _ in range(layer_size):
            leaf = leaves.popleft()
            neighbor = adjacency[leaf].pop()
            adjacency[neighbor].remove(leaf)
            if len(adjacency[neighbor]) == 1:
                leaves.append(neighbor)
    return sorted(leaves)


def solve(n: int, edges: list[list[int]]) -> list[int]:
    return _centers(n, edges)
