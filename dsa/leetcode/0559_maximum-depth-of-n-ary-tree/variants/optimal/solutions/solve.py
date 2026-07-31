class Node:
    """Local equivalent of LeetCode's Node for the standalone app template."""

    def __init__(self, val: int = 0, children: "list[Node] | None" = None):
        self.val = val
        self.children = [] if children is None else children


def solve(root: Node | None) -> int:
    if root is None:
        return 0

    maximum = 0
    stack = [[root, 1, 0]]

    while stack:
        node, depth, next_child = stack[-1]
        maximum = max(maximum, depth)
        if next_child == len(node.children):
            stack.pop()
            continue
        stack[-1][2] += 1
        stack.append([node.children[next_child], depth + 1, 0])

    return maximum
