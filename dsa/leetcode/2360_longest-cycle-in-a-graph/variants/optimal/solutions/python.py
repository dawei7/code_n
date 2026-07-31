from typing import List


def solve(edges: List[int]) -> int:
    visited = [False] * len(edges)
    answer = -1

    for start in range(len(edges)):
        if visited[start]:
            continue
        first_step: dict[int, int] = {}
        node = start
        step = 0
        while node != -1 and not visited[node]:
            visited[node] = True
            first_step[node] = step
            step += 1
            node = edges[node]
        if node in first_step:
            answer = max(answer, step - first_step[node])

    return answer
