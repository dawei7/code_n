"""Iterative postorder subtree aggregation for LeetCode 508."""

from collections import Counter


def solve(root) -> list[int]:
    subtree_sum = {}
    frequencies = Counter()
    maximum_frequency = 0
    stack = [(root, False)]

    while stack:
        node, expanded = stack.pop()
        if node is None:
            continue
        if not expanded:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))
            continue

        total = node.val + subtree_sum.get(node.left, 0) + subtree_sum.get(node.right, 0)
        subtree_sum[node] = total
        frequencies[total] += 1
        maximum_frequency = max(maximum_frequency, frequencies[total])

    return [total for total, count in frequencies.items() if count == maximum_frequency]
