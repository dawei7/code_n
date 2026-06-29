


def solve():
    def deserialize(arr):
        n = len(arr)
        if n == 0 or arr[0] == -1:
            return None

        root = TreeNode(arr[0])
        q = deque([root])

        i = 1
        while q and i < n:
            node = q.popleft()

            # left child
            if i < n and arr[i] != -1:
                node.left = TreeNode(arr[i])
                q.append(node.left)
            i += 1

            # right child
            if i < n and arr[i] != -1:
                node.right = TreeNode(arr[i])
                q.append(node.right)
            i += 1

        return root

    def serialize(root):
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            node = q.popleft()
            if node:
                res.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                res.append(-1)

        # Remove trailing nulls
        while res and res[-1] == -1:
            res.pop()

        return res


if __name__ == "__main__":
    solve()
