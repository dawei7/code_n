def solve(n: int, edges: list[list[int]], baseTime: list[int]) -> int:
    graph = [[] for _ in range(n)]
    for left, right in edges:
        graph[left].append(right)
        graph[right].append(left)

    parent = [-1] * n
    parent[0] = 0
    order = [0]
    for task in order:
        for neighbor in graph[task]:
            if neighbor != parent[task]:
                parent[neighbor] = task
                order.append(neighbor)

    downward = [0] * n
    for task in reversed(order):
        child_values = [
            downward[neighbor]
            for neighbor in graph[task]
            if parent[neighbor] == task
        ]
        if not child_values:
            downward[task] = baseTime[task]
        else:
            downward[task] = (
                2 * max(child_values) - min(child_values) + baseTime[task]
            )

    upward = [0] * n
    answer = None
    for task in order:
        incoming = [
            upward[task] if neighbor == parent[task] else downward[neighbor]
            for neighbor in graph[task]
        ]
        if not incoming:
            root_finish = baseTime[task]
        else:
            minimum = second_minimum = float("inf")
            maximum = second_maximum = float("-inf")
            for value in incoming:
                if value < minimum:
                    minimum, second_minimum = value, minimum
                elif value < second_minimum:
                    second_minimum = value
                if value > maximum:
                    maximum, second_maximum = value, maximum
                elif value > second_maximum:
                    second_maximum = value

            root_finish = 2 * maximum - minimum + baseTime[task]
            for index, neighbor in enumerate(graph[task]):
                if parent[neighbor] != task:
                    continue
                if len(incoming) == 1:
                    upward[neighbor] = baseTime[task]
                    continue
                excluded = incoming[index]
                earliest = second_minimum if excluded == minimum else minimum
                latest = second_maximum if excluded == maximum else maximum
                upward[neighbor] = 2 * latest - earliest + baseTime[task]

        if answer is None or root_finish < answer:
            answer = root_finish

    return answer
