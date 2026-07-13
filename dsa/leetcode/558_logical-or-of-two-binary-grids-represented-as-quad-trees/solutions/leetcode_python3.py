from typing import Optional


# Definition for a QuadTree node.
# class Node:
#     def __init__(self, val, isLeaf, topLeft=None, topRight=None,
#                  bottomLeft=None, bottomRight=None):
#         self.val = val
#         self.isLeaf = isLeaf
#         self.topLeft = topLeft
#         self.topRight = topRight
#         self.bottomLeft = bottomLeft
#         self.bottomRight = bottomRight
class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf:
            return Node(True, True) if quadTree1.val else quadTree2
        if quadTree2.isLeaf:
            return Node(True, True) if quadTree2.val else quadTree1

        children = [
            self.intersect(quadTree1.topLeft, quadTree2.topLeft),
            self.intersect(quadTree1.topRight, quadTree2.topRight),
            self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft),
            self.intersect(quadTree1.bottomRight, quadTree2.bottomRight),
        ]

        if all(
            child.isLeaf and child.val == children[0].val
            for child in children
        ):
            return Node(children[0].val, True)

        return Node(
            True,
            False,
            children[0],
            children[1],
            children[2],
            children[3],
        )

