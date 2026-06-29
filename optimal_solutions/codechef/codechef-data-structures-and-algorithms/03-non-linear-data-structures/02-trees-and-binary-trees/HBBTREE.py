


def solve():
    class Solution:
        def check_height(self, root):
            if root is None:
                return 0

            left_height = self.check_height(root.left)
            right_height = self.check_height(root.right)

            if left_height == -1 or right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1

            return 1 + max(left_height, right_height)

        def is_height_balanced(self, root):
            if root is None:
                print("YES")
                return

            if self.check_height(root) == -1:
                print("NO")
            else:
                print("YES")


if __name__ == "__main__":
    solve()
