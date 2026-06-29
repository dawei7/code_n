


def solve():
    class Solution:
        def preorderTraversal(self, root):
            if not root:
                return []

            result = []
            stack = [root]

            while stack:
                curr = stack.pop()
                result.append(curr.val)

                # Right child first, then Left child
                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)

            return result


if __name__ == "__main__":
    solve()
