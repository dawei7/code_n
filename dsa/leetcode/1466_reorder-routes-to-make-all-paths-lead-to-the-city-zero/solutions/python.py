def solve(n, connections):
    graph = [[] for _ in range(n)]
    for start, end in connections:
        graph[start].append((end, 1))
        graph[end].append((start, 0))

    reversals = 0
    visited = [False] * n
    visited[0] = True
    stack = [0]

    while stack:
        city = stack.pop()
        for neighbor, cost in graph[city]:
            if visited[neighbor]:
                continue
            visited[neighbor] = True
            reversals += cost
            stack.append(neighbor)

    return reversals
