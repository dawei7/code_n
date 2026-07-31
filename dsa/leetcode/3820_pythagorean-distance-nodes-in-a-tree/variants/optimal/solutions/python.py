from collections import deque


def solve(n: int, edges: list[list[int]], x: int, y: int, z: int) -> int:
    adjacency = [[] for _ in range(n)]
    for first, second in edges:
        adjacency[first].append(second)
        adjacency[second].append(first)

    def distances(start: int) -> list[int]:
        result = [-1] * n
        result[start] = 0
        queue = deque([start])

        while queue:
            node = queue.popleft()
            for neighbor in adjacency[node]:
                if result[neighbor] == -1:
                    result[neighbor] = result[node] + 1
                    queue.append(neighbor)

        return result

    distance_x = distances(x)
    distance_y = distances(y)
    distance_z = distances(z)

    answer = 0
    for node in range(n):
        first, second, third = sorted(
            (distance_x[node], distance_y[node], distance_z[node])
        )
        if first * first + second * second == third * third:
            answer += 1

    return answer
