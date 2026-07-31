def solve(n: int, edges: list[list[int]], baseTime: list[int]) -> int:
    children = [[] for _ in range(n)]
    for parent, child in edges:
        children[parent].append(child)

    order = [0]
    for task in order:
        order.extend(children[task])

    finish = [0] * n
    for task in reversed(order):
        if not children[task]:
            finish[task] = baseTime[task]
            continue

        earliest = min(finish[child] for child in children[task])
        latest = max(finish[child] for child in children[task])
        finish[task] = 2 * latest - earliest + baseTime[task]

    return finish[0]
