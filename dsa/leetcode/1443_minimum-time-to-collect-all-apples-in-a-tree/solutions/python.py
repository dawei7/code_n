def solve(n, edges, hasApple):
    adjacency = [[] for _ in range(n)]
    for first, second in edges:
        adjacency[first].append(second)
        adjacency[second].append(first)

    parent = [-2] * n
    parent[0] = -1
    order = []
    stack = [0]

    while stack:
        node = stack.pop()
        order.append(node)
        for neighbor in adjacency[node]:
            if parent[neighbor] == -2:
                parent[neighbor] = node
                stack.append(neighbor)

    needed = list(hasApple)
    total_time = 0
    for node in reversed(order[1:]):
        if needed[node]:
            total_time += 2
            needed[parent[node]] = True

    return total_time
