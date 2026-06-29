


def solve():
    class Solution:
        def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
            nodes = []  # list of tuples (col, row, val)
            self.dfs(root, 0, 0, nodes)
            nodes.sort()  # sorts by col, then row, then val

            res = []
            prev_col = float('-inf')
            for col, row, val in nodes:
                if col != prev_col:
                    res.append([])
                    prev_col = col
                res[-1].append(val)
            return res

        def dfs(self, node: Optional[TreeNode], row: int, col: int, nodes: List):
            if not node:
                return
            nodes.append((col, row, node.val))
            self.dfs(node.left, row + 1, col - 1, nodes)
            self.dfs(node.right, row + 1, col + 1, nodes)


if __name__ == "__main__":
    solve()
