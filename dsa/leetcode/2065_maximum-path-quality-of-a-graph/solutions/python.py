def solve(values: list[int], edges: list[list[int]], maxTime: int) -> int:
    graph = [[] for _ in values]
    for first, second, travel_time in edges:
        graph[first].append((second, travel_time))
        graph[second].append((first, travel_time))

    visits = [0] * len(values)
    visits[0] = 1
    best = values[0]

    def search(node: int, elapsed: int, quality: int) -> None:
        nonlocal best
        if node == 0:
            best = max(best, quality)

        for neighbor, travel_time in graph[node]:
            next_time = elapsed + travel_time
            if next_time > maxTime:
                continue

            first_visit = visits[neighbor] == 0
            visits[neighbor] += 1
            search(
                neighbor,
                next_time,
                quality + (values[neighbor] if first_visit else 0),
            )
            visits[neighbor] -= 1

    search(0, 0, values[0])
    return best
