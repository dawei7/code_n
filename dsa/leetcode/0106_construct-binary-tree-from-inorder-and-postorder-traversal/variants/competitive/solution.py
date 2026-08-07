from typing import List, Optional


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional["TreeNode"]:
        index_by_value = {value: index for index, value in enumerate(inorder)}
        postorder_index = len(postorder) - 1

        def build(left: int, right: int):
            nonlocal postorder_index
            if left > right:
                return None
            value = postorder[postorder_index]
            postorder_index -= 1
            middle = index_by_value[value]
            node = TreeNode(value)
            node.right = build(middle + 1, right)
            node.left = build(left, middle - 1)
            return node

        return build(0, len(inorder) - 1)
