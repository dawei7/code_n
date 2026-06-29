


def solve():
    class Solution:
        def findAncestors(self, n, edges):
            adj = [[] for _ in range(n)]
            indegree = [0] * n

            for x, y in edges:
                adj[x].append(y)
                indegree[y] += 1

            q = deque()
            for i in range(n):
                if indegree[i] == 0:
                    q.append(i)

            ans = [set() for _ in range(n)]

            while q:
                u = q.popleft()
                for v in adj[u]:
                    ans[v].add(u)
                    ans[v].update(ans[u])
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        q.append(v)

            return ans


if __name__ == "__main__":
    solve()
