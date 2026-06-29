


def solve():
    class Solution:
        def bstFromPreorder(self, preorder):
            if not preorder:
                return None

            root = TreeNode(preorder[0])
            left = [x for x in preorder[1:] if x < preorder[0]]
            right = [x for x in preorder[1:] if x > preorder[0]]

            root.left = self.bstFromPreorder(left)
            root.right = self.bstFromPreorder(right)
            return root


if __name__ == "__main__":
    solve()
