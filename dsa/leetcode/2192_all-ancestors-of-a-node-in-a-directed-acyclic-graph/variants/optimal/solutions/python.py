def solve(n: int, edges: list[list[int]]) -> list[list[int]]:
    graph = [[] for _ in range(n)]
    for source, destination in edges:
        graph[source].append(destination)

    ancestors = [[] for _ in range(n)]
    for ancestor in range(n):
        seen = [False] * n
        stack = [ancestor]

        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                if not seen[neighbor]:
                    seen[neighbor] = True
                    ancestors[neighbor].append(ancestor)
                    stack.append(neighbor)

    return ancestors
