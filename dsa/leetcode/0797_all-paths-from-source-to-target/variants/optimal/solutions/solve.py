def solve(graph: list[list[int]]) -> list[list[int]]:
    target = len(graph) - 1
    reverse_graph = [[] for _ in graph]
    for node, neighbors in enumerate(graph):
        for neighbor in neighbors:
            reverse_graph[neighbor].append(node)

    can_reach_target = [False] * len(graph)
    can_reach_target[target] = True
    stack = [target]
    while stack:
        node = stack.pop()
        for predecessor in reverse_graph[node]:
            if not can_reach_target[predecessor]:
                can_reach_target[predecessor] = True
                stack.append(predecessor)

    if not can_reach_target[0]:
        return []

    paths: list[list[int]] = []
    path = [0]

    def visit(node: int) -> None:
        if node == target:
            paths.append(path.copy())
            return
        for neighbor in graph[node]:
            if can_reach_target[neighbor]:
                path.append(neighbor)
                visit(neighbor)
                path.pop()

    visit(0)
    return paths
