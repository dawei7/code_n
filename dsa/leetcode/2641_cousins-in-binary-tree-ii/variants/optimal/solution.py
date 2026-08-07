# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root.val = 0
        level = [root]

        while level:
            next_level = []
            next_sum = 0

            for node in level:
                if node.left:
                    next_level.append(node.left)
                    next_sum += node.left.val
                if node.right:
                    next_level.append(node.right)
                    next_sum += node.right.val

            for node in level:
                sibling_sum = 0
                if node.left:
                    sibling_sum += node.left.val
                if node.right:
                    sibling_sum += node.right.val
                if node.left:
                    node.left.val = next_sum - sibling_sum
                if node.right:
                    node.right.val = next_sum - sibling_sum

            level = next_level

        return root
