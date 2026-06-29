


def solve():
    def in_order(root, nodes):
        if root is None:
            return
        in_order(root.left, nodes)
        nodes.append(root.val)
        in_order(root.right, nodes)

    class Solution:
        def get_predecessor(self, root, x):
            predecessor = None
            while root:
                if root.val < x:
                    predecessor = root
                    root = root.right
                else:
                    root = root.left
            return predecessor.val if predecessor else -1


if __name__ == "__main__":
    solve()
