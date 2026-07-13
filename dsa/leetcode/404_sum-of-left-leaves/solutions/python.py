"""Optimal app-local solution for LeetCode 404: Sum of Left Leaves."""


def solve(root) -> int:
    if root is None:
        return 0

    total = 0
    stack = [(root, False)]

    while stack:
        node, is_left = stack.pop()
        if node.left is None and node.right is None:
            if is_left:
                total += node.val
            continue
        if node.right is not None:
            stack.append((node.right, False))
        if node.left is not None:
            stack.append((node.left, True))

    return total
