from __future__ import annotations


def solve(edges: list[list[int]]) -> int:
    n = len(edges)
    children: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for node in range(1, n):
        parent, weight = edges[node]
        children[parent].append((node, weight))

    order = [0]
    for node in order:
        order.extend(child for child, _ in children[node])

    parent_edge_free = [0] * n
    parent_edge_chosen = [0] * n

    for node in reversed(order):
        baseline = sum(parent_edge_free[child] for child, _ in children[node])
        parent_edge_chosen[node] = baseline

        best_gain = 0
        for child, weight in children[node]:
            best_gain = max(
                best_gain,
                weight + parent_edge_chosen[child] - parent_edge_free[child],
            )
        parent_edge_free[node] = baseline + best_gain

    return parent_edge_free[0]
