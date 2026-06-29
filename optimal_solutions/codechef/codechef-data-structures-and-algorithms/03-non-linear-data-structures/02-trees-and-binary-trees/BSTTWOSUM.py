# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


def solve():
    class Solution:
        def dfs(self, root, values, k):
            if root is None:
                return False
            if (k - root.val) in values:
                return True
            values.add(root.val)
            return self.dfs(root.left, values, k) or self.dfs(root.right, values, k)

        def twoSumBST(self, root, S):
            values = set()
            check = self.dfs(root, values, S)
            if check:
                print("YES")
            else:
                print("NO")


if __name__ == "__main__":
    solve()
