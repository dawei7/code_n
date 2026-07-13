"""Iterative reverse inorder accumulation for LeetCode 538."""


def solve(root):
    total = 0
    stack = []
    node = root
    while stack or node is not None:
        while node is not None:
            stack.append(node)
            node = node.right
        node = stack.pop()
        total += node.val
        node.val = total
        node = node.left
    return root
