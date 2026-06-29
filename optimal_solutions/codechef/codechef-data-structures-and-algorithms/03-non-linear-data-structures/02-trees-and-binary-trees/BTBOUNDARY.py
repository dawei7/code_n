# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


def solve():
    class Solution:
        def print_leaves(self, root):
            if root is None:
                return

            self.print_leaves(root.left)

            if root.left is None and root.right is None:
                print(root.val, end=" ")

            self.print_leaves(root.right)

        def print_boundary_left(self, root):
            if root is None:
                return

            if root.left is not None:
                print(root.val, end=" ")
                self.print_boundary_left(root.left)
            elif root.right is not None:
                print(root.val, end=" ")
                self.print_boundary_left(root.right)

        def print_boundary_right(self, root):
            if root is None:
                return

            if root.right is not None:
                self.print_boundary_right(root.right)
                print(root.val, end=" ")
            elif root.left is not None:
                self.print_boundary_right(root.left)
                print(root.val, end=" ")

        def print_boundary(self, root):
            if root is None:
                return

            print(root.val, end=" ")
            self.print_boundary_left(root.left)
            self.print_leaves(root.left)
            self.print_leaves(root.right)
            self.print_boundary_right(root.right)


if __name__ == "__main__":
    solve()
