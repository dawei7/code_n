"""Iterative depth tracking for LeetCode 559."""


def solve(root) -> int:
    if root is None:
        return 0

    maximum = 0
    stack = [[root, 1, 0]]

    while stack:
        node, depth, next_child = stack[-1]
        maximum = max(maximum, depth)
        _value, children = node
        if next_child == len(children):
            stack.pop()
            continue
        stack[-1][2] += 1
        stack.append([children[next_child], depth + 1, 0])

    return maximum
