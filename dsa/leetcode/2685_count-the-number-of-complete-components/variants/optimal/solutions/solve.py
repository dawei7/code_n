def solve(n, edges):
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    seen = [False] * n
    answer = 0

    for start in range(n):
        if seen[start]:
            continue

        stack = [start]
        seen[start] = True
        vertices = 0
        degree_sum = 0

        while stack:
            node = stack.pop()
            vertices += 1
            degree_sum += len(graph[node])

            for neighbor in graph[node]:
                if not seen[neighbor]:
                    seen[neighbor] = True
                    stack.append(neighbor)

        if degree_sum == vertices * (vertices - 1):
            answer += 1

    return answer
