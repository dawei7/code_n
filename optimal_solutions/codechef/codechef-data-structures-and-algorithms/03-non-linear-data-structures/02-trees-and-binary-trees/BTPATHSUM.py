


def solve():
    class Solution:
        def traverse(self, root, paths, path, target, current_sum):
            if not root:
                return

            path.append(root.val)
            current_sum += root.val

            if not root.left and not root.right:
                if current_sum == target:
                    paths.append(path.copy())
            else:
                if root.left:
                    self.traverse(root.left, paths, path, target, current_sum)
                if root.right:
                    self.traverse(root.right, paths, path, target, current_sum)

            path.pop()

        def target_sum_paths(self, root, target):
            paths = []
            path = []
            self.traverse(root, paths, path, target, 0)

            for p in paths:
                print(" ".join(map(str, p)))


if __name__ == "__main__":
    solve()
