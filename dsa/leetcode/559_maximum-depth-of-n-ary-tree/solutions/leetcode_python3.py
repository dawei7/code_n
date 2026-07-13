from typing import Optional


# Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children if children is not None else []
class Solution:
    def maxDepth(self, root: Optional['Node']) -> int:
        if root is None:
            return 0

        maximum = 0
        stack = [[root, 1, 0]]

        while stack:
            node, depth, next_child = stack[-1]
            maximum = max(maximum, depth)
            if next_child == len(node.children):
                stack.pop()
                continue
            stack[-1][2] += 1
            stack.append([node.children[next_child], depth + 1, 0])

        return maximum
