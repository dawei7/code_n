from typing import List


def solve(n: int, edges: List[List[int]], good: List[int]) -> List[int]:
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
    downward = [1 if value else -1 for value in good]
    for node in reversed(order[1:]):
        downward[parent[node]] += max(0, downward[node])
    answer = downward[:]
    for node in order:
        for neighbor in graph[node]:
            if parent[neighbor] != node:
                continue
            parent_side = answer[node] - max(0, downward[neighbor])
            answer[neighbor] += max(0, parent_side)
    return answer
