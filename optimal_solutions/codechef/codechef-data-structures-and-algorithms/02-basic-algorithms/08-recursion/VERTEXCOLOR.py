


def solve():
    class Solution:
        def canColorGraph(self, N, M, E, edges):
            adj = [[] for _ in range(N)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            color = [0] * N
            return self.backtrack(0, N, M, adj, color)

        def backtrack(self, node, N, M, adj, color):
            if node == N:
                return True
            for c in range(1, M+1):
                if self.isSafe(node, c, adj, color):
                    color[node] = c
                    if self.backtrack(node + 1, N, M, adj, color):
                        return True
                    color[node] = 0
            return False

        def isSafe(self, node, c, adj, color):
            for neighbor in adj[node]:
                if color[neighbor] == c:
                    return False
            return True


if __name__ == "__main__":
    solve()
