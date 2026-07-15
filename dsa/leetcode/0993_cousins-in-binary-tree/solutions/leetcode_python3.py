from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = [(root, None)]
        head = 0

        while head < len(queue):
            level_end = len(queue)
            parent_x = parent_y = None
            found_x = found_y = False

            while head < level_end:
                node, parent = queue[head]
                head += 1
                if node.val == x:
                    parent_x = parent
                    found_x = True
                elif node.val == y:
                    parent_y = parent
                    found_y = True
                if node.left is not None:
                    queue.append((node.left, node))
                if node.right is not None:
                    queue.append((node.right, node))

            if found_x or found_y:
                return found_x and found_y and parent_x is not parent_y

        return False
