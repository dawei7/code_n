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


def solve(root) -> int:
    answer = 0

    def subtree_max(node):
        nonlocal answer
        if node is None:
            return float("-inf")

        left_max = subtree_max(node.left)
        right_max = subtree_max(node.right)
        if node.val >= left_max and node.val >= right_max:
            answer += 1
        return max(node.val, left_max, right_max)

    subtree_max(root)
    return answer
