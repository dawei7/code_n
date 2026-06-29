


def solve():
    class Solution:
        def lowestCommonAncestor(self, root, A, B):
            # Helper function to find LCA in the binary tree.
            def lca(node):
                if not node:
                    return None
                if node.data == A or node.data == B:
                    return node
                left = lca(node.left)
                right = lca(node.right)
                if left and right:
                    return node
                return left if left else right
            node = lca(root)
            return node.data if node else None


if __name__ == "__main__":
    solve()
