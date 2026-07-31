from typing import List


def solve(nums: List[int], edges: List[List[int]]) -> int:
    n = len(nums)
    graph = [[] for _ in range(n)]
    for first, second in edges:
        graph[first].append(second)
        graph[second].append(first)

    parent = [-1] * n
    entered = [0] * n
    exited = [0] * n
    order = []
    timer = 0
    stack = [(0, -1, False)]

    while stack:
        node, previous, leaving = stack.pop()
        if leaving:
            exited[node] = timer
            continue

        parent[node] = previous
        entered[node] = timer
        timer += 1
        order.append(node)
        stack.append((node, previous, True))
        for neighbor in reversed(graph[node]):
            if neighbor != previous:
                stack.append((neighbor, node, False))

    subtree_xor = nums.copy()
    for node in reversed(order[1:]):
        subtree_xor[parent[node]] ^= subtree_xor[node]

    total = subtree_xor[0]
    answer = float("inf")

    def is_ancestor(first: int, second: int) -> bool:
        return entered[first] <= entered[second] < exited[first]

    for first in range(1, n):
        for second in range(first + 1, n):
            if is_ancestor(first, second):
                values = (
                    subtree_xor[second],
                    subtree_xor[first] ^ subtree_xor[second],
                    total ^ subtree_xor[first],
                )
            elif is_ancestor(second, first):
                values = (
                    subtree_xor[first],
                    subtree_xor[second] ^ subtree_xor[first],
                    total ^ subtree_xor[second],
                )
            else:
                values = (
                    subtree_xor[first],
                    subtree_xor[second],
                    total ^ subtree_xor[first] ^ subtree_xor[second],
                )
            answer = min(answer, max(values) - min(values))

    return int(answer)
