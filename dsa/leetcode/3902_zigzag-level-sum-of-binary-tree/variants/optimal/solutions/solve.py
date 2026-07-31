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


def solve(root: TreeNode | None) -> list[int]:
    if root is None:
        return []
    answer: list[int] = []
    level = [root]
    odd_level = True
    while level:
        level_sum = 0
        traversal = level if odd_level else reversed(level)
        for node in traversal:
            required_child = node.left if odd_level else node.right
            if required_child is None:
                break
            level_sum += node.val
        answer.append(level_sum)
        next_level = []
        for node in level:
            if node.left is not None:
                next_level.append(node.left)
            if node.right is not None:
                next_level.append(node.right)
        level = next_level
        odd_level = not odd_level
    return answer
