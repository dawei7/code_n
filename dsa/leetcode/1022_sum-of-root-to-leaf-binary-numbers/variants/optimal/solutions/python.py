"""Optimal app-local solution for LeetCode 1022."""


def solve(root):
    def visit(node, prefix):
        if node is None:
            return 0

        current = prefix * 2 + node.val
        if node.left is None and node.right is None:
            return current

        return visit(node.left, current) + visit(node.right, current)

    return visit(root, 0)
