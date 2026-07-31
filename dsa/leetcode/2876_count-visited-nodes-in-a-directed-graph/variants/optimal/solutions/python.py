from collections import deque
from typing import List


def solve(edges: List[int]) -> List[int]:
    n = len(edges)
    indegree = [0] * n
    for next_node in edges:
        indegree[next_node] += 1

    queue = deque(node for node in range(n) if indegree[node] == 0)
    removed_order = []

    while queue:
        node = queue.popleft()
        removed_order.append(node)
        next_node = edges[node]
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            queue.append(next_node)

    answer = [0] * n

    for node in range(n):
        if indegree[node] == 0 or answer[node] != 0:
            continue

        cycle_nodes = [node]
        current = edges[node]
        while current != node:
            cycle_nodes.append(current)
            current = edges[current]

        cycle_length = len(cycle_nodes)
        for cycle_node in cycle_nodes:
            answer[cycle_node] = cycle_length

    for node in reversed(removed_order):
        answer[node] = answer[edges[node]] + 1

    return answer
