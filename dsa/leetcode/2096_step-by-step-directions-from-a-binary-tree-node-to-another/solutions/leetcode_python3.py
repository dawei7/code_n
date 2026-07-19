from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(
        self,
        root: Optional[TreeNode],
        startValue: int,
        destValue: int,
    ) -> str:
        parent = {root.val: (None, "")}
        stack = [root]

        while stack:
            node = stack.pop()
            if node.left:
                parent[node.left.val] = (node.val, "L")
                stack.append(node.left)
            if node.right:
                parent[node.right.val] = (node.val, "R")
                stack.append(node.right)

        start_ancestors = set()
        value = startValue
        while value is not None:
            start_ancestors.add(value)
            value = parent[value][0]

        downward_reversed = []
        value = destValue
        while value not in start_ancestors:
            parent_value, direction = parent[value]
            downward_reversed.append(direction)
            value = parent_value
        lowest_common_ancestor = value

        upward_count = 0
        value = startValue
        while value != lowest_common_ancestor:
            upward_count += 1
            value = parent[value][0]

        return "U" * upward_count + "".join(reversed(downward_reversed))
