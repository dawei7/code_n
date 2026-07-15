"""Optimal solution for LeetCode 1059: All Paths Lead to Destination."""


def solve(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    graph = [[] for _ in range(n)]
    for start, end in edges:
        graph[start].append(end)

    if graph[destination]:
        return False

    state = [0] * n
    stack = [(source, 0)]
    while stack:
        node, next_index = stack[-1]
        if state[node] == 0:
            if not graph[node]:
                if node != destination:
                    return False
                state[node] = 2
                stack.pop()
                continue
            state[node] = 1

        if next_index == len(graph[node]):
            state[node] = 2
            stack.pop()
            continue

        neighbor = graph[node][next_index]
        stack[-1] = (node, next_index + 1)
        if state[neighbor] == 1:
            return False
        if state[neighbor] == 0:
            stack.append((neighbor, 0))

    return True
