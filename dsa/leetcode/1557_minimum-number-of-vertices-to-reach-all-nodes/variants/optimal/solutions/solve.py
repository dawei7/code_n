def solve(n, edges):
    has_incoming_edge = [False] * n
    for _, destination in edges:
        has_incoming_edge[destination] = True

    return [vertex for vertex in range(n) if not has_incoming_edge[vertex]]
