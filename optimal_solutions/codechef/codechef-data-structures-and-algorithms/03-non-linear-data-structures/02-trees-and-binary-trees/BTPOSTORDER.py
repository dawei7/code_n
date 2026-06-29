


def solve():
    def post_order_traversal(root):
        if root is None:
            return
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.val, end=" ")


if __name__ == "__main__":
    solve()
