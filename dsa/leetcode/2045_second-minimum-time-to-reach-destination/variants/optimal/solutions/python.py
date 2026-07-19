from collections import deque


def solve(
    n: int,
    edges: list[list[int]],
    time: int,
    change: int,
) -> int:
    graph = [[] for _ in range(n + 1)]
    for first, second in edges:
        graph[first].append(second)
        graph[second].append(first)

    distances = [[float("inf"), float("inf")] for _ in range(n + 1)]
    distances[1][0] = 0
    queue = deque([(1, 0)])

    while queue:
        vertex, steps = queue.popleft()

        for neighbor in graph[vertex]:
            next_steps = steps + 1

            if next_steps < distances[neighbor][0]:
                distances[neighbor][1] = distances[neighbor][0]
                distances[neighbor][0] = next_steps
                queue.append((neighbor, next_steps))
            elif (
                distances[neighbor][0]
                < next_steps
                < distances[neighbor][1]
            ):
                distances[neighbor][1] = next_steps
                queue.append((neighbor, next_steps))

    elapsed = 0
    for _ in range(int(distances[n][1])):
        if (elapsed // change) % 2 == 1:
            elapsed += change - elapsed % change
        elapsed += time

    return elapsed
