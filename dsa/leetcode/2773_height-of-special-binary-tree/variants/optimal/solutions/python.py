from typing import Any


def solve(root: Any) -> int:
    height = 0
    stack = [(root, 0)]

    while stack:
        node, depth = stack.pop()
        height = max(height, depth)

        is_single_leaf = node.left is None and node.right is None
        is_linked_leaf = node.left is not None and node.left.right is node
        if is_single_leaf or is_linked_leaf:
            continue

        if node.left is not None:
            stack.append((node.left, depth + 1))
        if node.right is not None:
            stack.append((node.right, depth + 1))

    return height
