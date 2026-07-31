from collections import deque


def solve(
    k: int,
    row_conditions: list[list[int]],
    col_conditions: list[list[int]],
) -> list[list[int]]:
    def topological_order(conditions: list[list[int]]) -> list[int]:
        adjacency = [[] for _ in range(k + 1)]
        indegree = [0] * (k + 1)
        for before, after in conditions:
            adjacency[before].append(after)
            indegree[after] += 1

        queue = deque(
            value
            for value in range(1, k + 1)
            if indegree[value] == 0
        )
        order = []
        while queue:
            value = queue.popleft()
            order.append(value)
            for neighbor in adjacency[value]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return order if len(order) == k else []

    row_order = topological_order(row_conditions)
    column_order = topological_order(col_conditions)
    if not row_order or not column_order:
        return []

    row_position = {value: index for index, value in enumerate(row_order)}
    column_position = {value: index for index, value in enumerate(column_order)}
    matrix = [[0] * k for _ in range(k)]
    for value in range(1, k + 1):
        matrix[row_position[value]][column_position[value]] = value
    return matrix
