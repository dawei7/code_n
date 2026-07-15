"""Reference solution for LeetCode 1367."""

from typing import Any


VALUE_LIMIT = 100


def solve(head: Any, root: Any) -> bool:
    pattern = []
    node = head
    while node is not None:
        pattern.append(node.val)
        node = node.next

    length = len(pattern)
    prefix = [0] * length
    matched = 0
    for index in range(1, length):
        while matched and pattern[index] != pattern[matched]:
            matched = prefix[matched - 1]
        if pattern[index] == pattern[matched]:
            matched += 1
        prefix[index] = matched

    transitions = [[0] * (VALUE_LIMIT + 1) for _ in range(length)]
    for state in range(length):
        for value in range(1, VALUE_LIMIT + 1):
            if value == pattern[state]:
                transitions[state][value] = state + 1
            elif state:
                transitions[state][value] = transitions[prefix[state - 1]][value]

    stack = [(root, 0)]
    while stack:
        tree_node, state = stack.pop()
        state = transitions[state][tree_node.val]
        if state == length:
            return True
        if tree_node.left is not None:
            stack.append((tree_node.left, state))
        if tree_node.right is not None:
            stack.append((tree_node.right, state))
    return False
