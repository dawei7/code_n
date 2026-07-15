from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        subtree_sum = {}
        sums = []
        stack = [(root, False)]

        while stack:
            node, processed = stack.pop()
            if not processed:
                stack.append((node, True))
                if node.right is not None:
                    stack.append((node.right, False))
                if node.left is not None:
                    stack.append((node.left, False))
                continue

            current_sum = (
                node.val
                + subtree_sum.get(node.left, 0)
                + subtree_sum.get(node.right, 0)
            )
            subtree_sum[node] = current_sum
            sums.append(current_sum)

        total = subtree_sum[root]
        best = max(part * (total - part) for part in sums[:-1])
        return best % 1_000_000_007
