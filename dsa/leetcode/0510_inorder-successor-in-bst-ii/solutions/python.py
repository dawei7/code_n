"""Parent-pointer inorder successor for LeetCode 510."""


def solve(node):
    if node.right is not None:
        successor = node.right
        while successor.left is not None:
            successor = successor.left
        return successor

    current = node
    while current.parent is not None and current is current.parent.right:
        current = current.parent
    return current.parent
