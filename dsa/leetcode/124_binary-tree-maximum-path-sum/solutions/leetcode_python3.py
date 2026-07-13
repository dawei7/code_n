from typing import Optional


class Solution:
    def maxPathSum(self, root: Optional["TreeNode"]) -> int:
        best = float("-inf")

        def gain(node):
            nonlocal best
            if node is None:
                return 0
            left_gain = max(0, gain(node.left))
            right_gain = max(0, gain(node.right))
            best = max(best, node.val + left_gain + right_gain)
            return node.val + max(left_gain, right_gain)

        gain(root)
        return int(best)
