from typing import Optional


class Solution:
    def inorderSuccessor(self, root: "TreeNode", p: "TreeNode") -> Optional["TreeNode"]:
        successor = None
        node = root
        while node is not None:
            if node.val > p.val:
                successor = node
                node = node.left
            else:
                node = node.right
        return successor
