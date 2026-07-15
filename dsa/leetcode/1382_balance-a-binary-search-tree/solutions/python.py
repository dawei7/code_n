"""Reference solution for LeetCode 1382."""


def solve(root):
    nodes = []
    stack = []
    current = root

    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        nodes.append(current)
        current = current.right

    def build(left: int, right: int):
        if left > right:
            return None
        middle = (left + right) // 2
        node = nodes[middle]
        node.left = build(left, middle - 1)
        node.right = build(middle + 1, right)
        return node

    return build(0, len(nodes) - 1)
