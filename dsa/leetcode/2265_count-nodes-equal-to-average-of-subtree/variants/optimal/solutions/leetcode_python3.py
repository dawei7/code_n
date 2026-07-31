# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        answer = 0

        def visit(node):
            nonlocal answer
            if node is None:
                return 0, 0

            left_sum, left_count = visit(node.left)
            right_sum, right_count = visit(node.right)
            subtree_sum = left_sum + right_sum + node.val
            subtree_count = left_count + right_count + 1

            if subtree_sum // subtree_count == node.val:
                answer += 1

            return subtree_sum, subtree_count

        visit(root)
        return answer
