from collections import deque


def solve(operations: list[list]) -> list:
    queue = deque()
    results = []
    for operation in operations:
        if operation[0] == "push":
            queue.append(operation[1])
            for _ in range(len(queue) - 1):
                queue.append(queue.popleft())
        elif operation[0] == "pop":
            results.append(queue.popleft())
        elif operation[0] == "top":
            results.append(queue[0])
        else:
            results.append(not queue)
    return results
