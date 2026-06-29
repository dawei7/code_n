


def solve():
    class Solution:
        def kthAncestor(self, n, edges, v, k):
            LG = 17

            adj = [[] for _ in range(n + 1)]
            for u, w in edges:
                adj[u].append(w)
                adj[w].append(u)

            ancestor = [[-1] * LG for _ in range(n + 1)]

            def dfs(node, parent):
                ancestor[node][0] = parent

                for child in adj[node]:
                    if child != parent:
                        dfs(child, node)

            dfs(1, -1)

            for j in range(1, LG):
                for node in range(1, n + 1):
                    p = ancestor[node][j - 1]
                    if p != -1:
                        ancestor[node][j] = ancestor[p][j - 1]

            for j in range(LG - 1, -1, -1):
                if (k >> j) & 1:
                    v = ancestor[v][j]
                    if v == -1:
                        return -1

            return v


if __name__ == "__main__":
    solve()
