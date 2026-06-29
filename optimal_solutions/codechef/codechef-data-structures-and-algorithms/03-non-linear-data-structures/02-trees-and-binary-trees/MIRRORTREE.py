


def solve():
    def is_mirror(left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

    def is_mirror_tree(root):
        if root is None:
            print("YES")
            return
        if is_mirror(root.left, root.right):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()
