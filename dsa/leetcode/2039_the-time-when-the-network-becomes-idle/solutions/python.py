from collections import deque


def solve(edges: list[list[int]], patience: list[int]) -> int:
    graph = [[] for _ in patience]
    for first, second in edges:
        graph[first].append(second)
        graph[second].append(first)

    distance = [-1] * len(patience)
    distance[0] = 0
    queue = deque([0])

    while queue:
        server = queue.popleft()
        for neighbor in graph[server]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[server] + 1
                queue.append(neighbor)

    last_arrival = 0
    for server in range(1, len(patience)):
        round_trip = 2 * distance[server]
        last_send = (
            (round_trip - 1) // patience[server]
        ) * patience[server]
        last_arrival = max(last_arrival, last_send + round_trip)

    return last_arrival + 1
