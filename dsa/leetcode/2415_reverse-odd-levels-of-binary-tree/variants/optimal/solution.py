class Solution:
    def reverseOddLevels(self, root):
        def visit(left, right, reverse):
            if left is None:
                return
            if reverse:
                left.val, right.val = right.val, left.val
            visit(left.left, right.right, not reverse)
            visit(left.right, right.left, not reverse)

        visit(root.left, root.right, True)
        return root
