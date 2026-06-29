


def solve():
    class Solution:
        def rightSideView(self, root):
            if not root:
                return []

            res = []
            q = deque([root])

            while q:
                n = len(q)
                for i in range(n):
                    node = q.popleft()
                    if i == n - 1:  # rightmost node at this level
                        res.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            return res


if __name__ == "__main__":
    solve()
