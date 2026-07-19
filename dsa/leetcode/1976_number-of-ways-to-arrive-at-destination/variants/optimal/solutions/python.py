import heapq


def solve(n: int, roads: list[list[int]]) -> int:
    modulus = 1_000_000_007
    adjacency = [[] for _ in range(n)]
    for left, right, travel_time in roads:
        adjacency[left].append((right, travel_time))
        adjacency[right].append((left, travel_time))

    distances = [float("inf")] * n
    ways = [0] * n
    distances[0] = 0
    ways[0] = 1
    queue = [(0, 0)]

    while queue:
        distance, node = heapq.heappop(queue)
        if distance != distances[node]:
            continue

        for neighbor, travel_time in adjacency[node]:
            candidate = distance + travel_time
            if candidate < distances[neighbor]:
                distances[neighbor] = candidate
                ways[neighbor] = ways[node]
                heapq.heappush(queue, (candidate, neighbor))
            elif candidate == distances[neighbor]:
                ways[neighbor] = (ways[neighbor] + ways[node]) % modulus

    return ways[n - 1]
