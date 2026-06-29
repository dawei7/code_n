


def solve():
    class Solution:
        def hasPathSum(self, root, K):
            # Base case: if tree is empty
            if not root:
                return False
            # Check if current node is a leaf
            if root.left is None and root.right is None:
                return root.data == K
            # Recursively check for left and right subtree with reduced sum
            return self.hasPathSum(root.left, K - root.data) or self.hasPathSum(root.right, K - root.data)


if __name__ == "__main__":
    solve()
