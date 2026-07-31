from collections import deque


class TreeNode:
    """Local equivalent of LeetCode's TreeNode for the standalone app template."""

    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def solve(root, start: int) -> int:
    parent = {root: None}
    queue = deque([root])
    start_node = root

    while queue:
        node = queue.popleft()
        if node.val == start:
            start_node = node
        if node.left is not None:
            parent[node.left] = node
            queue.append(node.left)
        if node.right is not None:
            parent[node.right] = node
            queue.append(node.right)

    queue = deque([start_node])
    infected = {start_node}
    minutes = -1

    while queue:
        minutes += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            for neighbor in (node.left, node.right, parent[node]):
                if neighbor is not None and neighbor not in infected:
                    infected.add(neighbor)
                    queue.append(neighbor)

    return minutes
