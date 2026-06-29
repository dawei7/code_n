from collections import deque


def solve():
    N = 10 ** 5 + 10
    INF = 10 ** 9

    adj = [[] for _ in range(10)]
    vis = [0] * N
    d = [INF] * N

    def bfs(v):
        q = deque()
        q.append(v)

        d[v] = 0

        while q:
            u = q.popleft()

            if vis[u]:
                continue

            vis[u] = 1

            for x in adj[int(s[u])]:
                q.append(x)
                d[x] = min(d[x], d[u] + 1)

            adj[int(s[u])].clear()

            if u + 1 <= n - 1:
                q.append(u + 1)
                d[u + 1] = min(d[u + 1], d[u] + 1)

            if u - 1 >= 0:
                q.append(u - 1)
                d[u - 1] = min(d[u - 1], d[u] + 1)

    if __name__ == "__main__":
        s = input().strip()
        n = len(s)

        for i in range(n):
            adj[int(s[i])].append(i)

        bfs(0)

        print(d[n - 1])


if __name__ == "__main__":
    solve()
