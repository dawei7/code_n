"""Reference solution for LeetCode 1379."""


def solve(original, cloned, target):
    stack = [(original, cloned)]

    while stack:
        original_node, cloned_node = stack.pop()
        if original_node is target:
            return cloned_node

        if original_node.right is not None:
            stack.append((original_node.right, cloned_node.right))
        if original_node.left is not None:
            stack.append((original_node.left, cloned_node.left))

    return None
