from typing import List, Optional


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        node = root
        previous = None
        run_length = best_length = 0
        modes = []

        while stack or node is not None:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if previous is not None and node.val == previous:
                run_length += 1
            else:
                previous = node.val
                run_length = 1
            if run_length > best_length:
                best_length = run_length
                modes = [node.val]
            elif run_length == best_length:
                modes.append(node.val)
            node = node.right
        return modes
