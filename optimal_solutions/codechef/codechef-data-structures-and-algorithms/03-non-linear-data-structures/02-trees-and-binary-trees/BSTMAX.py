


def solve():
    def maxNodeInBST(root):
        current = root
        while current.right is not None:
            current = current.right
        return current.val


if __name__ == "__main__":
    solve()
