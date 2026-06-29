


def solve():
    class Solution:
        def isBST(self, root):
            def is_valid(node, min_val, max_val):
                if node is None:
                    return True

                if node.val <= min_val or node.val >= max_val:
                    return False

                return (
                    is_valid(node.left, min_val, node.val) and
                    is_valid(node.right, node.val, max_val)
                )

            if is_valid(root, float('-inf'), float('inf')):
                print("YES")
            else:
                print("NO")


if __name__ == "__main__":
    solve()
