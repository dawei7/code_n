


def solve():
    class Solution:
        def isChildrenSum(self, root: TreeNode) -> bool:
            if not root:
                return True  # empty tree
            if not root.left and not root.right:
                return True  # leaf node

            left_val = root.left.val if root.left else 0
            right_val = root.right.val if root.right else 0

            if root.val != left_val + right_val:
                return False

            return self.isChildrenSum(root.left) and self.isChildrenSum(root.right)


if __name__ == "__main__":
    solve()
