# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


def solve():
    def search_in_bst(root, x):
        if root is None:
            return False

        if root.val == x:
            return True

        if root.val < x:
            return search_in_bst(root.right, x)
        else:
            return search_in_bst(root.left, x)


if __name__ == "__main__":
    solve()
