


def solve():
    class Solution:
        def __init__(self):
            self.ans = []

        def distanceK(self, root, target, k):
            self.ans = []
            if not root:
                return self.ans
            if k == 0:
                self.ans.append(target.val)
                return self.ans

            self.downFromTarget(target, k)
            self.upFromTarget(root, target, k)
            return self.ans

        def upFromTarget(self, root, target, k):
            if not root:
                return -1
            if root == target:
                return 0

            left = self.upFromTarget(root.left, target, k)
            right = self.upFromTarget(root.right, target, k)

            if left != -1:
                temp = k - left - 1
                if temp == 0:
                    self.ans.append(root.val)
                else:
                    self.downFromTarget(root.right, temp - 1)
                return left + 1

            if right != -1:
                temp = k - right - 1
                if temp == 0:
                    self.ans.append(root.val)
                else:
                    self.downFromTarget(root.left, temp - 1)
                return right + 1

            return -1

        def downFromTarget(self, target, k):
            if not target:
                return
            if k == 0:
                self.ans.append(target.val)
                return
            self.downFromTarget(target.left, k - 1)
            self.downFromTarget(target.right, k - 1)


if __name__ == "__main__":
    solve()
