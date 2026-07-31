from collections import deque


class Node:
    """Local equivalent of LeetCode's Node for the standalone app template."""

    def __init__(self, val: int = 0, children: "list[Node] | None" = None):
        self.val = val
        self.children = [] if children is None else children


def solve(root: Node | None) -> list[list[int]]:
    if root is None:
        return []

    answer: list[list[int]] = []
    queue = deque([root])
    while queue:
        level: list[int] = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            queue.extend(node.children)
        answer.append(level)
    return answer
