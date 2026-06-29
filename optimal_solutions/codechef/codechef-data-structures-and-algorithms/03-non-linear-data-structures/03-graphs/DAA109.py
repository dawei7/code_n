


def solve():
    N = 2 * 10**5 + 1
    adj = [[] for _ in range(N)]
    vis = [False] * N

    def dfs(v):
        if vis[v]:
            return
        vis[v] = True

        for u in adj[v]:
            dfs(u)

    if __name__ == "__main__":
        n, m = map(int, input().split())

        for _ in range(m):
            a, b = map(int, input().split())
            adj[a].append(b)

        dfs(1)

        for i in range(1, n + 1):
            if vis[i]:
                print(i, end=" ")


if __name__ == "__main__":
    solve()
