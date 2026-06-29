


def solve():
    def countNodes(root):
        counts = {}
        def dfs(node):
            if not node:
                return 0
            left_count = dfs(node.left)
            right_count = dfs(node.right)
            total = left_count + right_count + 1
            counts[node.label] = total
            return total
        dfs(root)
        n = max(counts.keys()) if counts else 0
        res = [0] * n
        for i in range(1, n + 1):
            res[i - 1] = counts[i]
        return res


if __name__ == "__main__":
    solve()
