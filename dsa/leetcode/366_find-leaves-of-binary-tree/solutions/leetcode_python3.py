from typing import List, Optional


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        rounds = []

        def leaf_height(node: Optional[TreeNode]) -> int:
            if node is None:
                return -1
            height = 1 + max(leaf_height(node.left), leaf_height(node.right))
            if height == len(rounds):
                rounds.append([])
            rounds[height].append(node.val)
            return height

        leaf_height(root)
        return rounds

