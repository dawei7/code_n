"""Optimal app-local solution for LeetCode 1557."""


def solve(n: int, edges: list[list[int]]) -> list[int]:
    """Return precisely the vertices with no incoming edge."""
    has_incoming_edge = [False] * n
    for _, destination in edges:
        has_incoming_edge[destination] = True

    return [vertex for vertex in range(n) if not has_incoming_edge[vertex]]
