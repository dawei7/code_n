from typing import Optional


# Definition for a Node.
# class Node:
#     def __init__(self, val: int):
#         self.val = val
#         self.left = None
#         self.right = None
#         self.parent = None


class Solution:
    def inorderSuccessor(self, node: "Node") -> Optional["Node"]:
        if node.right is not None:
            successor = node.right
            while successor.left is not None:
                successor = successor.left
            return successor

        current = node
        while current.parent is not None and current is current.parent.right:
            current = current.parent
        return current.parent
