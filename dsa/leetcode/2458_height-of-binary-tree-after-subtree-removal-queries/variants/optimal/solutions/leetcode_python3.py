from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(
        self, root: Optional[TreeNode], queries: List[int]  # noqa: F821
    ) -> List[int]:
        heights = {}
        stack = [(root, False)]
        while stack:
            node, expanded = stack.pop()
            if node is None:
                continue
            if expanded:
                left_height = heights[node.left.val] if node.left else -1
                right_height = heights[node.right.val] if node.right else -1
                heights[node.val] = 1 + max(left_height, right_height)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        answer_by_value = {}
        stack = [(root, 0, 0)]
        while stack:
            node, depth, outside_height = stack.pop()
            answer_by_value[node.val] = outside_height
            left_height = heights[node.left.val] if node.left else -1
            right_height = heights[node.right.val] if node.right else -1

            if node.left:
                stack.append(
                    (
                        node.left,
                        depth + 1,
                        max(outside_height, depth + 1 + right_height),
                    )
                )
            if node.right:
                stack.append(
                    (
                        node.right,
                        depth + 1,
                        max(outside_height, depth + 1 + left_height),
                    )
                )

        return [answer_by_value[value] for value in queries]
