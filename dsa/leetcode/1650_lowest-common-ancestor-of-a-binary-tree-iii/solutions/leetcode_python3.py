"""
# Definition for a Node.
class Node:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
"""


class Solution:
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        first, second = p, q
        while first is not second:
            first = first.parent if first is not None else q
            second = second.parent if second is not None else p
        return first
