"""Optimal app-local solution for LeetCode 1325."""


def solve(root, target):
    result = root
    stack = [(root, None, None, False)]
    while stack:
        node, parent, side, visited = stack.pop()
        if not visited:
            stack.append((node, parent, side, True))
            if node.right is not None:
                stack.append((node.right, node, "right", False))
            if node.left is not None:
                stack.append((node.left, node, "left", False))
            continue

        if node.left is None and node.right is None and node.val == target:
            if parent is None:
                result = None
            else:
                setattr(parent, side, None)
    return result
