def solve(edges: list[list[int]], values: list[int]) -> int:
    n = len(values)
    graph = [[] for _ in range(n)]
    for first, second in edges:
        graph[first].append(second)
        graph[second].append(first)

    parent = [-2] * n
    parent[0] = -1
    order = [0]
    for node in order:
        for neighbor in graph[node]:
            if neighbor != parent[node]:
                parent[neighbor] = node
                order.append(neighbor)

    minimum_retained = [0] * n
    for node in reversed(order):
        child_loss = sum(
            minimum_retained[neighbor]
            for neighbor in graph[node]
            if parent[neighbor] == node
        )
        if child_loss == 0:
            minimum_retained[node] = values[node]
        else:
            minimum_retained[node] = min(values[node], child_loss)

    return sum(values) - minimum_retained[0]

