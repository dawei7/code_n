def solve(edges1: list[list[int]], edges2: list[list[int]], k: int) -> list[int]:
    def count_within(edges: list[list[int]], limit: int) -> list[int]:
        size = len(edges) + 1
        graph = [[] for _ in range(size)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)

        if limit < 0:
            return [0] * size

        counts = []
        for start in range(size):
            reachable = 0
            stack = [(start, -1, 0)]
            while stack:
                node, parent, distance = stack.pop()
                if distance > limit:
                    continue

                reachable += 1
                if distance < limit:
                    for neighbor in graph[node]:
                        if neighbor != parent:
                            stack.append((neighbor, node, distance + 1))

            counts.append(reachable)

        return counts

    first_counts = count_within(edges1, k)
    second_counts = count_within(edges2, k - 1)
    best_second = max(second_counts)
    return [count + best_second for count in first_counts]
