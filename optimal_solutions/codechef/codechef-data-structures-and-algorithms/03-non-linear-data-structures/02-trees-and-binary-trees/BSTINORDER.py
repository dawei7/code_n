


def solve():
    def print_nodes(root):
        def in_order(root):
            if root is None:
                return
            in_order(root.left)
            print(root.val, end=' ')
            in_order(root.right)

        in_order(root)
        print()


if __name__ == "__main__":
    solve()
