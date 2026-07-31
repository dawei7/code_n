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


def solve(root: TreeNode, target: TreeNode, k: int) -> list[int]:
    parents = {root: None}
    stack = [root]

    while stack:
        node = stack.pop()
        for child in (node.left, node.right):
            if child is not None:
                parents[child] = node
                stack.append(child)

    frontier = [target]
    visited = {target}

    for _ in range(k):
        next_frontier = []
        for node in frontier:
            for neighbor in (node.left, node.right, parents[node]):
                if neighbor is not None and neighbor not in visited:
                    visited.add(neighbor)
                    next_frontier.append(neighbor)
        frontier = next_frontier
        if not frontier:
            break

    return [node.val for node in frontier]
