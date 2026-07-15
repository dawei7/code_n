from typing import Optional


class Solution:
    def lcaDeepestLeaves(
        self, root: Optional["TreeNode"]
    ) -> Optional["TreeNode"]:
        def summarize(node):
            if node is None:
                return 0, None

            left_height, left_answer = summarize(node.left)
            right_height, right_answer = summarize(node.right)
            if left_height > right_height:
                return left_height + 1, left_answer
            if right_height > left_height:
                return right_height + 1, right_answer
            return left_height + 1, node

        return summarize(root)[1]
