from typing import List, Optional


class Solution:
    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional["TreeNode"]:
        postorder_index = {
            value: index for index, value in enumerate(postorder)
        }
        preorder_index = 0

        def build(left: int, right: int) -> "TreeNode":
            nonlocal preorder_index
            root = TreeNode(preorder[preorder_index])
            preorder_index += 1
            if left == right:
                return root

            first_child_root = preorder[preorder_index]
            first_child_end = postorder_index[first_child_root]
            root.left = build(left, first_child_end)
            if first_child_end + 1 < right:
                root.right = build(first_child_end + 1, right - 1)
            return root

        return build(0, len(postorder) - 1)
