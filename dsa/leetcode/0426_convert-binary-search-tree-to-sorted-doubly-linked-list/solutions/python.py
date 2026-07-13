"""Optimal app-local solution for LeetCode 426."""


def solve(root):
    if root is None:
        return None

    first = None
    previous = None

    def inorder(node) -> None:
        nonlocal first, previous
        if node is None:
            return

        inorder(node.left)
        if previous is None:
            first = node
        else:
            previous.right = node
            node.left = previous
        previous = node
        inorder(node.right)

    inorder(root)
    first.left = previous
    previous.right = first
    return first
