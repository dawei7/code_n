from typing import List


def solve(edges: List[int], node1: int, node2: int) -> int:
    def distances(start: int) -> List[int]:
        result = [-1] * len(edges)
        distance = 0
        node = start
        while node != -1 and result[node] == -1:
            result[node] = distance
            distance += 1
            node = edges[node]
        return result

    first = distances(node1)
    second = distances(node2)
    answer = -1
    best_distance = len(edges) + 1

    for node in range(len(edges)):
        if first[node] != -1 and second[node] != -1:
            candidate = max(first[node], second[node])
            if candidate < best_distance:
                best_distance = candidate
                answer = node

    return answer
