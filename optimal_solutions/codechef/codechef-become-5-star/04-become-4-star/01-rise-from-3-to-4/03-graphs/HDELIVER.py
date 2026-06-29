


def solve():
    N = 101
    adj = [[] for _ in range(N)]
    vis = [0] * N
    color = [0] * N

    def dfs(v, col):
        if vis[v]:
            return

        vis[v] = 1
        color[v] = col

        for x in adj[v]:
            dfs(x, col)

    if __name__ == "__main__":
        t = int(input())

        for _ in range(t):
            n, m = map(int, input().split())

            # Resetting the adjacency list, color, and visited array
            adj = [[] for _ in range(n + 1)]
            color = [0] * (n + 1)
            vis = [0] * (n + 1)

            for _ in range(m):
                x, y = map(int, input().split())
                adj[x].append(y)
                adj[y].append(x)

            current = 1
            for i in range(n):
                if not vis[i]:
                    # Color all the nodes connected with i 
                    # with the same color
                    dfs(i, current)
                    current += 1

            q = int(input())
            for _ in range(q):
                x, y = map(int, input().split())

                # Output YES if both nodes have the same color
                if color[x] == color[y]:
                    print("YO")
                else:
                    print("NO")


if __name__ == "__main__":
    solve()
