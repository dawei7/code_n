


def solve():
    class Solution:
        def insertIntoBST(self, root, val):
            if not root:
                return TreeNode(val)

            cur = root
            while True:
                if val < cur.val:
                    if cur.left is None:
                        cur.left = TreeNode(val)
                        break
                    cur = cur.left
                else:  # val > cur.val (unique guaranteed)
                    if cur.right is None:
                        cur.right = TreeNode(val)
                        break
                    cur = cur.right

            return root


if __name__ == "__main__":
    solve()
