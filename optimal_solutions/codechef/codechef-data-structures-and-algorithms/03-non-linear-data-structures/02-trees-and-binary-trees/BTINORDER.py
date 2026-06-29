


def solve():
    class Solution:
        def inOrderTraversal(self, root):
            if root is None:
                return
            self.inOrderTraversal(root.left)
            print(root.val, end=' ')
            self.inOrderTraversal(root.right)


if __name__ == "__main__":
    solve()
