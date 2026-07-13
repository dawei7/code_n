from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional["TreeNode"]:
        index_by_value = {value: index for index, value in enumerate(inorder)}
        preorder_index = 0

        def build(left: int, right: int):
            nonlocal preorder_index
            if left > right:
                return None
            value = preorder[preorder_index]
            preorder_index += 1
            middle = index_by_value[value]
            node = TreeNode(value)
            node.left = build(left, middle - 1)
            node.right = build(middle + 1, right)
            return node

        return build(0, len(inorder) - 1)
