


def solve():
    class Solution:
        def __init__(self):
            self.ans = -10**18

        def dfs(self, root):
            if not root:
                return 0

            left = max(0, self.dfs(root.left))
            right = max(0, self.dfs(root.right))

            self.ans = max(self.ans, root.val + left + right)

            return root.val + max(left, right)

        def maxPathSum(self, root):
            self.ans = -10**18
            self.dfs(root)
            return self.ans


if __name__ == "__main__":
    solve()
