from typing import List, Optional


class Solution:
    def pathSum(self, root: Optional["TreeNode"], targetSum: int) -> List[List[int]]:
        result = []
        path = []

        def search(node, remaining):
            if node is None:
                return
            path.append(node.val)
            remaining -= node.val
            if node.left is None and node.right is None:
                if remaining == 0:
                    result.append(path.copy())
            else:
                search(node.left, remaining)
                search(node.right, remaining)
            path.pop()

        search(root, targetSum)
        return result
