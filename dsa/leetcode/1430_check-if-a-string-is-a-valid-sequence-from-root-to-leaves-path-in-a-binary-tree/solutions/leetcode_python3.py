from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidSequence(self, root: Optional['TreeNode'], arr: List[int]) -> bool:
        def matches(node: Optional['TreeNode'], index: int) -> bool:
            if node is None or index == len(arr) or node.val != arr[index]:
                return False
            if node.left is None and node.right is None:
                return index == len(arr) - 1
            return matches(node.left, index + 1) or matches(node.right, index + 1)

        return matches(root, 0)
