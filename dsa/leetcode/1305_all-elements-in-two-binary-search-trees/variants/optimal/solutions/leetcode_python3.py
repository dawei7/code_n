from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> List[int]:
        def inorder(root: Optional[TreeNode]) -> List[int]:
            values = []
            stack = []
            node = root

            while node is not None or stack:
                while node is not None:
                    stack.append(node)
                    node = node.left
                node = stack.pop()
                values.append(node.val)
                node = node.right

            return values

        first = inorder(root1)
        second = inorder(root2)
        merged = []
        i = j = 0

        while i < len(first) and j < len(second):
            if first[i] <= second[j]:
                merged.append(first[i])
                i += 1
            else:
                merged.append(second[j])
                j += 1

        merged.extend(first[i:])
        merged.extend(second[j:])
        return merged
