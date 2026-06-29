


def solve():
    class Solution:
        def preOrderTraversal(self, root):
            if root is None:
                return
            print(root.val, end=' ')
            self.preOrderTraversal(root.left)
            self.preOrderTraversal(root.right)


if __name__ == "__main__":
    solve()
