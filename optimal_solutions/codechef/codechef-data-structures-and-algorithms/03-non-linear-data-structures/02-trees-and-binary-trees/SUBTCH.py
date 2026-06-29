


def solve():
    class Solution:
        def findSubtree(self, root1, root2):
            def isIdentical(n1, n2):
                if n1 is None and n2 is None:
                    return True
                if n1 is None or n2 is None:
                    return False
                if n1.val != n2.val:
                    return False
                return isIdentical(n1.left, n2.left) and isIdentical(n1.right, n2.right)

            def dfs(node):
                if node is None:
                    return False
                if isIdentical(node, root2):
                    return True
                return dfs(node.left) or dfs(node.right)

            return 1 if dfs(root1) else 0


if __name__ == "__main__":
    solve()
