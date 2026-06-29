from collections import deque


def solve():
    N = 200001
    INF = 1000000000

    adj = [[] for _ in range(N)]
    vis = [False] * N
    d = [INF] * N

    class Pair:
        def __init__(self, node, weight):
            self.node = node
            self.weight = weight

    def bfs(v):
        q = deque()
        q.append(v)
        d[v] = 0

        while q:
            u = q.popleft()

            if vis[u]:
                continue

            vis[u] = True

            for x in adj[u]:
                node, weight = x.node, x.weight

                if weight == 0:
                    q.appendleft(node)
                    d[node] = min(d[node], d[u])
                else:
                    q.append(node)
                    d[node] = min(d[node], d[u] + 1)

    if __name__ == "__main__":
        n, m = map(int, input().split())

        for i in range(1, n + 1):
            adj[i] = []

        for _ in range(m):
            x, y = map(int, input().split())
            adj[x].append(Pair(y, 0))
            adj[y].append(Pair(x, 1))

        bfs(1)

        if d[n] == INF:
            print("-1")
        else:
            print(d[n])


if __name__ == "__main__":
    solve()
