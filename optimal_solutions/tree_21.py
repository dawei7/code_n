"""Optimal solution for tree_21: Root-to-Leaf Paths.

Return every root-to-leaf path as a list of node-index
lists. DFS from the root, accumulating the path; record
a copy when a leaf is reached.
"""


def solve(children, root, n):
    if n == 0 or root == -1:
        return []
    out = []

    def dfs(i, path):
        if i == -1:
            return
        path.append(i)
        if children[i][0] == -1 and children[i][1] == -1:
            out.append(list(path))
        else:
            dfs(children[i][0], path)
            dfs(children[i][1], path)
        path.pop()
    dfs(root, [])
    return out
