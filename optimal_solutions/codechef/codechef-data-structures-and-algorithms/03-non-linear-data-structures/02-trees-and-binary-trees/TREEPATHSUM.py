


def solve():
    class Solution:

        def dfs(self, node, parent, s, target_sum, adj, degree, check):
            s += node

            for v in adj[node]:
                if v != parent:
                    self.dfs(v, node, s, target_sum, adj, degree, check)

            if parent != -1 and degree[node] == 1:
                if s == target_sum:
                    check[0] = True

        def solution(self, n, target_sum, adj):
            if n == 1:
                return target_sum == 1

            degree = [0] * (n + 1)
            for i in range(1, n + 1):
                degree[i] = len(adj[i])

            check = [False]  
            self.dfs(1, -1, 0, target_sum, adj, degree, check)
            return check[0]


if __name__ == "__main__":
    solve()
