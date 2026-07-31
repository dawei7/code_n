"""Optimal app-local solution for LeetCode 1522."""


class Node:
    """Local equivalent of LeetCode's N-ary tree node."""

    def __init__(self, val: int = 0, children: "list[Node] | None" = None):
        self.val = val
        self.children = [] if children is None else children


def solve(root: Node) -> int:
    order = []
    stack = [root]
    while stack:
        node = stack.pop()
        order.append(node)
        stack.extend(node.children)

    height = {}
    answer = 0
    for node in reversed(order):
        longest = second = 0
        for child in node.children:
            candidate = height[child] + 1
            if candidate > longest:
                longest, second = candidate, longest
            elif candidate > second:
                second = candidate
        answer = max(answer, longest + second)
        height[node] = longest

    return answer
