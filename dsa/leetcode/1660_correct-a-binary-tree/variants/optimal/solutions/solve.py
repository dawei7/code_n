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


class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        seen = set()

        def repair(node):
            if node is None:
                return None
            if node.right in seen:
                return None

            seen.add(node)
            node.right = repair(node.right)
            node.left = repair(node.left)
            return node

        return repair(root)


def solve(root: TreeNode) -> TreeNode:
    return Solution().correctBinaryTree(root)
