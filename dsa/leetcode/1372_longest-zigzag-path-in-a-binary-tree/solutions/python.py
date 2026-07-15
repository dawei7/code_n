"""Reference solution for LeetCode 1372."""

from typing import Any


def solve(root: Any) -> int:
    longest = 0
    stack = [(root, 0, 0)]

    while stack:
        node, left_length, right_length = stack.pop()
        longest = max(longest, left_length, right_length)
        if node.left is not None:
            stack.append((node.left, right_length + 1, 0))
        if node.right is not None:
            stack.append((node.right, 0, left_length + 1))

    return longest
