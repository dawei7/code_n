


def solve():
    class Solution:
        def are_identical_trees(self, root1, root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False
            return (root1.val == root2.val and
                    self.are_identical_trees(root1.left, root2.left) and
                    self.are_identical_trees(root1.right, root2.right))


if __name__ == "__main__":
    solve()
