from typing import List


def solve(edges: List[List[int]], cost: List[int]) -> List[int]:
    n = len(cost)
    graph = [[] for _ in range(n)]
    for first, second in edges:
        graph[first].append(second)
        graph[second].append(first)

    parent = [-1] * n
    order = [0]
    for node in order:
        for neighbor in graph[node]:
            if neighbor == parent[node]:
                continue
            parent[neighbor] = node
            order.append(neighbor)

    answer = [1] * n
    subtree_size = [1] * n
    extremes = [[] for _ in range(n)]

    for node in reversed(order):
        values = [cost[node]]
        for neighbor in graph[node]:
            if parent[neighbor] != node:
                continue
            subtree_size[node] += subtree_size[neighbor]
            for value in extremes[neighbor]:
                values.append(value)
                values.sort()
                if len(values) > 5:
                    values = values[:2] + values[-3:]

        extremes[node] = values
        if subtree_size[node] >= 3:
            answer[node] = max(
                0,
                values[-1] * values[-2] * values[-3],
                values[0] * values[1] * values[-1],
            )

    return answer
