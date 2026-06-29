


def solve():
    class Solution:
        def isSymmetric(self, root: TreeNode) -> bool:
            if not root:
                return True
            return self.isMirror(root.left, root.right)

        def isMirror(self, a: TreeNode, b: TreeNode) -> bool:
            if not a and not b:
                return True
            if not a or not b:
                return False
            return (a.val == b.val and 
                    self.isMirror(a.left, b.right) and 
                    self.isMirror(a.right, b.left))


if __name__ == "__main__":
    solve()
