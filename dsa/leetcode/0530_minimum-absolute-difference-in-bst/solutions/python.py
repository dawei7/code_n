"""Adjacent inorder differences for LeetCode 530."""


def solve(root) -> int:
    stack = []
    node = root
    previous = None
    minimum = float("inf")

    while stack or node is not None:
        while node is not None:
            stack.append(node)
            node = node.left
        node = stack.pop()
        if previous is not None:
            minimum = min(minimum, node.val - previous)
        previous = node.val
        node = node.right

    return int(minimum)
