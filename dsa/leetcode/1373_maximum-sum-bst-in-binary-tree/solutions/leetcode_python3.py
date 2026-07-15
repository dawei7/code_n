from typing import Optional


class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        summaries = {}
        best = 0
        stack = [(root, False)]

        while stack:
            node, expanded = stack.pop()
            if not expanded:
                stack.append((node, True))
                if node.right is not None:
                    stack.append((node.right, False))
                if node.left is not None:
                    stack.append((node.left, False))
                continue

            left = summaries.get(
                node.left, (True, float("inf"), float("-inf"), 0)
            )
            right = summaries.get(
                node.right, (True, float("inf"), float("-inf"), 0)
            )
            if left[0] and right[0] and left[2] < node.val < right[1]:
                total = left[3] + node.val + right[3]
                summaries[node] = (
                    True,
                    min(left[1], node.val),
                    max(right[2], node.val),
                    total,
                )
                best = max(best, total)
            else:
                summaries[node] = (False, 0, 0, 0)

        return best
