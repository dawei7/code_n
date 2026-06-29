


def solve():
    class Solution:
        def minimumDepth(self, root: Node) -> int:
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return 1
            if root.left is None:
                return 1 + self.minimumDepth(root.right)
            if root.right is None:
                return 1 + self.minimumDepth(root.left)
            left_depth = self.minimumDepth(root.left)
            right_depth = self.minimumDepth(root.right)
            return 1 + min(left_depth, right_depth)


if __name__ == "__main__":
    solve()
