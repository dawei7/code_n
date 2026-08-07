from typing import List, Optional


class Solution:
    def binaryTreePaths(self, root: Optional["TreeNode"]) -> List[str]:
        paths = []

        def visit(node: Optional["TreeNode"], prefix: str) -> None:
            if node is None:
                return
            path = f"{prefix}->{node.val}" if prefix else str(node.val)
            if node.left is None and node.right is None:
                paths.append(path)
                return
            visit(node.left, path)
            visit(node.right, path)

        visit(root, "")
        return paths
