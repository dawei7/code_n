def solve(n, roads, names, targetPath):
    graph = [[] for _ in range(n)]
    for left, right in roads:
        graph[left].append(right)
        graph[right].append(left)

    length = len(targetPath)
    previous = [int(names[city] != targetPath[0]) for city in range(n)]
    parent = [[-1] * n for _ in range(length)]

    for index in range(1, length):
        current = [0] * n
        for city in range(n):
            predecessor = min(graph[city], key=previous.__getitem__)
            current[city] = (
                previous[predecessor]
                + int(names[city] != targetPath[index])
            )
            parent[index][city] = predecessor
        previous = current

    city = min(range(n), key=previous.__getitem__)
    path = [city]
    for index in range(length - 1, 0, -1):
        city = parent[index][city]
        path.append(city)

    return path[::-1]

