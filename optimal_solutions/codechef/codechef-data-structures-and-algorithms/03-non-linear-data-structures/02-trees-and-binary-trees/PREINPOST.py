


def solve():
    class Solution:
        def inorder(self, root, res):
            if not root:
                return
            self.inorder(root.left, res)
            res.append(root.val)
            self.inorder(root.right, res)

        def preorder(self, root, res):
            if not root:
                return
            res.append(root.val)
            self.preorder(root.left, res)
            self.preorder(root.right, res)

        def postorder(self, root, res):
            if not root:
                return
            self.postorder(root.left, res)
            self.postorder(root.right, res)
            res.append(root.val)

        def getTraversals(self, root):
            inorder_res, preorder_res, postorder_res = [], [], []
            self.inorder(root, inorder_res)
            self.preorder(root, preorder_res)
            self.postorder(root, postorder_res)
            return [inorder_res, preorder_res, postorder_res]


if __name__ == "__main__":
    solve()
