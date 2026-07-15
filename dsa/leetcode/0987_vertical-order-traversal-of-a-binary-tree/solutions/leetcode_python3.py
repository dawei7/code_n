from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        coordinates = []
        stack = [(root, 0, 0)]

        while stack:
            node, row, column = stack.pop()
            coordinates.append((column, row, node.val))
            if node.left is not None:
                stack.append((node.left, row + 1, column - 1))
            if node.right is not None:
                stack.append((node.right, row + 1, column + 1))

        coordinates.sort()
        answer = []
        previous_column = None
        for column, _, value in coordinates:
            if column != previous_column:
                answer.append([])
                previous_column = column
            answer[-1].append(value)
        return answer
