"""Optimal app-local solution for LeetCode 1490."""


def solve(root):
    """Return an independently allocated clone of an encoded N-ary tree."""
    if root is None:
        return None

    cloned_root = [root[0], []]
    stack = [(root, cloned_root)]

    while stack:
        original, cloned = stack.pop()
        for child in original[1]:
            child_clone = [child[0], []]
            cloned[1].append(child_clone)
            stack.append((child, child_clone))

    return cloned_root

